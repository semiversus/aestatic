title: Fehlerbehandlung
parent: uebersicht.md

# Exceptions
Was passiert eigentlich, wenn etwas schiefgeht? Ein Beispiel:

```python
number = int("abc")
```

Die Ausführung bricht mit folgender Meldung ab:

```console
$> python main.py
Traceback (most recent call last):
  File "main.py", line 1, in <module>
    number = int("abc")
ValueError: invalid literal for int() with base 10: 'abc'
```

Python wirft in so einem Fall eine Exception (engl. *exception*, zu deutsch Ausnahme). Der *Traceback* zeigt an, in welcher Datei und Zeile der Fehler aufgetreten ist, welchen Typ die Exception hat (`ValueError`) und was der Grund war. Ein unbehandeltes Programm bricht damit ab.

Exceptions sind aber nicht nur Fehlermeldungen: Sie lassen sich gezielt abfangen und behandeln, wodurch das Programm kontrolliert weiterlaufen kann.

# try und except
Zum Abfangen einer Exception dient `try`/`except`:

```python
user_input = input("Bitte eine Zahl: ")

try:
    number = int(user_input)
    print("Die Zahl ist", number)
except ValueError:
    print("Das war keine Zahl!")
```

Dabei gilt:

* Der Block nach `try` wird "geschützt" ausgeführt. Tritt dabei eine Exception auf, so wird der Rest des Blocks übersprungen und der passende `except`-Block ausgeführt
* Danach läuft das Programm ganz normal weiter, sprich es bricht nicht mehr ab
* Tritt keine Exception auf, so wird der `except`-Block übersprungen
* Passt kein `except` zur aufgetretenen Exception, so bricht das Programm dennoch ab

Genau damit lässt sich die Aufgabe aus [Kontrollstrukturen](kontrollstrukturen.html) sauber lösen - eine Abfrage, so lange wiederholt wird, bis eine gültige Zahl vorliegt:

```python
while True:
    user_input = input("Zahl zwischen 1 und 100: ")

    try:
        number = int(user_input)
        break
    except ValueError:
        print("Ungültige Eingabe, nochmal versuchen")
```

# Passende Exceptions abfangen
Der `except`-Block gibt an, welche Exception-Typen er behandelt. Dabei sollte möglichst spezifisch abgefangen werden:

```python
except (ValueError, TypeError):   # mehrere Typen, kommasepariert in Klammern
except Exception as e:             # Zugriff auf das Exception-Objekt, z.B. print(e)
```

Ein `except` ohne Typ (`except:`) fängt zwar alles ab, ist aber schlechte Praxis: Damit werden auch Fehler versteckt, die man sehen sollte (z.B. Tippfehler im Code), was die Fehlersuche massiv erschwert. Als letzte Auffanginstanz eignet sich `Exception`, da von dieser Klasse fast alle Exceptions abgeleitet sind.

# Häufige Exceptions
| Exception | Auslöser |
|:---|:---|
| `ValueError` | Richtiger Typ, aber ungeeigneter Wert, z.B. `int("abc")` |
| `TypeError` | Unpassender Typ, z.B. `"a" + 5` |
| `ZeroDivisionError` | Division durch 0, z.B. `10 / 0` |
| `IndexError` | Index außerhalb einer Sequenz, z.B. `[1, 2, 3][10]` |
| `KeyError` | Fehlender Schlüssel in einem `dict` |
| `FileNotFoundError` | Angeforderte Datei existiert nicht |

Die Namen sind Programm: Sie sagen bereits, was schiefgelaufen ist, und erleichtern das gezielte Abfangen. Die vollständige Liste aller eingebauten Exceptions findet sich in der [Python-Dokumentation](https://docs.python.org/3/library/exceptions.html).

# else und finally
Analog zu Schleifen lässt sich auch bei der Fehlerbehandlung ein `else`-Anhang definieren, sowie ein `finally`-Block, der in jedem Fall ausgeführt wird:

```python
try:
    number = int(user_input)
except ValueError:
    print("Keine Zahl!")
else:
    print("Erfolg, die Zahl ist", number)
finally:
    print("Wird in jedem Fall ausgeführt, z.B. zum Aufräumen")
```

* `else` läuft, wenn keine Exception aufgetreten ist
* `finally` läuft immer - egal ob Erfolg, abgefangener oder unbehandelter Fehler. Typische Einsatzgebiete sind Aufräumarbeiten, etwa das Schließen einer Datei

# Eigene Fehler mittels raise
Mittels `raise` lässt sich selbst eine Exception auslösen - etwa wenn eine Funktion eine unzulässige Eingabe erhält:

```python
def set_age(age):
    if age < 0:
        raise ValueError("Alter darf nicht negativ sein: " + str(age))
```

Der Aufruf `set_age(-5)` bricht dann mit `ValueError: Alter darf nicht negativ sein: -5` ab, sprich der eigene Code verhält sich genau wie die eingebauten Funktionen auch.

# Aufgaben
* Was gibt das folgende Programm aus - und in welcher Reihenfolge?

```python
try:
    print("Start")
    result = 10 / 0
    print("Nach der Division")
except ZeroDivisionError:
    print("Division durch 0!")
finally:
    print("Aufräumen")
```

* Erweitere das Ratespiel aus [Erste Beispiele](beispiele.html) mittels `try`/`except`, sodass es bei einer Eingabe wie `"abc"` nicht mehr abstürzt, sondern erneut fragt
* Schreibe eine Funktion `divide(a, b)`, die bei `b == 0` mittels `raise` eine `ZeroDivisionError` mit eigenem Text auslöst
