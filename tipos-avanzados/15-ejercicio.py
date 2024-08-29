# 1. Eliminar los espacios en blanco de un string
# y devolver una lista con los caracteres restantes

# 2. Contar en un diccionario cuando se repiten
# los caracteres de un string

# 3. Ordenar las llaves de un diccionario
# por el valor que tienen y devolver una lista
# que contiene tuplas [("a", 3), ("b", 2), ("c", 4), ("d", 4)]

# 4. De un listado de tuplas, devolver las tuplas
# que tengan el mayor valor.
# [("a", 3), ("b", 2), ("c", 4), ("d", 4)] -> [("c", 4), ("d", 4)]

# 5. Crear un mensaje que diga:
# Los caracteres que más se repiten son:
# - C con 4 caracteres
# - D con 4 caracteres

# 6. Juntar la solucion de los ejercicios anteriores
# para encontrar los caracteres que más se repiten de un string.


def RemoveWhiteSpaces(text):
    return text.replace(" ", "")

def CountLetters(text):
    dic = {}
    for char in text:
        if char not in dic:
            dic[char] = 1
        else:
            dic[char] += 1
    
    return dic

def ConvertDictionaryToTuple(dic):
    l = list()
    for item in dic.items():
        l.append((item))

    return l


def ordena(dict):
    return sorted(
        dict.items(),
        key=lambda key:key[1],
        reverse=True
    )

def GetMaxTuples(list):
    max = 1
    resp = {}
    for item in list:
        if max < item[1]:
            resp[item[0]] = item[1]
    
    return resp

def ShowMessage(dict):
    text = "Los caracteres que más se repiten son:\n"
    for key, value in dict.items():
        text += f" -{key.upper()} con {value} repeticion/es\n"
    print(text)

# def GetMaxValue(l):
#     return max(
#         l,
#         key=lambda v:v[1],
#     )

withoutSpaces = RemoveWhiteSpaces("Hola que tal")
print("1- Eliminar espacios en blanco: ", withoutSpaces)
dictionary = CountLetters(withoutSpaces)
print("2- Contar en un diccionario: ", dictionary)
orderedDic = ordena(dictionary)
print("3- Ordenar diccionario: ", orderedDic)
dictList = ConvertDictionaryToTuple(dictionary)
print("3- Convertir diccionario en tuplas: ", dictList)
maxValues = GetMaxTuples(dictList)
print("4- Ddevolver las tuplas que tengan el mayor valor: ", maxValues)
ShowMessage(maxValues)
