title: Wieso gibt es kein logisches XOR in C?
date: 2016-02-15

In C gibt es vier bitweise Operatoren:

* *UND* Operator - `&`
* *ODER* Operator - `|`
* *Exklusiv ODER* Operator - `^`
* *INVERTIERUNG* - `~`

Neben den bitweisen Operatoren gibt es noch die logischen Verknüpfungen, die den bitweisen entsprechen:

* *UND* Verknüpfung - `&&`
* *ODER* Verknüpfung - `||`
* *INVERTIERUNG* - `!`

Hier fehlt offensichtlich die Exklusive *ODER* Verknüpfung - wieso gibt es kein `^^`?

Mögliche Gründe sind:

* Eine logische *Exklusiv ODER* Verknüpfung ist sehr selten.
* Die Kurzschlussauswertung wird nicht ermöglicht - Ist bei einer *UND* Verknüpfung der erste Term falsch muss der zweite nicht
mehr überprüft werden. Das gleiche gilt bei *ODER* mit dem ersten Term wahr. Bei *Exklusiv ODER* geht dies nicht.

## Und wenn ich es doch mal benötige?
Eine logische *Exklusiv ODER* Verknüpfung lässt sich wie folgt realisieren:

```c
if (!a != !b) {
  ...
}
```

Mittels logischer Invertierung `!` wird der entsprechende Term auf 0 (falsch) oder 1 (wahr) gebracht. Wenn diese logischen
Terme unterschiedlich sind ist die Gesamtaussage wahr.
