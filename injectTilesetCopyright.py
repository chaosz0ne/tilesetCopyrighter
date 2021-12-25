import json

print("Tiled-Editor Copyright-Info nach rc3.world-Vorgaben hinzufügen")
print("Datei rechte.json passend befüllen, dann Aufruf")
print("{$0} <tiledmapdatei.json>")
print("Die <tiledmapdatei.json> wird modifiziert! Vorher eigene Änderungen committen!")
print("")

with open("rechte.json", "r") as rechte_file:
    rechte = json.load(rechte_file)
    print("Folgende Rechte wurden zugeordnet:")
    for recht in rechte:
        print(recht["name"] + " zu -> " + recht["copytxt"])
    #json.dump(rechte, rechte_file, indent=2)

    with open()
