# LAS TUPLAS NO SE PUEDEN MODIFCAR
numeros = (1, 2, 3) + (4, 5, 6)
print(numeros)

punto = tuple([1, 2])
print(punto)
menosNumeros = numeros[:2]
print(menosNumeros)
primero, segundo, *otros = numeros
print(numeros)

for n in numeros:
    print(n)

# Para modificar una tupla, hay que convertirla previamente a una lista
listaNumeros = list(numeros)
listaNumeros[0] = "Chanchito Feliz"
print(listaNumeros)