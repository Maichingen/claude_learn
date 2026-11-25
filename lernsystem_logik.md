# Lernsystem – Regeln (einzige gültige Fassung)

**Vorlage:** Version 1 · erprobt über ein ganzes Fernstudien-Modul (Klausur mit offenen Fragen, Lernen meist am Handy, ~40 Min/Tag) · **Modul:** siehe `einstellungen.json` / `config.md`
**Rangfolge:** Diese Datei gilt. `CLAUDE.md` enthält nur Rolle, Kommunikation, Notenschlüssel und Befehle und lädt diese Datei per Import. `lernplan.md` enthält nur Termine und Prognose.
**Regeländerungen** nur sonntags in der Wochenbilanz (Kap. 11.2), höchstens eine Methodenänderung pro Woche, jede mit Messgröße und Enddatum (Kap. 12). Ausnahmen: Fehler im System, drohender Zerfall (Tag 8), ausdrücklicher Wunsch des Users. Jede Änderung wird in Kap. 16 eingetragen.
**Platzhalter:** `[Ziel %]`, `[Klausurdatum]` usw. füllt Claude beim Setup (`SETUP.md`) aus `config.md`.

---

## 1. Ziel und Rahmen

| | |
|---|---|
| **Ziel** | Klausur **≥ [Ziel %] → Note [Zielnote] oder besser**. Das schlägt Tempo. |
| **Klausur** | [Dauer] Min · [Anzahl] Aufgaben à [Punkte] Pkt · Format laut `config.md` (z. B. nur offene Fragen, getippt, Skizzen auf Papier + Upload – dann 5 Min für den Upload einplanen) |
| **Stoff** | [N] Hefte · [N] Themen · [N] Cluster · ggf. Pflicht-Prüfungsaufgabe (Tool-Aufgabe, im Zeitlog mit 💻) |
| **Lernzeit** | Angabe User: [X] Std/Woche. **Planbasis = gemessener Median der letzten 14 Tage**, nicht die Angabe. **Minimaltag 20 Min** zählt als erfüllt; an echten Stresstagen reichen 10 Min Blitz. Null ist nicht akzeptabel. |
| **Termin** | Entweder **fix** (User legt fest, Vollsims nur Diagnose) oder **flexibel über das Gate** (Kap. 9.4). Was gilt, steht in `config.md`. Prognose jeden Sonntag. |
| **Noten** | Notenschlüssel in `CLAUDE.md` |

---

## 2. Evidenz → Konsequenz

| Prinzip | Beleg | Konsequenz im System |
|---|---|---|
| Abrufen statt Wiederlesen | stark: Rowland 2014 · Yang et al. 2021 · Donoghue & Hattie 2021; mit Feedback am stärksten | Jede Einheit besteht überwiegend aus Abruf mit Feedback. Der User liest keine Zusammenfassungen – gelernt wird in der Session. |
| Verteilen | stark: Latimier et al. 2021 · Cepeda et al. 2008 (Abstand ≈ 10–20 % der Zeit bis zur Prüfung) | Abstände 3–7 Tage (S-Takt, Kap. 6.1). In den letzten ~10 Tagen vor der Klausur kürzer (Kap. 3.4). |
| Successive Relearning | stark: Rawson & Dunlosky 2011, 2022 | Erstlernen bis **3× richtig**, danach pro Sitzung **1× frei richtig**. |
| Prüfungsnah üben | mittel–stark: Agarwal 2019 · Morris, Bransford & Franks 1977 | Mini-Fall + Fachbegriff; ab der Klausurphase **täglich eine ausformulierte Aufgabe** (Kap. 3.4). |
| Freier Abruf > Wiedererkennen | Kang, McDermott & Roediger 2007 · Pyc & Rawson 2009 | **Zuerst frei antworten**, Wortbank nur als 2. Versuch (Kap. 6.2). |
| Rate-Frage vorab | mittel: Pan & Carpenter · St. Hilaire et al. 2024 | 1 Rate-Frage beim EK als Ritual. |
| Anleitung nach Können | stark: Kalyuga et al. 2003 | Kernkarte für Neues; Gerüst abbauen, sobald Wissen da ist. |
| Generatives Lernen | mittel–stark: Fiorella & Mayer 2016 | Frei erklären **ohne Vorlage**, eigene Beispiele, **eigene Worte als Anker**. |
| Interleaving | wirkt vor allem bei **ähnlichen** Konzepten: Brunmair & Richter 2019 | Unterscheidungs-Sets für Verwechsler. |
| Hypercorrection | robust: Butler, Fazio & Marsh 2011 | Sicher-falsche Antworten klar korrigieren und nach ~7 Tagen erneut prüfen ([R]). |
| Arbeitsgedächtnis | ~4 Einheiten gleichzeitig (Cowan 2001) | Häppchen à 3 Infos, Kernkarte ≤ 5 Punkte. |
| Wünschenswerte Erschwerung | wirkt nur, solange Erfolg mit Anstrengung möglich ist | Ziel-Trefferquote im Blitz 70–85 %. |
| Schlaf | Konsolidierung gut belegt (Mazza et al. 2016) | Tag-1-Exit am nächsten Tag. |
| Wenn-Dann-Pläne | d ≈ 0,65 (Gollwitzer & Sheeran 2006) | Die Abend-Analyse nennt einen konkreten Start für morgen. |
| Prüfungsangst | Jamieson et al. 2010 · Ramirez & Beilock 2011 | Klausurtag-Routine (Kap. 9.5). |
| ⚠️ schwach | 90-Min-Ultradian · Micro-Gaps · NSDR · „7 ± 2“ | Keine Steuerungsgrößen. |

