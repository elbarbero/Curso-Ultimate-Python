try:
    n1 = int(input("Ingresa el primer número: "))
except Exception as e:
    print("Ocurrió un error!")
    print(e)
else: # se ejecuta si no hay errores
    print("No ocurrió ningún error")
finally: # se ejecuta siempre, haya o no haya errores
    print("Se ejecuta siempre!")
