class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def habla(self):
        print(f"{self.nombre} dice Guau")


mi_perro = Perro("Kala", 3)
print(f"Mi perro se llama {mi_perro.nombre} y tiene {mi_perro.edad} ayos")
mi_perro.habla()