title: Objektorientierte Programmierung
parent: uebersicht.md
next: fehlerbehandlung.md

# Klassen und Objekte
Bislang wurden Daten und Funktionen getrennt voneinander betrachtet: Variablen speichern Werte, Funktionen verarbeiten sie. Die objektorientierte Programmierung (engl. *object-oriented programming* oder kurz *OOP*) führt diese beiden Konzepte zusammen. Eine **Klasse** (engl. *class*) dient dabei als Bauplan, mittels dessen sich Objekte erzeugen lassen, die sowohl Daten (Attribute) als auch Verhalten (Methoden) kapseln.

# Eine erste Klasse
Eine Klasse wird mittels `class` definiert. Der Name der Klasse wird üblicherweise mit einem Großbuchstaben begonnen:

```python
class Person:
    pass
```

Mittels dieses Bauplans lässt sich nun ein Objekt (engl. *object* bzw. *instance*, sprich Instanz) erzeugen:

```python
person = Person()
print(type(person))  # <class '__main__.Person'>
```

`Person()` ruft dabei automatisch eine besondere Methode auf, den Konstruktor, und liefert das fertige Objekt zurück.

# Attribute und der Konstruktor
Attribute sind Variablen, die zu einem Objekt gehören. Sie werden im Konstruktor `__init__` angelegt. `__init__` (sprich "dunder init", von *double underscore*) wird bei jedem neu erzeugten Objekt automatisch aufgerufen.

Das besondere Parameter `self` verweist dabei auf das Objekt selbst, sprich mittels `self` lassen sich Attribute auf dem Objekt ablegen:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("Anna", 17)
print(person.name)  # Anna
print(person.age)   # 17
```

Dabei gilt:

* `self` ist immer der erste Parameter einer Methode, wird beim Aufruf aber nicht explizit übergeben - Python setzt es automatisch auf das Objekt, auf dem die Methode aufgerufen wird
* Mittels `self.name = name` wird das Attribut `name` auf dem Objekt angelegt und mit dem übergebenen Wert belegt
* Auf die Attribute lässt sich von außen mittels Punktnotation zugreifen: `person.name`

Jedes Objekt erhält dadurch seine eigenen Attribute. Legt man ein zweites Objekt an, sind dessen Attribute unabhängig vom ersten:

```python
person1 = Person("Anna", 17)
person2 = Person("Ben", 16)

print(person1.name)  # Anna
print(person2.name)  # Ben

person1.age = 18     # nur person1 ändert sich
print(person1.age)   # 18
print(person2.age)   # 16
```

# Methoden
Neben Attributen kann eine Klasse auch Methoden definieren, sprich Funktionen, die zu dem Objekt gehören. Auch hier steht `self` als erster Parameter, mittels dessen auf die Attribute des Objekts zugegriffen wird:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hallo, ich bin {self.name} und {self.age} Jahre alt."

    def have_birthday(self):
        self.age += 1
        return self.age

person = Person("Anna", 17)
print(person.greet())        # Hallo, ich bin Anna und 17 Jahre alt.

new_age = person.have_birthday()
print(new_age)               # 18
print(person.greet())        # Hallo, ich bin Anna und 18 Jahre alt.
```

Der Aufruf `person.greet()` ist dabei äquivalent zu `Person.greet(person)` - Python übergibt das Objekt automatisch als erstes Argument, sprich `self`.

# Standardwerte im Konstruktor
Wie bei Funktionen lassen sich auch bei `__init__` Standardwerte (engl. *default arguments*) definieren:

```python
class Person:
    def __init__(self, name, age=0):
        self.name = name
        self.age = age

baby = Person("Lena")
print(baby.age)  # 0
```

# Attribute direkt in der Klasse
Neben den Instanzattributen (die mittels `self` pro Objekt angelegt werden) lassen sich auch Klassenattribute definieren, sprich Werte, die für alle Objekte derselben Klasse gelten:

```python
class Person:
    count = 0  # Klassenattribut

    def __init__(self, name):
        self.name = name
        Person.count += 1

p1 = Person("Anna")
p2 = Person("Ben")

print(Person.count)  # 2
print(p1.count)      # 2 (Zugriff auch über das Objekt möglich)
```

