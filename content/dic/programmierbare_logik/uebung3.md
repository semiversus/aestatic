title: VHDL Übung 3 - Toggle
next: uebung4.md
parent: uebersicht.md

# Übungsaufgabe

.. info:: In dieser Übung wird das BASYS2 Board verwendet

    Für weitere Fragen zum Board bitte das [Manual](basys2_manual.pdf) konsultieren.

In dieser Übung wollen wir den Zustand einer LED mittels Tastendruck wechseln. Beim Start ist die LED aus, nach einem
Tastendruck soll die LED ein sein, nach einem weiteren Tastendruck soll die LED wieder aus sein.

# Vorbereitung

* [Projektordner](vhdl_uebung_3.zip) herunterladen und entpacken
* Projekt <code>toggle.xise</code> öffnen

# Aufgabe 1 - Erste Implementierung

```vhdl
architecture behave of toggle is
  signal led_reg : std_ulogic := '0';
begin
  toggle_proc: process(CLK)
  begin
    if rising_edge(CLK) then
      if button_i='1' then
        led_reg <= not led_reg;
      end if;
    end if;
  end process;

  led_o <= led_reg;
end architecture;
```

# Aufgabe 2 - Verbesserung des Design
* Welches Problem ist in Aufgabe 1 aufgetreten?
* Wie kann es gelöst werden?
