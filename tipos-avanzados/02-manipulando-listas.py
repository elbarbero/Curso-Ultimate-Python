mascotas = ["Wolfgang", "Pelusa", "Pulga", "Copito"]
print(mascotas[0])
mascotas[0] = "Bicho"
print(mascotas)
print("Print 1 --> ", mascotas[:3])
print("Print 2 --> ", mascotas[2:])
print("Print 3 --> ", mascotas[-1])
print("Print 4 --> ", mascotas[::2])
print("Print 5 --> ", mascotas[1::2])
print("Print 6 --> ", mascotas[1:2:2])
print("Print 7 --> ", mascotas[:])

print("--------------------------------")

numeros = list(range(21))
print(numeros[1::2])