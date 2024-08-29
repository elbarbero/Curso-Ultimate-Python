from usuario_impuestos import guardar, pagar_impuestos
from usuarios.acciones import guardar as save_actions, pagar_acciones
from usuarios.impuestos.utilidades import pagar_impuestos as save_utils, pagar_utilidades
import usuarios


guardar()
pagar_impuestos()

# Modulos -> Son archivos
# Paquetes -> Son carpetas (Hay que crear el fichero __init__.py en la carpeta)

save_actions()
pagar_acciones()

save_utils()
pagar_utilidades()

print("_____ LISTA de DIR______")
print(dir(usuarios))

print("_________________")
print(usuarios.__name__)
print(usuarios.__package__)
print(usuarios.__path__)
print(usuarios.__file__)