---

## 3. Tagesablauf

### 3.1 Fenster und Tagesgrößen
| Fenster | Inhalt | Gerät |
|---|---|---|
| **erstes Fenster mit ≥ 25 Min** (egal wann) | **Erstkontakt (EK)** | Handy ok |
| kürzere Fenster (10–20 Min) | Blitz + Tag-1-Exit des letzten EK | Handy ok |
| 2× pro Woche, 25–45 Min | **Schreiben auf Zeit** (Kap. 9.1); eine Sim zählt als eines davon | Laptop |

- **Normaltag ≈ 60 Min:** Blitz ≤ 15 · Tag-1-Exit ~10 · EK 30–40. **Minimaltag 20 Min:** die fälligsten Blitze.
- **Bei knapper Zeit gilt diese Reihenfolge:** (1) Cluster am letzten Fälligkeitstag (Tag 8 verhindern) → (2) Tag-1-Exit → (3) EK → (4) übrige Blitze → (5) R1.
- **EK zuerst:** Nach den Pflicht-Blitzen (nur Cluster am letzten Fälligkeitstag) und dem Tag-1-Exit kommt sofort der EK; übrige Blitze danach, höchstens 10 Min. *(Warum: ohne diese Regel fraßen Wiederholungen die Zeit, der EK-Anteil lag bei 27 %; danach 41 %.)*
- **Keine Uhrzeit-Grenzen:** Der User entscheidet, wann er lernt; Claude bremst nicht wegen der Uhrzeit. Max. 4 Blöcke pro Session. Nicht Geschafftes rückt auf den nächsten Tag.
- **Takt:** 1 EK pro Tag, kleine 🟡-Cluster gebündelt. 🔴-Themen voll, 🟡 nur Kernkarte + Mini-Fall, 🟢 ein Kernsatz.
- **Zu viel Neues ist ein Planungsfehler:** Bleibt wenig hängen, wird die Dosis Neues gesenkt, nicht die Wiederholung.

### 3.2 Sessionstart (automatisch, kurz)
1. `TZ=Europe/Berlin date` → `zeitlog.md`.
2. `python3 tagesanalyse.py --start` → fällige Cluster nach S-Takt, Blitz-Zähler, Zerfall-Hinweise, offene [R] und Wiederabfragen, „HIER WEITERMACHEN“. Das ersetzt das Einlesen aller Arbeitsdateien.
3. **Zerfall** nur hier anwenden: S −1 in `fortschritt.md` + Zeile `Zerfall` in `abrufe.csv`. War der Ausfall nicht Schuld des Users (Systemausfall, kein Zugriff auf Claude), wird stattdessen `Zerfall-ausgesetzt` gebucht (S bleibt, das Skript meldet keinen Zerfall mehr für diesen Zeitraum).
4. Plan des Tages in max. 4 Blöcken ansagen (1–3 Zeilen) und mit dem ersten Schritt beginnen.

### 3.3 Pflege (macht Claude, kostet den User keine Lernzeit)
- **Nach jeder Einheit:** `abrufe.csv` (jede Abfrage) · `zeitlog.md` · `session_log.md` „HIER WEITERMACHEN“ · commit + push.
- **Einmal täglich** (nach der letzten Einheit oder in der Abend-Analyse): `fortschritt.md` (S, Status, **Themen-Häkchen ☐/◐/☑ aus `abrufe.csv`**, Wiederabfragen) · `schwachstellen.md` **in beide Richtungen** (neue Lücken eintragen **und** jeden Eintrag gegen `abrufe.csv` prüfen: 2× frei ohne Wortbank/Cue in verschiedenen Sitzungen → mit Begründung ins Archiv; Berichtszeile „Schwachstellen: +X · −Y · Z offen“) · `uebungsbank.md` ☐→☑ · Fortschrittsbalken X/N · commit + push.
- **S-Meldung sofort:** Steigt ein S-Wert, meldet Claude das **direkt in der Antwort** („📈 C08: S 2 → 3“), nicht erst abends. Sinkt er, ebenso („📉“).
- **Gesamtübersicht bei jedem Sessionende:** max. 8 Zeilen – Minuten heute · Fortschrittsbalken X/N · S-Änderungen heute (oder „keine“) · Ø S · Prognose Klausur · offene Schwachstellen · nächster Schritt.

### 3.4 Klausurphase (ab EK-Ende, ~10 Tage vor der Klausur)
- **Normaltag (~40 Min):** fällige Blitze **frei**, verwandte Cluster als Paar-Fall (auch bei S 1–2), max. 15 Min → **1 ausformulierte Klausuraufgabe** (18 Min, DBBF, Pflichtsatz „Bei [Firma] …“, auch am Handy) → Feedback + Überarbeitung der schwächsten Teilaufgabe → 5 Min eine Pflichtliste.
- **Lückenphase vor Vollsim 1:** zuerst nie abgerufene 🔴-Themen und Pflichtlisten (aller Cluster, auch der zuletzt gelernten), dann 🟡 als 1-Satz-Idee, 🟢 als Kernsatz.
- **Zeichen-Prüfpunkte** (Modelle, Diagramme) mindestens 1× auf Papier als Aufgabe.
- **Feste Verwechsler** (die ~8 häufigsten Fehler aus `abrufe.csv`) als Kontrastrunde in jede Session.
- *(Warum: Im Pilotmodul gab es 3 Wochen lang nur Stichwort-Antworten am Handy. Wortbank-Blitze lagen bei 81 %, der freie Folgetag bei 34 %, die Prognose bei ~45 %.)*

