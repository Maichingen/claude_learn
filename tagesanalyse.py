"""Kennzahlen für Sessionstart, Abend-Analyse und Wochenbilanz.

Regeln: lernsystem_logik.md (Kap. 3.2 Sessionstart, 6.1 S-Takt, 8.2 S-Wert, 11 Analyse).

Aufruf:  python3 tagesanalyse.py               Tagesbericht heute (Europe/Berlin)
         python3 tagesanalyse.py 26.10.        Tagesbericht für einen Tag (auch 26.10.2026 oder 2026-10-26)
         python3 tagesanalyse.py --start       Sessionstart: Fälligkeit, Blitz-Zähler, Zerfall, [R], Wiederabfragen
         python3 tagesanalyse.py --woche       Wochenbilanz über 14 Tage mit Mindest-Stichproben

Quellen: zeitlog.md (Netto-Minuten je Block, 💻 = Pflicht-/Tool-Aufgabe), abrufe.csv (einzige Rohquelle für
Abfragen), fortschritt.md (S-Werte, offene [R] und Wiederabfragen) und – falls vorhanden – das
Chat-Transkript, ausgewertet nur innerhalb geloggter Lernblöcke und nur als Summen.
"""
import csv
import datetime as dt
import glob
import json
import math
import os
import re
import statistics
import sys
from collections import Counter, defaultdict

BASE = os.path.dirname(os.path.abspath(__file__))

try:
    from zoneinfo import ZoneInfo
    BERLIN = ZoneInfo("Europe/Berlin")
except Exception:  # pragma: no cover
    BERLIN = None

FELDER = ["datum", "zeit", "geraet", "cluster", "typ", "methode", "ergebnis", "fehlerbild",
          "punkte", "max", "schaetzung", "konfidenz", "item", "anlass", "notiz"]
S_FAELLE = {"Tag1", "Exit", "R1", "R2", "Schreib", "Sim"}   # verzögerte Fälle, ändern S (Kap. 8.2)
VERZOEGERT = S_FAELLE | {"Blitz"}                            # Abruf nach mindestens einer Nacht
BUCHUNGEN = {"S+1", "Zerfall", "Zerfall-ausgesetzt"}                               # keine Abfragen
WOCHENTAG = ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]
# Modul-Einstellungen aus einstellungen.json (legt Claude beim Setup an, siehe SETUP.md)
def _einstellungen():
    pfad = os.path.join(BASE, "einstellungen.json")
    try:
        with open(pfad, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError):
        return {}


_E = _einstellungen()
EK_START = dt.date.fromisoformat(_E["ek_start"]) if _E.get("ek_start") else None   # Fahrplan-Start
EK_PRO_WOCHE = float(_E.get("ek_pro_woche", 6))   # Soll Erstkontakt-Teile pro Woche (lernplan.md)


def to_berlin(ts_utc):
    if BERLIN:
        return ts_utc.astimezone(BERLIN).replace(tzinfo=None)
    # Fallback ohne zoneinfo: Sommerzeit grob von April bis zum letzten Oktobersonntag
    off = 2 if 4 <= ts_utc.month <= 9 or (ts_utc.month == 10 and ts_utc.day < 25) else 1
    return (ts_utc + dt.timedelta(hours=off)).replace(tzinfo=None)


def heute():
    return to_berlin(dt.datetime.now(dt.timezone.utc)).date()


DATUM_RE = re.compile(r"(\d{1,2})\.(\d{1,2})\.?(\d{4})?")
ISO_RE = re.compile(r"(\d{4})-(\d{2})-(\d{2})")


def parse_datum(text, jahr=None):
    """'26.10.', '26.10', '26.10.2026', '2026-10-26', '29.10.–30.10.' (erstes Datum) -> date oder None."""
    if not text:
        return None
    m = ISO_RE.search(text)
    if m:
        return dt.date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
    m = DATUM_RE.search(text)
    if not m:
        return None
    try:
        return dt.date(int(m.group(3)) if m.group(3) else (jahr or heute().year), int(m.group(2)), int(m.group(1)))
    except ValueError:
        return None


