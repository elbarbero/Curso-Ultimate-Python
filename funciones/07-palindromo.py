# Realizado por Nicolas Schurmann
def no_space(texto):
    nuevo_texto = ""
    for char in texto: 
        if char != " ":
            nuevo_texto += char
    return nuevo_texto

def reverse(texto):
    texto_al_reves = ""
    for char in texto:
        texto_al_reves = char + texto_al_reves
    return texto_al_reves

def es_palindromo_1(texto):
    texto = no_space(texto)
    texto_reves = reverse(texto)
    return texto.lower() == texto_reves.lower()

print("Abba", es_palindromo_1("Abba"))
print("Reconocer", es_palindromo_1("Reconocer"))
print("Amo la paloma", es_palindromo_1("Amo la paloma"))
print("Hola Mundo", es_palindromo_1("Hola Mundo"))

# Realizado por mi
def es_palindromo_2(value):
    return value.lower().replace(" ", "")[::-1] == value.lower().replace(" ", "")

print("anil   ina", es_palindromo_2("anil   ina"))