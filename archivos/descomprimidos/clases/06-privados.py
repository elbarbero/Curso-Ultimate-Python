class Perro:
    def __init__(self, nombre, edad):
        self.__set_nombre(nombre)
        self.edad = edad

    def get_nombre(self):
        return self.__nombre

    def __set_nombre(self, nombre):
        self.__nombre = nombre

    def habla(self):
        print(f"{self.__nombre} dice Guau")

    @classmethod
    def factory(cls):
        return cls("Chanchito Feliz", 4) # cls() es lo mismo que poner Perro()


mi_perro = Perro.factory()
print(f"Mi perro se llama {mi_perro.get_nombre()} y tiene {mi_perro.edad} ayos")
print(mi_perro.__dict__)
print(mi_perro._Perro__nombre) # No se debe hacer así, es una mala practica