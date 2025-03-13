title: Huffman Kodierung
parent: uebersicht.md
next: uninformierte_suche.md

# Anwendung
Die Huffman Kodierung ist ein Algorithmus zur verlustfreien Datenkompression, der von David A. Huffman 1952 entwickelt wurde. Der Algorithmus basiert auf der Idee, häufige Zeichenfolgen mit kurzen Codes und seltene Zeichenfolgen mit langen Codes zu kodieren.

# Funktionsweise
Der Algorithmus besteht aus folgenden Schritten:
1. **Häufigkeitstabelle**: Zunächst wird die Häufigkeit jedes Zeichens im Eingabetext ermittelt.
2. **Erzeugung des Huffman-Baums**: Die Zeichen werden in einem binären Baum organisiert, wobei häufige Zeichen in der Nähe der Wurzel und seltene Zeichen in größeren Entfernungen platziert werden.
3. **Kodierung**: Die Huffman-Codes werden basierend auf dem Huffman-Baum generiert, wobei häufige Zeichen kurze Codes und seltene Zeichen lange Codes erhalten.

# Video
<iframe width="560" height="315" src="https://www.youtube.com/embed/6vgkip3z83s" title="YouTube video player" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>