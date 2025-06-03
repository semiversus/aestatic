title: VHDL Signaltypen
next: operatoren.md
parent: uebersicht.md

# Allgemeines
Um eine digitale Schaltung beschreiben zu können, benötigt man Leitungen, um einzelne Komponenten miteinander zu
verbinden. *Leitungen* entsprechen in VHDL den sogenannten Signalen (Schlüsselwort `signal`). Um in VHDL ein Signal zu
definieren, muss dieses einen bestimmten Signaltyp besitzen.

Der einfachste Signaltyp ist `bit`. Dieser kennt die beiden Werte `0` und `1`. Das mag auf den ersten Blick für digitale Schaltungen ausreichend erscheinen, in der Praxis reichen diese beiden Werte jedoch oft nicht aus.

Signale werden wie folgt definiert:

```vhdl
signal <name> : <typ>; -- Signal <name> ist vom Typ <typ> und wird nicht initialisiert
signal <name> : <typ> := <default>; -- Signal <name> ist vom Typ <typ> und wird mit <default> initialisiert
```

# Standard Logic 1164
In der Bibliothek *Standard Logic 1164* sind Signaltypen definiert, die mehr als nur `0` und `1` darstellen können. Um
diese Bibliothek in einer VHDL-Datei zu verwenden, sind folgende zwei Zeilen erforderlich:

```vhdl
library ieee;
use ieee.std_logic_1164.all;
```

Diese Typen verfügen über neun Werte – daher spricht man auch von einer *9-wertigen Logik*:

