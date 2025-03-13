title: A* Algorithmus
parent: informierte_suche.md
next: minmax.md

# Einleitung
Der *A*-Algorithmus ist ein informiertes Suchverfahren, das in der Graphentheorie und der künstlichen Intelligenz eingesetzt wird. Er kombiniert die Vorteile der Breitensuche mit einer heuristischen Schätzung der Kosten und findet so den kürzesten Pfad von einem Startknoten zu einem Zielknoten.

# Prinzip
Der A*-Algorithmus arbeitet ähnlich wie die Breitensuche, indem er den Suchbaum schichtweise durchsucht. Im Gegensatz zur Breitensuche verwendet er jedoch eine heuristische Funktion, um die Kosten eines Pfades zu schätzen. Diese Funktion berücksichtigt sowohl die tatsächlichen Kosten vom Startknoten zum aktuellen Knoten als auch eine Schätzung der Kosten vom aktuellen Knoten zum Zielknoten.

Die Kosten eines Pfades werden als Summe aus den tatsächlichen Kosten (G-Wert) und der geschätzten Kosten (H-Wert) berechnet:

# Video
<iframe width="560" height="315" src="https://www.youtube.com/embed/fI9PGLoRE2E" title="YouTube video player" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>