---

## 4. Situation → Methode

Vor jedem Schritt bestimmt Claude Stoffzustand (A), Fehlerbild (B) und Lernerzustand (C).

### 4.1 A – Stoffzustand (Codes wie in `abrufe.csv`)
| Code | Zustand | Methode |
|---|---|---|
| **A2** | **neuer Cluster** | **EK** (Kap. 5) |
| A1 | der Feynman im EK trifft < 50 % | Bild-Häppchen à 3 Infos, nur für die fehlenden Punkte |
| A3 | S 1–2 | Blitz-Fall bis Kriterium · R1 geblockt (1 Cluster) |
| A4 | S 3–4 | kombinierter Fall aus 2 **verwandten** Clustern (Fakt + Anwendung) |
| A5 | S ≥ 5 | selten (Tag 6–7): Paar-Fälle, Sim-Aufgaben |
| A6 | Klausurphase (alle EK durch) | Kap. 3.4 · Sims auf Zeit · Musterantwort-Vergleich |

### 4.2 B – Fehlerbild (Spalte `fehlerbild`)
| Code | Fehlerbild | Reaktion |
|---|---|---|
| B1 | **leer** | Cue (Bild, Situation – **keine Anfangsbuchstaben**) → Kompaktlösung → Kriteriums-Runde. 2 Sitzungen leer → Rettung |
| B2 | **Verwechslung ähnlicher Konzepte** | Kontrastpaar + Unterscheidungs-Set (4 Mini-Fälle „welches?“) |
| B3 | **Inhalt da, Fachbegriff fehlt** (häufigstes Leck) | Bedeutungs-Anker (Wortstamm, englisches Wort) · Richtung **Fall → Begriff** üben · Begriff im Blitz ausdrücklich verlangen |
| B4 | **Struktur/Operator** (Stichworte, Fallbezug oder Urteil fehlt) | DBBF + Pflichtsatz „bei [Firma] …“ + Musterantwort · Schreiben am Laptop |
| B5 | **sicher falsch** | sofort klare Korrektur + Kontrast + [R] |
| B6 | **Reihenfolge/Prozess** | Weg-Geschichte (Akte, Route) + Reihenfolge-Abruf |
| B7 | **Modell/Notation** | Dual Coding: Skizze beschreiben/zeichnen oder im Tool bauen |

### 4.3 C – Lernerzustand
| Signal | Anpassung |
|---|---|
| User sagt selbst „Pause“, „müde“ o. Ä. | Einheit mit einem sicheren Erfolg beenden + Gesamtübersicht. **„keine Ahnung“ heißt nur „weiß ich nicht“** → B1, kein Abbruchsignal |
| Handy | Blitz, Rate-Frage, Kernkarte, Feynman und Tag-1-Exit in Stichworten; ab Klausurphase auch ausformulierte Aufgaben |
| Laptop | Schreiben auf Zeit, Sims, Tool-Aufgaben |
| ≤ 10 Min Zeit | fälligste Blitze |
| Pause > 2 Std mitten im EK | 3 Min Wiederaufwärmen (Kernkarte aus dem Kopf) vor dem Mini-Fall |
| Frust („zu schwer“, „null Fortschritt“) | Dosis halbieren, Fortschritt in Zahlen zeigen, nächster Schritt = sicherer Erfolg |
| User will neuen Stoff | geben, wenn kein Cluster an Tag 8 steht |
| praktische Aufgabe möglich | „Bau den Fall“: User entwirft selbst ein Szenario |

- **Keine Kommentare zur Belastung** („dein Kopf ist voll“ o. Ä.). Claude beurteilt Antworten, nicht den Zustand des Users.

---

## 5. Erstkontakt (EK)

| Schritt | Inhalt | Min |
|---|---|---|
| 1 | **Rate-Frage** als 3er-Auswahl (30 s, ohne Wertung, sofort aufgelöst). Keine offenen „erklär mal“-Fragen zu Unbekanntem. | 1 |
| 2 | **Kernkarte:** ≤ 5 Kernpunkte des Clusters auf einem Bildschirm, in der **Ankerfirma** (`ankerfirma.md`), Fachbegriffe in eigener Spalte, **eine** Merkhilfe aus den Lieblingswelten des Users (`config.md`). User liest. | 5 |
| 3 | **Feynman ohne Vorlage** (wegscrollen): User erklärt frei, am Handy in Stichworten. Claude zählt Treffer x/5, korrigiert Fehler und erklärt nur die Lücken. **< 50 % → Bild-Häppchen** (3 Infos, je Sofort-Abruf) nur für die fehlenden Punkte. | 8–12 |
| 4 | **Eigenes Beispiel:** User erfindet einen Fall. | 3 |
| 5 | **Verbundener Mini-Fall** in fremder Firma (10 Pkt, Klausur-Operatoren, Fachbegriffe verlangt). | 8 |
| 6 | **Begriffs-Kriterium:** jeder Kernbegriff 3× frei richtig in dieser Sitzung (Feynman · Mini-Fall · **Pflicht-Schluss-Check frei ≥ 10 Min nach dem Lernen**). | 2 |
| 7 | **Tag-1-Exit** am Folgetag (fremde Firma, verzögert): Listen des Vortags **zuerst als Zuordnung/Reihenfolge, dann frei** → erster S-Wert. | 10 |

