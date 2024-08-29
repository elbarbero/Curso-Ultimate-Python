numeros = [1, 2, 3]

primero = numeros[0]
segundo = numeros[1]
tercero = numeros[2]

primero1, segundo1, tercero1 = numeros
print(primero1, segundo1, tercero1)

primero2, *otros = numeros
print(primero2, otros)

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

primero3, segundo2, *otros = numeros
print(primero3, segundo2, otros)

primero4, segundo3, *otros, ultimo = numeros
print(primero4, segundo3, ultimo, otros)

primero5, segundo4, *otros, penu, ultimo2 = numeros
print(primero4, segundo3, penu, ultimo, otros)