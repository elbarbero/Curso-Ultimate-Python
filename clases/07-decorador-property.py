class Perro:
    def __init__(self, nombre):
        self.nombre = nombre
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        if nombre.strip():
            self.__nombre = nombre


perro = Perro("Choclo")
print(perro)
print(perro.nombre)
perro.nombre = "Choclo 2"
print(perro.nombre)