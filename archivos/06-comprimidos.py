from zipfile import ZipFile
from pathlib import Path

# escribir zip
with ZipFile("archivos/comprimidos.zip", "w") as zip:
    for path in Path().rglob("*.*"):
        print(path)
        if str(path) != "archivos/comprimidos.zip":
            zip.write(path)

# leer zip
with ZipFile("archivos/comprimidos.zip", "r") as zip:
    print(zip.namelist)
    info = zip.getinfo("archivos/06-comprimidos.py")
    print(
        info.file_size,
        info.compress_size,
        info.compress_type
    )
    zip.extractall("archivos/descomprimidos")