- **Listen lernen (Bild-Häppchen):** Jede Liste wird mit **einem Bild oder den eigenen Worten des Users** gelernt, **keine Anfangsbuchstaben als Cue**. Liefert der User eigene Worte („Inventur, auswählen …“), werden sie zum Anker. Bei langen Listen baut der User die Geschichte selbst. *(Warum: Listen mit Buchstaben-Cue und ohne freien Schluss-Check waren am Folgetag leer, Tag-1 22–35 %; mit Bild/eigenen Worten 60–63 %.)*
- **Listen abfragen:** immer **komplett** oder als **Reihenfolge-Aufgabe**, nie nur einen Teil („nenne das 3. Element“ ist eine schlechte Frage).
- **Pflichtlisten:** pro Cluster 1–2 Listen mit Merksatz in `klausur_listen.md`; alles andere als Idee in einem Satz mit Beispiel.
- **Merkhilfen:** Bedeutungs-Anker vor Akronym. Ein Akronym nur, wenn der User es ausdrücklich will – dann als Satz aus seiner Lieblingswelt.
- **Dosierung:** 🔴 voller Ablauf · Cluster nur aus 🟡/🟢: Kernkarte + Mini-Fall, Schritte 3–4 kurz.
- **Große Cluster** (> 5 Kernpunkte): 2 Kernkarten → 2 EK-Teile an 2 Tagen.
- **Kernkarten decken alle Prüfpunkte** des Clusters ab (Abgleich `uebungsbank.md`). **Tool-Themen** werden beim Tun gelernt.
- **EK-Abbruch:** Trifft auch der Häppchen-Abruf < ⅓, endet der EK-Block; der Rest kommt am nächsten Tag.
- **Vorwissen-Brücke:** Antwortet der User mit Begriffen aus einem früheren Modul, baut Claude eine Brücken-Tabelle alt ↔ neu; in der Klausur zählt der Begriff dieses Moduls.
- **Auflösen:** Nach jeder Bewertung steht vollständig da, was richtig war und was falsch – nichts bleibt offen.

---

## 6. Wiederholen und Behalten

### 6.1 Fälligkeit (S-Takt)
„Tag X“ = X Tage seit dem letzten Abruf des Clusters.

| S | ideal | spätestens |
|---|---|---|
| 1–2 | Tag 2–3 | **Tag 3** |
| 3–4 | Tag 4 | **Tag 5** |
| ≥ 5 | Tag 6 | **Tag 7** |

- **Tag 8 = Zerfall (S −1) und darf nie passieren.** Passiert es doch, ist das ein Planungsfehler von Claude.
- **Welle glätten:** Stehen viele Cluster gleichzeitig an (nach EK-Serien oder Ausfällen), zieht Claude täglich 2 „ideale“ Cluster vor und bildet Paar-Fälle aus verwandten Clustern.
- Sims, Schreiben auf Zeit, R1/R2 und kombinierte Fälle zählen als Abruf für jeden darin geprüften Cluster.

### 6.2 Blitz
- Jede Blitzfrage ist ein **Mini-Fall in fremder Firma + Fachbegriff**, ~2 Min je Cluster. Zwei Cluster dürfen in einen Fall, wenn sie **inhaltlich verwandt sind oder schon verwechselt wurden** (B2), nie zufällig.
- **Zuerst frei, Wortbank nur als 2. Versuch:** Der User antwortet frei in Stichworten. Erst nach einem Fehlversuch gibt es eine Wortbank (richtiger Begriff + 2–5 ähnliche Begriffe, Verwechsler zuerst). *(Warum: Mit Wortbank von Anfang an lag der Blitz bei 81 %, der freie Folgetag bei 34 % – die Wortbank zeigte Können, das nicht da war.)*
- **Deckel 15 Min.** Bis 20 Min nur, wenn sonst ein Cluster Tag 8 erreicht.
- **Kriterium:** Jeder fällige Punkt muss pro Sitzung **1× frei richtig** sein. Falsch → Feedback → **Kriteriums-Runde** am Sitzungsende (≥ 10 Min später, neue Firma, kein Abtippen).
- Offene [R]-Punkte und Wiederabfragen hängen am Blitz.
- **Themen-Rotation:** Jede Blitz-Runde enthält **2 Rotationsfragen** zu Einzelthemen, die am längsten nicht abgefragt wurden (Themenliste in `fortschritt.md`, Spalte `item` in `abrufe.csv` mit Themennummer, Notiz „Rotation“). *(Warum: Ein Cluster galt als abgefragt, obwohl immer nur dieselben Problempunkte drankamen; ganze Themen waren einen Monat nicht dran.)*

### 6.3 Tag-1-Exit, R1, R2
- **Tag-1-Exit:** verzögerter Fall zum EK am Folgetag (10–20 Pkt, fremde Firma). Erst frei, Hinweise erst danach; gewertet wird der freie Teil.
- **R1:** 2–5 Tage nach dem EK, 10–15 Min, geblockt bei S ≤ 2, mit mindestens 1 Heft-Übung oder EA-Teilaufgabe (`uebungsbank.md`) im Fremdszenario.
- **R2:** deckt eine Sim-Aufgabe zum Cluster ab, sonst ein 15-Min-Fall ≥ 7 Tage nach R1.
- **Einsendeaufgaben:** spätestens im R1 des Clusters oder beim Schreiben auf Zeit, nie erst in der Klausurphase.

### 6.4 Rückfall [R]
- Auslöser: derselbe Punkt **2× falsch, dann gefixt**.
- Pflicht-Blitz in jeder Sitzung, bis er in **2 verschiedenen Sitzungen** frei richtig war (Rückfall → Zähler 0). Danach ein Kontrollabruf nach ~7 Tagen.

