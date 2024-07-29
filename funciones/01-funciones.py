def hola():
    print("Hola Mundo!")
    print("Ultimate Python")

def hola2(nombre, apellido):
    print("Hola Mundo!")
    print(f"¡Bienvenido {nombre} {apellido}!")

def hola3(nombre, apellido="Feliz"):
    print("Hola Mundo!")
    print(f"¡Bienvenido {nombre} {apellido}!")

hola()
hola2("Nicolas", "SCHurmann")
hola3("Nicolas")
hola3(apellido="Chanchito", nombre="Nicolas")