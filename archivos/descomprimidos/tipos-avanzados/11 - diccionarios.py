punto = {"x": 25, "y": 50}
print(punto)
print(punto["x"])
print(punto["y"])

punto["z"] = 45

if "lala" in punto:
    print("Encontre lala ", punto["lala"])
    
print("Encontre el valor ", punto.get("x"))
print("El valor por defecto si no existe es ", punto.get("lala", 97))

del punto["x"]
del (punto["y"])

print(punto)
punto["x"] = 25

for valor in punto:
    print(valor)

for valor in punto:
    print(valor, punto[valor])

for valor in punto.items():
    print(valor)

for llave,valor in punto.items():
    print(llave, valor)

usuarios = [
    {"id": 1, "nombre": "Chanachito"},
    {"id": 2, "nombre": "Feliz"},
    {"id": 3, "nombre": "Nicolas"},
    {"id": 4, "nombre": "Felipe"},
]

for user in usuarios:
    print(user["nombre"])