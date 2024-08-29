import os

if __name__ != "__main__":
    from ..gestion.crud import guardar

def pagar_impuestos():
    print("Guardando utilidades")
    guardar()

def pagar_utilidades():
    print(f"Pagando utilidades desde {os.path.basename(__file__)}")


if __name__ == "__main__":
    print("Tarea de mantenimiento")