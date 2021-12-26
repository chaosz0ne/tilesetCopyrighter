# tilesetCopyrighter
Ein PY-Skript, mit dem tiled-Editor-Maps bearbeitet werden können
fügt je Tileset eine custom-Property *tilesetCopyright* (string) hinzu und gibt ihr eine Lizenz.
Die Lizenz wird in Abhängigkeit des Bildnamens (xyz.png) ermittelt.
Infos dazu stehen in *rechte.json* (bitte gerne erweitern für eigenen Bedarf und als Pull Request für alle)

Das Skript kann idempotent (immer wieder) ausgeführt werden und es überschreibt die bisherigen copyright infos.
Aber auch nur das.
Leider ist die Formatierung des map-JSON erhelbich anders als Tiled es macht. Also muss man es mit Tiled nochmal hübsch speichern.

Aufruf:

python3 injectTilesetCopyright.py meinemap.json

-> danach ist meinemap.json aktualisiert.


Beispiel: aus diesem hier:
```
        {
            "columns": 8,
            "firstgid": 1,
            "image": "../floortileset.png",
            "imageheight": 256,
            "imagewidth": 256,
            "margin": 0,
            "name": "floortileset",
            "spacing": 0,
            "tilecount": 64,
            "tileheight": 32,
            "tiles": [
                {
                    "id": 21,
                    "properties": [
                        {
                            "name": "collides",
                            "type": "bool",
                            "value": true
                        }
                    ]
                }
            ],
            "tilewidth": 32,
        },
```

wird 

```
        {
            "columns": 8,
            "firstgid": 1,
            "image": "../floortileset.png",
            "imageheight": 256,
            "imagewidth": 256,
            "margin": 0,
            "name": "floortileset",
            "spacing": 0,
            "tilecount": 64,
            "tileheight": 32,
            "tiles": [
                {
                    "id": 21,
                    "properties": [
                        {
                            "name": "collides",
                            "type": "bool",
                            "value": true
                        }
                    ]
                }
            ],
            "tilewidth": 32,
            "properties": [
                {
                    "name": "tilesetCopyright",
                    "type": "string",
                    "value": "CC0BY unbekannt"
                }
            ]
        },
```
