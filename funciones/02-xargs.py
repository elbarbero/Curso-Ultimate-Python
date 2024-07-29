def suma(a, b):
    print(a+b)

def suma2(*numbers):
    resultado = 0
    for n in numbers:
        resultado += n
    print(resultado)


suma(23, 34)
suma2(23, 34, 3, 84, 0.2598, 11)