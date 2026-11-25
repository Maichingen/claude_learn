#!/usr/bin/env python3
"""Exportiert schwachstellen.md als mobil lesbares PDF.

Zwei Modi:
    python export_schwachstellen.py              -> schwachstellen.pdf (A5, fortlaufend)
    python export_schwachstellen.py --retain     -> retain_export_NNN.pdf (A5, 1 Abschnitt/Seite,
                                                    NUR neue Abschnitte seit dem letzten Export)

Quelle fuer --retain ist retain_karten.md (fertige Frage-Antwort-Paare, aus
denen eine Karteikarten-App wie Retain ihre Karten baut); fehlt die Datei, dient schwachstellen.md
als Quelle.

Retain-Export ist fortlaufend: Bereits exportierte Karten stehen in
retain_exportiert.json und kommen nie ein zweites Mal in ein Retain-PDF. Jeder
Export bekommt eine neue Nummer (001, 002, ...), damit beim Import in Retain
keine doppelten Karten entstehen.

Hintergrund: CLAUDE.md verlangt den PDF-Export nach jeder Lerneinheit
("Einheit beenden", Schritt 6) sowie einen Retain-optimierten Export
(A5, eine Karte pro Seite) fuer retain.cards.

Umsetzung mit fpdf2 statt der in CLAUDE.md Schritt 4b genannten Kombination
markdown2 + weasyprint: WeasyPrint benoetigt unter Windows GTK-Systembibliotheken
(libgobject-2.0-0), die hier nicht vorhanden sind. fpdf2 ist reines Python und
laeuft ohne externe Abhaengigkeiten.
"""

from __future__ import annotations

import json
import re
import sys
from datetime import date
from dataclasses import dataclass, field
from pathlib import Path

from fpdf import FPDF
from fpdf.enums import XPos, YPos

# --- Konfiguration -----------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent
SOURCE_FILE = BASE_DIR / "schwachstellen.md"
RETAIN_STATE_FILE = BASE_DIR / "retain_exportiert.json"
RETAIN_SOURCE_FILE = BASE_DIR / "retain_karten.md"


def _modulname() -> str:
    try:
        return json.loads((BASE_DIR / "einstellungen.json").read_text(encoding="utf-8")).get("modul_kurz", "Modul")
    except (OSError, ValueError):
        return "Modul"


MODUL = _modulname()

# A5 explizit in mm statt als Namenskonstante - fpdf2 warnt sonst ueber die
# in Release 2.8.5 korrigierten Formatmasse.
PAGE_FORMAT = (148, 210)
MARGIN_MM = 12
LINE_HEIGHT_MM = 5.5

FONT_NAME = "Body"
# Windows: Arial · Linux: DejaVu · sonst Fallback Helvetica (ohne Umlaut-Garantie)
_KANDIDATEN = [
    (Path("C:/Windows/Fonts"), "arial.ttf", "arialbd.ttf", "ariali.ttf"),
    (Path("/usr/share/fonts/truetype/dejavu"), "DejaVuSans.ttf", "DejaVuSans-Bold.ttf", "DejaVuSans-Oblique.ttf"),
]
FONT_DIR, _R, _B, _I = next(((d, r, b, i) for d, r, b, i in _KANDIDATEN if (d / r).exists()), _KANDIDATEN[0])
FONT_REGULAR = FONT_DIR / _R
FONT_BOLD = FONT_DIR / _B
FONT_ITALIC = FONT_DIR / _I

SIZE_TITLE = 15
SIZE_HEADING = 12
SIZE_BODY = 10
SIZE_LABEL = 10
SIZE_FOOTER = 8

# Emoji rendern in Arial nicht - durch Textmarker ersetzen.
GLYPH_REPLACEMENTS = {
    "\U0001f534": "[ROT]",
    "\U0001f7e1": "[GELB]",
    "\U0001f7e2": "[GRUEN]",
    "\u26a0\ufe0f": "!",
    "\u26a0": "!",
    "\U0001f393": "[VORWISSEN]",
    "\u2705": "[x]",
    "\u274c": "[ ]",
    "\u2192": "->",
    "\u2190": "<-",
    "\u2248": "~",
    "\u20ac": "EUR",
    "\u2260": "ist nicht",
    "\u2212": "-",
    "\u2014": "-",
    "\u2013": "-",
    "\u201e": '"',
    "\u201c": '"',
    "\u201d": '"',
    "\u00b7": "*",
}

# Zeilen, die als hervorgehobenes Label gerendert werden.
LABEL_PREFIXES = (
    "Kernaussage:",
    "Erklaerung",
    "Erklärung",
    "Haeufiger Fehler:",
    "Häufiger Fehler:",
    "Merksatz:",
    "Herleitung:",
    "Frage:",
    "Antwort:",
)


@dataclass
class Card:
    """Ein Schwachstellen-Eintrag."""

    title: str
    lines: list[str] = field(default_factory=list)


# --- Parsing -----------------------------------------------------------------


