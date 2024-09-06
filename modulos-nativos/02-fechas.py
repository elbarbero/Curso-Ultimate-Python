import time
from datetime import datetime

# https://docs.python.org/3/library/datetime.html

print(time.time())

fecha = datetime(2024, 8, 29)
fecha2 = datetime(2024, 9, 29)
print(fecha)

ahora = datetime.now()
print(ahora)

fechaStr = datetime.strptime("14-02-2023", "%d-%m-%Y")
print(fechaStr)

print(fecha.strftime("%d-%m-%Y"))
print(fecha > fecha2)

print(
    fecha.year,
    fecha.month,
    fecha.day,
    fecha.hour,
    fecha.minute
)