def tagstr(d):
    return f"{WOCHENTAG[d.weekday()]} {d.day:02d}.{d.month:02d}."


def cluster_liste(text):
    return re.findall(r"C\d{2}", text or "")


# ---------- zeitlog.md ----------

BLOCKTYP = [("EK", r"\bEK\b|Häppchen|Kernkarte"), ("Blitz", r"Blitz|Wiederabfrage"), ("Tag1", r"Tag-1|Exit"),
            ("R", r"\bR[12]\b"), ("Rettung", r"Rettung"), ("Sim", r"\bSim\b|Simulation"),
            ("Schreib", r"Schreib|EA\b|Einsendeaufgabe")]


def blocktyp(text):
    if "💻" in text:
        return "H4"
    treffer = [(m.start(), typ) for typ, muster in BLOCKTYP for m in [re.search(muster, text)] if m]
    return min(treffer)[1] if treffer else "sonst"


def zeitlog():
    """Blöcke aus zeitlog.md: datum, start, ende, netto (None = unbekannt), typ. Σ-Zeilen werden ignoriert."""
    path = os.path.join(BASE, "zeitlog.md")
    bloecke = []
    if not os.path.exists(path):
        return bloecke
    for line in open(path, encoding="utf-8"):
        if not line.startswith("|"):
            continue
        z = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(z) < 6 or z[0].startswith("**"):
            continue
        d = parse_datum(z[0])
        if not d:
            continue
        m = re.search(r"(\d+)", z[4])
        netto = int(m.group(1)) if m and "unbekannt" not in z[4] else None
        bloecke.append({"datum": d, "start": z[1], "ende": z[2], "netto": netto, "typ": blocktyp(z[5])})
    return bloecke


def tageszeit(d, bloecke):
    """dict gesamt/stoff/h4/ek in Minuten oder None, wenn für den Tag nichts geloggt ist."""
    werte = [b for b in bloecke if b["datum"] == d and b["netto"] is not None]
    if not werte:
        return None
    summe = lambda f: sum(b["netto"] for b in werte if f(b))
    return {"gesamt": summe(lambda b: True), "h4": summe(lambda b: b["typ"] == "H4"),
            "stoff": summe(lambda b: b["typ"] != "H4"), "ek": summe(lambda b: b["typ"] == "EK")}


def median_tage(bis, tage, bloecke, feld="gesamt"):
    """Median über die `tage` Tage vor `bis` (ohne `bis`); Tage ohne Eintrag zählen nicht mit."""
    werte = [t[feld] for i in range(1, tage + 1) for t in [tageszeit(bis - dt.timedelta(days=i), bloecke)] if t]
    return (statistics.median(werte) if werte else None), tage - len(werte)


# ---------- abrufe.csv ----------

def abrufe():
    """Alle Zeilen aus abrufe.csv (Datum als date) + Anzahl defekter Zeilen (werden nicht gelesen)."""
    path = os.path.join(BASE, "abrufe.csv")
    rows, defekt = [], 0
    if not os.path.exists(path):
        return rows, defekt
    with open(path, encoding="utf-8", newline="") as f:
        r = csv.reader(f, delimiter=";")
        kopf = [k.strip() for k in (next(r, None) or [])]
        for z in r:
            if not "".join(z).strip():
                continue
            if len(z) < 7:
                defekt += 1
                continue
            if len(z) > len(kopf):
                z = z[:len(kopf) - 1] + [";".join(z[len(kopf) - 1:])]
            e = dict(zip(kopf, [c.strip() for c in z] + [""] * (len(kopf) - len(z))))
            for k in FELDER:
                e.setdefault(k, "")
            e["datum"] = parse_datum(e["datum"])
            if e["datum"] is None:
                defekt += 1
                continue
            rows.append(e)
    rows.sort(key=lambda e: (e["datum"], e["zeit"]))
    return rows, defekt


