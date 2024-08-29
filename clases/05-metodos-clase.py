class Perro:
    Patas = 4

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @classmethod
    def habla(cls):
        print("¡Guau!")

    @classmethod
    def factory(cls):
        return cls("Chanchito Feliz", 4) # cls() es lo mismo que poner Perro()


mi_perro = Perro("Kala", 3)
mi_perro2 = Perro("Troski", 7)
print(Perro.habla())
mi_perro3 = Perro.factory()
print(f"Mi perro se llama {mi_perro3.nombre} y tiene {mi_perro3.edad} ayos")
