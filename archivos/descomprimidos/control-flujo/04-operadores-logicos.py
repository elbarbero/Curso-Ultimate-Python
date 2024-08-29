# and, or, not

gas = False
encendido = True
edad = 18

if gas and encendido:
    print("Puedes avanzar")
    
if gas or encendido:
    print("Puedes avanzar a medias")
    
if not gas and encendido:
    print("No tienes gas")
    
if gas and encendido and edad > 17:
    print("Puedes avanzar. Eres mayor de edad.")
    
if gas and (encendido and edad > 17):
    print("Puedes avanzar. Coche arrandado y con gasolina")
    
if not gas and (encendido or edad > 17):
    print("Puedes avanzar.")