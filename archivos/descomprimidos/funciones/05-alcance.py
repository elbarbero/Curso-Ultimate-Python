saludo = "Hola global"

def saludar():
    saludo = "Hola Mundo"
    print(saludo)

def saludoChanchito():
    saludo = "Hola Chanchito"
    print(saludo)

def saludarGlobal():
    global saludo
    saludo = "Hola Mundo"

print(saludo)
saludarGlobal()
print(saludo)