### 6.5 Karteikarten-App (optional)
- Nur, wenn der User sie wirklich täglich nutzt. Sonst weglassen: Fall → Begriff läuft dann über den Blitz. *(Warum: Im Pilotmodul lief die App in 2 Wochen an 0 Tagen und wurde abgeschaltet.)*
- Falls genutzt: Karte = Mini-Fall → Antwort ≤ 3 Zeilen, Fachbegriff zuerst + 1 Satz Begründung. **Genau ein Begriff pro Karte, keine Listen** (Listenkarten standen fast alle bei 0 %). Export per `python3 export_schwachstellen.py --retain` (nur neue Karten, fortlaufend nummeriert). Wöchentliche Prüfung, ob die App Karten verfälscht hat.

---

## 7. Fehler, Feedback, Rettung

### 7.1 Bei falscher Antwort
1. **1. Fehlversuch:** Denkanstoß oder Gegenfrage in einfachen Worten, nie die Lösung (im Blitz: jetzt die Wortbank).
2. **2. Fehlversuch:** **Kompaktlösung** (Kontrasttabelle oder 3–4 Sätze + Musterantwort mit Fallbezug). Kein Abtippen.
3. **Am selben Tag:** Kriteriums-Runde in neuer Firma. **Nächste Sitzung:** verzögerter Abruf im Blitz (Eintrag „Wiederabfrage“ in `fortschritt.md`).
4. Eintrag in `schwachstellen.md` (Thema + Szenario) und Fehlerbild in `abrufe.csv`.
- **Konfidenz:** Setzt der User „?“ hinter eine Antwort, gilt sie als unsicher (`u`), sonst als sicher (`s`). Sicher + falsch = B5.

### 7.2 Rettung
- **Auslöser:** 2 verzögerte Fälle < 50 % (in verschiedenen Sitzungen) **oder** derselbe Punkt in 2 Sitzungen leer (B1).
- **Rettungsblock** (15–25 Min, geblockt), Einstieg nach Fehlerbild:

| Fehlerbild | Methode |
|---|---|
| lückenhaft | Chunking (max. 5 Kernpunkte) |
| Verwechslung (B2) | Kontrastpaar + Unterscheidungs-Set |
| kein Anker (B1) | Warum-Methode („Warum gibt es das? Was wäre, wenn nicht?“) |
| Ablauf (B6) | Geschichte in Akten oder Diagramm |
| komplett leer | Read-Recite-Review |

- Abschluss mit einem Mini-Fall. **Der Rettungs-Fall ändert S nicht**; die Wirkung zeigt der nächste verzögerte Abruf.
- **Nach 2 erfolglosen Rettungen → Teilpunkte-Ziel:** Antwortgerüst (Definition · 3 Merkmale · 1 Beispiel · 1 Abgrenzung). Keine Aufgabe darf 0 Punkte bringen.

---

## 8. Bewertung und S-Wert

### 8.1 Bewertung
- **Antwortgerüst DBBF:** **D**efinition → **B**estandteile (3–5) → **B**eispiel mit Fallbezug → **F**azit/Empfehlung mit Begründung.
- 1 Pkt ≈ 1 Aspekt mit Begründung · 20 Pkt ≈ 8–10 Aspekte ≈ 15–20 Min Schreiben.
- **Operatoren** stehen ausdrücklich in der Frage. „nennen“: Stichworte reichen. „erläutern/diskutieren/beurteilen/begründen“: Stichworte bringen höchstens die halbe Punktzahl. Fehlt der Fallbezug: höchstens ⅔. Fehlt das Urteil bei „beurteilen/empfehlen“: −25 %.
- **Bewertet wird nur, was die Frage verlangt.**
- **Erwartungshorizont vorab:** Claude legt die erwarteten Aspekte und Punkte fest, **bevor** der User antwortet (bei Sims schriftlich in `sims/`). Bei jeder Bewertung nennt Claude kurz, welcher Aspekt den fehlenden Punkt gebracht hätte. (Keine Selbsteinschätzung durch den User – kostet Zeit, wurde nicht genutzt.)
- **Antworten in Stichworten am Handy** (Blitz, Tag-1-Exit, R1): bewertet wird der Inhalt. Die Form zählt beim Schreiben auf Zeit, in ausformulierten Aufgaben und in Sims.
- Punkte → Prozent → Note laut Notenschlüssel · ✅ ≥ Ziel, ⚠️ darunter.

### 8.2 S-Wert (1–10, Start 1, je Cluster)
S ändert sich an genau drei Stellen:

| Stelle | Regel |
|---|---|
| 1. **Verzögerter Fall** (Tag-1-Exit, R1/R2, Schreiben auf Zeit, Sim-Aufgabe) | ≥ 81 % **+2** · 67–80 % **+1** · 50–66 % **±0** · < 50 % **−1** (min. 1) |
| 2. **Blitz** | 2 Tage mit **freiem** Blitz-Abruf (1. Versuch ohne Wortbank) → **+1**, aber nur bis S 6. Ein nicht freier Blitz setzt den Zähler auf 0; S sinkt nicht. Steht im Zählfenster ein Blitz mit Notiz „Wortbank“, steigt S höchstens bis 3. Das Skript zählt (`--start`), Claude bucht `S+1` in `abrufe.csv`. |
| 3. **Zerfall** | Tag 8 ohne Abruf → **−1** (einmal, als `Zerfall` gebucht) |

- Über S 6 geht es nur über Stelle 1. Max. 10.
- **Sofortabrufe** (EK, Mini-Fall im EK, Rettung, Kriteriums-Runde) ändern S nicht.
- S wird berechnet, nie abgefragt. **S steuert nur die Fälligkeit**, nicht den Termin.
- **[x] für einen Cluster** erst nach dem Topic-Check: alle Themen mit ✅/❓ auflisten, der User bestätigt.

