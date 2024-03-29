title: VHDL Test (3)
parent: uebersicht.md

# Allgemeines
* [Projektordner](vhdl_test_3.zip) herunterladen und entpacken
* Insgesamt gibt es <span class="tag is-rounded is-info">29 Punkte</span>
* Die einzelnen Punkte bauen meist nicht aufeinander auf. Statt langer Fehlersuche lieber auf das nächste Beispiel wechseln.

# Einschaltverzögerung
## Vorbereitung
* Projekt <samp>led_toggle/led_toggle.xise</samp> öffnen

## Aufgabenstellung
Zwei LEDs sollen mittels zwei Taster angesteuert werden.

* `button_toggle` - Wechselt zwischen LED1 und LED2, bzw. schaltet LED1 ein, falls die LEDs ausgeschaltet waren.
* `button_off` - Schaltet die LEDs aus

## Entwurf der Zustandsmaschine
<span class="tag is-rounded is-info">5 Punkte</span>

Zur Realisierung wird eine Zustandsmaschine genutzt.

* Bearbeite die Datei <samp>led_toggle_fsm.vhd</samp>
* Definiere die drei Zuständen `OFF`, `LED1` und `LED2`
* Der Startzustand ist `OFF`
* Der Eingang `toggle_i` wechselt von `OFF` nach `LED1` bzw. wechselt von `LED1` nach `LED2` und umgekehrt
* Der Eingang `off_i` wechselt immer in den Zustand `OFF`
* Der Eingang `off_i` hat die höhere Priorität als der Eingang `toggle_i`
* Der Ausgang `led1_o` ist auf `'1'`, wenn die Zustandmaschine im Zustand `LED1` ist
* Der Ausgang `led2_o` ist auf `'1'`, wenn die Zustandmaschine im Zustand `LED2` ist

.. info:: Testbench

    Teste die Implementierung mittels der Testbench <samp>led_toggle_fsm_tb.vhd</samp>. Mittels <kbd>F6</kbd> lässt sich
    der gesamte Bereich zoomen.

## Implementierung des Top Levels
<span class="tag is-rounded is-info">5 Punkte</span>

Zur Verfügung stehen die Komponenten <samp>button_dectect</samp> und <samp>led_toggle_fsm</samp>. Diese
Komponenten werden genutzt, um im Top Level <samp>led_toggle.vhd</samp> die gewünschte Funktionalität zu realisieren.

* Die Instanz der Komponente <samp>button_detect</samp> mit dem Namen `toggle_detect_component` ist bereits erstellt
    * `button_i` ist mit dem Eingang `button_toggle_i` verbunden
    * `detect_o` ist mit dem (bereits definiertem) Signal `toggle_detect` verbunden
* Erstelle eine Instanz der Komponente <samp>button_detect</samp> mit dem Namen `off_detect_component` analog zu `toggle_detect_component`
    * `button_i` ist mit dem Eingang `button_off_i` verbunden
    * `detect_o` ist mit dem (bereits definiertem) Signal `off_detect` verbunden
* Erstelle eine Instanz der Komponente <samp>led_toggle_fsm</samp> mit dem Namen `led_toggle_fsm_component`
    * `toggle_i` ist mit dem Signal `toggle_detect` verbunden
    * `off_i` ist mit dem Signal `off_detect` verbunden
    * `led1_o` ist mit dem Ausgang `led1_o` verbunden
    * `led2_o` ist mit dem Ausgang `led2_o` verbunden
* Jede Komponente hat einen Takteingang `clk`, welcher mit dem globalen `clk` verbunden wird

.. info:: Testbench

    Teste die Implementierung mittels der Testbench <samp>led_toggle_tb.vhd</samp>.

## Erweiterung der *Constraints* Datei
<span class="tag is-rounded is-info">2 Punkte</span>

In der Datei <samp>led_toggle.ucf</samp> ist nur das Signal `clk` definiert. Erweitere die Datei um folgende Zuordnungen

* `button_toggle_i` wird durch den Taster <samp>BTN0</samp> angesteuert
* `button_off_i` wird durch den Taster <samp>BTN1</samp> angesteuert
* `led1_o` ist die LED <samp>LD0</samp>
* `led2_o` ist die LED <samp>LD1</samp>

.. figure:: ../basys2_pinout.svg
    :title: Pinout des BASYS2 Boards
    :author: Digilent Inc. BASYS2 Manual
    :source: https://digilent.com/shop/about-fpga-boards/
    :license: &copy; Digilent

## Test am Board
<span class="tag is-rounded is-info">1 Punkt</span>

Synthetisiere das Projekt und teste das Ergebnis am Board

# Ampel mit Überwachung
## Vorbereitung
* Projekt <samp>lights/lights.xise</samp> öffnen

## Aufgabenstellung
Es soll eine Ampel mit zwei Modis realisiert werden:

