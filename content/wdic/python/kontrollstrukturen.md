title: Kontrollstrukturen
parent: uebersicht.md
next: paketmanagement.md

# Verzweigungen
Bislang wurden Programme von oben nach unten abgearbeitet. Für alles Weitere sind Kontrollstrukturen (engl. *control structures*) erforderlich: Sie erlauben es, je nach Bedingung unterschiedliche Codepfade auszuführen bzw. Anweisungen zu wiederholen.

Zuerst die Verzweigung mittels `if`:

```python
temperature = 12

if temperature < 15:
    print("Kalt")
elif temperature < 25:
    print("Angenehm")
else:
    print("Heiß")
```

Dabei gilt:

* Die Bedingung nach `if` wird ausgewertet. Ist sie wahr (`True`), so wird der eingerückte Block ausgeführt, ansonsten wird er übersprungen
* `elif` (kurz für *else if*) und `else` sind optional, `elif` kann mehrfach vorkommen. Die Bedingungen werden der Reihe nach geprüft, sobald eine zutrifft, werden die restlichen übersprungen
* Blöcke werden in Python nicht mittels Klammern, sondern mittels Einrückung definiert (üblich sind 4 Leerzeichen). `elif` und `else` stehen auf derselben Höhe wie das zugehörige `if`

# Bedingungen
Vergleichsoperatoren liefern einen Wahrheitswert (`True` bzw. `False`):

| Operator | Bedeutung |
|:---:|:---|
| `==` | gleich |
| `!=` | ungleich |
| `<`, `>`, `<=`, `>=` | Vergleiche |
| `in` | enthalten in (z.B. `"a" in "Ananas"`, `3 in [1, 2, 3]`) |

Mehrere Bedingungen lassen sich mittels `and`, `or` und `not` kombinieren:

```python
age = 17
has_ticket = True

if age >= 16 and has_ticket:
    print("Einlass erlaubt")
```

Als Bedingung ist aber jeder Wert erlaubt, nicht nur `True` bzw. `False`. Python interpretiert leere bzw. Null-Werte (`0`, `0.0`, `""`, leere Listen, `None`) als falsch, alles andere als wahr. Das erlaubt knifflige Abkürzungen wie:

```python
name = ""
if not name:
    print("Kein Name angegeben")
```

# Die while-Schleife
Eine `while`-Schleife wiederholt einen Block, solange die Bedingung wahr ist:

```python
countdown = 5

while countdown > 0:
    print(countdown)
    countdown -= 1

print("Start!")
```

Wichtig: Die Bedingung muss irgendwann falsch werden, sprich im Block muss etwas passieren, das die Bedingung verändert. Bleibt die Bedingung immer wahr, erhält man eine Endlosschleife - abbrechen lässt sich ein laufendes Programm dann im Terminal mittels <kbd>Ctrl</kbd> + <kbd>c</kbd>.

Die `while`-Schleife passt immer dann, wenn die Anzahl der Durchläufe vorab nicht bekannt ist, z.B. bei einer Abfrage, bis eine gültige Eingabe vorliegt.

# Die for-Schleife
Die `for`-Schleife läuft über die Elemente einer Sequenz (z.B. eine Liste oder ein String), sprich der Block wird einmal pro Element ausgeführt:

```python
word_list = ['Warthog', 'Hedgehog', 'Badger']

for word in word_list:
    print(word)
```

Soll eine Zahlensequenz durchlaufen werden, so dient `range()`, mittels dessen auch das klassische "zähle von x bis y" ausgedrückt wird:

```python
for i in range(5):          # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 10):      # 2, 3, ..., 9
    print(i)

for i in range(0, 100, 10): # 0, 10, 20, ..., 90
    print(i)
```

Wird zusätzlich zum Element der Index benötigt, so liefert `enumerate()` beides:

```python
for index, word in enumerate(['Warthog', 'Hedgehog']):
    print(index, word)  # 0 Warthog / 1 Hedgehog
```

In Python wird die `for`-Schleife also viel universeller eingesetzt als das `for` aus C-ähnlichen Sprachen: Statt einem Zähler steht das zu verarbeitende Element im Mittelpunkt. Sie entspricht dem `foreach` in C#.

# break und continue
Innerhalb einer Schleife steuern zwei Anweisungen den Ablauf:

* `break` verlässt die Schleife sofort
* `continue` überspringt den Rest des aktuellen Durchlaufs und springt zur nächsten Iteration

Typisches Beispiel - Suche in einer Liste:

```python
word_list = ['Warthog', 'Hedgehog', 'Badger', 'Drake']
search = 'Badger'

for word in word_list:
    if word == search:
        print(search, 'gefunden!')
        break
```

# Aufgaben
* Was gibt das folgende Programm aus? Was macht der `else`-Block der Schleife?

```python
for word in ['Warthog', 'Hedgehog', 'Badger']:
    if word == 'Drake':
        break
else:
    print('Drake nicht gefunden')
```

* Schreibe ein Programm, das alle Zahlen von 1 bis 100 ausgibt, die durch 3 **oder** durch 5 teilbar sind
* Schreibe eine Abfrage mittels `while`, die so lange eine Eingabe anfordert, bis diese eine Zahl zwischen 1 und 100 ist