def zahl(text):
    try:
        return float(text.replace(",", "."))
    except (ValueError, AttributeError):
        return None


def wilson(k, n, z=1.96):
    if not n:
        return (0.0, 0.0)
    p = k / n
    mitte = (p + z * z / (2 * n)) / (1 + z * z / n)
    rand = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / (1 + z * z / n)
    return (100 * max(0.0, mitte - rand), 100 * min(1.0, mitte + rand))


def quote(rows, ki=False):
    n = len(rows)
    if not n:
        return "–"
    k = sum(1 for r in rows if r["ergebnis"] == "frei")
    text = f"{k}/{n} frei ({100 * k / n:.0f} %)"
    if ki:
        lo, hi = wilson(k, n)
        text += f", 95 %-Bereich {lo:.0f}–{hi:.0f} %"
    return text


def faelle(rows):
    """Verzögerte Fälle mit Punkten, je (datum, cluster, typ) zusammengefasst -> Liste (datum, cluster, typ, methode, %)."""
    summe = defaultdict(lambda: [0.0, 0.0, ""])
    for r in rows:
        p, m = zahl(r["punkte"]), zahl(r["max"])
        if r["typ"] in S_FAELLE and p is not None and m:
            s = summe[(r["datum"], r["cluster"], r["typ"])]
            s[0] += p
            s[1] += m
            s[2] = s[2] or r["methode"]
    return [(d, c, t, s[2], 100 * s[0] / s[1]) for (d, c, t), s in sorted(summe.items())]


def kalibrierung(rows):
    """Geschätzte gegen erreichte Punkte je Fall (Kap. 8.1) -> (Ø Abweichung in Pkt, n) oder None."""
    faelle_ = defaultdict(lambda: [0.0, None])
    for r in rows:
        p, s = zahl(r["punkte"]), zahl(r["schaetzung"])
        if r["typ"] in S_FAELLE and p is not None:
            f = faelle_[(r["datum"], r["cluster"], r["typ"])]
            f[0] += p
            if s is not None:
                f[1] = s
    diffs = [s - p for p, s in faelle_.values() if s is not None]
    return (statistics.mean(diffs), len(diffs)) if diffs else None


def kalib_text(rows):
    k = kalibrierung(rows)
    if not k:
        return "noch keine Schätzungen"
    d, n = k
    richtung = "zu optimistisch" if d > 0.5 else "zu vorsichtig" if d < -0.5 else "treffsicher"
    return f"Ø {d:+.1f}".replace(".", ",") + f" Pkt je Fall ({richtung}, n={n}{'' if n >= 5 else ', wenig Daten'})"


# ---------- fortschritt.md ----------

def fortschritt():
    """Cluster (S, Status, letzte Wiederholung) + offene [R]- und Wiederabfrage-Zeilen."""
    path = os.path.join(BASE, "fortschritt.md")
    cluster, r_offen, wa_offen = {}, [], []
    if not os.path.exists(path):
        return cluster, r_offen, wa_offen
    abschnitt = ""
    for line in open(path, encoding="utf-8"):
        if line.startswith("## "):
            abschnitt = line[3:].strip().lower()
            continue
        if not line.startswith("| "):
            continue
        z = [c.strip() for c in line.strip().strip("|").split("|")]
        if not z or not re.match(r"C\d{2}", z[0]):
            continue
        if abschnitt.startswith("cluster-tracking") and len(z) >= 7:
            s = re.match(r"(\d+)", z[4])
            cluster[z[0][:3]] = {"name": z[1], "status": z[2], "S": int(s.group(1)) if s else 1,
                                 "letzte": parse_datum(z[6])}
        elif abschnitt.startswith("rückfall") and len(z) >= 4 and "stabil" not in z[-1]:
            r_offen.append(f"{z[0]} {z[1]}")
        elif abschnitt.startswith("wiederabfrage") and len(z) >= 3 \
                and not z[-1].startswith("✅") and "erledigt" not in z[-1]:
            kurz = re.sub(r"\*\*", "", z[1])
            wa_offen.append(f"{z[0]}: {kurz[:70]}{'…' if len(kurz) > 70 else ''}")
    return cluster, r_offen, wa_offen


