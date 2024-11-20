title: Digital Signange
next: aggregator.md
parent: uebersicht.md

# Projekt: Raspberry Pi Pico 2 Mainboard

## Ziel
Entwicklung eines Mainboards, das den [Raspberry Pi Pico 2](https://www.raspberrypi.com/products/raspberry-pi-pico-2/) als zentrale Recheneinheit integriert und zusätzliche Funktionen sowie Schnittstellen bereitstellt.

## Beschreibung

### Hardware
- **Zentrale Einheit:** Raspberry Pi Pico.
- **Erweiterungen auf dem Mainboard:**
  - GPIO-Breakout für einfacheren Zugriff auf die Pins.
  - Spannungswandler oder Power-Management für 3,3V und 5V Komponenten.
  - USB-Port für Kommunikation oder Stromversorgung.
  - Steckplätze für Sensoren und Module (z. B. I²C-, SPI- und UART-Schnittstellen).
  - Zusätzliche LEDs zur Statusanzeige (Power, Aktivität, Fehler).
  - Reset-Taster und Bootloader-Taster.
  - Erweiterte Peripherieoptionen, z. B.:
    - Steckplätze für Servos oder Motorsteuerungen.
    - Relaismodule.
    - Analog-Digital-Wandler für zusätzliche analoge Eingänge.

### Software
- **Firmware-Programmierung:** Basiscode für den Raspberry Pi Pico zur Steuerung der Peripherie.
- **Pin-Mapping-Dokumentation:** Klar definierte Zuweisung der GPIOs zu den Funktionen des Mainboards.
- **Testprogramme:** Entwicklung kleiner Anwendungen zum Testen der Peripherie (z. B. LED-Blink, Sensorabfrage).

### Funktionalität
- Das Mainboard ermöglicht eine einfache und modulare Erweiterung des Raspberry Pi Pico.
- Bereitstellung von stabilen Spannungen und Plug-and-Play-Schnittstellen für Peripheriegeräte.
- Optimierung der Bedienung durch Statusanzeigen und praktische Steuerelemente (z. B. Taster).
- Testplattform für zukünftige Projekte oder Experimente.

### Erweiterungen
- Integration eines kleinen OLED-Displays oder eines 7-Segment-Displays zur Ausgabe von Daten.
- Entwicklung eines Shieldsystems, bei dem zusätzliche Module (z. B. WLAN, Motorsteuerung) einfach auf das Mainboard aufgesteckt werden können.
- Optionale Bluetooth- oder Wi-Fi-Kommunikation durch passende Module.
- Einsatz eines E-Paper-Displays für energiesparende Anwendungen.

---

## Lernziele
- Entwicklung einer Leiterplatte (PCB) mit CAD-Tools (z. B. KiCad, Eagle).
- Vertiefung der Kenntnisse über den Raspberry Pi Pico und seine Peripherieschnittstellen.
- Grundlagen der Schaltungstechnik und Spannungsversorgung.
- Test und Debugging von Hardware-Schaltungen.
- Integration von Software und Hardware.