title: Python Unittest Übung
parent: uebersicht.md

# Unittests

Vorbereitungen:

1. Neues Verzeichnis erstellen (Name `unittests`)
1. Dieses Verzeichnis mit VS Code öffnen
1. Eine leere Datei `main.py` in diesem Ordner erstellen
1. In VS Code das Terminal öffnen und `python -m venv .venv` ausführen
1. Nun gibt es zwei Varianten:
  1. VS Code sollte nun die virtuelle Umgebung erkennen und fragen, ob man es auswählen will -> Dies mit "Ja" (bzw. "Yes") bestätigen
  2. Falls VS Code nicht nachfragt, hilft es das aktuelle Terminal zu schließen (Mülleimer-Symbol) und wieder zu öffnen
1. Das Paket pytest mittels `python -m pip install pytest` installieren

## Übung Durchschnittsalter
* Dateiname: `average_age.py`
* Funktion: `def get_average_age(persons_dict: dict) -> float:`

Der Funktion wird ein *Dictionary* übergeben. Die *Keys* sind Personennamen (*Strings*) und die *Values* sind das Alter.

Beispiel:

```python
>>> get_average_age({'Klaus': 17, 'Hubert': 19, 'Otto': 20})
18.666666666666668
```

### Unittest
* Dateiname: `test_average_age.py`

* Der Unittest soll die Funktion `get_average_age` sinvoll testen.
* Sind die Anforderungen vollständig definiert?

## Übung Median
* Dateiname: `median.py` bzw. `test_median.py`
* Funktion: `def calc_median(numbers: list) -> float:`

Der Funktion wird eine Liste an Zahlen übergeben. Zurückgegeben wird der sogenannte [Median](https://de.wikipedia.org/wiki/Median) -> die Zahl, die in der Mitte steht, wenn die Liste sortiert ist.

Beispiel:

```python
>>> calc_median([3, 1, 6, 10 ,2])
3
```

Auch in dieser Übung ist der entsprechende Unittest zu entwerfen

## Übung Progressive Steuern
* Dateiname: `progressive_tax.py` bzw. `test_progressive_tax.py`
* Funktion: `def calc_tax(earnings: float) -> float:`

Implementiere eine Funktion die die progressiven Steuern laut [Österreichischer Einkommenssteuertabelle](https://www.finanz.at/steuern/lohnsteuertabelle/) berechnet.

Beispiel:

```python
>>> calc_tax(700)
0
>>> calc_tax(2000)
242.366  # using data from 2023: 985.42€: 0%, 1605,50€: 20%, 2683.92€: 30%
```

## Übung Zinseszins
* Dateiname: `compound_interest.py` bzw. `test_compound_interest.py`
* Funktion: `def calc_compound_interest(value: float, years: int, interest: float) -> float:`

Wir berechnen den [Zinseszins](https://de.wikipedia.org/wiki/Zinseszins). Dazu starten wir mit einem Kapital (`value`), legen es für eine bestimmte Anzahl an Jahren (`years`) an zu einem bestimmten Zinssatz in Prozent (`interest`).

Beispiel:

```python
>>> calc_compound_interest(1000, 1, 1)
1010
>>> calc_compount_interest(1, 2000, 0.5)
21484.41
```

## Übung Elemente zählen
* Dateiname: `enumerate_list.py` bzw. `test_enumerate_list.py`
* Funktion: `def enumerate_list(elements: list) -> dict:`

Aus einer Liste an Elemente soll ein Dictionary erstellt werden, welches die Anzahl der enthaltenen Elemente angibt.

Beispiel:

```python
>>> enumerate_list(['A', 'B', 'B', 'C', 'A', 'A'])
{'A': 3, 'B': 2, 'C': 1}
>>> enumerate_list([1, 0, 2, 2, 0, 0, 1, 2])
{1: 2, 0: 3, 2: 3}
```

## Übung Gemeinsamkeiten
* Dateiname: `common_list.py` bzw. `test_common_list.py`
* Funktion: `def get_common_elements(list1: list, list2: list) -> list:`

Die Funktion ermittelt die Elemente, die in beiden Listen sind. Die Ausgabe ist selbst wieder
eine Liste, deren Sortierung aber beliebig sein kann.

Beispiel:

```python
>>> get_common_elements([1, 2, 3, 4, 1], [2, 1])
[1, 2]
>>> get_common_elements(['A', 1, 'A', 0, 'B'], ['C', 'D'])
[]
```

## Übung Wörter durcheinander würfeln
* Dateiname: `shuffle.py` bzw. `shuffle.py`
* Funktion: `def shuffle_words(message: str) -> str:`

Ein String bestehend aus mehreren Wörtern soll wortweise durcheinander gewürfelt werden. Dabei
soll jeweils der erste und letzte Buchstabe eines Wortes unverändert bleiben.

Beispiel:

```python
>>> shuffle_words('Hier wohnt Herr Schuster')
'Heir wnoht Hrer Steuschr'
```

Hinweise:

* Um einen String zufällig zu sortieren seht ihr hier in der ersten Antwort ein Beispiel: [Stackoverflow](https://stackoverflow.com/questions/2668312/shuffle-string-in-python/2668366#2668366)
* Beim Testen wird es auch etwas schwieriger, weil ihr überprüfen müsst, ob das Resultat gültig ist. [sorted()](https://docs.python.org/3/library/functions.html#sorted) kann hier hilfreich sein!
* Im String kommen keine Satzzeichen vor (`.`, `,`, ...)

## Übung Niedrigster Preis
* Dateiname: `lowest_price.py` bzw. `test_lowest_price.py`
* Funktion: `def lowest_price(items: dict) -> list:`

Der Funktion wird ein Dictionary mit Artikelnamen und deren Preisen gegeben. Zurückgegeben werden soll eine Liste mit den drei günstigsten Artikeln.

Beispiel:

```python
>>> get_cheapest_articles({'Allegro': 17.5, 'Adagio': 3.5, 'Forte': 15, 'Largo': 5, 'Legato': 18})
['Adagio', 'Largo', 'Forte']
```

Hinweis:

* Das Wörterbuch enthält immer mindestens drei Einträge