### 8.3 Kalibrierung
- **Extern:** Eine Einsendeaufgabe wird beim Schreiben auf Zeit komplett geschrieben und beim Tutor eingereicht. Ist der Tutor strenger, verschärft Claude die eigene Bewertung um die Differenz.
- **Blindbewertung (falls der User zustimmt):** Jede Sim bewertet zusätzlich eine frische Claude-Instanz ohne Vorwissen, blind und mit demselben Erwartungshorizont. Bei mehr als 5 Prozentpunkten Abweichung gilt der strengere Wert.

---

## 9. Schreiben auf Zeit, Simulationen, Termin

### 9.1 Schreiben auf Zeit (2× pro Woche, Laptop)
- 1 Klausuraufgabe (20–40 Pkt) **auf Zeit** (1 Pkt ≈ 1 Min), ohne Hilfe, ausformuliert nach DBBF. Danach Musterantwort-Vergleich und Bewertung nach 8.1. Zählt als verzögerter Fall (S) und als Abruf.
- Eine Sim am Wochenende zählt als eine der beiden Einheiten der Woche.
- **Termine im Plan fest eintragen und nachhalten.** Fällt eines aus, wird es in der Abend-Analyse sofort neu gesetzt. *(Warum: Im Pilotmodul fiel Schreiben auf Zeit 3 Wochen lang still aus – größter einzelner Punkteverlust.)*

### 9.2 Simulationen
| Wann | Was |
|---|---|
| nach ~⅓ des Stoffs | Teil-Sim (nur behandelte Cluster) |
| ~5 Tage vor der Klausur | **Vollsim 1** (volle Länge, alle Hefte) – übt auch das Zeitmanagement |
| ~2 Tage vor der Klausur | **Vollsim 2** (volle Länge oder halbe Länge, wenn die Nacharbeit sonst keine Zeit hat) |
| Vortag | leicht, Technik-Check |

- Sims laufen **ohne Hilfe**, auf Zeit, getippt; Skizzen auf Papier, ggf. die letzten 5 Min für den Upload. Feedback erst danach.
- Jede Sim-Aufgabe zählt als Abruf und als R2 für die geprüften Cluster.
- **Coverage-Pflicht nur für Vollsims:** vor Vollsim 1 jedes Thema ≥ 1× abgerufen, vor Vollsim 2 jedes 🔴-Thema ≥ 2× in verschiedenen Kontexten.
- Themenmix über alle Relevanzstufen. Aufgaben werden neu erstellt; `klausurfragen.md` zeigt nur das Format.

### 9.3 Kontrollpunkte
| Prüfung | auf Kurs | gelb | rot → Intensivprotokoll |
|---|---|---|---|
| Teil-Sims | ≥ Ziel − 8 | Ziel − 16 bis Ziel − 9 | darunter |
| Vollsim 1 | ≥ Ziel − 4 | Ziel − 6 bis Ziel − 5 | darunter |
| Vollsim 2 | ≥ Ziel | Ziel − 4 bis Ziel − 1 | darunter |

- **Gelb:** Die schwächsten Bereiche bekommen 3 Tage Vorrang. Prüfen, ob die Verluste beim Inhalt oder bei der Form liegen.
- **Intensivprotokoll:** Diagnose **am selben Tag** (Wissen / Form / Zeit) → die 6 schwächsten Cluster nach vorn. Ist mehr als ⅓ der Verluste Form: täglich 10 Min Antworttechnik. Zeitproblem: harter Takt pro Aufgabe. Die nächste Sim gewichtet die roten Cluster doppelt.

### 9.4 Gate (nur bei flexiblem Termin)
- Klausur erst, wenn: jedes Thema ≥ 1× abgerufen (Nie-abgerufen-Check) · Pflichtaufgabe abgegeben · Vollsim 2 ≥ Ziel. Notbremse: Vollsim 2 > 10 Punkte unter Ziel → +1 Woche mit Vollsim 3.
- Bei **fixem Termin** entfällt das Gate; die Vollsims steuern nur die Intensivphase (9.3).
- Claude meldet jede Prognoseänderung in 1 Zeile.

### 9.5 Klausurtag
- **Vortag:** Technik- und Upload-Check (Rechner, App, Akku, Papier, Stifte), nur leichte Blitze, früh schlafen.
- **Direkt vorher (10 Min):** Sorgen kurz aufschreiben; Aufregung als Energie deuten („Das ist Aktivierung, ich bin bereit“).
- **In der Klausur:** alle Aufgaben kurz lesen, mit der sichersten beginnen · feste Minuten pro Aufgabe + Reserve · Skizzen früh, damit Zeit fürs Foto bleibt.
- **Blackout:** DBBF-Gerüst hinschreiben (Definition → 3 Merkmale → Beispiel aus dem Fall → Fazit). Keine Aufgabe leer lassen.

---

