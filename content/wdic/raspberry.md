title: RaspberryPi
parent: ../unterricht.md

# Inbetriebnahme
## Vorbereitungen

* Flashen des aktuellen Raspberry Pi OS mittels [Raspberry Pi Imager](https://www.raspberrypi.com/software/)
  * 64 Bit Version wird bevorzugt (32 Bit geht aber auch)
  * Die *Lite* Version ist die minimale Installation und reicht für unsere Anwendungen vollkommen aus
* Kopieren der Datei [firstrun.sh](./raspberry/firstrun.sh) auf die SD Karte (in die FAT32 Bootpartition)
* Editieren der Datei `cmdline.txt`
  * Falls es keinen Eintrag `systemd.run=/boot/firstrun.sh systemd.run_success_action=reboot systemd.unit=kernel-command-line.target` gibt, diesen hinzufügen 
* Öffne die Datei und ändere in der 3. Zeile den Namen ("max_muster" ist voreingestellt)
* SD Karte in den Raspberry Pi stecken und booten

Der Raspberry Pi verbindet sich nun mit dem Wifi "wdic" (Passwort "raspberry"). Nun kann mittels [Putty](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html) über SSH zugegriffen werden.

* Der Benutzername ist "pi" (Passwort "raspberry")

## Verbinden über VS Code
VS Code bietet die Möglichkeit sich per SSH mit dem RaspberryPi zu verbinden und dann direkt auf dem RaspberryPi zu arbeiten. Dazu ist die VS Code Extension "Remote Explorer" notwendig.

Weitere Infos gibt es hier:
* [Raspberry Pi Remote Development Based On VSCode Tutorial](https://www.waveshare.com/wiki/Raspberry_Pi_Remote_Development_Based_On_vscode_Tutorial)
* [https://code.visualstudio.com/docs/remote/ssh](https://code.visualstudio.com/docs/remote/ssh)
