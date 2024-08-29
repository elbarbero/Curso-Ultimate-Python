mascotas = [
    "Pelusa",
    "Pulga",
    "Wolfgang",
    "Felipe",
    "Pulga", 
    "Chanchito Feliz"
    ]

mascotas.insert(1, "Melvin")
print(mascotas)
mascotas.append("Chanchito Triste")
print(mascotas)

mascotas.remove("Pulga") # Elimina el primero que encuentra en la lista
print(mascotas)

removed = mascotas.pop()
print(f"Element removed --> {removed}")
print(mascotas)
removed = mascotas.pop(1)
print(f"Element removed --> {removed}")
print(mascotas)
del mascotas[0]
print(mascotas)

mascotas.clear()
print(mascotas)
