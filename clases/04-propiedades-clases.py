class Perro:
    Patas = 4

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def habla(self):
        print(f"{self.nombre} dice Guau")


mi_perro = Perro("Kala", 3)
print(Perro.Patas)
Perro.Patas = 3 # Desde la clase actua como un propiedad estatica
print(Perro.Patas)
mi_perro.Patas = 5 # Desde el objeto actua como una propiedad de la instancia
print(mi_perro.Patas)
print(Perro.Patas)