def coverage_offen():
    """Anzahl Einzelthemen ohne Abruf (☐) und nur teilweise (◐) in der Einzelthema-Coverage."""
    path = os.path.join(BASE, "fortschritt.md")
    if not os.path.exists(path):
        return None, None
    text = open(path, encoding="utf-8").read()
    teil = text.split("## Einzelthema-Coverage", 1)[-1].split("\n## ", 1)[0]
    return teil.count("☐"), teil.count("◐")


# ---------- Fälligkeit, Blitz-Zähler, Zerfall ----------

def takt(s):
    """(ideal ab Tag, spätestens Tag) laut S-Takt (Kap. 6.1)."""
    if s <= 2:
        return 2, 3
    if s <= 4:
        return 4, 5
    return 6, 7


def letzter_abruf(rows, cid, fallback=None):
    tage = [r["datum"] for r in rows if cid in cluster_liste(r["cluster"]) and r["typ"] not in BUCHUNGEN]
    kandidaten = [d for d in tage + [fallback] if d]
    return max(kandidaten) if kandidaten else None


def blitz_zaehler(rows, cid):
    """Tage mit ausschließlich freiem Blitz seit dem letzten S-Ereignis (Kap. 8.2, Stelle 2)."""
    eigene = [r for r in rows if cid in cluster_liste(r["cluster"])]
    resets = [(r["datum"], r["zeit"]) for r in eigene if r["typ"] in (S_FAELLE | BUCHUNGEN) - {"Zerfall-ausgesetzt"}]
    seit = max(resets) if resets else None
    tage = defaultdict(list)
    for r in eigene:
        if r["typ"] == "Blitz" and (seit is None or (r["datum"], r["zeit"]) > seit):
            tage[r["datum"]].append(r["ergebnis"])
    zaehler = 0
    for d in sorted(tage):
        zaehler = zaehler + 1 if all(e == "frei" for e in tage[d]) else 0
    return zaehler


def blitz_mit_wortbank(rows, cid):
    """True, wenn im aktuellen Zählfenster ein Blitz mit Wortbank liegt (S+1 dann nur bis S 3, Kap. 12)."""
    eigene = [r for r in rows if cid in cluster_liste(r["cluster"])]
    resets = [(r["datum"], r["zeit"]) for r in eigene if r["typ"] in (S_FAELLE | BUCHUNGEN) - {"Zerfall-ausgesetzt"}]
    seit = max(resets) if resets else None
    return any(r["typ"] == "Blitz" and "wortbank" in r.get("notiz", "").lower()
               and (seit is None or (r["datum"], r["zeit"]) > seit) for r in eigene)


def zerfall_faellig(rows, cid, letzte, d):
    if not letzte or (d - letzte).days < 8:
        return False
    gebucht = [r["datum"] for r in rows if r["typ"] in ("Zerfall", "Zerfall-ausgesetzt") and cid in cluster_liste(r["cluster"])
               and r["datum"] > letzte]
    return not gebucht or (d - max(gebucht)).days >= 7


def faelligkeit(d, rows, cluster):
    """Liste je begonnenem Cluster: (dringlichkeit, cid, S, tage, ideal, spaet, zaehler)."""
    liste = []
    for cid, c in sorted(cluster.items()):
        if c["status"].startswith("[ ]"):
            continue
        letzte = letzter_abruf(rows, cid, c["letzte"])
        if not letzte:
            continue
        tage = (d - letzte).days
        ideal, spaet = takt(c["S"])
        liste.append({"cid": cid, "S": c["S"], "tage": tage, "ideal": ideal, "spaet": spaet,
                      "zaehler": blitz_zaehler(rows, cid), "letzte": letzte,
                      "zerfall": zerfall_faellig(rows, cid, letzte, d)})
    return sorted(liste, key=lambda x: (x["tage"] - x["spaet"], x["tage"]), reverse=True)


