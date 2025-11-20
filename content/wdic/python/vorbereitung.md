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

print(people)
print("removed:", removed)
print("x:", x)
print("names:", names)
print("people_dict:", people_dict)
```