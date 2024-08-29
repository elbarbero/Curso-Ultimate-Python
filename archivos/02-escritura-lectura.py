from pathlib import Path

archivo = Path("archivos/archivo-prueba.txt")
texto = archivo.read_text("utf-8")
print(texto)

l = archivo.read_text("utf-8").split('\n')
print(l)
print("----------------------------")
l.insert(0, "Hola mundo!")
print(l)
print("----------------------------")
string = "\n".join(l)
print(string)

archivo.write_text(string, "utf-8")