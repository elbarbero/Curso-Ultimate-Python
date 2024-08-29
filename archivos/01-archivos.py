from pathlib import Path
from time import ctime

archivo = Path("archivos/archivo-prueba.txt")
# archivo.exists()
# archivo.rename()
# archivo.unlink() # elimina el archivo

print(archivo.stat())
print("acceso ", archivo.stat().st_atime)
print("acceso ", ctime(archivo.stat().st_atime))
print("creacion ", ctime(archivo.stat().st_birthtime))
print("modificacion ", ctime(archivo.stat().st_mtime))