* `U`: *undefiniert* – wird in der Simulation für nicht initialisierte Signale verwendet
* `X`: *unbekannt* (starker Treiber) – wenn zwei Ausgänge miteinander verbunden sind, die gegensätzliche Werte treiben (`0` und `1`)
* `0`: *logische Null* (starker Treiber)
* `1`: *logische Eins* (starker Treiber)
* `Z`: *hochohmig*
* `W`: *unbekannt* (schwacher Treiber)
* `L`: *logische Null* (schwacher Treiber)
* `H`: *logische Eins* (schwacher Treiber)
* `-`: *unwichtig* (vgl. *don't care* in KV-Diagrammen)

Werden mehrere Ausgänge zusammengeschaltet, setzen sich starke Treiber gegen schwache durch. Ein `U` dominiert
gegenüber allen anderen Werten. Die Funktion, die dieses Verhalten beschreibt, nennt sich *Resolution*-Funktion.

.. warning:: *Resolved* Signale
    Innerhalb eines FPGAs besteht keine Notwendigkeit, mehrere Ausgänge **direkt** miteinander zu verbinden. Solche Fälle lassen sich immer über eine kombinatorische Logik lösen.

## `std_logic` und `std_ulogic`
Der Signaltyp `std_logic` aus der *Standard Logic 1164*-Bibliothek nutzt die oben beschriebene 9-wertige Logik. Er ist *resolved*, d. h. mehrere Treiber können gleichzeitig ein Signal ansteuern. Das kann die Fehlersuche erschweren – insbesondere, wenn das Synthese-Tool keine Warnung ausgibt.

Zur Vermeidung solcher Fehler gibt es `std_ulogic`. Das *U* steht für *unresolved*, also nicht aufgelöst. Bei mehreren Treibern erzeugt das Tool einen Fehler.

Vorteile von `std_logic`:
* Häufig in bestehenden Beispielen und Vorlagen verwendet
* Viele VHDL-Generatoren nutzen `std_logic`

Vorteile von `std_ulogic`:
* Fehler durch mehrfaches Treiben werden zuverlässig erkannt
* Simulationen können (je nach Tool) schneller laufen, da keine Resolution notwendig ist

Die Umwandlung zwischen `std_logic` und `std_ulogic` ist jederzeit möglich.

.. info:: In diesem Skriptum wird `std_ulogic` verwendet

    Alle gezeigten Beispiele lassen sich auch mit `std_logic` realisieren.

## Definition eines Signals mit `std_ulogic`
```vhdl
signal led_reg : std_ulogic := '0'; -- Signal vom Typ std_ulogic, initialisiert mit '0'
```

# Busse mittels `std_ulogic_vector`
In vielen Anwendungen werden mehrere Signale zu einem *Bus* zusammengefasst. Dazu wird der Signaltyp `std_ulogic_vector`
verwendet.

Um einen Bus `data_reg` mit 8 Signalen zu definieren und diesen mit den Bits `"00000001"` zu initialisieren wird folgende
Definition genutzt:

```vhdl
signal data_reg : std_ulogic_vector(7 downto 0) := "00000001";
```

## `downto` und `to`
Im obigen Beispiel wurde `downto` genutzt um innerhalb des Vektors die einzelnen Indizies zu definieren. Wir können auf
ein einzelnes Signal im Bus mittels `data_reg(0)` zugreifen. Dies wurde laut obiger Definition `'1'` zurückliefern und
entspricht somit (wie erwartet) dem niederwertigsten Bit.

Würde `data_reg` wie folgt definiert sein:

```vhdl
signal data_reg : std_ulogic_vector(0 to 7) := "00000001";
```

würden wir bei `data_reg(0)` den Wert `'0'` zurückbekommen, da der Index 0 nun dem äußerst linken Bit entspricht.

.. info:: Verwende `downto`

    Da bei den meisten Darstellungen das höchstwertigste Bit links und das niederwertigste Bit rechts steht bietet sich
    `downto` an. Prinzipiell spricht nichts gegen eine Verwendung von `to` solange man weiß, was man tut!

## Literale
Wir haben im obigen Beispiel die Initialisierung mit dem Bitstring `"00000001"` gesehen. Solche Werte werden *Literale* (
engl. *literals*) genannt. In diesem Beispiel wird jedes einzelne Bit aufgeschlüsselt. Das gleiche Ergebnis erzielt man
mittels `x"01"` für die Darstellung mittels hexadezimaler Zahl.

Eine andere Möglichkeit bietet die Darstellung mittels Mapping:

```vhdl
signal data_reg : std_ulogic_vector(7 downto 0) := (0 => '1', others=>'0');
```

Diese Definition setzt den Index 0 auf `'1'` und alle anderen Bits auf `'0'`.

## Verknüpfen von Bussen
Busse lassen sich beliebig zusammenführen und aufteilen. Im folgenden Beispiel wird der 8 Bit Bus `data_in_reg` in zwei
Teilbusse `low_nibble` und `high_nibble` mit jeweils 4 Bit aufgeteilt. Der 8 Bit Bus `data_out_reg` besteht aus den
einzelnen 4 Bit Bussen, die in umgekehrter Reihenfolge wieder zusammengesetzt werden.

```vhdl
signal data_in_reg : std_ulogic_vector(7 downto 0);
signal low_nibble : std_ulogic_vector(3 downto 0);
signal high_nibble : std_ulogic_vector(3 downto 0);
signal data_out_reg : std_ulogic_vector(7 dowto 0);

low_nibble <= data_in_reg(3 downto 0);
high_nibble <= data_in_reg(7 downto 4);
data_out_reg <= low_nibble & high_nibble;
```

Das gleiche würde sich auch wie folgt realisieren lassen:

```vhdl
data_out_reg <= data_in_reg(3 downto 0) & data_in_reg(7 downto 4);
```

# Numerische Signaltypen `unsigned` und `signed`
Der Signaltyp `std_ulogic_vector` ist eine einfache Ansammlung einzelner `std_ulogic` Signale. Damit zu rechnen ist
nicht unmittelbar möglich. Für diese Anwendungsfälle gibt es die Bibliothek `numeric_std` mit den Signaltypen `unsigned`
und `signed`.

```vhdl
library ieee ;
use ieee.numeric_std.all;
```

Die Definition selbst entspricht der Definition von Bussen mittels `std_ulogic_vector`:

```vhdl
signal counter_reg : unsigned(7 downto 0);
```

Damit werden nun Addition und Subtraktion mit anderen `unsigned` bzw. `signed` Typen sowie *Integern* möglich:

```vhdl
counter_reg <= counter_reg + 1;
```

# Ganzzahlen mittels `integer`

In vielen Anwendungen werden arithmetische Operationen mit Signalen durchgeführt. Oft ist es aber nicht notwendig, auf
die einzelnen Bits zuzugreifen. Für solche Zwecke gibt folgende Ganzzahl Signaltypen:

* `integer`: Ganzzahl, je nach Synthesetool meist als 32 Bit vorzeichbehaftete Zahl representiert
* `natural`: Subtype von `integer` die positive Zahlen inklusive `0` enthält.
* `positive`: Subtype von `integer` die ausschließlich positive Zahlen enthält (ohne `0`).

## Eingrenzung mittels `range`
Für Signale kann der Wertebereich der Ganzzahltypen weiter eingeschränkt werden. Für einen Zähler im Dezimalsystem
bietet sich eventuell folgende Definition an:

```vhdl
signal dec_counter_reg : integer range 0 to 9;
```

.. warning:: Überlauf bei `integer`
    Wenn wie im obigen Beispiel der Bereich auf 0 bis 9 eingeschränkt ist, bedeutet dies nicht, dass bei einem Überlauf
    (9+1) das Ergebnis auf 0 überläuft. Es ist ein Hinweis für Simulation und Synthese, die im Falle eine Warnung
    ausgeben können, der Überlauf selbst muss aber durch eine eigene Beschreibung abgefangen werden.

# Konvertierung und Casting

Wird ein Signaltyp mit dem Wert eines anderen Signaltyps angesteuert benötigt man eine Konvertierung bzw. einen *Cast*.

Die Typen `std_ulogic_vector`, `unsigned` und `signed` sind Vektoren. Hier reicht es aus den Typ zu *casten*. Bei einer
Umwandlung von einem `integer` zu einem Vektor benötigt man die Information, wieviele Bits notwendig sind.

Für die folgenden Beispiele gehen wir von folgender Definition aus:

```vhdl
signal sul_vector : std_ulogic_vector(7 downto 0);
signal u_vector : unsigned(7 downto 0);
signal s_vector : signed(7 downto 0);
signal int : integer range 0 to 255;
```

## `std_ulogic_vector`

```vhdl
u_vector <= unsigned(sul_vector);
s_vector <= signed(sul_vector);
int <= to_integer(unsigned(sul_vector));
```

Die Umwandlung eines `std_ulogic_vector` in `unsigned` und `signed` geht einfach, da es sich nur die Interpretation der
Bits ändert.

Bei der Umwandlung in einen `integer` gibt es das Problem, dass `std_ulogic_vector` nur eine Ansammlung
von Bits ist, ohne eine Wertigkeit vorzugeben. Die Umwandlung zu `integer` geschieht über einen Cast zu `unsigned` bzw.
`signed` und dann die Konvertierung in einen `integer`.

## `unsigned` und `signed`

```vhdl
-- Umwandlung von unsigned
sul_vector <= std_ulogic_vector(u_vector);
int <= to_integer(u_vector);

-- Umwandlung von signed
sul_vector <= std_ulogic_vector(s_vector);
int <= to_integer(s_vector);
```

Die Umwandlung funktioniert hier änhlich zu `std_ulogic_vector`.

## `integer`

```vhdl
u_vector <= to_unsigned(int, 8);
s_vector <= to_signed(int, 8);
sul_vector <= std_ulogic_vector(to_unsigned(int, 8));
```

Bei der Konvertierung eines `integer`s in einen Vektor sind entsprechende Konvertierungsfunktionen zu nutzen. Der Weg
von `integer` zu `std_ulogic_vector` kann dabei je nach Anwendung über `to_unsigned` und `to_signed` führen.