def normalize(text: str) -> str:
    """Ersetzt Zeichen, die die PDF-Schrift nicht darstellen kann."""
    for source, target in GLYPH_REPLACEMENTS.items():
        text = text.replace(source, target)
    # Fallback: alles, was die Kernschrift (Latin-1) nicht kann, durch "?" ersetzen statt abzubrechen
    return text.encode("latin-1", "replace").decode("latin-1")


def strip_markdown(text: str) -> str:
    """Entfernt Markdown-Auszeichnungen, behaelt den Text."""
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
    text = re.sub(r"\*(.+?)\*", r"\1", text)
    text = re.sub(r"`(.+?)`", r"\1", text)
    text = re.sub(r"\[\[(.+?)\]\]", r"\1", text)
    return text.strip()


def parse_cards(markdown: str) -> list[Card]:
    """Zerlegt schwachstellen.md in Karten.

    Jede `## `-Ueberschrift startet eine Karte. Der Vorlagen-Codeblock und der
    Platzhalter "(noch keine)" werden uebersprungen, damit ein leeres
    schwachstellen.md nicht als Karte durchrutscht.
    """
    cards: list[Card] = []
    current: Card | None = None
    in_code_block = False

    for raw_line in markdown.splitlines():
        line = raw_line.rstrip()

        if line.strip().startswith("```"):
            in_code_block = not in_code_block
            continue
        if in_code_block:
            continue

        if line.startswith("## "):
            heading = strip_markdown(line[3:])
            if heading.lower().startswith(("eintraege", "einträge")):
                current = None
                continue
            current = Card(title=heading)
            cards.append(current)
            continue

        if current is None:
            continue

        if line.strip() in ("", "---") or line.strip() == "(noch keine)":
            if line.strip() == "" and current.lines and current.lines[-1] != "":
                current.lines.append("")
            continue

        current.lines.append(strip_markdown(line))

    return [card for card in cards if card.lines]


# --- Rendering ---------------------------------------------------------------


class SchwachstellenPDF(FPDF):
    """A5-PDF mit Fusszeile."""

    def __init__(self, *, subtitle: str) -> None:
        super().__init__(orientation="P", unit="mm", format=PAGE_FORMAT)
        self.subtitle = subtitle
        self.set_margins(MARGIN_MM, MARGIN_MM, MARGIN_MM)
        self.set_auto_page_break(auto=True, margin=MARGIN_MM)
        self._register_fonts()

    def _register_fonts(self) -> None:
        """Laedt Arial fuer vollen Umlaut-Support; sonst Helvetica (Latin-1)."""
        if not FONT_REGULAR.exists():
            self.font_family_name = "Helvetica"
            return
        self.add_font(FONT_NAME, "", str(FONT_REGULAR))
        if FONT_BOLD.exists():
            self.add_font(FONT_NAME, "B", str(FONT_BOLD))
        if FONT_ITALIC.exists():
            self.add_font(FONT_NAME, "I", str(FONT_ITALIC))
        self.font_family_name = FONT_NAME

    def footer(self) -> None:
        self.set_y(-MARGIN_MM)
        self.set_font(self.font_family_name, "I", SIZE_FOOTER)
        self.set_text_color(130, 130, 130)
        self.cell(0, 5, f"{self.subtitle}  -  Seite {self.page_no()}", align="C")
        self.set_text_color(0, 0, 0)

    def text_block(self, text: str, *, height: float = LINE_HEIGHT_MM) -> None:
        """Schreibt einen umbrechenden Textblock und setzt x zurueck auf den Rand.

        Ohne new_x=LMARGIN laesst fpdf2 den Cursor am rechten Zellenrand stehen;
        das naechste multi_cell(w=0) haette dann keine Breite mehr.
        """
        self.multi_cell(
            0,
            height,
            text,
            align="L",
            new_x=XPos.LMARGIN,
            new_y=YPos.NEXT,
        )


def write_title_page(pdf: SchwachstellenPDF, card_count: int, stand: str) -> None:
    pdf.add_page()
    pdf.set_font(pdf.font_family_name, "B", SIZE_TITLE)
    pdf.text_block("Schwachstellen", height=8)
    pdf.set_font(pdf.font_family_name, "", SIZE_BODY)
    pdf.set_text_color(90, 90, 90)
    pdf.text_block(MODUL)
    pdf.text_block(f"{card_count} Eintraege  -  {stand}")
    pdf.set_text_color(0, 0, 0)
    pdf.ln(4)