Klassenattribute eignen sich z.B. zum Zählen, wie viele Objekte insgesamt erzeugt wurden.

# Die String-Darstellung: __str__
Wird ein Objekt mittels `print()` ausgegeben, erscheint standardmäßig nur die Speicheradresse. Mittels der Methode `__str__` lässt sich definieren, wie das Objekt als Text dargestellt wird:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"

person = Person("Anna", 17)
print(person)  # Person(name=Anna, age=17)
```

Methoden, die mit doppeltem Unterstrich beginnen und enden (sogenannte *dunder methods*), haben in Python eine besondere Bedeutung - `__str__` wird z.B. automatisch von `print()` und `str()` aufgerufen.

# Kapselung: private Attribute
In Python gibt es keine echte Privatheit, sprich Attribute lassen sich theoretisch von außen verändern. Per Konvention werden Attribute, die nicht von außen geändert werden sollen, mit einem Unterstrich begonnen:

```python
class Bankkonto:
    def __init__(self, inhaber, guthaben=0):
        self.inhaber = inhaber
        self._guthaben = guthaben  # konventionell "privat"

    def einzahlen(self, betrag):
        if betrag > 0:
            self._guthaben += betrag

    def get_guthaben(self):
        return self._guthaben

konto = Bankkonto("Anna", 100)
konto.einzahlen(50)
print(konto.get_guthaben())  # 150
```

Das Attribut `_guthaben` ist damit als "intern" markiert. Der Zugriff von außen ist zwar technisch möglich (`konto._guthaben`), aber per Konvention unerwünscht. Kontrollierter Zugriff erfolgt stattdessen über Methoden wie `get_guthaben()`.

# Vererbung
Eine Klasse lässt sich von einer anderen Klasse ableiten (engl. *inheritance*, sprich Vererbung). Die abgeleitete Klasse (auch *Unterklasse* genannt) übernimmt dabei alle Attribute und Methoden der Basisklasse und kann diese erweitern oder überschreiben:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hallo, ich bin {self.name}."

class Schueler(Person):  # Schueler erbt von Person
    def __init__(self, name, age, klasse):
        super().__init__(name, age)  # Konstruktor der Basisklasse aufrufen
        self.klasse = klasse

    def greet(self):  # überschreibt die Methode der Basisklasse
        return f"Hallo, ich bin {self.name} aus der {self.klasse}."

s = Schueler("Anna", 17, "4AHIF")
print(s.greet())     # Hallo, ich bin Anna aus der 4AHIF.
print(s.age)         # 17 (Attribut von Person)
```

Dabei gilt:

* `class Schueler(Person)` leitet `Schueler` von `Person` ab
* `super().__init__(name, age)` ruft den Konstruktor der Basisklasse auf, sprich die Attribute `name` und `age` werden dort angelegt
* Eine überschriebene Methode (hier `greet`) ersetzt das Verhalten der Basisklasse
* Mittels `isinstance(s, Person)` lässt sich prüfen, ob ein Objekt von einer bestimmten Klasse (oder einer davon abgeleiteten) stammt: `isinstance(s, Person)` liefert `True`

# Aufgaben
* Schreibe eine Klasse `Rechteck` mit den Attributen `breite` und `hoehe`. Der Konstruktor soll beide Werte entgegennehmen. Ergänze die Methoden `flaeche()` und `umfang()`, die beide als `return` zurückgeben
* Erweitere die Klasse `Person` um eine Methode `is_volljährig()`, die `True` zurückgibt, wenn `age >= 18`, sonst `False`
* Leite von `Person` eine Klasse `Lehrer` ab mit zusätzlichem Attribut `fach`. Überschreibe `greet()`, sodass z.B. `Hallo, ich bin Herr Müller und unterrichte Informatik.` ausgegeben wird
* Schreibe eine Klasse `Zaehler`, die ein Klassenattribut `anzahl` verwendet, um mitzuzählen, wie viele Objekte erzeugt wurden. Teste mit drei Objekten
