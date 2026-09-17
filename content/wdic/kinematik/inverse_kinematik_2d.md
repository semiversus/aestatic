title: Inverse Kinematik - Herleitung am 2D-Modell
parent: uebersicht.md
next: inverse_kinematik_probleme.md
latex: true

# Allgemeines
Um die inverse Kinematik konkret herzuleiten, wird im folgenden ein vereinfachtes Modell betrachtet: ein
planarer Roboterarm mit zwei Gliedern und zwei Rotationsgelenken in der Ebene. Dieses Modell ist ausreichend,
um die wesentlichen Eigenschaften der inversen Kinematik zu verstehen - Mehrdeutigkeit, Reichweite und die
analytische Lösbarkeit.

Der Arm besteht aus folgenden Elementen:

* **Glied 1** - das erste Glied, fix am Ursprung befestigt, Länge \\(l_1\\)
* **Glied 2** - das zweite Glied, am Ende von Glied 1 angeschlossen, Länge \\(l_2\\)
* **Gelenk 1** - Rotationsgelenk am Ursprung, Winkel \\(\theta_1\\) (gegen die x-Achse)
* **Gelenk 2** - Rotationsgelenk am Übergang zwischen Glied 1 und Glied 2, Winkel \\(\theta_2\\) (relativ zu Glied 1)

Der Endeffektor befindet sich am Ende von Glied 2. Gesucht sind die Winkel \\(\theta_1\\) und \\(\theta_2\\), die
den Endeffektor an eine gegebene Position \\((x, y)\\) führen.

# Vorwärtsgeschaltete Kinematik
Bevor die inverse Kinematik gelöst wird, muss die vorwärtsgeschaltete Kinematik aufgestellt werden. Die Position
des Endeffektors ergibt sich aus der Verkettung der beiden Glieder. Der Winkel des zweiten Glieds gegen die x-Achse
ist \\(\theta_1 + \theta_2\\), da \\(\theta_2\\) relativ zum ersten Glied definiert ist.

Die x-Koordinate des Endeffektors lautet:

$$x = l_1 \cos(\theta_1) + l_2 \cos(\theta_1 + \theta_2)$$

Die y-Koordinate lautet entsprechend:

$$y = l_1 \sin(\theta_1) + l_2 \sin(\theta_1 + \theta_2)$$

Diese beiden Gleichungen bilden die vorwärtsgeschaltete Kinematik. Sie sind eindeutig, d.h. für gegebene Winkel
\\(\theta_1\\) und \\(\theta_2\\) liefert sich genau eine Position \\((x, y)\\).

# Inverse Kinematik
Die inverse Kinematik kehrt die obigen Gleichungen um: Gegeben sind \\((x, y)\\), gesucht sind \\(\theta_1\\) und
\\(\theta_2\\). Die Herleitung erfolgt in zwei Schritten. Zuerst wird der Winkel \\(\theta_2\\) berechnet, danach
lässt sich \\(\theta_1\\) mittels \\(\theta_2\\) bestimmen.

## Schritt 1: Winkel \\(\theta_2\\)
Zur Berechnung von \\(\theta_2\\) wird der Abstand vom Ursprung zur Zielposition herangezogen. Mittels des
Satzes des Pythagoras ergibt sich der Abstand \\(r\\) zu:

$$r^2 = x^2 + y^2$$

Mittels des Kosinussatzes im Dreieck, das durch den Ursprung, das Gelenk 2 und den Endeffektor gebildet wird,
lässt sich eine Beziehung zwischen \\(r\\), \\(l_1\\), \\(l_2\\) und \\(\theta_2\\) herleiten. Der Kosinussatz
lautet:

$$r^2 = l_1^2 + l_2^2 - 2\,l_1\,l_2\,\cos(\pi - \theta_2)$$

Da \\(\cos(\pi - \theta_2) = -\cos(\theta_2)\\) gilt, folgt daraus:

$$r^2 = l_1^2 + l_2^2 + 2\,l_1\,l_2\,\cos(\theta_2)$$

