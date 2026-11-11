title: List Comprehension
parent: uebersicht.md
next: paketmanagement.md

# List Comprehension
Mittels einer *List Comprehension* (sprich eine kompakte Schreibweise, um Listen zu erzeugen) lässt sich eine Liste in einer einzigen Zeile aufbauen - statt dafür eine `for`-Schleife mit `append()` zu verwenden. List Comprehensions zählen zu den beliebtesten Konstrukten in Python, da sie kompakt und zugleich gut lesbar sind.

# Grundform
Die Grundform einer List Comprehension lautet:

```python
[ausdruck for element in sequenz]
```

Dabei wird die Sequenz durchlaufen, für jedes Element der `ausdruck` ausgewertet und das Ergebnis in eine neue Liste eingetragen. Das folgende Beispiel erzeugt eine Liste der Quadratzahlen von 0 bis 9:

```python
squares = [x * x for x in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

Dies ist äquivalent zu:

```python
squares = []
for x in range(10):
    squares.append(x * x)
```

Die List Comprehension erledigt beide Schritte - Schleife und Anhängen - in einem einzigen Konstrukt.

# Mit Bedingung
Häufig sollen nur bestimmte Elemente in die neue Liste aufgenommen werden. Dazu wird eine `if`-Bedingung angehängt:

```python
[ausdruck for element in sequenz if bedingung]
```

Beispiel - nur die geraden Zahlen von 0 bis 19:

```python
even_numbers = [x for x in range(20) if x % 2 == 0]
print(even_numbers)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
```

Oder alle Wörter aus einer Liste, die länger als 5 Buchstaben sind:

```python
word_list = ['Warthog', 'Hedgehog', 'Badger', 'Drake', 'Eft']
long_words = [word for word in word_list if len(word) > 5]
print(long_words)  # ['Warthog', 'Hedgehog', 'Badger']
```

# Mit if-else
Soll der Ausdruck selbst von einer Bedingung abhängen, steht das `if`/`else` vor dem `for`:

```python
[ausdruck_if_true if bedingung else ausdruck_if_false for element in sequenz]
```

Beispiel - Zahlen klassifizieren als "gerade" bzw. "ungerade":

```python
labels = ["gerade" if x % 2 == 0 else "ungerade" for x in range(6)]
print(labels)  # ['gerade', 'ungerade', 'gerade', 'ungerade', 'gerade', 'ungerade']
```

# Verschachtelte Comprehensions
List Comprehensions lassen sich auch verschachteln, sprich mehrere `for`-Teile hintereinander schreiben. Damit lässt sich z.B. eine Matrix (Liste von Listen) abflachen:

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [x for row in matrix for x in row]
print(flat)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

Dabei wird zuerst über die Zeilen (`for row in matrix`), dann über die Elemente der jeweiligen Zeile (`for x in row`) iteriert - die Reihenfolge der `for`-Teile entspricht der Schachtelung einer normalen `for`-Schleife.

# Dictionary und Set Comprehension
Neben Listen lassen sich mittels derselben Syntax auch *Mengen* (engl. *set*) und *Zuordnungen* (engl. *dictionary*) kompakt erzeugen:

```python
# Set Comprehension - eindeutige Quadratzahlen
unique_squares = {x * x for x in range(-5, 6)}
print(unique_squares)  # {0, 1, 4, 9, 16, 25}

# Dictionary Comprehension - Wort zu seiner Länge
words = ['Warthog', 'Badger', 'Drake']
lengths = {word: len(word) for word in words}
print(lengths)  # {'Warthog': 7, 'Badger': 6, 'Drake': 5}
```

Die Klammern bestimmen dabei den Typ: `[...]` für Liste, `{...}` für Set bzw. Dictionary (mit `key: value`), `(...)` für einen Generator (engl. *generator expression*), der die Werte erst bei Bedarf erzeugt und damit speicherschonender ist.

# Lesbarkeit: Wann einsetzen?
List Comprehensions sind ideal, wenn eine einzelne Liste aus einer vorhandenen Sequenz erzeugt wird. Sobald mehrere unabhängige Schritte nötig sind - z.B. eine Liste aufbauen und anschließend sortieren, oder mehrere Listen kombinieren - wird eine normale `for`-Schleife oft klarer. Als Faustregel gilt: Was in eine Zeile passt und verständlich bleibt, lässt sich mittels List Comprehension ausdrücken, alles andere mittels expliziter Schleife.

# Aufgaben
* Erzeuge mittels List Comprehension eine Liste aller Zahlen von 1 bis 100, die durch 3 teilbar sind
* Ausgehend von einer Liste `temperatures = [12, 18, 25, 8, 30, 15]` sollen mittels List Comprehension zwei Listen entstehen: eine mit allen Temperaturen über 20 und eine mit allen Temperaturen darunter
* Erzeuge mittels verschachtelter List Comprehension eine 5x5-Multiplikationstabelle als Liste von Listen: `[[1, 2, ..., 5], [2, 4, ..., 10], ...]`
* Zähle mittels Dictionary Comprehension, wie oft jeder Buchstabe in einem Wort vorkommt, z.B. `{'a': 3, 'n': 1, 's': 1}` für `'Ananas'`