def tempo(d, rows):
    """EK-Teile seit Fahrplan-Start gegen das Soll (Vorziehen bei Vorsprung, Kap. 11.1)."""
    if EK_START is None:
        return "kein Fahrplan-Start in einstellungen.json (ek_start)"
    ist = len({(r["datum"], c) for r in rows if r["typ"] in ("EK-Sofort", "EK-Fall") and EK_START <= r["datum"] <= d
               for c in cluster_liste(r["cluster"])})
    soll = round(EK_PRO_WOCHE * max(0, (d - EK_START).days) / 7)
    diff = ist - soll
    urteil = (f"Vorsprung +{diff} → Fahrplan vorziehen" if diff > 0 else
              "im Plan" if diff == 0 else f"Rückstand {diff} (Neuplanung sonntags)")
    return f"{ist} EK-Teile seit {EK_START.day:02d}.{EK_START.month:02d}. · Soll {soll} ({EK_PRO_WOCHE}/Woche) → {urteil}"


def hier_weitermachen():
    path = os.path.join(BASE, "session_log.md")
    if not os.path.exists(path):
        return []
    zeilen, drin = [], False
    for line in open(path, encoding="utf-8"):
        if "HIER WEITERMACHEN" in line and "~~" not in line:
            if drin:
                break
            drin = True
        elif drin and line.startswith("#"):
            break
        if drin and line.strip():
            zeilen.append(line.rstrip())
    return zeilen


def bericht_start(d):
    rows, defekt = abrufe()
    cluster, r_offen, wa_offen = fortschritt()
    liste = faelligkeit(d, rows, cluster)
    muss = [x for x in liste if x["tage"] >= x["spaet"]]
    kann = [x for x in liste if x["ideal"] <= x["tage"] < x["spaet"]]
    rest = [x for x in liste if x["tage"] < x["ideal"]]
    fmt = lambda x: f"{x['cid']} (S{x['S']}, Tag {x['tage']}/{x['spaet']}, Blitz-Zähler {x['zaehler']}/2)"
    begonnen = sum(1 for c in cluster.values() if not c["status"].startswith("[ ]"))
    out = [f"## Sessionstart {tagstr(d)} · {begonnen}/{len(cluster)} Cluster begonnen", ""]
    ueber = [x for x in muss if x["tage"] > x["spaet"]]
    if ueber:
        out.append("- **Überfällig:** " + " · ".join(fmt(x) for x in ueber))
    heute_spaet = [x for x in muss if x["tage"] == x["spaet"]]
    if heute_spaet:
        out.append("- **Heute spätestens:** " + " · ".join(fmt(x) for x in heute_spaet))
    if kann:
        out.append("- **Kann heute (ideal):** " + " · ".join(fmt(x) for x in kann))
    if rest:
        out.append("- Noch nicht fällig: " + " · ".join(f"{x['cid']} (S{x['S']}, Tag {x['tage']})" for x in rest))
    out.append(f"- **Blitz-Bedarf:** {len(muss)} Pflicht-Cluster ≈ {2 * len(muss)} Min"
               + (" → über dem Deckel 15: Überhang morgen" if 2 * len(muss) > 15 else ""))
    s_plus = [x["cid"] for x in liste if x["zaehler"] >= 2
              and x["S"] < (3 if blitz_mit_wortbank(rows, x["cid"]) else 6)]
    out.append("- **S+1 buchen:** " + (", ".join(s_plus) if s_plus else "–"))
    zerfall = [x["cid"] for x in liste if x["zerfall"]]
    out.append("- **Zerfall anwenden (S −1, einmal):** " + (", ".join(zerfall) if zerfall else "–"))
    out.append("- **Offene [R]:** " + ("; ".join(r_offen) if r_offen else "–"))
    out.append(f"- **Offene Wiederabfragen ({len(wa_offen)}):** " + ("; ".join(wa_offen) if wa_offen else "–"))
    offen, teil = coverage_offen()
    if offen is not None:
        out.append(f"- Coverage: {offen} Themen ohne Abruf, {teil} nur teilweise")
    out.append(f"- Tempo (bis gestern): {tempo(d - dt.timedelta(days=1), rows)}")
    if defekt:
        out.append(f"- ⚠️ {defekt} defekte Zeile(n) in abrufe.csv übersprungen")
    hw = hier_weitermachen()
    if hw:
        out += ["", *hw[:8]]
    return "\n".join(out)


