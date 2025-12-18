title: RaspberryPi
parent: ../unterricht.md

# Inbetriebnahme
## Vorbereitungen

* Flashen des aktuellen Raspberry Pi OS mittels [Raspberry Pi Imager](https://www.raspberrypi.com/software/)

![Imager 1](raspberry/imager_screen1.png)
![Imager 2](raspberry/imager_screen2.png)
![Imager 3](raspberry/imager_screen3.png)
![Imager 4](raspberry/imager_screen4.png)
![Imager 5](raspberry/imager_screen5.png)
![Imager 6](raspberry/imager_screen6.png)
![Imager 7](raspberry/imager_screen7.png)
![Imager 8](raspberry/imager_screen8.png)
![Imager 9](raspberry/imager_screen9.png)


## Verbinden über VS Code
VS Code bietet die Möglichkeit sich per SSH mit dem RaspberryPi zu verbinden und dann direkt auf dem RaspberryPi zu arbeiten. Dazu ist die VS Code Extension **Remote Explorer** und **Remote SSH** notwendig.

Weitere Infos gibt es hier:
* [Raspberry Pi Remote Development Based On VSCode Tutorial](https://www.waveshare.com/wiki/Raspberry_Pi_Remote_Development_Based_On_vscode_Tutorial)
* [https://code.visualstudio.com/docs/remote/ssh](https://code.visualstudio.com/docs/remote/ssh)

## Git `user.name` und `user.email`
Im Terminal (am Raspberry) folgenden Befehl ausführen:
* `git config --global user.name "Max Muster"`
* `git config --global user.email "max@muster.com"`