* Orange-Blinken (Orange Leuchte geht ein und aus)
* Wechsel zwischen Grün, Orange, Rot, Rot-Orange und wieder Grün

Die Ausgänge für die drei Farben der Ampel werden mittels drei Bit Vektor dargestellt:

* Bit0 (ganz rechts) entspricht der grünen Leuchte
* Bit1 entspricht der orangen Leuchte
* Bit2 (ganz links) entspricht der roten Leuchte.

So steht z.B. `"110"` für eine Ampel, bei der Rot und Orange leuchtet. Bei `OFF` soll nichts leuchten.

Zusätzlich soll eine *Überwachung* vorhanden sein, die feststellt, ob es zu ungültigen Kombinationen gekommen ist (z.B.
wenn Rot und Grün gleichzeitig leuchten). Die Überwachung würde in diesem Fall die Ampel Rot leuchten lassen.

## Überwachung
<span class="tag is-rounded is-info">5 Punkte</span>

Die Komponente `supervisor` (deutsch *Überwacher*) soll die Zustände der drei Lampen überprüfen. Dazu hat die Komponente
den Eingang `monitor_i` und den Ausgang `result_o`.

* Liegt an `monitor_i` eine gültige Kombination an (z.B. `"001"` für Grün) soll diese Kombination am Ausgang `result_o` erscheinen
* Liegt eine ungültige Kombination an (z.B. `"101"`) soll stattdessen die Kombination für Rot ausgegeben werden (`"100"`)
* Gültige Kombinationen sind alle Ausgaben der Zustände `GREEN`, `ORANGE`, `RED`, `RED_ORANGE` und `OFF`

Die Komponente ist in vier Ausführungen (*Architectures*) bereits in der Datei <samp>supervisor.vhd</samp> beschrieben. Die
*Architectures* lauten `behave1`, `behave2`, `behave3` und `behave4`.

Erstelle in der Datei <samp>supervisor_tb.vhd</samp> eine Testbench, die herausfindet, welche der vier Ausführungen
funktioniert (es ist genau eine).

## Komponente `lights_fsm`
<span class="tag is-rounded is-info">5 Punkte</span>

Erstelle die Komponente `lights_fsm` durch Bearbeitung der Datei <samp>lights_fsm.vhd</samp>.

* Die Ampel wechselt nur den Zustand, wenn `next_i` gleich `'1'` ist
* Ist der Eingang `mode_i` gleich `'0'` soll die Ampel zwischen den Zuständen `ORANGE` und `OFF` wechseln
* Bei `mode_i` gleich `'1'` soll die Ampel zyklisch zwischen `GREEN`, `ORANGE`, `RED`, `RED_ORANGE` wechseln und anschließend bei `GREEN` wieder starten
* Ist die Ampel im Zustand `GREEN`, `RED` oder `RED_ORANGE` und `mode_i` ist `'0'` soll der nächste Zustand `ORANGE` sein
* Ist die Ampel im Zustand `OFF` und `mode_i` ist `'1'` soll der nächste Zustand `ORANGE` sein
* Der Startzustand ist `ORANGE`

.. info:: Testbench

    Teste die Implementierung mittels der Testbench <samp>lights_fsm_tb.vhd</samp>.

## Implementierung des Top Levels
<span class="tag is-rounded is-info">5 Punkte</span>

Zur Verfügung stehen die Komponenten <samp>counter</samp>, <samp>light_fsm</samp> und <samp>supervisor</samp>. Diese
Komponenten werden genutzt, um im Top Level <samp>lights.vhd</samp> die gewünschte Funktionalität zu realisieren.

Mit dem <samp>counter</samp> soll ein 700 Millisekunden Takt generiert werden. Wieviel Takte des 50 Mhz Taktes sind dazu
notwendig und wieviel Bits werden benötigt, um diesen Wert darstellen zu können? Trage diese Werte in der Default-Einstellung
von `COUNTER_WIDTH` und `COUNTER_MAXIMUM` ein:

```vhdl
entity lights is
    generic (
    COUNTER_WIDTH : integer := 4; -- <<< TODO
    COUNTER_MAXIMUM : integer := 9 -- <<< TODO
    );
    port (
    clk : in std_ulogic; -- 50 MHz clock
    mode_i : in std_ulogic;
    leds_o : out std_ulogic_vector(2 downto 0)
    );
end entity;
```

Erstelle das Top Level anhand des folgenden Blockschaltbildes:

![Top Level für Lights](test3_lights.jpg)

Gegebenenfalls müssen noch Signale definiert werden.

.. info:: Testbench

    Teste die Implementierung mittels der Testbench <samp>lights_tb.vhd</samp>.

## Test am Board
<span class="tag is-rounded is-info">1 Punkt</span>

Synthetisiere das Projekt und teste das Ergebnis am Board
