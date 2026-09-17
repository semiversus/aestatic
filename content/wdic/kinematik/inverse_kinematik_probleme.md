title: Inverse Kinematik - Singularitäten und weitere Probleme
parent: uebersicht.md
latex: true

# Allgemeines
Die inverse Kinematik ist im allgemeinen nicht so unproblematisch wie die vorwärtsgeschaltete Kinematik. Neben der
Mehrdeutigkeit, die im Artikel [Herleitung am 2D-Modell](inverse_kinematik_2d.html) behandelt wurde, treten weitere
Probleme auf, die für die praktische Umsetzung von Bedeutung sind. Die wichtigsten davon sind *Singularitäten*,
*Redundanz* und die Beschränkung des *Arbeitsraums*.

# Singularitäten
Eine Singularität (engl. *Singularity*) ist eine Konfiguration, in der der Roboter einen oder mehrere Freiheitsgrade
verliert, sprich in der bestimmte Bewegungsrichtungen des Endeffektors nicht mehr erreichbar sind. Mathematisch
äußert sich eine Singularität darin, dass die *Jacobimatrix* \\(\mathbf{J}\\) ihren vollen Rang verliert, wodurch
sie nicht mehr invertierbar ist.

## Arten von Singularitäten
Bei Robotern mit Rotationsgelenken lassen sich im wesentlichen drei Arten von Singularitäten unterscheiden:

