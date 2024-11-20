title: Digital Signange
next: pico2_mainboard.md
parent: uebersicht.md

# Projekt: Digital Signage mit Raspberry Pi

## Ziel
Entwicklung eines digitalen Informationsdisplays, das Inhalte dynamisch über ein Webinterface oder [MQTT](https://de.wikipedia.org/wiki/MQTT) empfangen und darstellen kann. Die Stromversorgung des Displays soll über ein Relais gesteuert werden.

## Beschreibung

### Hardware
- **Raspberry Pi** zur Steuerung.
- Ein geeignetes Display (z. B. HDMI-Monitor oder kleines LCD).
- Elektronik zur Steuerung der Stromversorgung des Displays.

### Software
- Erstellung einer Benutzeroberfläche zur Verwaltung der angezeigten Inhalte (z. B. Texte, Bilder, Videos).
- Kommunikation mit dem Raspberry Pi über **MQTT** oder ein **Webinterface**.
- Steuerung des Relais zur Ein-/Ausschaltung des Displays über die Benutzeroberfläche.

### Funktionalität
- Nutzer können Inhalte (z. B. Begrüßungsnachrichten, Wetterdaten, Zeitpläne) über ein Webinterface oder MQTT-Client einstellen.
- Das Display wird entsprechend aktualisiert und zeigt die Inhalte an.
- Das Relais schaltet die Stromversorgung des Displays automatisch ab, wenn keine Inhalte angezeigt werden sollen (Stromsparmodus).

### Erweiterungen
- Integration eines Timers für geplante Display-Ansteuerung (z. B. automatische Aktivierung während der Schulzeit).
- Einsatz von Sensoren zur Umgebungserkennung, z. B. **Bewegungssensor**, der das Display bei Annäherung aktiviert.
- Darstellung von Echtzeitdaten (z. B. Wetter, Nachrichten, Uhrzeit) durch Abruf von Online-Diensten (z.B. WebUntis).

## Lernziele
- Umgang mit dem **Raspberry Pi** als Steuerzentrale.
- Ansteuerung von Hardware-Komponenten wie **Relaismodulen**.
- Kommunikation über **MQTT-Protokoll** oder Webtechnologien.
- Grundkenntnisse in Frontend- und Backend-Entwicklung.
- Optimierung des Energieverbrauchs durch gezielte Steuerung der Stromversorgung.