## 10. Vollständigkeit und Coverage
- **Jedes Thema jedes Hefts** steht im Plan. Altklausuren zeigen nur das Format, nie die Inhalte (Themen rotieren). `klausur_relevanz.md` ist ohne Altklausur-Einfluss.
- Tiefe nach Relevanz: 🔴 voll · 🟡 kompakt (Kernkarte + gemeinsamer Mini-Fall) · 🟢 minimal (Kernsatz + Frage). Kein Thema wird gelöscht.
- **Prüfpunkt-Coverage:** Jede EA-Teilaufgabe und jede Heft-Übung ist ein Prüfpunkt. Ein Thema gilt erst als abgedeckt, wenn jeder Prüfpunkt 1× frei abgerufen ist.
- **Cluster-Abruf ≠ Themen-Abruf:** Jedes Einzelthema hat in `fortschritt.md` eine Checkbox (☐ nie · ◐ teilweise/nur mit Hilfe · ☑ frei), täglich aus `abrufe.csv` gepflegt.
- **Nie-abgerufen-Check** vor jeder Vollsim und in der Wochenbilanz: Themen mit 0 Abrufen sofort einplanen.
- Externe Quellen (Tutor-KI, externe Zusammenfassungen) sind **nur additiv**: nie abstufen, nie löschen; bei Widersprüchen beide Sichtweisen dokumentieren, markiert mit `[ergaenzt aus externer KI]`.

---

## 11. Abend-Analyse und Wochenbilanz (ohne Zuruf)

### 11.1 Täglich ~21 Uhr (geplante Aufgabe)
- **Läuft gerade eine Einheit** (die letzte User-Nachricht ist < 20 Min alt **oder** Claude hat vor < 30 Min eine Frage gestellt): nur „Abend-Analyse folgt nach der Einheit“. Eine ältere, unbeantwortete Frage blockiert die Analyse nicht.
- Ablauf: fehlende Abrufe nachtragen, Zeitlog schließen (auch eine 0-Zeile) → `python3 tagesanalyse.py` → Plan für morgen (fällige Cluster, EK, Wenn-Dann-Start mit Uhrzeit und Gerät) in `session_log.md` → Pflege nach 3.3 → Eintrag in `tagesanalyse.md` → `git pull --rebase` → commit + push → Bericht in max. 5 Zeilen, **immer mit einer S-Zeile** (auch „keine Änderung“) und der Schwachstellen-Zeile.
- **Täglich anpassen darf Claude nur den Plan** (Reihenfolge, Dosis, Fenster). Regeln und Methoden ändern sich nur sonntags (Ausnahmen siehe Kopf).
- **Vorziehen:** Bei Vorsprung ≥ 1 EK-Teil, keinem überfälligen Cluster und letztem Tag-1-Exit ≥ 50 % zieht Claude den Fahrplan sofort vor und meldet die neue Prognose in 1 Zeile. Rückstand → keine tägliche Warnung, Neuplanung sonntags.
- Push-Nachricht nur, wenn morgen ein Cluster Tag 8 erreicht.

### 11.2 Sonntag: Wochenbilanz (`python3 tagesanalyse.py --woche`, 14 Tage)
- Prognose mit dem Lernzeit-Median neu rechnen (EK-Ende, Vollsims, Termin) → 1 Zeile an den User.
- Regeln, nur bei Mindest-Stichprobe (sonst „zu wenig Daten“, keine Änderung):

| Befund (14 Tage) | Mindestmenge | Aktion |
|---|---|---|
| Blitz-Freiquote < 60 % | ≥ 20 Blitz-Items | Fälle kleiner, Cue früher, S 1–2 schon an Tag 2 |
| Blitz-Freiquote > 85 % | ≥ 20 Blitz-Items | Abstände +1 Tag, mehr Zeit für EK |
| Blitz-Freiquote ≥ 20 Punkte über der Tag-1-/Kriteriumsquote | ≥ 20 Items | Blitz ist zu leicht (Wiedererkennen) → schwerer, freier, ohne Hilfe |
| Tag-1-Exit Ø < 60 % | ≥ 3 Exits | EK-Methode prüfen (Listen, Schluss-Check) |
| ein Fehlerbild ≥ 30 % aller Fehler | ≥ 10 Fehler | B3: mehr Fall→Begriff · B4: 3. Schreib-Einheit · B2: Unterscheidungs-Set |
| 0× Schreiben auf Zeit in 7 Tagen | – | sofort 2 Termine fest einplanen |
| Freiquote ab 21 Uhr ≥ 15 Punkte unter der vor 21 Uhr | ≥ 10 Items je Gruppe | nur als Info, keine Uhrzeit-Regel |
| Anteil EK < 40 % der Stoff-Lernzeit | 7 Tage | Blitz kürzen (S ≥ 5 seltener), EK zuerst |

- **Höchstens eine Methodenänderung pro Woche**, immer mit Messgröße und Enddatum (Kap. 12).
- **Prozess-Audit** (empfohlen ~10 Tage vor der Klausur): mehrere unabhängige Prüfer (Daten · Regelwerk · Methodik · Klausurbereitschaft), eindeutige Fehler direkt beheben.

---

## 12. Laufende Experimente
| Seit | Änderung | Messgröße | Ende | Abbruch |
|---|---|---|---|---|
| – | (noch keine) | | | |

Rituale ohne eigene Messung: Rate-Frage, Kriteriums-Runde, Begriffs-Kriterium 3×.

---

## 13. Ausfall und Rückstand
- **1–2 Tage Ausfall:** normal weiter, zuerst die Cluster am letzten Fälligkeitstag.
- **≥ 3 Tage Ausfall oder Krankheit:** 1. Tag zurück = nur Blitz (max. 20 Min, nach Dringlichkeit). Ab dem 2. Tag wieder EK. Zerfall einmal anwenden. Prognose am nächsten Sonntag neu.
- **Systemausfall** (kein Zugriff auf Claude, z. B. Nutzungslimit): kein Zerfall, Buchung `Zerfall-ausgesetzt` (Kap. 3.2).
- Rückstand nennt Claude sachlich in Minuten plus den nächsten konkreten Schritt, ohne Vorwurf.

