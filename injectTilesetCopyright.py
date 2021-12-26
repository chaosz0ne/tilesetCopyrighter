import json
import sys

# bildname in lizenztext wandeln, daten ist rechte-json
def img2liz(image, daten):
    for cpr in daten:
        if cpr["name"] in image:
            return cpr["copytxt"]
    return False

# lizenz-property einbauen, falls nicht vorhanden
def addLiz(ts, lizTxt):
    prop = json.loads('{"name":"tilesetCopyright", "type":"string"}')
    prop["value"] = lizTxt
    if "properties" in ts:
        p = ts["properties"]
        # altes falls enthalten entfernen, neues hinzu
        for i in range(len(p)):
            if p[i]["name"] == "tilesetCopyright":
                del p[i]
                break
        p.append(prop)
    else:
        ts["properties"] = [ prop ]



print("Tiled-Editor Copyright-Info nach rc3.world-Vorgaben hinzufügen")
print("Datei rechte.json passend befüllen, dann Aufruf")
print(sys.argv[0] + " <tiledmapdatei.json>")
print("Die <tiledmapdatei.json> wird modifiziert! Vorher eigene Änderungen committen!")
print("")

with open("rechte.json", "r") as rechte_file:
    rechte = json.load(rechte_file)
    print("Folgende Rechte wurden zugeordnet:")
    for recht in rechte:
        print(recht["name"] + " zu -> " + recht["copytxt"])

    if len(sys.argv) <= 1:
        print("Du hast vergessen die Tiled-Datei (Json) als Arument anzugeben. Ende.")
        exit(1)
    
    tiledfile = sys.argv[1]
    print("Überschreibe jetzt die Datei mit geändertem Inhalt: " + tiledfile)
    mapjson = []
    with open(tiledfile, "r") as map_file:
        mapjson = json.load(map_file)
        try:
            tilesets = mapjson["tilesets"]
            for ts in tilesets:
                print("Bearbeite tileset " + ts["name"])
                image = ts["image"]
                lizTxt = img2liz(image, rechte)
                if lizTxt:
                    print("--> verwende Lizenz " + lizTxt)
                    addLiz(ts, lizTxt)
                else:
                    print("--> keine Lizenz zu " + image + " gefunden")


        except:
            print("fail")
            exit(1)


    with open(tiledfile, "w") as map_out_file:
        json.dump(mapjson, map_out_file, indent=4)
    print("geschrieben")


