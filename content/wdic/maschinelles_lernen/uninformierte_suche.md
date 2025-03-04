title: Uninformierte Suche
parent: uebersicht.md
next: informierte_suche.md

Uninformierte Suchalgorithmen sind grundlegende Techniken zur Problemlösung in der Informatik, bei denen keine zusätzlichen Informationen über die Struktur des Suchraums (abgesehen von der aktuellen Position und den möglichen Aktionen) verwendet werden. Diese Algorithmen erkunden systematisch einen Graphen oder einen Baum, um eine Lösung zu finden, ohne explizite Heuristiken oder Optimierungen. Zwei der bekanntesten uninformierten Suchalgorithmen sind die **Breitensuche** und die **Tiefensuche**.

# Breitensuche (Breadth-First Search, BFS)

Die **Breitensuche** ist ein uninformierter Suchalgorithmus, der alle Knoten eines Graphen oder Baumes in der Reihenfolge ihrer Entfernung zum Startknoten besucht, also schichtweise. Sie beginnt beim Startknoten und erkundet zunächst alle benachbarten Knoten (also alle Knoten der ersten Schicht), dann die Knoten der zweiten Schicht, und so weiter, bis sie das Ziel erreicht oder alle Knoten durchlaufen hat.

## Funktionsweise der Breitensuche
1. Der Startknoten wird in eine **Warteschlange** (Queue) eingefügt.
2. Solange die Warteschlange nicht leer ist:
   - Entnimmt der Algorithmus den vordersten Knoten der Warteschlange.
   - Dieser Knoten wird als besucht markiert und seine benachbarten, noch nicht besuchten Knoten werden in die Warteschlange eingefügt.
3. Der Algorithmus endet, wenn der Zielknoten gefunden oder alle erreichbaren Knoten besucht wurden.

- **Optimale Lösung**: Bei einem ungewichteten Graphen garantiert die Breitensuche, dass sie die kürzeste Lösung (in Bezug auf die Anzahl der Kanten) findet.
- **Speicherbedarf**: Da alle Knoten der aktuellen Schicht gespeichert werden müssen, kann der Speicherbedarf sehr hoch werden, besonders bei großen Graphen.

# Tiefensuche (Depth-First Search, DFS)

Die **Tiefensuche** ist ein weiterer uninformierter Suchalgorithmus, der so lange wie möglich entlang eines Pfades geht, bevor er zurückkehrt und andere Pfade ausprobiert. Im Gegensatz zur Breitensuche, die schichtweise vorgeht, folgt die Tiefensuche einem Pfad bis zum Ende, bevor sie zu einem anderen Pfad wechselt.

## Funktionsweise der Tiefensuche
1. Der Startknoten wird in einen **Stapel** (Stack) eingefügt.
2. Solange der Stapel nicht leer ist:
   - Der Algorithmus entnimmt den obersten Knoten des Stapels.
   - Dieser Knoten wird als besucht markiert und seine benachbarten, noch nicht besuchten Knoten werden in den Stapel eingefügt.
3. Der Algorithmus endet, wenn der Zielknoten gefunden oder alle erreichbaren Knoten besucht wurden.

- **Speicherbedarf**: Da nur der aktuelle Pfad im Speicher gehalten werden muss, ist der Speicherbedarf der Tiefensuche meist niedriger als der der Breitensuche.
- **Nicht optimal**: Die Tiefensuche garantiert nicht, dass sie die kürzeste Lösung findet, da sie manchmal tief in den Graphen vordringt, ohne das Ziel zu erreichen, und dann zurückkehren muss.

# Video

<iframe width="560" height="315" src="https://www.youtube.com/embed/7RCp2jNwxjQ" title="YouTube video player" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>