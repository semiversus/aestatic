title: Python Hausübung 3
parent: uebersicht.md

Für alle Übungen sollte man sich das Verhalten bei Grenzfällen überlegen und entsprechende Fehlerausgaben implementieren. Jede Übung ergebt Punkte, aufgeteilt auf die eigentliche Übung und eine Erweiterung.

# Namen sortieren
<span class="tag is-rounded is-info">1 + 2 Punkte</span>
Der Benutzer soll eine Liste an Namen eingeben können. Wenn der Nutzer statt einers Namens einfach Enter betätigt, sollen die Namen in sortierter Reihenfolge ausgegeben werden.

```
Name: Roman Huber
Name: Sabine Maria Ebenhoch
Name: Anton Valentin Lenz
Name: Susanne Sonne
Name:
Anton Valentin Lenz
Roman Huber
Sabine Maria Ebenhoch
Susanne Sonne
```

Erweiterung: Die Sortierung soll nicht nach dem Vornamen sondern dem Nachnamen erfolgen. Dazu gehen wir davon aus, dass das letzte Wort der Nachname ist.

# Tabelle zeichnen
<span class="tag is-rounded is-info">2 + 2 Punkte</span>
Der Benutzer wird nach Breite und Höhe einer Tabelle gefragt und diese wird im Anschluss gezeichnet.

```
Zeilen: 2
Spalten: 5
+-+-+-+-+-+
| | | | | |
+-+-+-+-+-+
| | | | | |
+-+-+-+-+-+
```

Erweiterung: In die Kästchen sollen abwechselnd die Zeichen X und O eingefügt werden.
```
+-+-+-+-+-+
|X|O|X|O|X|
+-+-+-+-+-+
|O|X|O|X|O|
+-+-+-+-+-+
```

# Hangman
<span class="tag is-rounded is-info">3 + 1 Punkte</span>
Beim Spiel Hangman soll der Spieler probieren ein Wort zu raten, in dem er Buchstaben vorgibt. Ist der Buchstabe richtig, werden die richtigen Buchstaben angezeigt. Bei einem Fehler wird die Anzahl der möglichen Versuche verringert (es startet mit 5 Versuchen)

```
_______
Buchstabe: E
Nur noch 4 Versuche
Buchstabe: O
_O_O___
Buchstabe: T
_O_OT__
Buchstabe: R
RO_OT__
Buchstabe: I
RO_OTI_
Buchstabe: B
ROBOTI_
Buchstabe: K
ROBOTIK – Richtig!
```

Erweiterung: Bei der Eingabe und beim Wort sollen Groß- und Kleinschreibung ignoriert werden.

# Kleinste Differenz
<span class="tag is-rounded is-info">2 + 2 Punkte</span>
Der Benutzer soll eine Liste an Zahlen eingeben können. Wenn der Nutzer statt einer Zahl einfach Enter betätigt, sollen die beiden Zahlen mit der kleinsten Differenz ausgegeben werden

```
Zahl: 3
Zahl: 8
Zahl: 7
Zahl:
Die beiden Zahlen mit der kleinsten Differenz sind 7 und 8
```

Erweiterung: Erlaube die Verarbeitung von Kommazahlen. Dabei soll der Nutzer `.` und `,` als Dezimaltrennzeichen verwenden können.

# Häufigster Buchstabe
<span class="tag is-rounded is-info">2 + 1 Punkte</span>
Der Benutzer soll einen Satz eingeben können und das Programm ermittelt, welcher Buchstabe am häufigsten vorkommt.

```
Satz: Also lautet ein Beschluß - Daß der Mensch was lernen muß.
Der häufigste Buchstabe ist e
```

Mögliche Erweiterung: Die Groß- und Kleinschreibung soll ignoriert werden. Es soll außerdem der zweit und dritthäufigste Buchstabe angezeigt werden.

# Geldausgabe
<span class="tag is-rounded is-info">3 + 3 Punkte</span>
Wir gehen von der 1 Euro Münze bis zum 100 Euro Schein aus. Der Benutzer wird nach einem Betrag gefragt und das Programm gibt aus welche Scheine und Münzen man minimal benötigt, um diesen Betrag abzubilden.

```
Betrag: 149
1x100
2x20
1x5
2x2
```

Mögliche Erweiterung: Nutze Kommazahlen als Betrag und Erweitere die Ausgabe um Cent Münzen. Erweitere die Ausgabe um das Wort “Schein” und “Münze” (z.B. 1x100 Schein)

# Zeitangabe
<span class="tag is-rounded is-info">3 + 3 Punkte</span>
Der Benutzer trägt einen Wert in Sekunden ein und die Ausgabe wird in Jahre, Tage, Stunden, Minuten und Sekunden angezeigt.

```
Anzahl an Sekunden: 94200
0y, 1d, 2h, 10min, 0s
```

Erweiterung: Statt der Kurzzeichen soll Stunden/Stunde usw. ausgeben werden. Bei Anzahl 0 soll der entsprechende Wert nicht ausgegeben werden. Die Ausgabe wird durch Beistriche getrennt und der letzte Wert mit ` und ` ausgegeben z.B. `1 Tag, 2 Stunden und 10 Minuten`.

# Zahlen in Worte wandeln <span class="tag is-rounded is-info">3 + 3 Punkte</span>
Der Benutzer gibt eine Zahl kleiner Hundert ein und diese Zahl wird dann in Worten ausgegeben.

```
Zahl: 47
siebenundvierzig
```

Mögliche Erweiterung: Es sollen Zahlen bis kleiner Zehntausend umgewandelt werden