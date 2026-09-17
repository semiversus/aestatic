title: Hardwareentwicklung Teil 1 & Teil 2
parent: ../../unterricht.md

# Projekt Roboter

In diesem Projekt wird ein kleiner Roboter entwickelt, wobei zunächst Schaltplan und Layout erstellt und anschließend der Roboter aufgebaut wird. Der Roboter verfügt über zwei Motoren, die jeweils individuell mittels einer Vollbrücke (engl. *H-bridge*) angesteuert werden.

Als Mikrocontroller dient ein ATmega328. In der Basisausführung erhält der Roboter weiters drei Taster und einen Beschleunigungssensor, um zu erkennen, ob er irgendwo angestoßen ist.

Jedes Team wählt zusätzlich weitere Erweiterungen, um den Roboter zu erweitern (Batteriemanagement, Fernsteuerung, Display, Servos, Strom- und Spannungsmessung am Motor, Drehzahlerkennung, ...)

Folgende Komponenten werden für die Baisausführung benötigt:
* Mikrocontroller: [Microchip ATMega328P](https://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-7810-Automotive-Microcontrollers-ATmega328P_Datasheet.pdf) (Gehäuse TQFP32)
* Beschleunigungssensor: [Bosch BMI323](https://www.bosch-sensortec.com/en/products/motion-sensors/imus/bmi323)
* Vollbrücke: [Toshiba TB67H450AFNG](https://toshiba.semicon-storage.com/ap-en/semiconductor/product/motor-driver-ics/brushed-dc-motor-driver-ics/detail.TB67H450AFNG.html)
* Programmierstecker: ISP 6pin

Teil 1 des Projekt konzentriert sich auf die Entwicklung der Hardware, Teil 2 auf die Implementierung der Firmware.

.. figure:: robot.jpg
    :title: Bild dient nur als Beispiel
    :author: STEMpedia
    :source: https://ai.thestempedia.com/docs/quarky/quarky-ultimate-kit-robot-configurations/quarky-2-wheel-drive-horizontal-robot/

# Weitere Ideen
## Batteriemanagement
Mittels eines Batteriemanagementsystems (engl. *Battery Management System* oder kurz *BMS*) lässt sich der Ladezustand des Akkus überwachen und ein Tiefentladen verhindern. Dazu werden die Einzelzellspannungen gemessen und der Stromfluss beim Laden kontrolliert, sprich der Akku wird vor Überladung und Tiefentladung geschützt.

## Fernsteuerung
Zur Fernsteuerung kann ein Funkmodul verwendet werden, etwa mittels Bluetooth oder eines 2,4-GHz-Transceivers. Damit lässt sich der Roboter von einem PC oder Smartphone aus steuern, wobei sowohl manuelle Fahrkommandos als auch automatisierte Bewegungsabläufe übertragen werden können.

## Display
Ein Display dient zur Anzeige von Statusinformationen wie Akkuspannung, Motordrehzahl oder Sensorwerten. Je nach Anforderung kann ein einfaches Zeichendisplay (z.B. HD44780-kompatibel) oder ein grafisches OLED-Display verwendet werden, das mittels I²C oder SPI an den Mikrocontroller angeschlossen wird.

## Servos
Zusätzliche Servomotoren (engl. *servos*) ermöglichen es, den Roboter um weitere Bewegungsachsen zu erweitern. Die Ansteuerung erfolgt mittels PWM-Signalen, wobei Position und Geschwindigkeit des Servos direkt vorgegeben werden können.

## Strom- und Spannungsmessung am Motor
Durch die Messung von Strom und Spannung an den Motoren lassen sich Rückschlüsse auf die mechanische Last und den Betriebszustand ziehen. Ein erhöhter Stromfluss kann auf ein Blockieren der Räder hinweisen, sprich der Roboter kann selbstständig erkennen, wenn er gegen ein Hindernis fährt, und entsprechend reagieren.

## Drehzahlerkennung
Mittels Drehzahlerkennung kann die Geschwindigkeit der Räder geregelt werden, anstatt die Motoren nur mit einer festen PWM vorzugeben. Als Sensor dient typischerweise ein Hallsensor oder ein optischer Encoder, der die Drehzahl erfasst und dem Mikrocontroller als Rückführgröße zur Verfügung stellt.

# Termine Schuljahr 2026/2027
* 17.9.
* 24.9.
* 1.10.
* 8.10. **Check 1** (Überprüfung der Fortschritts)
* 15.10.
* 22.10. **Abgabe PCB Layout**
* 29.10. *Herbstferien*
* 5.11.
* 12.11. **Check 2**
* 19.11.
* 26.11.
* 3.12. **Abgabe Teil 1 (Hardware)**
* 10.12.
* 17.12.
* 24.12. *Weihnachtsferien*
* 31.12. *Weihnachtsferien*
* 7.12. *Weihnachtsferien*
* 14.1.
* 21.1.
* 28.1. **Abgabe Teil 2 (Software)**