title: Inverse Kinematik - Einführung
parent: uebersicht.md
next: inverse_kinematik_2d.md
latex: true

# Allgemeines
Die *Kinematik* (von griech. *κίνημα* für Bewegung) beschreibt die Geometrie von Bewegungen, ohne die zu Grunde liegenden
Kräfte zu betrachten. Im Kontext der Robotik geht es darum, die Position von Gelenken und Gliedern eines Roboters in
Abhängigkeit von seinen Gelenkwinkeln zu beschreiben. Die Kinematik beantwortet also die Frage, *wo* sich ein Punkt des
Roboters befindet, wenn die Gelenke in einer bestimmten Konfiguration stehen.

Bei einem Roboterarm spricht man von der *vorwärtsgeschalteten Kinematik* (engl. *Forward Kinematics* oder auch *Direct
Kinematics*), wenn aus den Gelenkwinkeln die Position des Endeffektors (engl. *End Effector*, sprich des Werkzeugs oder
Greifers am Ende des Arms) berechnet wird. Das inverse Problem - die *inverse Kinematik* (engl. *Inverse Kinematics* oder
kurz *IK*) - geht den umgekehrten Weg: Gegeben ist eine Zielposition des Endeffektors, gesucht sind die Gelenkwinkel, die
diese Position erreichen.

.. info:: Endeffektor

    Der Endeffektor ist das am Ende eines Roboterarms angebrachte Werkzeug, z.B. ein Greifer, ein Schweißbrenner oder
    ein Paint-Spray. In der Kinematik wird der Endeffektor meist als ein einzelner Punkt am Ende der kinematischen Kette
    betrachtet.

# Vorwärtsgeschaltete Kinematik
Die vorwärtsgeschaltete Kinematik lässt sich für starre Roboterarme systematisch berechnen. Jedes Gelenk wird mittels
seiner Gelenkvariablen (Winkel bei Rotationsgelenken, Verschiebung bei Prismengelenken) beschrieben. Die Position des
Endeffektors ergibt sich als Verkettung von Transformationen, die durch die einzelnen Gelenke und Glieder definiert
sind.

Mittels der *Denavit-Hartenberg*-Notation (kurz *DH*) lässt sich die vorwärtsgeschaltete Kinematik in einer systematischen
Form beschrieben. Jedes Gelenk wird durch vier Parameter charakterisiert, wodurch sich die Transformationsmatrix der
gesamten kinematischen Kette als Produkt der einzelnen Gelenkmatrizen ergibt. Die vorwärtsgeschaltete Kinematik ist
somit immer eindeutig - für eine gegebene Konfiguration der Gelenkwinkel existiert genau eine Position des Endeffektors.

# Inverse Kinematik
Die inverse Kinematik kehrt diese Abbildung um. Aus einer gewünschten Position (und Orientierung) des Endeffektors
sollen die zugehörigen Gelenkwinkel berechnet werden. Dieses Problem ist wesentlich anspruchsvoller als die
vorwärtsgeschaltete Kinematik, da die Umkehrung nicht eindeutig sein muss und im allgemeinen Fall keine geschlossene
Lösung existiert.

## Mehrdeutigkeit
Für einen gegebenen Endeffektor kann es mehrere Gelenkkonfigurationen geben, die dieselbe Position erreichen. Ein
einfaches Beispiel ist ein menschlicher Arm: Um einen Punkt auf einer Tischplatte zu berühren, kann der Ellenbogen
nach oben oder nach unten zeigen - beide Konfigurationen führen zur gleichen Handposition. Man spricht in diesem
Zusammenhang von *Lösungsvarianten* bzw. *Konfigurationen* (z.B. *elbow-up* und *elbow-down*).

Die Anzahl der Lösungen hängt von der Struktur des Roboters ab. Ein Roboterarm mit \\(n\\) Rotationsgelenken kann
im allgemeinen Fall bis zu \\(2^{n-1}\\) verschiedene Lösungen aufweisen, wobei nicht alle Lösungen innerhalb der
mechanischen Grenzen der Gelenke (engl. *Joint Limits*) liegen müssen.

## Lösungsansätze
Im wesentlichen lassen sich zwei Klassen von Lösungsverfahren unterscheiden:

* **Analytische Verfahren** - Die Gelenkwinkel werden mittels geschlossener Formeln berechnet. Voraussetzung dafür ist,
  dass die kinematische Struktur des Roboters eine geschlossene Lösung zulässt. Dies ist für viele klassische
  Industrieroboter mit 6 Gelenken der Fall, da deren Struktur spezielle Eigenschaften aufweist (z.B. sich schneidende
  Gelenkachsen). Die analytische Lösung ist schnell und eindeutig berechenbar, liefert aber alle möglichen
  Konfigurationen auf einmal.

