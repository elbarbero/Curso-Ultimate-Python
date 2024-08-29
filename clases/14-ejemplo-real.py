class Model():
    tabla = False

    def __init__(self):
        if not self.tabla:
            print("Error, tienes que definir un tabla")
    
    def guardar(self):
        print(f"Guardando {self.tabla} en BBDD")
    
    @classmethod
    def buscar_por_id(self, oid):
        print(f"Buscando por id {oid} en la tabla {self.tabla}")
    

class Usuario(Model):
        tabla = "Usuario"

    
user = Usuario()
user.guardar()
Usuario.buscar_por_id(123)