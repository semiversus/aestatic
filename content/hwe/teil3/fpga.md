title: FPGA Mainboard
next: visitor.md
parent: uebersicht.md

# Projekt: Mainboard mit Lattice ECP5 FPGA

## Ziel
Entwicklung eines Mainboards, das auf einem **Lattice ECP5 FPGA** basiert, um die vielseitigen Anwendungen moderner FPGAs zu demonstrieren. Das Mainboard soll Schnittstellen für Peripheriegeräte bieten und sowohl einfache Hardwarebeschleunigung als auch digitale Logikaufgaben ermöglichen.

---

## Beschreibung

Das Mainboard soll eine vielseitige Plattform sein, die sich für die Entwicklung und Implementierung digitaler Logik, Hardwarebeschleunigung oder komplexer Steuerungssysteme eignet. Der Fokus liegt auf:
- Der Implementierung des FPGA-Designs.
- Der Bereitstellung von Peripherieschnittstellen.
- Der Programmierbarkeit über eine geeignete Entwicklungsumgebung.

---

## Hardwareanforderungen

### **Hauptkomponenten:**
- **Lattice ECP5 FPGA**:
  - Modell: z. B. LFE5U-45F (oder höher, je nach Verfügbarkeit).
  - FPGA-Ressourcen: LUTs, Flip-Flops, DSP-Blöcke, Block-RAM.
- **Spannungsversorgung**:
  - Mehrspannungsversorgung für FPGA-Kern (z. B. 1,2 V) und IO-Bänke (z. B. 3,3 V).
  - Low-Dropout-Regler (LDO) oder Schaltregler zur effizienten Stromversorgung.
- **Speicher**:
  - SDRAM (z. B. 32 MB bis 64 MB).
  - Flash-Speicher für die FPGA-Konfiguration (z. B. SPI-Flash).
- **Kommunikationsschnittstellen**:
  - USB zu UART für Debugging und Steuerung.
  - SPI/I2C für externe Sensoren und Module.
  - High-Speed-Schnittstelle wie PCIe oder Gigabit-Ethernet (optional).
- **Peripherieanschlüsse**:
  - GPIO-Pins (General Purpose Input/Output).
  - JTAG für Programmierung und Debugging.
  - Anschlüsse für LED- und Tasteransteuerung.

### **I/O-Module und Erweiterung**:
- **HDMI/DVI-Ausgabe** (optional):
  - Unterstützung für Videobeschleunigung.
- **PMOD- und Erweiterungssteckplätze**:
  - Anbindung externer Module wie Displays, Sensoren oder Motorsteuerungen.
- **SPI-Flash-Speicher**:
  - Speicherung von FPGA-Bitstreams oder Benutzerdaten.

---

## Projektphasen

### **Phase 1: Planung und Schaltplanerstellung**
- **Ziele:**
  - Definition der Anforderungen (z. B. Anzahl GPIOs, Schnittstellen, Stromversorgung).
  - Erstellen eines Schaltplans mit EDA-Software (z. B. KiCAD, Altium Designer).
- **Aufgaben:**
  1. Auswahl eines passenden Lattice ECP5-Modells basierend auf Projektanforderungen.
  2. Entwurf der Spannungsversorgung, einschließlich Reglern und Filterkondensatoren.
  3. Einbindung der Speichermodule (SDRAM, SPI-Flash).
  4. Planung der Peripherieschnittstellen und Steckverbindungen.

### **Phase 2: PCB-Design und Fertigung**
- **Ziele:**
  - Layout des Mainboards und Vorbereitung für die Fertigung.
- **Aufgaben:**
  1. Entwurf eines mehrlagigen PCBs:
     - Power-Plane für stabile Stromversorgung.
     - Signal-Plane für Hochgeschwindigkeitssignale (z. B. DDR, PCIe).
  2. Signal- und Impedanzkontrolle:
     - Berücksichtigung von Leitungsführung und Terminierung.
  3. Fertigung des PCBs und Bestellung der Bauteile.
- **Ergebnisse:**  
  - Fertiges PCB-Layout bereit zur Produktion.

### **Phase 3: Aufbau und Inbetriebnahme**
- **Ziele:**
  - Zusammenbau des Mainboards und Überprüfung der Grundfunktionen.
- **Aufgaben:**
  1. Bestückung des PCBs mit Bauteilen.
  2. Ersttests:
     - Überprüfung der Spannungsversorgung.
     - Verbindungstests über JTAG.
  3. Initiales Laden eines FPGA-Bitstreams zur Überprüfung grundlegender Funktionen.
- **Ergebnisse:**  
  - Funktionsfähige Hardware mit Basisbetrieb.

### **Phase 4: FPGA-Design und Softwareintegration**
- **Ziele:**
  - Entwicklung von FPGA-Designs und Testsoftware.
- **Aufgaben:**
  1. FPGA-Konfiguration:
     - Erstellen eines Designs mit der Lattice Diamond IDE oder alternativen Open-Source-Tools (z. B. Yosys/Nextpnr).
     - Laden des Bitstreams über JTAG oder SPI-Flash.
  2. Testdesigns:
     - LED-Blinken, UART-Kommunikation, Speicherzugriff.
     - Einfaches Signalverarbeitungsmodul (z. B. Multiplikator mit DSP-Blöcken).
  3. Erweiterung:
     - Implementierung einer Videobeschleunigung (z. B. HDMI-Ausgabe).
     - Anbindung externer Module über GPIO oder PMOD.
- **Ergebnisse:**  
  - Funktionierende FPGA-Designs mit Anbindung an Peripherie und Speicher.

### **Phase 5: Dokumentation und Abschluss**
- **Ziele:**
  - Dokumentation der Hardware und FPGA-Designs.
- **Aufgaben:**
  1. Erstellung eines Schaltplans mit allen finalen Verbindungen.
  2. Anleitung zur Programmierung des FPGA und Nutzung der Schnittstellen.
  3. Zusammenfassung der Testergebnisse und Verbesserungsvorschläge.
- **Ergebnisse:**  
  - Vollständige Dokumentation des Projekts.

---

## Lernziele
- Verständnis für FPGA-Architekturen und deren Anwendungsmöglichkeiten.
- Planung und Umsetzung eines Mainboards mit modernen Entwicklungswerkzeugen.
- Grundlagen des PCB-Designs und der Hochfrequenzsignale.
- Nutzung von Tools wie Lattice Diamond, Yosys oder KiCad.
- Verständnis für Hardware-Software-Integration und Systemdesign.
