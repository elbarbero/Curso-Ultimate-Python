import json
from pathlib import Path

# escribir json
productos = [
    {"id": 1, "name": "Surfboard"},
    {"id": 2, "name": "Bicicleta"},
    {"id": 3, "name": "Skate"}
]

data = json.dumps(productos)
print(data)
Path("archivos/productos.json").write_text(data)

# leer json
data2 = Path("archivos/productos.json").read_text(encoding="utf-8")
productos_list = json.loads(data2)
print(productos_list)

# modificar json
productos[0]["name"] = "Chanchito feliz"
data = json.dumps(productos)
Path("archivos/productos.json").write_text(data)