# ---------- Chat-Transkript (nur innerhalb geloggter Blöcke, nur Summen) ----------

def fenster(d, bloecke):
    """Zeitfenster der geloggten Blöcke eines Tages (±5 Min)."""
    out = []
    for b in bloecke:
        if b["datum"] != d:
            continue
        try:
            a = dt.datetime.combine(d, dt.datetime.strptime(b["start"], "%H:%M").time())
        except ValueError:
            continue
        try:
            e = dt.datetime.combine(d, dt.datetime.strptime(b["ende"], "%H:%M").time())
        except ValueError:
            e = a + dt.timedelta(minutes=b["netto"] or 0)
        out.append((a - dt.timedelta(minutes=5), e + dt.timedelta(minutes=5)))
    return out


def transkript(d, bloecke):
    files = glob.glob(f"/root/.claude/projects/*{os.path.basename(BASE)}*/*.jsonl")
    if not files:
        return None
    zeiten = fenster(d, bloecke)
    if not zeiten:
        return {"n": 0}
    msgs = []
    for f in files:
        for line in open(f, encoding="utf-8", errors="ignore"):
            try:
                e = json.loads(line)
            except ValueError:
                continue
            if e.get("type") != "user" or not e.get("timestamp") or e.get("isSidechain"):
                continue
            c = e.get("message", {}).get("content")
            if isinstance(c, list):
                if any(isinstance(x, dict) and x.get("type") == "tool_result" for x in c):
                    continue
                txt = " ".join(x.get("text", "") for x in c if isinstance(x, dict) and x.get("type") == "text")
            else:
                txt = str(c or "")
            txt = re.sub(r"\[Image[^\]]*\]", "", txt).strip()
            if not txt or txt.startswith("<") or "Stop hook" in txt or txt.startswith("This session is being continued"):
                continue
            t = to_berlin(dt.datetime.fromisoformat(e["timestamp"].replace("Z", "+00:00")))
            if t.date() == d and any(a <= t <= b for a, b in zeiten):
                msgs.append((t, txt))
    if not msgs:
        return {"n": 0}
    klein = lambda x: x.lower()
    ka = sum(1 for _, x in msgs if re.search(r"\bkeine ahnung\b", klein(x))
             or (len(x) < 40 and re.search(r"wei(ß|ss) (ich )?(es )?nicht", klein(x))))
    frust = sum(1 for _, x in msgs if re.search(r"zu schwer|zu viel stoff|null fortschritt|bringt (doch |eh )?nichts|frustriert",
                                                  klein(x)))
    spaet = sum(1 for t, _ in msgs if (t.hour, t.minute) >= (21, 30))
    laengen = [len(x) for _, x in msgs if len(x) < 2000]
    return {"n": len(msgs), "keine_ahnung": ka, "frust": frust, "spaet": spaet,
            "laenge": sum(laengen) / max(1, len(laengen))}


# ---------- Berichte ----------