* **Numerische Verfahren** - Die Gelenkwinkel werden iterativ angenähert. Ausgehend von einer Startkonfiguration wird
  schrittweise eine Lösung gesucht, die der Zielposition immer näher kommt. Diese Verfahren sind allgemeingültig,
  sprich sie funktionieren für beliebige kinematische Strukturen. Der Rechenaufwand ist allerdings höher und es ist
  nicht garantiert, dass ein Minimum gefunden wird - die Iteration kann in einem lokalen Minimum stecken bleiben.

.. info:: Geschlossene Lösung

    Eine geschlossene Lösung (engl. *closed-form solution*) liegt vor, wenn sich das Resultat mittels einer
    endlichen Anzahl von elementaren Rechenoperationen (Addition, Multiplikation, Wurzelziehen, trigonometrische
    Funktionen, usw.) ausdrücken lässt. Für Roboterarme, bei denen die letzten drei Gelenkachsen in einem Punkt
    zusammenlaufen (sog. *sphärisches Handgelenk*), lässt sich die inverse Kinematik in eine Positionsaufgabe und eine
    Orientierungsaufgabe zerlegen. Beide Teilaufgaben besitzen eine geschlossene Lösung.

# Anwendungen
Die inverse Kinematik ist eine der grundlegenden Aufgaben in der Robotik. Typische Anwendungsfelder sind:

* **Bahnplanung** - Der Endeffektor soll einer vorgegebenen Bahn (z.B. einer Geraden, einem Kreis oder einer Schweißnaht)
  folgen. Für jeden Punkt der Bahn müssen die Gelenkwinkel berechnet werden.
* **Greifen** - Um ein Objekt zu greifen, muss der Greifer an eine bestimmte Position geführt und in eine bestimmte
  Orientierung gebracht werden.
* **Animation** - In der Computeranimation und in Videospielen wird die inverse Kinematik verwendet, um Bewegungen von
  Charakteren natürlich aussehen zu lassen. Die Füße sollen z.B. den Boden berühren, während der Rest des Körpers
  animiert wird.
* **CAD/CAM** - Bei der Programmierung von CNC-Maschinen und Robotern aus CAD-Daten müssen Werkzeugbahnen in
  Gelenkwinkel übersetzt werden.

# Jacobimatrix
Ein zentrales Werkzeug für die numerische Lösung der inversen Kinematik ist die *Jacobimatrix* (auch
*Jacobian* genannt). Die Jacobimatrix beschreibt die lokale rate der Änderung der Endeffektorposition in Abhängigkeit
von den Gelenkwinkeln, sprich sie linearisiert die vorwärtsgeschaltete Kinematik an einem bestimmten Punkt.

Die Jacobimatrix \\(\mathbf{J}\\) verbindet die Gelenkwinkelgeschwindigkeiten \\(\dot{\boldsymbol\theta}\\) mit der
Geschwindigkeit des Endeffektors \\(\dot{\mathbf{x}}\\):

$$\dot{\mathbf{x}} = \mathbf{J}(\boldsymbol\theta)\,\dot{\boldsymbol\theta}$$

Mittels Inversion der Jacobimatrix lässt sich die inverse Kinematik iterativ lösen:

$$\Delta\boldsymbol\theta = \mathbf{J}^{-1}\,\Delta\mathbf{x}$$

wobei \\(\Delta\mathbf{x}\\) die Abweichung des Endeffektors von der Zielposition und \\(\Delta\boldsymbol\theta\\) die
entsprechende Korrektur der Gelenkwinkel darstellt. Diese Iteration wird wiederholt, bis die Abweichung ausreichend
klein ist.

Auf Probleme, die bei der Inversion der Jacobimatrix auftreten können - insbesondere *Singularitäten* - wird im
Artikel [Singularitäten und weitere Probleme](inverse_kinematik_probleme.html) näher eingegangen.

# Zusammenfassung
Die inverse Kinematik kehrt die vorwärtsgeschaltete Kinematik um: Statt aus Winkeln die Position zu berechnen, wird
aus einer Position die zugehörigen Winkel gesucht. Das Problem ist im allgemeinen nicht eindeutig und besitzt nicht
immer eine geschlossene Lösung. Analytische Verfahren sind schnell, setzen aber spezielle kinematische Strukturen
voraus. Numerische Verfahren sind allgemeingültig, benötigen aber mehr Rechenzeit und können in lokalen Minima
stecken bleiben. Die Jacobimatrix dient als zentrales Werkzeug für die numerische Lösung.

Im folgenden Artikel wird die inverse Kinematik anhand eines einfachen zweidimensionalen Modells - einem Arm mit zwei
Gliedern und zwei Rotationsgelenken - hergeleitet. Siehe [Herleitung am 2D-Modell](inverse_kinematik_2d.html).
