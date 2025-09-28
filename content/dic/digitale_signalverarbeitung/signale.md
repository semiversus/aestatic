title: Signale
parent: uebersicht.md
next: lti_systeme.md
latex: true

# Allgemeines
Ein Signal ist einer messbaren physikalischer Größe (z.B. Spannung) eine Information zuordnet. Dabei ändert sich im
Allgemeinen der Betrag als Funktion der Zeit.

# Kontinuierliche und diskrete Signale
## Analogsignal
Ein Analogsignal ist im Rahmen der Signaltheorie eine Form eines Signals mit stufenlosem und unterbrechungsfreiem
Verlauf. Ein Analogsignal wird als glatte Funktion beschrieben und es lässt sich damit beispielsweise der zeitlich
kontinuierliche Verlauf einer physikalischen Größe wie der Schalldruck in Form eines analogen Audiosignals beschreiben.
Der Wertebereich eines Analogsignals wird als Dynamikumfang bezeichnet.

Im Gegensatz zu einem Digitalsignal weist ein Analogsignal einen stufenlosen und beliebig feinen Verlauf auf und kann im
Dynamikbereich theoretisch unendlich viele Werte annehmen. Bei realen physikalischen Größen ist die Auflösung allerdings
durch Störungen wie das Rauschen oder durch Verzerrungen begrenzt.

.. figure:: signal_wk_zk.svg
    :title: Wert- und zeitkontinuierliches Signal

Bei einem Analogsignal spricht man auch von einem Signal, das *wert- und zeitkontinuierlich* ist.

## Zeitdiskrete Signale
Ein zeitdiskretes Signal kann als Folge \\(x[n]\\) von reellen Zahlen mit \\(n \in \mathbb{N}\\) beschrieben werden. Der Index \\(n\\)
stellt die normierte Zeitvariable dar, welche auf die Abtastrate normiert ist. Üblicherweise erfolgt die Abtastung zu
konstanten Abständen.

.. figure:: signal_wk_zd.svg
    :title: Wertkontinuierliches und zeitdiskretes Signal

Hier spricht man von einem Signal, das *wertkontinuierlich und zeitdiskret* ist. Die Darstellung wird im englischen oft
als *Stem*- oder *Lollipop*-Graph bezeichnet. Die Werte zwischen den diskreten Abtastzeitpunkten sind nicht 0 sondern
undefiniert.

## Wertdiskrete Signale
Digitale Systeme nutzen AD- und DA-Wandler um Analogsignale in digitale Werte zu wandeln. Bei dieser *Quantisierung*
wird das wertkontinuierliche Signal einer *Quantisierungsstufe* von aneinandergrenzender Intervalle endlicher Zahl zugewiesen.

.. figure:: signal_wd_zk.svg
    :title: Wertdiskretes und zeitkontinuierliches Signal

Bei diesem Plot ist die Zeit kontinuierlich, die möglichen Werte hingegen diskret. Der nächste Plot zeigt ein Signal,
das wert- und zeitdiskret ist.

.. figure:: signal_wd_zd.svg
    :title: Wert- und zeitdiskretes Signal

Während sich zeitkontinuierliche Signale nur als Funktion darstellen lassen kann man bei zeitdiskreten Signalen auch eine
Folge angeben. Im obigen Beispiel wäre dies:

$$x[n]=(\ldots,\ 0,\ 3,\ 3,\ 2,\ 0,\ {-1},\ \underline{0},\ 2,\ 4,\ 3,\ 1,\ 0,\ 0,\ \ldots)$$

Um die Position des Index 0 zu markieren wird der entsprechende Wert unterstrichen. Die Folge wird aber auch oft wie folgt
angeschrieben:

$$x[n]=0\quad 3\quad 3\quad 2\quad 0\quad {-1}\quad \underline{0}\quad 2\quad 4\quad 3\quad 1\quad 0\quad 0$$

In weiterer Folge werden ausschließlich zeitdiskrete Signale behandelt.

# Transformation von Signalen
## Verschiebung im Zeitbereich
Bei einer Verschiebung im Zeitbereich wird ein Signal um ein oder mehr Abtastintervalle nach links oder rechts verschoben.

Für die folgenden Beispiele wird dieses Ausgangssignal \\(x[n]\\) verwendet:
.. figure:: signal_original.svg
    :title: Beispielsignal

Um die Werte für \\(x[n-1]\\) zu ermitteln, werden für \\(n\\) alle natürlichen Zahlen eingesetzt. An der Position 0 ist
dies also der Wert von \\(x[-1]\\), für die Position 1 der Wert von \\(x[0]\\) usw. Das Signal wird also insgesamt nach
rechts geschoben.

.. figure:: signal_shift_minus_1.svg
    :title: Verschiebung nach rechts

Wird eine positive Zahl zum Index addiert verschiebt sich das Signal nach links:
.. figure:: signal_shift_plus_2.svg
    :title: Verschiebung nach links

## Spiegelung im Zeitbereich
Bei der Spiegelung des Signals um die Y-Achse wird der Index negiert. Der Wert an der Position 0 bleibt gleich, der Wert
an der Position 1 ist gleich \\(x[-1]\\), usw.

