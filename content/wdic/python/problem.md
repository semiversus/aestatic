title: Typische Probleme
parent: uebersicht.md

# Sammlung an typischen Problemen

Manche Skripte haben Probleme mit folgenden Dingen:
  * Sonderzeichen und Leerzeichen im Pfad -> möglichst vermeiden
  * OneDrive bzw. Netzlaufwerk -> Projekte lokal speichern

Execution Policy:
```
File ... cannot be loaded because running scripts is disabled on
this system. For more information, see about_Execution_Policies at
https:/go.microsoft.com/fwlink/?LinkID=135170.
```

Bei der oben angeführten Fehlermeldung verhindert eine Richtlinie das Ausführen von Skripten. Führe folgenden Befehl in der Powershell aus: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`