def write_card(pdf: SchwachstellenPDF, card: Card, *, own_page: bool) -> None:
    """Rendert eine Karte. own_page=True erzwingt einen Seitenumbruch davor."""
    if own_page or pdf.get_y() > pdf.h - 60:
        pdf.add_page()

    pdf.set_font(pdf.font_family_name, "B", SIZE_HEADING)
    pdf.set_text_color(20, 20, 20)
    pdf.text_block(normalize(card.title), height=6.5)
    pdf.ln(1.5)

    for line in card.lines:
        if not line:
            pdf.ln(2)
            continue
        is_label = line.startswith(LABEL_PREFIXES)
        if is_label:
            pdf.set_font(pdf.font_family_name, "B", SIZE_LABEL)
            pdf.set_text_color(0, 0, 0)
        else:
            pdf.set_font(pdf.font_family_name, "", SIZE_BODY)
            pdf.set_text_color(40, 40, 40)
        pdf.text_block(normalize(line))

    pdf.set_text_color(0, 0, 0)
    pdf.ln(5)


def extract_stand(markdown: str) -> str:
    match = re.search(r"\*\*Stand:\*\*\s*([0-9]{4}-[0-9]{2}-[0-9]{2})", markdown)
    return f"Stand {match.group(1)}" if match else "Stand unbekannt"


# --- Einstiegspunkt ----------------------------------------------------------


def build_pdf(*, retain_mode: bool) -> tuple[Path, int]:
    if not SOURCE_FILE.exists():
        raise FileNotFoundError(f"Quelldatei fehlt: {SOURCE_FILE}")

    source = RETAIN_SOURCE_FILE if retain_mode and RETAIN_SOURCE_FILE.exists() else SOURCE_FILE
    markdown = source.read_text(encoding="utf-8")
    cards = parse_cards(markdown)
    stand = extract_stand(markdown)

    batch_nr = None
    if retain_mode:
        state = load_retain_state()
        exported = {title for batch in state["batches"] for title in batch["karten"]}
        cards = [card for card in cards if card.title not in exported]
        if not cards:
            return None, 0
        batch_nr = len(state["batches"]) + 1
        target = BASE_DIR / f"retain_export_{batch_nr:03d}.pdf"
    else:
        target = BASE_DIR / "schwachstellen.pdf"
    subtitle = f"Karten-Export {MODUL}" if retain_mode else f"Schwachstellen {MODUL}"

    pdf = SchwachstellenPDF(subtitle=subtitle)

    if not cards:
        pdf.add_page()
        pdf.set_font(pdf.font_family_name, "B", SIZE_HEADING)
        pdf.text_block("Noch keine Schwachstellen erfasst", height=7)
        pdf.set_font(pdf.font_family_name, "", SIZE_BODY)
        pdf.set_text_color(90, 90, 90)
        pdf.text_block(
            'Eintraege entstehen bei "Einheit beenden", sobald in einem '
            "Mini-Fallszenario eine echte Luecke sichtbar wird."
        )
    else:
        if not retain_mode:
            write_title_page(pdf, len(cards), stand)
        for card in cards:
            write_card(pdf, card, own_page=retain_mode)

    pdf.output(str(target))
    if retain_mode:
        state["batches"].append(
            {"nr": batch_nr, "datum": date.today().isoformat(), "datei": target.name,
             "karten": [card.title for card in cards]}
        )
        save_retain_state(state)
    return target, len(cards)


def load_retain_state() -> dict:
    if RETAIN_STATE_FILE.exists():
        return json.loads(RETAIN_STATE_FILE.read_text(encoding="utf-8"))
    return {"batches": []}


def save_retain_state(state: dict) -> None:
    RETAIN_STATE_FILE.write_text(
        json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


def build_master_pdf() -> tuple[Path, int]:
    """Alle Retain-Karten in einer Datei (retain_master.pdf), ohne Buchfuehrung zu aendern.

    Paket 001 stammte noch aus schwachstellen.md, daher werden dessen Karten von dort ergaenzt.
    """
    state = load_retain_state()
    first_titles = set(state["batches"][0]["karten"]) if state["batches"] else set()
    legacy = [c for c in parse_cards(SOURCE_FILE.read_text(encoding="utf-8")) if c.title in first_titles]
    cards = legacy + parse_cards(RETAIN_SOURCE_FILE.read_text(encoding="utf-8"))
    target = BASE_DIR / "retain_master.pdf"
    pdf = SchwachstellenPDF(subtitle=f"Karten-Master {MODUL} (alle Karten)")
    for card in cards:
        write_card(pdf, card, own_page=True)
    pdf.output(str(target))
    return target, len(cards)


def main() -> int:
    if "--master" in sys.argv[1:]:
        target, count = build_master_pdf()
        print(f"{target.name} erstellt - {count} Abschnitte (Buchfuehrung unveraendert)")
        return 0
    retain_mode = "--retain" in sys.argv[1:]
    try:
        target, count = build_pdf(retain_mode=retain_mode)
    except FileNotFoundError as error:
        print(f"FEHLER: {error}", file=sys.stderr)
        return 1
    except OSError as error:
        print(f"FEHLER beim Schreiben des PDF: {error}", file=sys.stderr)
        return 1

    if target is None:
        print("Keine neuen Retain-Karten seit dem letzten Export - kein PDF erstellt")
        return 0
    label = "neue Abschnitte" if retain_mode else "Eintraege"
    print(f"{target.name} erstellt - {count} {label}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
