buscar = 6
for numero in range(5):
    print(numero)

for numero in range(5):
    print(numero, numero * 'Hola mundo')

for numero in range(5):
    if numero == buscar:
        print('Encontrado -->', buscar)
        break
else:
    print("No encontré el número :(")

for char in "Ultimate python":
    print(char)