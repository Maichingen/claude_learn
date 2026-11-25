# claude_learn – Lernsystem für Fernstudien-Klausuren mit Claude Code

Ein fertiges Regelwerk, mit dem Claude Code als persönlicher Lerncoach für **ein Modul** arbeitet: Erstkontakt, verteilte Wiederholung, Fehleranalyse, Klausursimulationen, tägliche Auswertung. Es ist über ein ganzes Modul erprobt und neutral, ohne Lernstände oder Stoff.

## So startest du
1. Repo als **privates** Repo kopieren (Template oder Fork), eins pro Modul.
2. Die Studienhefte (PDF) in den Ordner legen. Die `.gitignore` hält sie aus dem Repo heraus.
3. Claude Code im Ordner starten und **„Neues Modul“** schreiben. Claude führt durch `SETUP.md`: Rahmen klären, Hefte zusammenfassen, Klausurrelevanz, Cluster, Plan, Automatik.
4. Danach jeden Tag **„Weitermachen“**. Claude misst die Zeit, wählt den nächsten Schritt und pflegt alle Dateien selbst.

## Was drin ist
| Datei | Inhalt |
|---|---|
| `lernsystem_logik.md` | **alle Regeln**: Tagesablauf, Methoden je Situation, S-Wert, Wiederholungstakt, Bewertung, Sims, Abend-Analyse, Herkunft der Regeln |
| `CLAUDE.md` | Rolle, Kommunikation, Befehle (lädt die Regeln) |
| `SETUP.md` | Einrichtung eines neuen Moduls |
| `tagesanalyse.py` | Sessionstart-Check, Tagesbericht, Wochenbilanz (`--start`, `--woche`) |
| `export_schwachstellen.py` | Schwachstellen als Handy-PDF (braucht `pip install fpdf2`) |
| `config.md`, `einstellungen.json` | Modul-Einstellungen (beim Setup ausgefüllt) |
| übrige `.md`/`.csv` | leere Arbeitsdateien |

## Kernideen in einem Satz je Regel
- Gelernt wird nur durch **Abruf in realistischen Fällen**, nicht durch Lesen.
- **Zuerst frei antworten**, Hilfen gibt es erst nach einem Fehlversuch.
- Der **S-Wert** je Cluster steuert, wann wiederholt wird, und steigt nur durch verzögerte, freie Abrufe.
- **Listen** werden mit Bild oder eigenen Worten gelernt, nicht mit Anfangsbuchstaben.
- **Klausurphase**: jeden Tag eine ausformulierte Aufgabe, dazu zwei Vollsimulationen.
- Geplant wird mit der **gemessenen** Lernzeit, nicht mit der gewünschten.
