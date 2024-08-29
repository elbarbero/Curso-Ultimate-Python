from pathlib import Path

path = Path("rutas")
# path.exists()
# path.mkdir()
# path.rmdir()
# path.rename("chanchito-feliz")

print(path.iterdir())

for p in path.iterdir():
    print(p)

archivos = [p for p in path.iterdir() if not p.is_dir()]
print(archivos)

archivos = [p for p in path.glob("*.py")]
print(archivos)

archivos = [p for p in path.glob("01-*.py")]
print(archivos)

archivos = [p for p in path.glob("**/*.py")] # ** ->busca todos los archivos dentro del path definido arriba
print(archivos)

archivos = [p for p in path.rglob("*.py")] # r ->indica que es recursivo y funciona igual que la linea de arriba
print(archivos)