def bericht_tag(d):
    bloecke = zeitlog()
    rows, defekt = abrufe()
    t = tageszeit(d, bloecke)
    med, ohne = median_tage(d, 14, bloecke)
    out = [f"## Tagesanalyse {tagstr(d)}", ""]
    if t:
        out.append(f"- **Lernzeit:** {t['gesamt']} Min (Stoff {t['stoff']}, davon EK {t['ek']} · Pflicht/Tool {t['h4']}) · "
                   f"Median 14 Tage {med:.0f} Min" if med is not None else f"- **Lernzeit:** {t['gesamt']} Min")
        out.append("  - Minimaltag (20 Min) " + ("✅ erfüllt" if t["gesamt"] >= 20 else "❌ nicht erfüllt"))
    else:
        out.append("- **Lernzeit:** ? (kein Eintrag im Zeitlog)")
    if ohne:
        out.append(f"  - {ohne} der letzten 14 Tage ohne Zeitlog-Eintrag (zählen im Median nicht)")
    woche = [tageszeit(d - dt.timedelta(days=i), bloecke) for i in range(7)]
    out.append(f"- **7 Tage:** {sum(w['gesamt'] for w in woche if w)} Min, davon Stoff {sum(w['stoff'] for w in woche if w)} "
               f"({sum(1 for w in woche if w)} Tage mit Eintrag)")

    heute_rows = [r for r in rows if r["datum"] == d and r["typ"] not in BUCHUNGEN]
    verz = [r for r in heute_rows if r["typ"] in VERZOEGERT]
    sofort = [r for r in heute_rows if r["typ"] not in VERZOEGERT]
    out.append(f"- **Abrufe heute:** verzögert {quote(verz)} · sofort (EK, Rettung, Kriterium) {quote(sofort)}")
    nach_typ = defaultdict(list)
    for r in heute_rows:
        nach_typ[r["typ"]].append(r)
    for typ, rr in sorted(nach_typ.items()):
        out.append(f"  - {typ}: {quote(rr)}")
    for fd, c, typ, meth, p in faelle([r for r in rows if r["datum"] == d]):
        out.append(f"  - Fall {c} {typ} ({meth or '?'}): {p:.0f} %")
    if any(r["schaetzung"] for r in heute_rows):
        out.append(f"  - Selbsteinschätzung heute: {kalib_text([r for r in rows if r['datum'] == d])}")
    fb = Counter(r["fehlerbild"] for r in heute_rows if r["fehlerbild"])
    if fb:
        out.append("- **Fehlerbilder heute:** " + ", ".join(f"{k}×{v}" for k, v in fb.most_common()))
    out.append(f"- **Tempo:** {tempo(d, rows)}")
    w7 = [r for r in rows if 0 <= (d - r["datum"]).days < 7 and r["typ"] not in BUCHUNGEN]
    out.append(f"- **Blitz 7 Tage:** {quote([r for r in w7 if r['typ'] == 'Blitz'], ki=True)}")
    fb7 = Counter(r["fehlerbild"] for r in w7 if r["fehlerbild"])
    if fb7:
        out.append("  - Fehlerbilder 7 Tage: " + ", ".join(f"{k}×{v}" for k, v in fb7.most_common()))

    tr = transkript(d, bloecke)
    if tr is None:
        out.append("- **Chat-Verhalten:** Transkript nicht verfügbar")
    elif tr["n"] == 0:
        out.append("- **Chat-Verhalten:** keine Nachrichten in geloggten Lernblöcken")
    else:
        out.append(f"- **Chat-Verhalten (nur Lernblöcke):** {tr['n']} Nachrichten · „keine Ahnung“ {tr['keine_ahnung']}× · "
                   f"Frust-Signale {tr['frust']}× · nach 21:30 {tr['spaet']} · Ø Länge {tr['laenge']:.0f} Zeichen")
    if defekt:
        out.append(f"- ⚠️ {defekt} defekte Zeile(n) in abrufe.csv übersprungen")
    return "\n".join(out)


