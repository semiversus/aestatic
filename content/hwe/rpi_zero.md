title: Raspberry Pi Zero
parent: ../unterricht.md

# Vorbereitung
Folgendes wird benötigt:
* Raspberry Pi Zero W (oder 2)
* Micro SD Karten Lesegerät (oft im Notebook vorhanden)
* Micro USB auf USB A Kabel

# Installation
* Ein Raspberry Pi OS hier herunterladen: [https://www.raspberrypi.com/software/](https://www.raspberrypi.com/software/)
  * Wähle die "Raspberry Pi OS Lite"
  * Im Zweifel die nicht 64-Bit Variante wählen, die funktioniert mit allen Raspberry Pis
* Mittels [Raspberry Pi Imager](https://downloads.raspberrypi.org/imager/imager_latest.exe) das Image auf die MicroSD Karte kopieren

# Verbindung mit dem Raspberry Pi aufbauen
## Mittels USB Kabel
* Bearbeiten der Datei `config.txt` (auf der FAT32 Partition der MicroSD Karte)
  * Füge folgende Zeile am Ende der Datei hinzu: `dtoverlay=dwc2`
* Bearbeiten der Datei `cmdline.txt` (auch auf der FAT32 Partition)
  * Füge folgenden Text hinter `rootwait` hinzu: `modules-load=dwc2,g_ether`
* Klicke auf "Auswerfen" bei der MicroSD Karte und stecke sie in den Raspberry Pi Zero
*