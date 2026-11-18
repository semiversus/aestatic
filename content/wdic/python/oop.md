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

Mittels dieses Bauplans lässt sich nun ein Objekt (engl. *object* bzw. *instance*, sprich Instanz) erzeugen. `Person()` ruft dabei automatisch eine besondere Methode auf, den Konstruktor, und liefert das fertige Objekt zurück. Zum Ausprobieren:

.. python::
    class Person:
        pass

    person = Person()
    print(type(person))

# Attribute und der Konstruktor
Attribute sind Variablen, die zu einem Objekt gehören. Sie werden im Konstruktor `__init__` angelegt. `__init__` (sprich "dunder init", von *double underscore*) wird bei jedem neu erzeugten Objekt automatisch aufgerufen.

Das besondere Parameter `self` verweist dabei auf das Objekt selbst, sprich mittels `self` lassen sich Attribute auf dem Objekt ablegen:

.. python::
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

    person = Person("Anna", 17)
    print(person.name)
    print(person.age)

Dabei gilt:

* `self` ist immer der erste Parameter einer Methode, wird beim Aufruf aber nicht explizit übergeben - Python setzt es automatisch auf das Objekt, auf dem die Methode aufgerufen wird
* Mittels `self.name = name` wird das Attribut `name` auf dem Objekt angelegt und mit dem übergebenen Wert belegt
* Auf die Attribute lässt sich von außen mittels Punktnotation zugreifen: `person.name`

Jedes Objekt erhält dadurch seine eigenen Attribute. Legt man ein zweites Objekt an, sind dessen Attribute unabhängig vom ersten:

.. python::
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

    person1 = Person("Anna", 17)
    person2 = Person("Ben", 16)

    print(person1.name)
    print(person2.name)

    person1.age = 18     # only person1 changes
    print(person1.age)
    print(person2.age)

# Methoden
Neben Attributen kann eine Klasse auch Methoden definieren, sprich Funktionen, die zu dem Objekt gehören. Auch hier steht `self` als erster Parameter, mittels dessen auf die Attribute des Objekts zugegriffen wird:

.. python::
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
    print(person.greet())

    new_age = person.have_birthday()
    print(new_age)
    print(person.greet())

Der Aufruf `person.greet()` ist dabei äquivalent zu `Person.greet(person)` - Python übergibt das Objekt automatisch als erstes Argument, sprich `self`.

# Standardwerte im Konstruktor
Wie bei Funktionen lassen sich auch bei `__init__` Standardwerte (engl. *default arguments*) definieren:

.. python::
    class Person:
        def __init__(self, name, age=0):
            self.name = name
            self.age = age

    baby = Person("Lena")
    print(baby.age)

# Klassenattribute
Neben den Instanzattributen (die mittels `self` pro Objekt angelegt werden) lassen sich auch Klassenattribute definieren, sprich Werte, die für alle Objekte derselben Klasse gelten. Klassenattribute eignen sich z.B. zum Zählen, wie viele Objekte insgesamt erzeugt wurden:

.. python::
    class Person:
        count = 0  # class attribute

        def __init__(self, name):
            self.name = name
            Person.count += 1

    p1 = Person("Anna")
    p2 = Person("Ben")

    print(Person.count)
    print(p1.count)  # access via the object works too

# Die String-Darstellung: __str__
Wird ein Objekt mittels `print()` ausgegeben, erscheint standardmäßig nur die Speicheradresse. Mittels der Methode `__str__` lässt sich definieren, wie das Objekt als Text dargestellt wird:

.. python::
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def __str__(self):
            return f"Person(name={self.name}, age={self.age})"

    person = Person("Anna", 17)
    print(person)

Methoden, die mit doppeltem Unterstrich beginnen und enden (sogenannte *dunder methods*), haben in Python eine besondere Bedeutung - `__str__` wird z.B. automatisch von `print()` und `str()` aufgerufen.

# Kapselung: private Attribute
In Python gibt es keine echte Privatheit, sprich Attribute lassen sich theoretisch von außen verändern. Per Konvention werden Attribute, die nicht von außen geändert werden sollen, mit einem Unterstrich begonnen. Kontrollierter Zugriff erfolgt stattdessen über Methoden:

.. python::
    class BankAccount:
        def __init__(self, owner, balance=0):
            self.owner = owner
            self._balance = balance  # conventionally "private"

        def deposit(self, amount):
            if amount > 0:
                self._balance += amount

        def get_balance(self):
            return self._balance

    account = BankAccount("Anna", 100)
    account.deposit(50)
    print(account.get_balance())

Das Attribut `_balance` ist damit als "intern" markiert. Der Zugriff von außen ist zwar technisch möglich (`account._balance`), aber per Konvention unerwünscht.