def bericht_woche(d):
    bloecke = zeitlog()
    rows, defekt = abrufe()
    cluster, _, _ = fortschritt()
    fenster14 = [r for r in rows if 0 <= (d - r["datum"]).days < 14 and r["typ"] not in BUCHUNGEN]
    tage = [tageszeit(d - dt.timedelta(days=i), bloecke) for i in range(14)]
    mit = [t for t in tage if t]
    med, _ = median_tage(d + dt.timedelta(days=1), 14, bloecke)
    out = [f"## Wochenbilanz bis {tagstr(d)} (14 Tage)", ""]
    out.append(f"- **Lernzeit:** {sum(t['gesamt'] for t in mit)} Min an {len(mit)} Tagen mit Eintrag · "
               f"Median {med:.0f} Min/Tag" if med is not None else "- **Lernzeit:** keine Daten")
    if mit:
        stoff = sum(t["stoff"] for t in mit)
        ek = sum(t["ek"] for t in mit)
        out.append(f"  - Stoff {stoff} · Pflicht/Tool {sum(t['h4'] for t in mit)} · EK-Anteil am Stoff "
                   f"{100 * ek / stoff:.0f} %" if stoff else "  - kein Stoff geloggt")
    blitz = [r for r in fenster14 if r["typ"] == "Blitz"]
    hinweis = "" if len(blitz) >= 20 else " → zu wenig Daten (< 20) für eine Regeländerung"
    out.append(f"- **Blitz-Freiquote:** {quote(blitz, ki=True)}{hinweis}")
    fl = faelle(fenster14)
    nach_meth = defaultdict(list)
    for _, _, _, meth, p in fl:
        nach_meth[meth or "?"].append(p)
    if nach_meth:
        out.append("- **Verzögerte Fälle (Ø %):** " + " · ".join(
            f"{m}: {statistics.mean(v):.0f} % (n={len(v)}{'' if len(v) >= 3 else ', zu wenig'})" for m, v in nach_meth.items()))
    out.append(f"- **Selbsteinschätzung:** {kalib_text(fenster14)}")
    fehler = [r for r in fenster14 if r["fehlerbild"]]
    if fehler:
        fb = Counter(r["fehlerbild"] for r in fehler)
        out.append(f"- **Fehlerbilder (n={len(fehler)}{'' if len(fehler) >= 10 else ', zu wenig'}):** "
                   + ", ".join(f"{k} {100 * v / len(fehler):.0f} %" for k, v in fb.most_common()))
    verz = [r for r in fenster14 if r["typ"] in VERZOEGERT]
    frueh = [r for r in verz if r["zeit"] < "21:00"]
    spaet = [r for r in verz if r["zeit"] >= "21:00"]
    out.append(f"- **Freiquote vor/ab 21 Uhr:** {quote(frueh)} / {quote(spaet)}"
               + ("" if min(len(frueh), len(spaet)) >= 10 else " → zu wenig Daten"))
    out.append(f"- **Tempo:** {tempo(d, rows)}")
    offen = sorted(cid for cid, c in cluster.items() if c["status"].startswith("[ ]"))
    eks = {c for r in fenster14 if r["typ"] in ("EK-Sofort", "EK-Fall") for c in cluster_liste(r["cluster"])}
    out.append(f"- **EK:** {len(eks)} Cluster in 14 Tagen · offen {len(offen)} ({', '.join(offen)})")
    for pro_woche in (6, 5, 4):
        if offen:
            ende = d + dt.timedelta(days=math.ceil(7 * len(offen) / pro_woche))
            out.append(f"  - bei {pro_woche} EK/Woche: EK-Ende ≈ {tagstr(ende)}")
    o, t = coverage_offen()
    if o is not None:
        out.append(f"- **Nie-abgerufen-Check (kein Thema ohne Abruf):** {o} Themen ohne Abruf, {t} nur teilweise")
    if defekt:
        out.append(f"- ⚠️ {defekt} defekte Zeile(n) in abrufe.csv übersprungen")
    return "\n".join(out)


if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "--start":
        print(bericht_start(heute()))
    elif args and args[0] == "--woche":
        print(bericht_woche(parse_datum(args[1]) if len(args) > 1 else heute()))
    else:
        tag = parse_datum(args[0]) if args else heute()
        if tag is None:
            sys.exit(f"Unbekanntes Datum: {args[0]} (erwartet 26.10., 26.10.2026 oder 2026-10-26)")
        print(bericht_tag(tag))
