title: Funktionen in Python
parent: uebersicht.md

# Grundlagen von Funktionen

Funktionen sind wiederverwendbare Codeblöcke, die eine bestimmte Aufgabe erfüllen. Sie helfen dabei, Code zu strukturieren, zu organisieren und Wiederholungen zu vermeiden.

## Definition einer Funktion

Eine Funktion wird in Python mit dem Schlüsselwort `def` definiert:

```python
def function_name(parameter):
    """Optional: Docstring to describe the function"""
    # Function code
    return result  # Optional: return value
```

### Einfaches Beispiel

```python
def greet(name):
    """Greets a person with their name"""
    return f"Hallo {name}!"

# Function call
message = greet("Anna")
print(message)  # Output: Hallo Anna!
```

## Parameter und Argumente

### Positionsargumente (Positional Arguments)

Argumente werden in der Reihenfolge der Parameter übergeben:

```python
def add(a, b):
    return a + b

result = add(5, 3)  # a=5, b=3
print(result)  # Output: 8
```

### Schlüsselwort-Argumente (Keyword Arguments)

Argumente werden explizit mit dem Parameternamen übergeben:

```python
def describe_person(name, age, city):
    return f"{name} ist {age} Jahre alt und lebt in {city}."

# Keyword Arguments - order doesn't matter
info = describe_person(age=25, city="Wien", name="Maria")
print(info)  # Output: Maria ist 25 Jahre alt und lebt in Wien.
```

### Standard-Argumente (Default Arguments)

Parameter können Standardwerte haben, die verwendet werden, wenn kein Argument übergeben wird:

```python
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

# Different calls
print(greet("Max"))                           # Hi Max!
print(greet("Lisa", "Hallo"))                 # Hallo Lisa!
print(greet("Tom", "Guten Tag", "."))         # Guten Tag Tom.
print(greet("Sarah", end="?"))                # Hi Sarah?
```

## Erweiterte Parametertypen

### *args - Variable Anzahl von Positionsargumenten

```python
def sum_numbers(*numbers):
    """Calculates the sum of any number of numbers"""
    total = 0
    for number in numbers:
        total += number
    return total

print(sum_numbers(1, 2, 3))        # Output: 6
print(sum_numbers(5, 10, 15, 20))  # Output: 50
```

### **kwargs - Variable Anzahl von Schlüsselwort-Argumenten

```python
def create_profile(name, **additional_info):
    """Creates a user profile with additional information"""
    profile = {"name": name}
    profile.update(additional_info)
    return profile

user = create_profile("Alex", age=30, job="Developer", city="Berlin")
print(user)  # {'name': 'Alex', 'age': 30, 'job': 'Developer', 'city': 'Berlin'}
```

### Kombination aller Parametertypen

```python
def complete_function(required_param, default_param="default", *args, **kwargs):
    """Demonstrates all parameter types"""
    print(f"Required parameter: {required_param}")
    print(f"Default parameter: {default_param}")
    print(f"Additional positional arguments: {args}")
    print(f"Keyword arguments: {kwargs}")

complete_function("important", "changed", 1, 2, 3, name="Test", value=42)
```

## Type Hints

Type Hints helfen dabei, den erwarteten Datentyp von Parametern und Rückgabewerten zu dokumentieren:

```python
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
print(f"New price: {new_price}")  # Output: New price: 80.0
```

## Best Practices

1. **Beschreibende Namen verwenden**: `calculate_tax()` statt `calc()`
2. **Docstrings schreiben**: Dokumentiere was die Funktion macht
3. **Type Hints verwenden**: Mache Datentypen explizit
4. **Eine Aufgabe pro Funktion**: Halte Funktionen fokussiert
5. **Sinnvolle Standardwerte**: Verwende sinnvolle Default-Parameter
6. **Immutable Default-Argumente**: Vermeide mutable Objekte als Standardwerte

```python
# Bad: Mutable Default-Argument
def bad_function(items=[]):  # Dangerous!
    items.append("new")
    return items

# Better: Use None as default
def good_function(items=None):
    if items is None:
        items = []
    items.append("new")
    return items
```