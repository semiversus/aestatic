title: I&sup2;C Übungsaufgaben
parent: i2c.md

# Aufgabe ADXL345
In dieser Übung wird der Beschleunigungssensor [ADXL345](http://www.analog.com/en/products/mems/mems-accelerometers/adxl345.html) von [Analog Devices](http://www.analog.com/) angesteuert. Die angaben stammen aus dem entsprechenden [Datenblatt](http://www.analog.com/media/en/technical-documentation/data-sheets/ADXL345.pdf).

Die 7-Bit Adresse des Bausteins wird für diese Übung mit <samp>001 1101</samp> (0x1D) angenommen.

## Register
Der Baustein verfügt intern über mehrere Register. Jeder Register ist ein Byte groß.
.. figure:: adxl345_registers.svg
    :title: Registerübersicht
    :author: Datenblatt ADXL345
    :source: http://www.analog.com/media/en/technical-documentation/data-sheets/ADXL345.pdf
    :license: &copy;Analog Devices

In der folgenden Abbildung sieht man insgesamt vier Übertragungsarten:

* Schreiben eines Bytes in ein Register
* Schreiben mehrerer Byte in mehrere Register
* Lesen eines Bytes aus einem Register
* Lesen mehrere Bytes aus mehreren Registern

.. figure:: adxl345_overview.svg
    :title: Lesen und Schreiben einzelner sowie mehrer Bytes
    :author: Datenblatt ADXL345
    :source: http://www.analog.com/media/en/technical-documentation/data-sheets/ADXL345.pdf
    :license: &copy;Analog Devices
Hinweise zum Bild:

1. Dieses *START* ist entweder ein *repeated START* oder ein *STOP* mit anschließendem *START*
2. Der graue schattierte Bereich markiert die Phasen, in denen die entsprechende Komponente den Buszustand beobachtet

## Beispiel

Beschreiben des Registers `OFSX` (0x1E) mit dem Wert 0x02:

![Schreibe 0x02 auf das Register 0x1E](i2c_write_0x1E_0x02.svg)

Lesen der Register `THRES_ACT` und `THRES_INACT` (0x24 und 0x25)

![Lesen der Register 0x24 und 0x25](i2c_read_0x24.svg)

## Aufgabenstellung
Skizziere folgende Übertragungen am I&sup2;C Bus:

* Beschreiben des Registers `DUR` mit dem Wert <samp>0x05</samp>
* Bechreiben der Registers `OFSX`, `OFSY`, `OFSZ` mit den  Werten <samp>[0x17, 0x2A, 0x04]</samp> (mit nur einem Zugriff)
* Lesen des Registers `ACT_TAP_STATUS` (angenommener Inhalt ist <samp>0x10</samp>)
* Lesen der Register `DATAX0` bis `DATAY1` (angenommener Inhalt ist <samp>[0x08, 0xE3, 0x01, 0xA7]</samp>, mit nur einem Zugriff)
