title: Funktionen in Python
parent: uebersicht.md
next: oop.md

# Grundlagen von Funktionen

Funktionen sind wiederverwendbare Codeblöcke, die eine bestimmte Aufgabe erfüllen. Sie helfen dabei, Code zu strukturieren, zu organisieren und Wiederholungen zu vermeiden.

# Definition einer Funktion

Eine Funktion wird in Python mit dem Schlüsselwort `def` definiert:

```python
def function_name(parameter):
    """Optional: Docstring zur Beschreibung der Funktion"""
    # Funktionscode
    return result  # Optional: Rückgabewert
```

# Ein einfaches Beispiel

.. python::
    def greet(name):
        """Greets a person with their name"""
        return f"Hallo {name}!"

    message = greet("Anna")
    print(message)

# Parameter und Argumente

## Positionsargumente (Positional Arguments)

Argumente werden in der Reihenfolge der Parameter übergeben:

.. python::
    def add(a, b):
        return a + b

    result = add(5, 3)  # a=5, b=3
    print(result)

## Schlüsselwort-Argumente (Keyword Arguments)

Argumente werden explizit mit dem Parameternamen übergeben:

.. python::
    def describe_person(name, age, city):
        return f"{name} ist {age} Jahre alt und lebt in {city}."

    info = describe_person(age=25, city="Wien", name="Maria")
    print(info)

## Standard-Argumente (Default Arguments)

Parameter können Standardwerte haben, die verwendet werden, wenn kein Argument übergeben wird:

.. python::
def greet(name: str, greeting: str = "Hi", end: str = "!") -> str:
    """
    Creates a greeting message

    Args:
        name: The name of the person to greet
        greeting: The greeting (default: "Hi")
        end: The character at the end (default: "!")

    Returns:
        The formatted greeting message
    """
    return f"{greeting} {name}{end}"

    print(greet("Max"))
    print(greet("Lisa", "Hi"))
    print(greet("Tom", "Guten Tag", "."))
    print(greet("Sarah", end="?"))

# Erweiterte Parametertypen

## *args - Variable Anzahl von Positionsargumenten

.. python::
    def sum_numbers(*numbers):
    """Calculates the sum of any number of numbers"""
        total = 0
        for number in numbers:
            total += number
        return total

    print(sum_numbers(1, 2, 3))
    print(sum_numbers(5, 10, 15, 20))

## **kwargs - Variable Anzahl von Schlüsselwort-Argumenten

.. python::
    def create_profile(name, **additional_info):
    """Creates a user profile with additional information"""
        profile = {"name": name}
        profile.update(additional_info)
        return profile

    user = create_profile("Alex", age=30, job="Developer", city="Berlin")
    print(user)

## Kombination aller Parametertypen

.. python::
    def complete_function(required_param, default_param="default", *args, **kwargs):
        print(f"Pflichtparameter: {required_param}")
        print(f"Standardparameter: {default_param}")
        print(f"Weitere Positionsargumente: {args}")
        print(f"Schlüsselwort-Argumente: {kwargs}")

    complete_function("wichtig", "geändert", 1, 2, 3, name="Test", value=42)

# Type Hints

Type Hints helfen dabei, den erwarteten Datentyp von Parametern und Rückgabewerten zu dokumentieren:

.. python::
    def calculate_discount(price: float, discount_percent: int = 10) -> float:
        """
        Calculates the price after discount

        Args:
            price: The original price
            discount_percent: The discount percentage (default: 10)

        Returns:
            The reduced price
        """
        discount = price * (discount_percent / 100)
        return price - discount

    new_price = calculate_discount(100.0, 20)
    print(f"Neuer Preis: {new_price}")

# Best Practices

1. **Beschreibende Namen verwenden**: `calculate_tax()` statt `calc()`
2. **Docstrings schreiben**: Dokumentiere, was die Funktion macht
3. **Type Hints verwenden**: Mache Datentypen explizit
4. **Eine Aufgabe pro Funktion**: Halte Funktionen fokussiert
5. **Sinnvolle Standardwerte**: Verwende sinnvolle Default-Parameter