* **Arbeitsraumgrenze** (engl. *Boundary Singularity*) - Der Arm ist vollständig ausgestreckt oder eingeknickt.
  Der Endeffektor befindet sich am Rand des Arbeitsraums. In dieser Konfiguration kann der Endeffektor nicht weiter
  in die Richtung der Ausstreckung bewegt werden. Für den 2D-Zweigelenkarm entspricht dies dem Fall
  \\(r = l_1 + l_2\\) bzw. \\(r = |l_1 - l_2|\\) (siehe [Reichweite](inverse_kinematik_2d.html#reichweite)).

* **Gelenkausrichtung** (engl. *Alignment Singularity*) - Zwei oder mehr Gelenkachsen fallen zusammen, d.h. sie
  sind parallel und liegen auf derselben Geraden. In dieser Konfiguration kann eine Drehung eines der betroffenen
  Gelenke die gleiche Bewegung des Endeffektors bewirken wie die Drehung eines anderen - die Gelenke sind kinematisch
  redundant zueinander und der Roboter verliert einen Freiheitsgrad.

* **Handgelenkssingularität** (engl. *Wrist Singularity*) - Bei Robotern mit sphärischem Handgelenk (die letzten
  drei Gelenkachsen schneiden sich in einem Punkt) tritt eine Singularität auf, wenn die Achsen von Gelenk 4 und
  Gelenk 6 kollinear sind. In dieser Konfiguration kann Gelenk 6 die gleiche Drehung wie Gelenk 4 bewirken.

## Auswirkungen
In der Nähe einer Singularität wird die Jacobimatrix beinahe singulär, sprich ihre Determinante geht gegen null.
Dadurch wachsen die Gelenkwinkelkorrekturen \\(\Delta\boldsymbol\theta = \mathbf{J}^{-1}\,\Delta\mathbf{x}\\) über
alle Grenzen - schon kleine Bewegungen des Endeffektors erfordern extrem große Gelenkwinkeländerungen.

Die Konsequenzen für die Praxis sind:

* **Endliche Gelenkgeschwindigkeiten** - Die Gelenkmotoren können die geforderten Winkelgeschwindigkeiten nicht
  liefern, der Roboter bleibt stehen oder weicht von der Bahn ab.
* **Gelenklimit-Verletzung** - Die berechneten Winkel überschreiten die mechanischen Grenzen der Gelenke.
* **Steuerungsinstabilität** - Die numerische Iteration kann divergieren, sprich es wird keine Lösung gefunden.

## Umgang mit Singularitäten
Singularitäten lassen sich nicht vermeiden, da sie durch die kinematische Struktur des Roboters bedingt sind.
In der Praxis werden folgende Strategien eingesetzt:

* **Umgehung** - Die Bahnplanung wird so gestaltet, dass Singularitäten nicht durchfahren werden. Dies ist nicht
  immer möglich, insbesondere wenn die Zielposition am Rand des Arbeitsraums liegt.
* **Dämpfung** - Anstatt die Jacobimatrix direkt zu invertieren, wird eine gedämpfte Inversion verwendet (engl.
  *Damped Least Squares* oder *DLS*). Die Korrektur wird mittels:

  $$\Delta\boldsymbol\theta = \mathbf{J}^T\left(\mathbf{J}\,\mathbf{J}^T + \lambda\,\mathbf{I}\right)^{-1}\Delta\mathbf{x}$$

  wobei \\(\lambda\\) ein Dämpfungsfaktor ist. In der Nähe einer Singularität wird \\(\lambda\\) erhöht, wodurch
  die Gelenkwinkelkorrekturen begrenzt werden. Der Nachteil ist eine reduzierte Genauigkeit.

* **Pseudoinverse** - Anstelle der direkten Inversion wird die *Moore-Penrose-Pseudoinverse* \\(\mathbf{J}^+\\)
  verwendet, die auch für singuläre Matrizen definiert ist. Die Pseudoinverse liefert die Lösung mit minimaler
  Gelenkwinkeländerung, sprich sie wählt unter allen möglichen Lösungen diejenige mit dem kleinsten
  Gelenkwinkelnorm.

# Redundanz
Ein Roboter heißt *redundant* (engl. *Redundant*), wenn er mehr Gelenkfreiheitsgrade besitzt als für die Aufgabe
notwendig sind. Ein Roboterarm, der in der Ebene arbeitet und eine Position \\((x, y)\\) erreichen soll, benötigt
mindestens zwei Freiheitsgrade. Besitzt der Arm drei oder mehr Gelenke, so ist er redundant - es gibt unendlich
viele Gelenkkonfigurationen, die dieselbe Position erreichen.

.. info:: Freiheitsgrad

    Ein Freiheitsgrad (engl. *Degree of Freedom* oder kurz *DOF*) entspricht einer unabhängigen Bewegungsmöglichkeit.
    Ein Rotationsgelenk in der Ebene liefert einen Freiheitsgrad (den Drehwinkel). Im dreidimensionalen Raum benötigt
    man für eine beliebige Positionierung und Orientierung des Endeffektors sechs Freiheitsgrade (drei für die
    Position, drei für die Orientierung).

Redundanz ist kein Problem, sondern eine Möglichkeit: Der überschüssige Freiheitsgrad kann genutzt werden, um
zusätzlich Optimierungskriterien zu erfüllen, z.B.:

* **Kollisionvermeidung** - Der Arm wird so konfiguriert, dass er Hindernisse ausweicht.
* **Gelenkschonung** - Die Gelenkwinkel werden so gewählt, dass die mechanische Belastung minimiert wird.
* **Singuläritätsvermeidung** - Der überschüssige Freiheitsgrad wird genutzt, um Singularitäten zu umfahren.

Mathematisch wird die Redundanz mittels der Nullraum-Projektion gelöst. Die allgemeine Lösung der inversen
Kinematik bei Redundanz lautet:

$$\boldsymbol\theta = \mathbf{J}^+\,\Delta\mathbf{x} + (\mathbf{I} - \mathbf{J}^+\,\mathbf{J})\,\boldsymbol\xi$$

wobei \\(\mathbf{J}^+\\) die Pseudoinverse, \\(\mathbf{I}\\) die Einheitsmatrix und \\(\boldsymbol\xi\\) ein
beliebiger Vektor ist. Der zweite Term beschreibt die Nullraumbewegung, die den Endeffektor nicht bewegt, aber die
Gelenkkonfiguration verändert. Mittels \\(\boldsymbol\xi\\) kann das Optimierungskriterium gesteuert werden.

# Arbeitsraum
Der *Arbeitsraum* (engl. *Workspace* oder auch *Reachable Workspace*) ist die Menge aller Positionen, die der
Endeffektor erreichen kann. Die Begrenzung des Arbeitsraums ergibt sich aus den Gliedlängen und den
Gelenklimiten.

Für den 2D-Zweigelenkarm (siehe [Reichweite](inverse_kinematik_2d.html#reichweite)) ist der Arbeitsraum ein
ringförmiger Bereich mit dem Innenradius \\(|l_1 - l_2|\\) und dem Außenradius \\(l_1 + l_2\\).

Bei komplexeren Robotern im dreidimensionalen Raum ist der Arbeitsraum schwieriger zu beschreiben. Die Form
hängt von der kinematischen Struktur ab und kann Hohlräume aufweisen, d.h. Bereiche, die nicht erreichbar sind,
obwohl sie innerhalb der äußeren Reichweite liegen. Solche Hohlräume entstehen durch die Orientierung der
Gelenkachsen und die Gelenklimiten.

Zusätzlich unterscheidet man zwischen:

* **Positionsarbeitsraum** (engl. *Reachable Workspace*) - Die Menge aller Positionen, die der Endeffektor
  erreichen kann, unabhängig von der Orientierung.
* **Orientierungsarbeitsraum** (engl. *Dexterous Workspace*) - Die Menge aller Positionen, die der Endeffektor
  bei jeder Orientierung erreichen kann. Der Orientierungsarbeitsraum ist eine Teilmenge des
  Positionsarbeitsraums.

# Gelenklimiten
Jedes Gelenk hat mechanische Grenzen, die den Bereich der Gelenkwinkel einschränken. Diese Limiten werden durch
die mechanische Konstruktion bedingt und können nicht überschritten werden. Für Rotationsgelenke gibt es
typischerweise einen minimalen und einen maximalen Winkel, zwischen denen das Gelenk bewegt werden kann.

Bei der Lösung der inversen Kinematik muss geprüft werden, ob die berechneten Winkel innerhalb der Gelenklimiten
liegen. Ist dies nicht der Fall, so ist die Lösung nicht realisierbar und eine andere Konfiguration muss
gewählt werden. Bei redundanten Robotern kann die Nullraum-Projektion genutzt werden, um eine Konfiguration
zu finden, die innerhalb der Gelenklimiten liegt.

# Numerische Methoden
Für Roboter, die keine analytische Lösung zulassen, werden numerische Verfahren eingesetzt. Die wichtigsten
davon sind:

* **Jacobian-basierte Verfahren** - Mittels der (gedämpften) Jacobimatrix wird iterativ eine Lösung angenähert.
  Diese Verfahren wurden bereits im Artikel [Einführung](inverse_kinematik.html#jacobimatrix) behandelt.

* **Cyclic Coordinate Descent** (kurz *CCD*) - Die Gelenkwinkel werden nacheinander, Gelenk für Gelenk,
  optimiert. Für jedes Gelenk wird der Winkel so eingestellt, dass der Endeffektor möglichst nah an die
  Zielposition kommt. Danach wird das nächste Gelenk betrachtet. Der Vorgang wird wiederholt, bis die
  Abweichung ausreichend klein ist. CCD ist einfach zu implementieren und konvergiert schnell, kann aber
  in lokalen Minima stecken bleiben.

* **Forward And Backward Reaching Inverse Kinematics** (kurz *FABRIK*) - Dieses Verfahren arbeitet nicht
  mit der Jacobimatrix, sondern betrachtet den Arm als eine Kette von Punkten. In einem Vorwärts-Schritt
  wird der Endeffektor auf die Zielposition gesetzt und die Glieder rückwärts angepasst. In einem
  Rückwärts-Schritt wird der Basispunkt fixiert und die Glieder vorwärts korrigiert. FABRIK ist sehr
  effizient und wird häufig in der Computeranimation eingesetzt.

# Zusammenfassung
Die inverse Kinematik ist mit mehreren Problemen behaftet, die bei der praktischen Umsetzung berücksichtigt
werden müssen:

* **Singularitäten** - Konfigurationen, in denen die Jacobimatrix nicht invertierbar ist und der Roboter
  Freiheitsgrade verliert. Dämpfung und Pseudoinverse sind die gängigen Gegenmaßnahmen.
* **Redundanz** - Mehr Freiheitsgrade als notwendig. Kein Problem, sondern eine Möglichkeit zur Optimierung
  mittels Nullraum-Projektion.
* **Arbeitsraum** - Nicht jede Position ist erreichbar. Die Begrenzung ergibt sich aus Gliedlängen und
  Gelenklimiten.
* **Gelenklimiten** - Mechanische Grenzen, die die realisierbaren Lösungen einschränken.
* **Numerische Verfahren** - Für Roboter ohne analytische Lösung stehen CCD, FABRIK und Jacobian-basierte
  Verfahren zur Verfügung.
