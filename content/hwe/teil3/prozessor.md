title: Prozessor
next: fpga.md
parent: uebersicht.md

# Projekt: Einfacher Prozessor mit diskreten Transistoren

## Ziel
Entwicklung und Simulation eines einfachen Prozessors, der ausschließlich auf diskreter Transistorlogik basiert. Die Schüler werden grundlegende digitale Bausteine entwerfen und simulieren, um schrittweise einen Prozessor zu realisieren.

## Beschreibung

Das Projekt besteht aus drei Hauptphasen:  

1. **Beschreibung und Simulation einfacher Gatter mit diskreter Transistorlogik (LTSpice)**  
   - Logikgatter wie AND, OR, NOT und NAND werden mit Transistoren (NPN und PNP) entworfen, simuliert und getestet.  

2. **Beschreibung und Simulation der ALU und anderer Grundbausteine des Prozessors (Logisim)**  
   - Aufbau und Simulation der ALU sowie weiterer Bausteine wie Register, Speicher und Steuerwerk in Logisim.  

3. **Beschreibung und Simulation des vollständigen Prozessors (Logisim)**  
   - Integration aller Komponenten in Logisim, um einen funktionierenden Prozessor mit minimalem Befehlssatz zu simulieren.

## Projektphasen

### **Phase 1: Beschreibung und Simulation einfacher Gatter (LTSpice)**  
- **Ziele:**
  - Verständnis der grundlegenden Funktionsweise von Transistoren als Schalter.
  - Aufbau digitaler Logikgatter mit diskreten Transistoren.
- **Aufgaben:**
  1. Simulation von Transistoren in LTSpice:
     - Untersuchung des Verhaltens eines einzelnen Transistors als Schalter.
     - Simulation einfacher Verstärkerschaltungen.
  2. Design und Simulation grundlegender Logikgatter:
     - **NOT-Gatter:** Ein einzelner Transistor invertiert das Eingangssignal.
     - **AND-Gatter:** Zwei Transistoren in Reihe, gesteuert durch zwei Eingänge.
     - **OR-Gatter:** Zwei Transistoren parallel geschaltet.
     - **NAND-Gatter:** Kombination von Transistoren zur Implementierung eines universellen Gatters.
  3. Überprüfung der Gatter-Logik durch Simulation von Wahrheitstabellen.
- **Ergebnisse:**  
  - Funktionierende LTSpice-Simulationen für alle grundlegenden Logikgatter.
  - Erkenntnisse über Signalflüsse und Schaltzeiten in Transistorschaltungen.

### **Phase 2: Beschreibung und Simulation der ALU und Grundbausteine (Logisim)**  
- **Ziele:**
  - Aufbau der ALU für arithmetische und logische Operationen.
  - Entwicklung weiterer Prozessorbausteine wie Register und Steuerwerk.
- **Aufgaben:**
  1. **ALU:**
     - Simulation eines 4-Bit-Addierers (Halbaddierer/Volladdierer).
     - Implementierung logischer Operationen wie AND, OR, XOR.
     - Auswahl der Operationen mit einem Multiplexer.
  2. **Register:**
     - Aufbau eines 4-Bit-Registers mit Flip-Flops.
     - Simulation des Ladens, Speicherns und Zurücksetzens von Werten.
  3. **Steuerwerk:**
     - Implementierung eines einfachen Taktgenerators.
     - Simulation einer Zustandsmaschine zur Steuerung der Befehlsabfolge.
  4. **Speicher:**
     - Aufbau eines kleinen Speichers (z. B. 16 x 4-Bit).
     - Adressierung und Datenfluss zwischen Speicher und ALU simulieren.
- **Ergebnisse:**  
  - Funktionierende Simulation der ALU und Grundbausteine in Logisim.
  - Verständnis der Interaktion zwischen den Bausteinen.

### **Phase 3: Beschreibung und Simulation des vollständigen Prozessors (Logisim)**  
- **Ziele:**
  - Integration der Bausteine zu einem vollständigen Prozessor.
  - Simulation eines minimalen Befehlssatzes und einfacher Programme.
- **Aufgaben:**
  1. **Integration:**
     - Zusammenschalten der ALU, Register, Speicher und Steuerwerk.
     - Synchronisation aller Komponenten über den Taktgenerator.
  2. **Instruction Set Architecture (ISA):**
     - Definition eines minimalen Befehlssatzes:
       - `ADD` (Addition von zwei Zahlen).
       - `LOAD` (Laden eines Werts in ein Register).
       - `STORE` (Speichern eines Werts im Speicher).
       - `JMP` (Springen zu einer Adresse).
  3. **Simulation von Programmen:**
     - Test eines einfachen Programms (z. B. Addition zweier Zahlen und Speichern des Ergebnisses).
     - Debugging der Datenflüsse und Steuersequenzen.
  4. **Visualisierung:**
     - Verwendung von LEDs oder Logisim-Symbolen zur Anzeige der Datenflüsse und Registerinhalte.
- **Ergebnisse:**  
  - Funktionierende Simulation eines vollständigen 4-Bit-Prozessors.
  - Verständnis des Zusammenspiels aller Prozessorbausteine.

## Lernziele
- Vermittlung der Grundlagen digitaler Schaltungen mit Transistoren.
- Verständnis der Funktionsweise grundlegender Prozessorbausteine wie ALU, Register und Steuerwerk.
- Entwicklung und Simulation einer kompletten CPU-Architektur.
- Einführung in Simulationswerkzeuge (LTSpice und Logisim).
