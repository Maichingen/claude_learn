# Zeitlog – echte Lernzeit

**Messung:** Claude liest die Uhrzeit per `TZ=Europe/Berlin date` aus. Gemessen wird bei Sessionstart, Blockwechsel, „Pause“ und Sessionende, Pausen werden abgezogen. Lücken über 15 Min rekonstruiert Claude aus den Chat-Zeitstempeln und zieht sie ab.
**Form:** eine Zeile je Block. Die Blöcke-Spalte beginnt mit dem Blocktyp (EK · Blitz · Tag1 · R1 · Rettung · Schreib · Sim · 💻 Pflicht/Tool). Tage ohne Lernen bekommen eine 0-Zeile.

| Datum | Start | Ende | Pausen (Min) | Netto (Min) | Blöcke | Gerät |
|---|---|---|---|---|---|---|
