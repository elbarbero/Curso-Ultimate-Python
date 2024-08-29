pila = []
pila.append(1)
pila.append(2)
pila.append(3)

print(pila)
removed = pila.pop()
print(removed)
print(pila)
print(pila[-1])

if not pila: # si esta vacia...
    print("Pila vacia")