.. info:: Kosinussatz

    Der Kosinussatz (auch *Law of Cosines*) verallgemeinert den Satz des Pythagoras für beliebige Dreiecke. Für ein
    Dreieck mit den Seiten \\(a\\), \\(b\\), \\(c\\) und dem Winkel \\(\gamma\\) gegenüber der Seite \\(c\\) gilt:

    $$c^2 = a^2 + b^2 - 2\,a\,b\,\cos(\gamma)$$

Umgestellt nach \\(\cos(\theta_2)\\) ergibt sich:

$$\cos(\theta_2) = \frac{x^2 + y^2 - l_1^2 - l_2^2}{2\,l_1\,l_2}$$

Mittels des Arkuskosinus lässt sich \\(\theta_2\\) berechnen:

$$\theta_2 = \arccos\!\left(\frac{x^2 + y^2 - l_1^2 - l_2^2}{2\,l_1\,l_2}\right)$$

## Schritt 2: Winkel \\(\theta_1\\)
Sobald \\(\theta_2\\) bekannt ist, lässt sich \\(\theta_1\\) mittels der vorwärtsgeschalteten Kinematik
berechnen. Dazu wird die Position des Gelenks 2 (am Ende von Glied 1) herangezogen. Diese Position lautet:

$$x_1 = l_1 \cos(\theta_1)$$
$$y_1 = l_1 \sin(\theta_1)$$

Der Winkel \\(\theta_1\\) lässt sich in zwei Anteile zerlegen: der Winkel \\(\alpha\\) vom Ursprung zur
Zielposition und der Winkel \\(\beta\\) zwischen der Verbindungslinie Ursprung-Ziel und dem ersten Glied.
Somit gilt:

$$\theta_1 = \alpha - \beta$$

Der Winkel \\(\alpha\\) berechnet sich direkt aus der Zielposition:

$$\alpha = \arctan2(y, x)$$

Dabei wird \\(\arctan2\\) (die zweiargumentige Arkustangens-Funktion) verwendet, die den korrekten Quadranten
berücksichtigt.

Für den Winkel \\(\beta\\) wird nochmals der Kosinussatz angewendet, diesmal im Dreieck aus Ursprung,
Gelenk 2 und Endeffektor. Die Seiten sind \\(l_1\\) (Ursprung bis Gelenk 2), \\(r = \sqrt{x^2+y^2}\\) (Ursprung
bis Endeffektor) und \\(l_2\\) (Gelenk 2 bis Endeffektor). Der Winkel \\(\beta\\) liegt am Ursprung, somit
 gilt:

$$\cos(\beta) = \frac{l_1^2 + r^2 - l_2^2}{2\,l_1\,r}$$

bzw.

$$\beta = \arccos\!\left(\frac{l_1^2 + x^2 + y^2 - l_2^2}{2\,l_1\sqrt{x^2+y^2}}\right)$$

Daraus ergibt sich für \\(\theta_1\\):

$$\theta_1 = \arctan2(y, x) - \arccos\!\left(\frac{l_1^2 + x^2 + y^2 - l_2^2}{2\,l_1\sqrt{x^2+y^2}}\right)$$

# Mehrdeutigkeit
Die obige Herleitung liefert eine Lösung für \\(\theta_1\\) und \\(\theta_2\\). Es existiert aber eine zweite
Lösung, die dieselbe Position \\((x, y)\\) erreicht. Der Grund dafür liegt im Arkuskosinus: \\(\cos(\theta_2)\\)
ist für \\(\theta_2\\) und \\(-\theta_2\\) gleich. Somit gibt es zwei mögliche Werte für \\(\theta_2\\):

$$\theta_2 = \pm\arccos\!\left(\frac{x^2 + y^2 - l_1^2 - l_2^2}{2\,l_1\,l_2}\right)$$

Die beiden Lösungen entsprechen den beiden Konfigurationen:

