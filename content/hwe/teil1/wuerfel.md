title: Würfel
next: sirene.md
parent: uebersicht.md

# Kurzbeschreibung
Mittels 7 LEDs soll das Würfelbild dargestellt werden. Dazu wird eine digitale
Logik aufgebaut, die zur Ansteuerung der LEDs dient (siehe [Automatentheorie](../../dic/grundlagen_der_digitaltechnik/automatentheorie.html)).

Ein Timer [NE555](https://de.wikipedia.org/wiki/NE555) dient als Taktgeber. Durch das Drücken eines Tasters wird das
Rechtecksignal des Tasters mit dem Takteingang des Automaten verbunden.

Anschlüsse:

* Klemme mit 2 Anschlüssen für die Versorgung (5 Volt)

# Recherche
Das zentrale Bauteil ist der *NE555*

* Wie ist ein NE555 aufgebaut?
* Wie lässt sich die Frequenz einstellen?
* Wodurch wird die maximale Frequenz limitiert?

# Spezifikation
* Die Frequenz des Timers soll zwischen 10kHz und 100kHz liegen
