title: Informierte Suche
parent: uebersicht.md
next: dijkstra.md


Die *informierte Suche* ist ein wichtiges Konzept in der Graphentheorie und des maschinellen Lernens. Im Gegensatz zur uninformierten Suche nutzt sie zusätzliches Wissen über das Problem, um die Effizienz des Suchverfahrens zu verbessern.

# Branch and Bound

Branch-and-Bound ist eine Optimierungsmethode, die in der Graphentheorie und der diskreten Mathematik Anwendung findet. Das Verfahren teilt den Lösungsraum in kleinere Teilmengen auf (Branch) und berechnet Schranken (Bound), um suboptimale Lösungen frühzeitig auszuschließen.

Prinzip:
- **Verzweigung** (Branch): Der Ausgangsgraph wird in disjunkte Teilmengen aufgeteilt.
- **Beschränkung** (Bound): Bei Maximierungsproblemen wird die obere Schranke, bei Minimierungsproblemen die untere Schranke berechnet.

Branch-and-Bound erzeugt einen Entscheidungsbaum und ist ein Meta-Verfahren, das für verschiedene Optimierungsprobleme angepasst werden kann.

<iframe width="560" height="315" src="https://www.youtube.com/embed/5D4pjWX56Po" title="YouTube video player" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

# Heuristik

Eine Heuristik ist eine Strategie zur Problemlösung, die auf Erfahrungen oder Faustregeln basiert. In der informierten Suche werden heuristische Funktionen verwendet, um die Suche zu lenken und vielversprechende Pfade zuerst zu erkunden.

Eigenschaften einer guten Heuristik:
- **Zulässigkeit**: Eine Heuristik ist zulässig, wenn sie die tatsächlichen Kosten zum Ziel niemals *überschätzt*.
- **Monotonie**: Die geschätzten Kosten nehmen entlang des Pfades von der Wurzel aus niemals ab.

Ein Beispiel für die Anwendung von Heuristiken ist die Lösung des n-Puzzle-Problems, bei dem verschiedene Heuristiken wie die Anzahl falsch platzierter Rechtecke oder die Summe der Distanzen zur Zielposition verwendet werden können.

# Hill-Climbing-Verfahren

Hill-Climbing ist ein lokales Suchverfahren, das in der Graphentheorie und der Optimierung eingesetzt wird. Der Algorithmus versucht die Lösung schrittweise zu verbessern, indem er zu benachbarten Knoten übergeht, die einen besseren Wert der Zielfunktion aufweisen.

Charakteristiken:

- Einfach zu implementieren
- Kann in lokalen Optima stecken bleiben
- Nicht garantiert, das globale Optimum zu finden

<iframe width="560" height="315" src="https://www.youtube.com/embed/T4PFoYQ9fVc" title="YouTube video player" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

# Beam-Verfahren

Das Beam-Verfahren ist eine Erweiterung der Breitensuche, bei der nur eine begrenzte Anzahl der vielversprechendsten Knoten (der "Beam") auf jeder Ebene des Suchbaums weiterverfolgt wird. Dies reduziert den Speicherbedarf und die Rechenzeit, kann aber dazu führen, dass die optimale Lösung übersehen wird.

<iframe width="560" height="315" src="https://www.youtube.com/embed/sZzgAn-fYVE" title="YouTube video player" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

