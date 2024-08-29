from varname import nameof # pip install varname

numeros = [2,56, 41, 11, 5, 94, 74]

numeros.sort()
print(numeros)

numeros.sort(reverse=True)
print(numeros)

newList = sorted(numeros, reverse=False) # el metodo Sorted me devulta una nueva lista ordenada
print(f"Lista {nameof(numeros)} --> {numeros}")
print(f"Lista {nameof(newList)} --> {newList}")

usuarios = [
    [4, "Chanchito"], 
    [1, "Felipe"], 
    [5, "Pulga"]
    ]
usuarios.sort()
print(usuarios)

usuarios = [
    ["Chanchito", 4], 
    ["Felipe", 1], 
    ["Pulga", 5]
    ]

def ordena(element):
    return element[1]

usuarios.sort(key=ordena)
print(usuarios)

# Funcion lambda
usuarios.sort(key=lambda e:e[1], reverse=True)
print(usuarios)