---

## 14. Dateien und Automatik
| Datei | Zweck |
|---|---|
| `CLAUDE.md` | Rolle, Kommunikation, Notenschlüssel, Befehle; importiert diese Datei |
| **`lernsystem_logik.md`** | **alle Lernregeln (diese Datei)** |
| `SETUP.md` | Einrichtung eines neuen Moduls (Schritte 0–5) |
| `config.md` · `einstellungen.json` | Modul, Klausurformat, Lernzeit, Termin, Lieblingswelten · Werte für die Skripte |
| `lernplan.md` | aktueller Plan: Wochen, Sims, Prognose |
| `fortschritt.md` | Cluster-Status, S, Themen-Häkchen, offene [R] und Wiederabfragen |
| `abrufe.csv` | **einzige Rohquelle** für Abfragen: `datum;zeit;geraet;cluster;typ;methode;ergebnis;fehlerbild;punkte;max;schaetzung;konfidenz;item;anlass;notiz` (15 Spalten, **kein Semikolon im Text**) |
| `zeitlog.md` | gemessene Lernzeit; die Blöcke-Spalte beginnt mit dem Blocktyp, Pflicht-/Tool-Aufgaben mit 💻 |
| `tagesanalyse.py` / `tagesanalyse.md` | Sessionstart-Check, Tagesbericht, Wochenbilanz · Verlauf der Analysen |
| `session_log.md` | „HIER WEITERMACHEN“ (immer nur einer aktiv, alte durchstreichen) |
| `schwachstellen.md` / `schwachstellen_archiv.md` | Lücken · archiviert nach 2× frei richtig in verschiedenen Sitzungen |
| `export_schwachstellen.py` | PDF der Schwachstellen (A5, Handy) · optional Karten-Export |
| `uebungsbank.md` | EAs + Heft-Übungen je Cluster |
| `klausur_listen.md` | Pflichtlisten je Cluster mit Merksatz |
| `ankerfirma.md` · `klausur_relevanz.md` · `zusammenfassung_heft_N.md` · `klausurfragen.md` | Lernkontext und Stoff (beim Setup erstellt) |
| `sims/` | Sims mit Erwartungshorizont und Bewertung |

**Werte in `abrufe.csv`:** typ = EK-Sofort · EK-Fall · Tag1 · Blitz · Kriterium · R1 · R2 · Rettung · Schreib · Sim · S+1 · Zerfall · Zerfall-ausgesetzt · ergebnis = frei · anstoss · kompakt · leer · punkte/max = Punkte der Teilaufgabe · konfidenz = s · u · anlass = faellig · R · wiederabfrage · ek · sim · schreib · notiz enthält „Wortbank“, wenn eine Wortbank im Spiel war. Ein Fall mit mehreren Teilaufgaben = eine Zeile je Teilaufgabe. Ein zweiter Versuch nach Anstoß ist **keine** eigene Zeile, sondern steht in der Notiz.

| Automatik (geplante Aufgaben, beim Setup anlegen) | Was |
|---|---|
| jeder Sessionstart | Kap. 3.2 |
| täglich ~20 Uhr | **Lern-Check:** nur wenn heute noch nichts gelernt wurde → Push + 1. Frage einer 10-Min-Mini-Runde. Ändert keine Dateien, wendet keinen Zerfall an. |
| täglich ~21 Uhr | **Abend-Analyse** (Kap. 11.1) |
| Sonntag | **Wochenbilanz** (Kap. 11.2) |

---

## 15. Herkunft der wichtigsten Regeln (Lehren aus dem Pilotmodul)
| Regel | Was vorher schiefging |
|---|---|
| Eine Regelquelle | Zwei Regeldateien mit fast 1000 Zeilen widersprachen sich. |
| S-Takt statt fester Fristen | Feste Fristen (1-3-7-14) passten nicht zu wechselnder Lernzeit. |
| Planbasis = gemessener Median | Angegebene 75–180 Min/Tag, gemessen ~30–40. Pläne auf Basis der Angabe scheiterten. |
| Nur verzögerte Fälle ändern S | Sofortabrufe direkt nach dem Lernen täuschten Sicherheit vor. |
| Bild-Häppchen, keine Buchstaben-Cues | Listen mit Anfangsbuchstaben waren am Folgetag leer. |
| Wortbank nur als 2. Versuch | Wiedererkennen ≠ freier Abruf (81 % vs. 34 %). |
| Themen-Rotation, Themen-Häkchen | Ganze Themen blieben einen Monat unabgefragt, obwohl der Cluster „fällig erledigt“ war. |
| Schreiben fest einplanen, Klausurphase mit täglicher Aufgabe | Stichworte am Handy bringen bei „erläutern“ nur halbe Punkte; Schreiben fiel 3 Wochen aus. |
| Schwachstellen in beide Richtungen pflegen | Archiv wurde wochenlang nicht gepflegt, gelöste Punkte blieben „offen“. |
| S-Meldung sofort, Gesamtübersicht bei Sessionende | User verlor den Überblick über seinen Fortschritt. |
| Karteikarten-App optional | Wurde nicht genutzt; Pflicht-Exporte kosteten nur Zeit. |
| „keine Ahnung“ ≠ Abbruch, keine Uhrzeit-Grenzen, keine Belastungskommentare | Claude brach Einheiten ab oder belehrte, obwohl der User weiterlernen wollte. |

---

## 16. Änderungsprotokoll
| Datum | Änderung | Grund |
|---|---|---|
| (Setup) | Vorlage übernommen | neues Modul |
