title: Paketmanagement
parent: uebersicht.md
next: funktionen.md

# Pakete und Paketmanager
Python bringt bereits eine umfangreiche Standardbibliothek mit. Für viele Aufgaben lohnt es sich aber, auf fertige Pakete (engl. *packages*) zurückzugreifen, die auf [PyPI](https://pypi.org), dem offiziellen Paketindex von Python, veröffentlicht werden - sei es zum Erstellen von Diagrammen, zum Abrufen von Webseiten oder für formatierte Ausgaben im Terminal.

Ein Paketmanager dient zum Installieren und Verwalten solcher Pakete. Klassisch wird dafür `pip` verwendet. In der Praxis ergibt sich damit aber schnell ein Problem: Installiert man Pakete "global", so können sich Projekte gegenseitig in die Quere kommen, z.B. wenn zwei Projekte unterschiedliche Versionen desselben Pakets benötigen. Deshalb arbeitet man mit sogenannten virtuellen Umgebungen (engl. *virtual environments*), sprich jedes Projekt erhält seine eigene, isolierte Sammlung an Paketen.

Genau hier setzt **uv** (gesprochen wie die Abkürzung für *ultraviolet*) an: Das Tool kombiniert einen sehr schnellen Paketmanager mit der Verwaltung virtueller Umgebungen und Abhängigkeiten (engl. *dependencies*) und deckt damit den gesamten Workflow eines Projekts ab.

# Installation von uv
Je nach Plattform erfolgt die Installation mittels eines Einzeilers im Terminal.

Unter Windows (PowerShell):

```console
$> powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Unter macOS/Linux:

```console
$> curl -LsSf https://astral.sh/uv/install.sh | sh
```

Alternativ lässt sich uv auch mittels `pip install uv` installieren.

Nach einem Neustart des Terminals lässt sich die Installation überprüfen:

```console
$> uv --version
```

Erscheint eine Versionsnummer, war die Installation erfolgreich.

# Verwendung: ein kleines Beispiel
Es soll das Paket `rich` verwendet werden, mittels dessen sich Ausgaben im Terminal farbig und formatiert darstellen lassen.

Dazu wird ein neues Projekt angelegt und das Paket installiert:

```console
$> uv init paket_demo
$> cd paket_demo
$> uv add rich
```

Was dabei passiert:

* `uv init` legt ein neues Projekt an, sprich ein Verzeichnis mit der Konfigurationsdatei `pyproject.toml` und einem Python-Skript `main.py`
* `uv add rich` installiert das Paket und trägt es in `pyproject.toml` ein. Weiters wird eine Sperrdatei `uv.lock` mit den exakten Versionen aller Abhängigkeiten angelegt sowie eine virtuelle Umgebung im Verzeichnis `.venv` erstellt

Nun wird der Inhalt von `main.py` durch folgendes Programm ersetzt:

```python
from rich import print

print("[bold green]Hallo[/bold green] vom Paket [italic]rich[/italic]!")
```

Die Ausführung erfolgt mittels `uv run`:

```console
$> uv run main.py
Hallo vom Paket rich!
```

Dabei wird das Skript automatisch in der virtuellen Umgebung des Projekts ausgeführt, sprich `rich` steht zur Verfügung, ohne dass die Umgebung selbst aktiviert werden muss.

# Die wichtigsten Befehle im Überblick
* `uv init NAME` - legt ein neues Projekt an
* `uv add PAKET` - installiert ein Paket und trägt es in `pyproject.toml` ein
* `uv remove PAKET` - entfernt ein Paket wieder
* `uv run SKRIPT` - führt ein Skript in der virtuellen Umgebung des Projekts aus
* `uv lock` - schreibt die exakten Versionen aller Abhängigkeiten in `uv.lock` fest
* `uv sync` - stellt die Umgebung anhand von `uv.lock` wieder her (z.B. nach einem `git clone`)

Abhängigkeiten werden üblicherweise ohne `.venv` in der Versionsverwaltung gespeichert, `uv.lock` und `pyproject.toml` hingegen schon. Damit lässt sich ein Projekt auf einem anderen Rechner mittels `uv sync` exakt wiederherstellen.
