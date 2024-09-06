from datetime import datetime, timedelta

fecha1 = datetime(2023, 1, 1) + timedelta(weeks=1)
fecha2 = datetime(2023, 2, 1)

delta = fecha2 - fecha1
print(delta)
print("Días: ", delta.days)
print("Segundos: ", delta.seconds)
print("Microsegundos: ", delta.microseconds)
print("total_secondas(): ", delta.total_seconds())