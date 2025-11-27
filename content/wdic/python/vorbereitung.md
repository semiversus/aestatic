title: Python Test Vorbereitung
parent: uebersicht.md

# Stoffübersicht
## Grundlegende Syntaxelemente
* Standard Datentypen: `int`, `float`, `str`, `bool`
* Typumwandlungen: `int()`, `float()`, `str()`, `bool()`
* Variablenzuweisung und Benennungskonventionen
* Ein- und Ausgabe: `input()`, `print()`
* Kommentare: `#` für einzeilige, `''' '''` oder `""" """` für mehrzeilige

## Kontrollstrukturen
* Bedingte Anweisungen: `if`, `elif`, `else`
* Schleifen: `for`, `while`
* Schleifensteuerung: `break`, `continue`, `pass`

## Funktionen
* Funktionsdefinition: `def`, Parameter, Rückgabewerte
* Argumenttypen: Positionsargumente, Schlüsselwortargumente, Standardargumente
* Gültigkeitsbereich von Variablen: lokal vs. global

## Datenstrukturen
* Listen (`list`): Erstellung, Zugriff, Slicing (`[start:end]`),Methoden (`append`, `remove`, ...)
* Tupel (`tuple`): Erstellung, Zugriff, Unveränderlichkeit
* Dictionaries (`dict`): Erstellung, Zugriff, Methoden (`keys`, `values`, `items`)
* Mengen (`set`): Erstellung, Zugriff, Methoden (`add`, `remove`, ...)

## Fehlerbehandlung
* Try-Except-Blöcke: `try`, `except`, `finally`

## Module und Bibliotheken
* Importieren von Modulen:`import`, `from ... import`
* Standardbibliothek: `math`, `random`, `datetime`, `os`, `sys`
* Installation und Nutzung externer Bibliotheken (z.B. via `pip`)

## Objektorientierte Programmierung (OOP)
* Klassen und Objekte: `class`, `__init__`, `self`
* Attribute und Methoden
* Vererbung und Polymorphismus

## Fortgeschrittene Themen
* Generatoren und Iteratoren (z.B. `range`)
* List Comprehensions

# Links
* [python-lernen.de](https://www.python-lernen.de/)
* [Offizielles Python Tutorial](https://docs.python.org/3/tutorial/index.html)

# Beispielaufgaben
## Aufgabe 1

```python
count = 0
total = 0

for i in range(1, 6):
    if i % 2 == 0:
        total += i
        count += 1
    else:
        total -= i
    print(count, total)
```

Welche Ausgabe erzeugt der obige Code?

## Aufgabe 2

```python
def transform(values):
    temp = []
    for v in values:
        if v % 3 == 0:
            temp.append(v + 10)
        elif v % 2 == 0:
            temp.append(v // 2)
        else:
            temp.append(v - 1)

    final = [x for x in temp if x >= 5]
    return sum(final)

print(transform([1, 2, 3, 4, 5, 6]))
```

## Aufgabe 3
``` python
def say_hello(name: str, greeting: str = "Hello", end: str = "!") -> str:
    print(f"{greeting} {name}{end}")

say_hello(greeting="Hi", name="Alice", end=".")
say_hello(name = "Diana", "Good morning", end = "...")
say_hello("Bob", end="?")
say_hello("Charlie", "Welcome", "!!!")
say_hello(end = ".")
```

Welche Ausgabe erzeugt der obige Code? Streiche die fehlerhaften Funktionsaufrufe durch.

## Aufgabe 4
```python
people = [
    {"name": "Anna", "age": 17},
    {"name": "Bob", "age": 20},
    {"name": "Carla", "age": 18}
]

people[1]["name"] = people[0]["name"]

people.append({"name": "Greta", "age": "17"})

x = people[2]["name"][1]

temp = people[0]
people[0] = people[-1]
people[-1] = temp

removed = people.pop(1)

names = [p["name"] for p in people if isinstance(p["age"], int)]

for p in people:
    if type(p["age"]) == int and p["age"] >= 18:
        p["age"] = str(p["age"]) + "?"

people_dict = {i: p["name"][0] for i, p in enumerate(people)}
```

Variable|Wert
:---:|:---:
`people`|
`removed`|
`x`|
`names`|
`people_dict`|

## Aufgabe 5
```python
a = {1, 2, 3, 3, 2}
b = set(3, 4)
a.add(5)
a.remove(1)
c = a.union(b)
d = a.intersection(b)
e = a - b
```

Welche Werte sind in den Variablen `a`, `b`, `c`, `d` und `e` nach Ausführung des Codes enthalten?

## Aufgabe 5
```python
class Counter:
    total = 0   # Klassenvariable

    def __init__(self, start=0):
        self.value = start

    def inc(self):
        self.value += 1
        Counter.total += 1

    def __repr__(self):
        return f"Counter(value={self.value}, total={Counter.total})"


class LimitedCounter(Counter):
    def __init__(self, start=0, limit=2):
        super().__init__(start)
        self.limit = limit

    def inc(self):
        if self.value < self.limit:
            super().inc()
        else:
            print("limit reached")

    def reset(self):
        # Achtung: verändert bewusst die Klassenvariable!
        Counter.total = 0
        self.value = 0


c1 = Counter()
c2 = LimitedCounter(start=1, limit=2)
```

Befehl|c1.value|c2.value|c1.total|c2.total
:---:|:---:|:---:|:---:|:---:
`c1.inc()`| | | |
`c2.inc()`| | | |
`c2.inc()`| | | |
`c2.reset()`| | | |
