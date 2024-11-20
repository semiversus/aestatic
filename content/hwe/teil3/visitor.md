title: Besucherzähler
parent: uebersicht.md

# Projekt: Besucherzähler mittels Bluetooth MAC Adressen und MQTT

## Ziel
Entwicklung eines Systems zur Schätzung der Anzahl der Besucher in einem Raum oder Gebäude, basierend auf den **Bluetooth MAC-Adressen** der Geräte in der Nähe. Der Besucherzähler soll mit einem **ESP32** realisiert werden und die gezählten Besucherzahlen in Echtzeit über **MQTT** an ein zentrales System übertragen.

## Beschreibung

Das Projekt nutzt die Fähigkeit des **ESP32**, als Bluetooth-Empfänger zu agieren. Der ESP32 scannt regelmäßig nach Bluetooth-Geräten in der Nähe und extrahiert deren **MAC-Adressen**. Jedes Mal, wenn ein Gerät erkannt wird, wird es als ein Besucher gezählt. Diese Informationen werden dann über MQTT an ein zentrales System übertragen.

### Hardware:
- **ESP32** als Hauptcontroller.
- **MQTT-Broker** (z. B. Mosquitto, HiveMQ) zur Kommunikation.
- **Power Supply** für den ESP32 (z. B. USB-Stromversorgung oder Batterie).

### Software:
- **ESP32 mit Bluetooth Low Energy (BLE)** zur MAC-Adressen-Erkennung.
- **MQTT-Broker** für die Datenkommunikation.
- **Zentrale Anwendung** zur Visualisierung der Daten, z. B. ein Dashboard mit **Grafana** oder eine einfache Webinterface-Anwendung.
- **Arduino IDE** oder **ESP-IDF** für die Programmierung des ESP32.

## Projektphasen

### **Phase 1: Planung und Vorbereitung**
- **Ziele:**
  - Festlegung der Anforderungen und der Architektur des Systems.
  - Auswahl des Kommunikationsprotokolls (MQTT) und des verwendeten MQTT-Brokers.
- **Aufgaben:**
  1. Festlegung des Einsatzbereichs (z. B. ein Raum, ein Gebäude).
  2. Festlegung des gewünschten Zählmechanismus:
     - **Bluetooth MAC-Adresse scannen**: Erfassung der MAC-Adressen von Geräten in der Nähe.
     - **Doppelte MAC-Adressen vermeiden**: Sicherstellen, dass dieselbe MAC-Adresse nicht mehrfach gezählt wird (z. B. durch Caching und Timeout-Mechanismus).
  3. Festlegung des MQTT-Servers:
     - Auswahl eines lokalen MQTT-Servers (z. B. Mosquitto) oder eines Cloud-basierten MQTT-Dienstes.

### **Phase 2: Hardwareaufbau und Bluetooth-Scanning**
- **Ziele:**
  - Aufbau der Hardware und Konfiguration des Bluetooth-Scanning-Systems auf dem ESP32.
- **Aufgaben:**
  1. **ESP32 vorbereiten**:
     - Konfiguration des ESP32 für den **Bluetooth Low Energy (BLE)**-Scan-Modus.
     - Initialisierung des Bluetooth-Moduls auf dem ESP32 zur Suche nach Geräten.
  2. **MAC-Adressen sammeln**:
     - Programmierung des ESP32, um nach Bluetooth-Geräten in der Nähe zu scannen.
     - Extrahieren und Speichern der MAC-Adressen der gefundenen Geräte.
  3. **Datenübertragung**:
     - Testen der Kommunikation mit einem MQTT-Broker, um MAC-Adressen und Besucherzahlen zu senden.

### **Phase 3: Softwareentwicklung und Besucherzählung**
- **Ziele:**
  - Entwicklung der Logik zur Besucherzählung und Übertragung der Daten.
- **Aufgaben:**
  1. **Zählmechanismus**:
     - Bei jeder gefundenen MAC-Adresse wird die Anzahl der Besucher erhöht.
     - **Filterung** von mehrfach gesendeten MAC-Adressen innerhalb eines kurzen Zeitraums, um Duplikate zu vermeiden.
  2. **Datenübertragung über MQTT**:
     - Implementierung eines MQTT-Clients auf dem ESP32, der die Besucherdaten (z. B. aktuelle Besucherzahl) regelmäßig an den MQTT-Broker sendet.
  3. **Timeout und Caching**:
     - Implementierung eines Zeitmechanismus, um MAC-Adressen nach einer bestimmten Zeit aus der Liste zu entfernen, wenn sie nicht mehr gefunden werden.
  4. **Optimierung**:
     - Anpassung des Scanning-Intervalls, um eine Balance zwischen Genauigkeit und Stromverbrauch zu erreichen.

### **Phase 4: Integration und Visualisierung**
- **Ziele:**
  - Empfang der Besucherzahl über MQTT und deren Visualisierung.
- **Aufgaben:**
  1. **Zentrale Anwendung erstellen**:
     - Ein Dashboard oder eine Webanwendung entwickeln, die die aktuellen Besucherzahlen anzeigt.
     - Beispiel: Verwendung von **Grafana** zur Visualisierung der Daten, oder ein einfaches **Webinterface** zur Darstellung der Besucherzahl in Echtzeit.
  2. **Daten empfangen und visualisieren**:
     - Konfiguration eines **MQTT-Clients** auf dem zentralen System, um die gesendeten Besucherzahlen zu empfangen und darzustellen.

### **Phase 5: Test und Optimierung**
- **Ziele:**
  - Sicherstellen, dass das System zuverlässig funktioniert und die Besucherzahlen korrekt geschätzt werden.
- **Aufgaben:**
  1. **Testen des Bluetooth-Scanning**:
     - Überprüfung, ob der ESP32 die MAC-Adressen korrekt erfasst und Besucher korrekt zählt.
  2. **Fehlerbehebung**:
     - Sicherstellen, dass keine doppelten Zählungen stattfinden und das System korrekt reagiert, wenn Geräte den Bereich betreten oder verlassen.
  3. **Optimierung der Zählgenauigkeit**:
     - Anpassung der Parameter, wie z. B. Scanning-Intervalle, Timeout für MAC-Adressen und MQTT-Übertragungsintervalle, um eine möglichst genaue Zählung zu erzielen.

### **Phase 6: Dokumentation und Abschluss**
- **Ziele:**
  - Dokumentation des Systems und des Quellcodes.
- **Aufgaben:**
  1. **Erstellung eines Schaltplans**:
     - Überblick über die verwendeten Komponenten und Verbindungen.
  2. **Dokumentation der Software**:
     - Beschreibung des Codes, insbesondere der Logik für Bluetooth-Scanning, Besucherzählung und MQTT-Kommunikation.
  3. **Testberichte**:
     - Zusammenfassung der Testergebnisse und Optimierungsvorschläge.

## Lernziele
- Verständnis der Funktionsweise von **Bluetooth Low Energy (BLE)** zur Erkennung von Geräten in der Nähe.
- Implementierung eines **MQTT-basierten Systems** zur Übertragung von Daten in Echtzeit.
- Entwicklung eines Besucherzählmechanismus basierend auf **MAC-Adressen** und deren Schätzung.
- Einführung in die Nutzung des **ESP32** für drahtlose Kommunikation und die Implementierung von IoT-Systemen.
