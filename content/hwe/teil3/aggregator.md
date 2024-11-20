title: Datenaggregator
next: prozessor.md
parent: uebersicht.md

# Projekt: MQTT-Datenaggregator mit ESP32

## Ziel
Entwicklung eines Systems zur Datenerfassung, -aggregation und -speicherung. Mehrere ESP32-Module erfassen Sensor- und GPIO-Daten (z. B. ADC-Werte, Digital-Inputs) und senden diese per MQTT an ein zentrales System, das die Daten speichert und visualisiert.

## Beschreibung

### Hardware
- **ESP32**:
  - Datenerfassung über ADC-Pins (z. B. Spannung, Temperatur, Lichtintensität).
  - Überwachung von Digital-Inputs (z. B. Tasterzustände, Bewegungsmelder).
- **Zentrales System**:
  - Raspberry Pi, PC oder Server mit installiertem MQTT-Broker (z. B. Mosquitto).
  - Speicherlösung für aggregierte Daten:
    - Datenbank (z. B. InfluxDB, SQLite, MySQL).
    - Optionale lokale Speicherung in JSON- oder CSV-Dateien.
- Optional:
  - Sensoren (z. B. DHT22, LDR, Spannungsmessmodule).
  - Anzeigeeinheit (OLED oder LCD für vor-Ort-Datenanzeige).

### Software

#### 1. **ESP32-Firmware**
- **Funktionalität:**
  - Periodische Abfrage der ADC-Werte und Digital-Inputs.
  - Versand der Messwerte an den MQTT-Broker.
  - MQTT-Client-Setup mit Topics für jeden Datenpunkt (z. B. `esp32_1/adc1`, `esp32_1/input1`).
  - Konfiguration der Abfrageintervalle (z. B. 1 Sekunde, 10 Sekunden).
- **Erweiterungen:**
  - OTA-Update (Over-the-Air) für Firmwareaktualisierungen.
  - MQTT-Kommunikation für Konfigurationsänderungen (z. B. Samplingrate).

#### 2. **Zentrales System**
- **Funktionalität:**
  - MQTT-Broker für die Kommunikation.
  - Aggregation der Daten von mehreren ESP32-Modulen:
    - Strukturierte Speicherung der Daten mit Zeitstempel.
    - Gruppierung nach Quelle (ESP32-Modul) und Datentyp (ADC, Digital-Input).
  - Speicherung der Daten in einer Datenbank oder als CSV-/JSON-Dateien.
  - Optionale Visualisierung der Daten:
    - Verwendung von Tools wie **Grafana**, **Node-RED** oder eigener Webanwendungen.
- **Erweiterungen:**
  - Webinterface zur Anzeige der gespeicherten Daten.
  - Alarm- oder Benachrichtigungssystem bei Grenzwertüberschreitungen.

---

### Funktionalität
- Mehrere ESP32-Module sammeln Daten und senden sie per MQTT an den zentralen Broker.
- Das zentrale System speichert und verarbeitet die empfangenen Daten.
- Visualisierung der aggregierten Daten in Echtzeit über Dashboards.
- Benutzerdefinierte Benachrichtigungen bei kritischen Ereignissen (z. B. ADC-Werte außerhalb eines sicheren Bereichs).

## Lernziele
- Einführung in das MQTT-Protokoll und dessen Implementierung auf ESP32.
- Sensordatenerfassung über ADC und GPIOs.
- Aufbau eines zentralen Datenmanagementsystems mit MQTT-Broker.
- Speicherung und Visualisierung von Echtzeitdaten.
- Grundlagen von Datenbanken und Webvisualisierung.