.. figure:: signal_flip.svg
    :title: Spiegelung um die Y-Achse

## Skalierung im Zeitbereich
Bei der Skalierung wird der Index mit einem Faktor multipliziert. Ist dieser Faktor größer als 1 wird das Signal
gestaucht. Bei einer Stauchung gehen unmittelbar Werte verloren:

.. figure:: signal_scale2.svg
    :title: Skalierung um Faktor 2

Ist der Faktor kleiner als 1 wird das Signal gestreckt. Nicht definierte Indizes werden mit dem Wert 0 ausgegeben:
.. figure:: signal_scale1_2.svg
    :title: Skalierung um Faktor 0.5

## Kombination von Transformationen
Wenn Verschiebung, Spiegelung und Skalierung gleichzeitig angewendet werden sollen ist die Reihenfolge wichtig:

* Verschieben
* Spiegeln
* Skalieren

Um die Impulsfolge für das Signal \\(x[-2n+2]\\) zu ermitteln wird das Signal zuerst Verschoben:
.. figure:: signal_shift_plus_2.svg
    :title: Verschiebung nach links

Anschließend gespiegelt:
.. figure:: signal_shift_flip.svg
    :title: Spiegelung

Und zum Schluss skaliert:
.. figure:: signal_shift_flip_scale.svg
    :title: Skalierung

# Eigenschaften von Signalen
## Gerade und ungerade Signale
Ein Signal ist gerade wenn gilt \\(x[n]=x[-n]\\), d.h. wenn das Signal gleich dem um die Y-Achse gespiegelten Signal ist.

.. figure:: signal_even.svg
    :title: Beispiel für ein gerades Signal

Ein Signal ist ungerade wenn gilt \\(x[n]=-x[-n]\\), d.h. wenn das Signal gleich dem um den 0-Punkt um 180 Grad rotierten
Signal ist. Diese Symmetrie fordert auch, dass der Wert an der Position 0 gleich 0 ist.

.. figure:: signal_odd.svg
    :title: Beispiel für ein ungerades Signal

Jedes Signal lässt sich in seine gerade und ungerade Komponente zerlegen. Für die gerade Komponente gilt:

$$y_{gerade}[n]=\frac{1}{2}(x[n]+x[-n])$$

Für die ungerade Komponente gilt:

$$y_{ungerade}[n]=\frac{1}{2}(x[n]-x[-n])$$

## Periodische Signale
Ein Signal ist periodisch, wenn es die Bedingung \\(x[n]=x[n+k*P]\\) erfüllt, wobei \\(k \in \mathbb{N}\\) und \\(P\\) das
Periodenintervall darstellt.

.. figure:: signal_periodic4.svg
    :title: Periodisches Signal mit der Periode 4

.. figure:: signal_periodic1.svg
    :title: Periodisches Signal mit dem Sonderfall der Periode 1

## Kausale Signale
Ein Signal nennt man *kausal*, wenn alle Werte des Signals auf der negativen Zeitachse Null sind. Beispiele dafür sind
der Einheitsimpuls oder der Einheitssprung. Sind die Werte des Signals auf der negativen Zeitachse ungleich Null spricht
man auch von einem *antikausalen* Signal.

# Elementarsignale
## Einheitimpuls
Der Einheitsimpuls \\(\delta[n]\\) (auch Dirac-Impuls genannt) ist definiert durch:

$$\delta[n]=\begin{cases} 1 & \text{für } n = 0 \\\\ 0 & \text{für } n \neq 0 \end{cases}$$

.. figure:: signal_delta.svg
    :title: Einheitsimpuls

### Ausblendeigenschaft
Der Einheitsimpuls hat eine Ausblendeigenschaft: Wird ein beliebiges Signal mit dem Einheitsimpuls multipliziert, sind
alle Werte 0, außer dem Wert an Position 0 - dieser entspricht dem ursprünglichen Wert des Signals an der Position 0.

Wird der Einheitsimpuls zusätzlich zeitlich verschoben, lässt sich auch die Ausblendeigenschaft entsprechend steuern.
Es gilt:

$$x[n]\cdot\delta[n-k]=\begin{cases} x[n] & \text{für } n = k \\\\ 0 & \text{für } n \neq k \end{cases}$$

## Einheitssprung
Der Einheitssprung \\(u[n]\\) ist definiert durch:

$$u[n]=\begin{cases}1 & \text{für } n \geq 0 \\\\ 0 & \text{für } n < 0 \end{cases}$$

.. figure:: signal_step.svg
    :title: Einheitssprung

Der Einheitssprung kann auch als Summe von vielen Einheitsimpulse aufgefasst werden:

$$u[n]=\delta[n] + \delta[n-1] + \delta[n-2] + \delta[n-3] + \ldots=\sum\limits_{k=0}^\infty \delta[n-k]$$

# Signalsynthese
Ein Signal lässt sich aus beliebig vielen Komponenten zusammensetzen:

.. figure:: signal_synth.svg
    :title: Zusammengesetztes Signal