* **Elbow-up** - \\(\theta_2 > 0\\): Das Gelenk 2 ist nach oben geknickt
* **Elbow-down** - \\(\theta_2 < 0\\): Das Gelenk 2 ist nach unten geknickt

Für jede Lösung von \\(\theta_2\\) ergibt sich ein entsprechender Winkel \\(\theta_1\\). Die vollständigen
Lösungen lauten somit:

$$\theta_2 = \pm\arccos\!\left(\frac{x^2 + y^2 - l_1^2 - l_2^2}{2\,l_1\,l_2}\right)$$

$$\theta_1 = \arctan2(y, x) \mp \arccos\!\left(\frac{l_1^2 + x^2 + y^2 - l_2^2}{2\,l_1\sqrt{x^2+y^2}}\right)$$

Das Vorzeichen von \\(\theta_2\\) und das Vorzeichen von \\(\beta\\) sind gekoppelt - ein positives \\(\theta_2\\)
führt zu einem negativen \\(\beta\\) und umgekehrt.

# Reichweite
Nicht jede Position \\((x, y)\\) ist erreichbar. Die Bedingung für die Erreichbarkeit ergibt sich aus dem
Argument des Arkuskosinus, das im Bereich \\([-1, 1]\\) liegen muss:

$$-1 \le \frac{x^2 + y^2 - l_1^2 - l_2^2}{2\,l_1\,l_2} \le 1$$

Daraus lassen sich zwei Grenzfälle ableiten:

* **Maximale Reichweite** - Der Arm ist vollständig ausgestreckt: \\(r = l_1 + l_2\\). Der Endeffektor
  befindet sich auf einem Kreis mit Radius \\(l_1 + l_2\\) um den Ursprung.
* **Minimale Reichweite** - Der Arm ist vollständig eingeknickt: \\(r = |l_1 - l_2|\\). Ist \\(l_1 = l_2\\),
  so kann der Endeffektor bis in den Ursprung reichen.

Zwischen diesen Grenzen ist jeder Punkt erreichbar. Die Menge aller erreichbaren Punkte wird als
*Arbeitsraum* (engl. *Workspace*) bezeichnet.

# Beispiel
Gegeben sei ein Roboterarm mit \\(l_1 = 3\\) und \\(l_2 = 2\\). Die Zielposition sei \\((x, y) = (3, 2)\\).

Zuerst wird der Abstand berechnet:

$$r = \sqrt{3^2 + 2^2} = \sqrt{13} \approx 3{,}61$$

Der Abstand liegt im Bereich \\([l_1 - l_2, l_1 + l_2] = [1, 5]\\), die Position ist somit erreichbar.

Für \\(\theta_2\\) ergibt sich:

$$\cos(\theta_2) = \frac{9 + 4 - 9 - 4}{2 \cdot 3 \cdot 2} = \frac{0}{12} = 0$$

$$\theta_2 = \pm\arccos(0) = \pm 90^{\circ}$$

Für \\(\alpha\\) gilt:

$$\alpha = \arctan2(2, 3) \approx 33{,}69^{\circ}$$

Für \\(\beta\\) ergibt sich:

$$\cos(\beta) = \frac{9 + 13 - 4}{2 \cdot 3 \cdot \sqrt{13}} = \frac{18}{6\sqrt{13}} \approx 0{,}832$$

$$\beta \approx \arccos(0{,}832) \approx 33{,}69^{\circ}$$

Somit lautet die *Elbow-down*-Lösung (\\(\theta_2 = -90^{\circ}\\)):

$$\theta_1 = 33{,}69^{\circ} - 33{,}69^{\circ} = 0^{\circ}$$

Die *Elbow-up*-Lösung (\\(\theta_2 = +90^{\circ}\\)) lautet:

$$\theta_1 = 33{,}69^{\circ} + 33{,}69^{\circ} = 67{,}38^{\circ}$$

Im folgenden Artikel werden Probleme behandelt, die bei der inversen Kinematik auftreten können -
insbesondere Singularitäten. Siehe [Singularitäten und weitere Probleme](inverse_kinematik_probleme.html).
