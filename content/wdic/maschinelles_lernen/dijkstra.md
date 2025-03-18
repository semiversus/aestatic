title: Dijkstra Algorithmus
parent: informierte_suche.md
next: minmax.md

# Einleitung
Der *Dijkstra Algorithmus* ist ein Verfahren aus der Graphentheorie, das zur Bestimmung des kürzesten Pfades in einem gewichteten Graphen eingesetzt wird. Der Algorithmus wurde von dem niederländischen Informatiker [Edsger W. Dijkstra](https://de.wikipedia.org/wiki/Edsger_W._Dijkstra) entwickelt und erstmals 1959 veröffentlicht.

# Prinzip
Der Dijkstra Algorithmus arbeitet mit einem gewichteten Graphen, bei dem jedem Knoten ein Kostenwert zugeordnet ist. Das Ziel des Algorithmus ist es, den kürzesten Pfad von einem Startknoten zu allen anderen Knoten im Graphen zu finden. Dabei werden die Kosten der Pfade schichtweise aktualisiert, bis alle Knoten erreicht wurden.

1. **Initialisierung**: Setze die Distanz zum Startknoten auf 0 und zu allen anderen Knoten auf unendlich.
2. **Iterative Verarbeitung**:
  * Wähle den Knoten mit der aktuell kleinsten bekannten Distanz.
  * Für jeden Nachbarn dieses Knotens:
    * Berechne die Gesamtdistanz vom Start über den aktuellen Knoten zum Nachbarn.
    * Falls diese Distanz kürzer ist als die bisher bekannte, aktualisiere sie.
3. **Abbruch**: Wenn alle Knoten bearbeitet wurden oder das Ziel erreicht ist.


# Video
<iframe width="560" height="315" src="https://www.youtube.com/embed/bwqyKuRVcJ8" title="YouTube video player" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>