import random
import string

lista = [1, 2, 3, 4, 5, 6, 7]
lista2 = [1, 2, 3, 4, 5, 6, 7]
random.shuffle(lista)

print(random.random())
print(random.randint(1, 10))
print(lista)
print(random.choice(lista2))
print(random.choices(lista2, k=3))
print(random.choices("kjjehkhcfjeri3", k=3))
s = "".join(random.choices("kjjehkhcfjeri3", k=5))
print(s)

chars = string.ascii_letters
digitos = string.digits
seleccion = random.choices(chars + digitos, k=16)
print(seleccion)

contrasena = "".join(seleccion)
print(contrasena)