#Los metodos magicos son todos aquellos que empiezan con un doble guion, como el __init__
# https://rszalski.github.io/magicmethods/

class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def habla(self):
        print(f"{self.nombre} dice ¡Guau!")

    def __str__(self):
        return f"Clase Perro: {self.nombre}"
    
    def __del__(self): # este es el destructor
        print(f"Chao perro: {self.nombre}")


perro = Perro("Chanchito", 7)
print(perro)

del perro