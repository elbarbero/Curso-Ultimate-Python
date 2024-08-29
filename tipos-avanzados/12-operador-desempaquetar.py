lista1 = [1, 2, 3, 4]
print(1, 2, 3, 4)
print(*lista1)

lista2 = [5, 6]

combinada = [*lista1, *lista2]
print(*combinada)

combinada = ["Hola", *lista1, "Adios", *lista2]
print(*combinada)

punto1 = {"x": 19}
punto2 = {"y": 15}
nuevoPunto = {**punto1, **punto2} # Los recorre de izquierda hacia la derecha
print(nuevoPunto)
nuevoPunto = {**punto1, "lala": "Hola", **punto2, "z": "Mundo"} # Los recorre de izquierda hacia la derecha
print(nuevoPunto)