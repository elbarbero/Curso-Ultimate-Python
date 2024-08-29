from collections import deque

fila = deque([1, 2, 3])
fila.append(4)
fila.append(5)
fila.append(6)
print(fila)

fila.popleft()
print(fila)

if not fila: # si la fila esta vacia...
    print("Fila esta vacia")
else:
    print("Fila no esta vacia")