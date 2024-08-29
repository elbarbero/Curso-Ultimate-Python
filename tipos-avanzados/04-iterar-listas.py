mascotas = ["Pelusa", "Pulga", "Felipe", "Chanchito Feliz"]

for mascota in mascotas:
    print(mascota)
    
tuple = enumerate(mascotas)
for mascota in tuple:
    print(mascota)
    
for indice, mascota in enumerate(mascotas):
    print(f"{indice} --> {mascota}")