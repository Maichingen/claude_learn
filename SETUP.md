# Setup – neues Modul einrichten

Claude führt diese Schritte der Reihe nach aus, **jeweils auf „Go“ des Users**. Jeder Schritt endet mit einer kurzen Bestätigung.

## Schritt 0 – Rahmen klären
Diese Fragen stellt Claude, eine nach der anderen:
1. Wie heißt das Modul, und an welcher Hochschule?
2. Wie sieht die Klausur aus (Dauer, Punkte, Aufgabenzahl, Fragetyp, getippt/handschriftlich, Skizzen)?
3. Ist der Termin fix (Datum) oder flexibel (schreibbar, wann du bereit bist)?
4. Wie viel Zeit hast du pro Woche, und lernst du eher am Handy oder am Laptop?
5. Welche Note willst du mindestens? Wie lautet der Notenschlüssel?
6. Welche 2–3 Filme, Bücher oder Spiele magst du? Daraus baut Claude die Merkhilfen.

Danach schreibt Claude `config.md` und `einstellungen.json` (`modul_kurz`, `ek_start` = erster Tag des Fahrplans im Format JJJJ-MM-TT, `ek_pro_woche`) und setzt die Platzhalter in `CLAUDE.md` und `lernsystem_logik.md` Kap. 1.

## Schritt 1 – Hefte einlesen (je Heft einzeln)
Die PDFs liegen im Ordner. **Studienmaterial nicht in ein öffentliches Repo pushen**, dafür ist die `.gitignore` da.

1. **Lesen:** Überschriften, Lernziele und Fazit zuerst. Dann alle Themen auflisten, auch Nebenthemen, Beispielboxen und Exkurse. Je Sinnabschnitt klären: Was ist das Kernthema? Welche Modelle? Warum relevant? Wie hängt es mit anderen Themen zusammen?
2. **Schreiben:** `zusammenfassung_heft_N.md`, die ohne das Original verständlich ist. Je Thema gibt es einen Schnellüberblick und eine Vertiefung im Retain-Format (Überschriften als Fragen, kurze Blöcke).
3. **Genauigkeits-Stichprobe:** 2 zufällige Kernaussagen gegen die Heftstelle prüfen und Fehler sofort korrigieren. Meldung: „Stichprobe 2/2 korrekt“.
4. Einsendeaufgaben (EA) und Heft-Übungen kommen nach `uebungsbank.md`. Jede Teilaufgabe ist ein Prüfpunkt.
5. Liegen Altklausuren vor, kommen sie nach `klausurfragen.md`. Sie dienen **nur als Format-Referenz**, nicht zur Priorisierung, weil die Themen rotieren.

## Schritt 2 – Klausurrelevanz
`klausur_relevanz.md` enthält alle Themen aller Hefte mit 🔴/🟡/🟢. Grundlage sind Häufigkeit, Tiefe und Querverweise im Skript, **nicht** Altklausuren. Zu jedem Thema gehört eine Kernaussage in einem Satz. Am Ende folgt die Vollständigkeitsprüfung: „X Themen, davon Y 🔴, Z 🟡, W 🟢“.

## Schritt 3 – Cluster, Ankerfirma, Plan
1. **Cluster:** Themen, die in einem Klausurfall zusammen vorkommen würden, bilden einen Cluster (C01, C02 …, je ≤ 5 Kernpunkte, sonst 2 EK-Teile). Jedes Einzelthema bekommt in `fortschritt.md` eine eigene Checkbox.
2. **Ankerfirma:** eine erfundene Firma, die zum Modul passt (`ankerfirma.md`), mit Personen, Abteilungen und Systemen. In ihr spielt jede Kernkarte.
3. **Pflichtlisten:** pro Cluster 1–2 Listen in `klausur_listen.md`, jeweils mit Merksatz bzw. Bild.
4. **Machbarkeits-Check:** Die Kapazität ergibt sich aus Lerntagen × **realistischen** Minuten. Anfangs sind das 60 % der Angabe, ab Woche 3 gilt der gemessene Median. Den Bedarf schätzt Claude grob: 🔴 ~90 Min, 🟡 ~55, 🟢 ~12–35 Min je Thema plus die Sims. Daraus folgt eine Ampel (🟢 ≤ 85 %, 🟡 ≤ 100 %, 🔴 darüber).
5. **Triage bei 🔴:** zuerst 🟢 auf Minimalabdeckung, dann 🟡 reduzieren. 🔴 wird nie gekürzt, kein Thema wird gelöscht. Reicht das nicht, nennt Claude die Lücke in Minuten und schlägt mehr Zeit oder einen späteren Termin vor.
6. `lernplan.md` enthält 1 EK pro Tag, Schreiben auf Zeit 2× pro Woche, Teil-Sim, die Klausurphase (~10 Tage) mit Vollsim 1 und 2 sowie die Prognose.

## Schritt 4 – Startdateien prüfen
`fortschritt.md` (Cluster-Tabelle + Themen-Checkboxen), leere `abrufe.csv` (nur Kopfzeile), `zeitlog.md`, `schwachstellen.md`, `session_log.md` mit dem ersten „HIER WEITERMACHEN“. Danach `python3 tagesanalyse.py --start` testen.

## Schritt 5 – Automatik
Als geplante Aufgaben anlegen (Claude Code im Web: Scheduled Tasks):
- **19:57 Lern-Check:** nur wenn heute noch nichts gelernt wurde, eine Push-Nachricht und die 1. Frage einer 10-Min-Runde.
- **20:44 Abend-Analyse:** nach `lernsystem_logik.md` Kap. 11.1.
- **Sonntag:** Wochenbilanz nach Kap. 11.2.
- **~10 Tage vor der Klausur:** einmaliges Prozess-Audit.

Dann folgen „Los“ und der erste EK.