# Vererbung
Eine Klasse lässt sich von einer anderen Klasse ableiten (engl. *inheritance*, sprich Vererbung). Die abgeleitete Klasse (auch *Unterklasse* genannt) übernimmt dabei alle Attribute und Methoden der Basisklasse und kann diese erweitern oder überschreiben:

.. python::
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def greet(self):
            return f"Hallo, ich bin {self.name}."

    class Student(Person):  # Student inherits from Person
        def __init__(self, name, age, grade):
            super().__init__(name, age)  # call the base class constructor
            self.grade = grade

        def greet(self):  # overrides the base class method
            return f"Hallo, ich bin {self.name} aus der {self.grade}."

    s = Student("Anna", 17, "4AHIF")
    print(s.greet())
    print(s.age)  # attribute of Person

Dabei gilt:

* `class Student(Person)` leitet `Student` von `Person` ab
* `super().__init__(name, age)` ruft den Konstruktor der Basisklasse auf, sprich die Attribute `name` und `age` werden dort angelegt
* Eine überschriebene Methode (hier `greet`) ersetzt das Verhalten der Basisklasse
* Mittels `isinstance(s, Person)` lässt sich prüfen, ob ein Objekt von einer bestimmten Klasse (oder einer davon abgeleiteten) stammt: `isinstance(s, Person)` liefert `True`

# Aufgabe: Playlist

Starter-Code - führe ihn aus und erweitere ihn Schritt für Schritt:

.. python::
    class Song:
        def __init__(self, title, artist, duration):
            self.title = title
            self.artist = artist
            self.duration = duration  # Sekunden

        def __str__(self):
            minutes = self.duration // 60
            seconds = self.duration % 60
            return f"{self.title} von {self.artist} ({minutes}:{seconds:02d})"

    song1 = Song("Rosa", "Herbert Grönemeyer", 233)
    song2 = Song("Bohemian Rhapsody", "Queen", 354)

    print(song1)
    print(song2)

**Schritt 1 - Song testen.** Führe den Starter-Code aus. Die Ausgabe sollte lauten:

```
Rosa von Herbert Grönemeyer (3:53)
Bohemian Rhapsody von Queen (5:54)
```

**Schritt 2 - Klasse `Playlist`.** Ergänze unterhalb der Klasse `Song` eine Klasse `Playlist`. Der Konstruktor legt eine leere Liste `self._songs` an (konventionell "privat"). Ergänze weiters zwei Methoden:

* `add_song(song)` - hängt einen Song an die Liste an
* `total_duration()` - liefert die Summe aller Song-Dauern in Sekunden als `return`

Teste mittels:

```python
pl = Playlist()
pl.add_song(song1)
pl.add_song(song2)
print(pl.total_duration())
```

Erwartete Ausgabe: `587`

**Schritt 3 - String-Darstellung der Playlist.** Ergänze der Klasse `Playlist` eine Methode `__str__`, die die Songs nummeriert ausgibt und am Ende die Gesamtzeit im Format `m:ss` anhängt:

```
1: Rosa von Herbert Grönemeyer (3:53)
2: Bohemian Rhapsody von Queen (5:54)
Gesamt: 9:47
```

Teste mittels `print(pl)`. Hinweis: Die Gesamtzeit lässt sich mittels `total_duration()` berechnen, das Format `9:47` erhält man analog zu Schritt 1 mittels `//`, `%` und `:02d`.

**Schritt 4 - Song entfernen.** Ergänze eine Methode `remove_song(title)`, die den Song mit dem passenden Titel aus `self._songs` löscht und `True` zurückgibt. Existiert kein Song mit diesem Titel, so soll `False` zurückgegeben werden. Teste mittels:

```python
print(pl.remove_song("Rosa"))
print(pl.remove_song("Unbekannt"))
print(pl)
```

Erwartete Ausgabe:

```
True
False
1: Bohemian Rhapsody von Queen (5:54)
Gesamt: 5:54
```

**Schritt 5 - Vererbung: `PremiumPlaylist`.** Leite eine Klasse `PremiumPlaylist` von `Playlist` ab. Der Konstruktor nimmt zusätzlich `owner` entgegen und ruft mittels `super().__init__()` den Konstruktor der Basisklasse auf. Überschreibe `__str__`, sodass am Anfang `Playlist von {owner}` steht, z.B.:

```
Playlist von Anna
1: Bohemian Rhapsody von Queen (5:54)
Gesamt: 5:54
```

Teste mittels:

```python
premium = PremiumPlaylist("Anna")
premium.add_song(song2)
print(premium)
```

**Schritt 6 - Klassenattribut.** Ergänze der Klasse `Playlist` ein Klassenattribut `count = 0`, das im Konstruktor mittels `Playlist.count += 1` erhöht wird. Teste am Ende:

```python
print(Playlist.count)
```

Nach den obigen Schritten (eine `Playlist`, eine `PremiumPlaylist`) sollte `2` ausgegeben werden.
