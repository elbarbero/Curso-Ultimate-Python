import csv
import os

# escribir
with open("archivos/archivo.csv", "w", newline="") as archivo:
    writer = csv.writer(archivo)
    writer.writerow(["twit_id", "user_id", "text"])
    writer.writerow([1000, 1, "este es un twit"])
    writer.writerow([1001, 2, "otro twit"])

# leer
with open("archivos/archivo.csv", "r") as archivo:
    reader = csv.reader(archivo)
    print(list(reader))
    archivo.seek(0)
    for linea in reader:
        if linea:
            print(linea)

# actualizar CSV
with open("archivos/archivo.csv", "r") as r, open("archivos/archivo_temp.csv", "w", newline="") as w:
    reader = csv.reader(r)
    writer = csv.writer(w)
    for linea in reader:
        if linea[0] == "1000":
            writer.writerow([1000, 1, "texto modificado"])
        else:
            writer.writerow(linea)

os.remove("archivos/archivo.csv")
os.rename("archivos/archivo_temp.csv", "archivos/archivo.csv")

