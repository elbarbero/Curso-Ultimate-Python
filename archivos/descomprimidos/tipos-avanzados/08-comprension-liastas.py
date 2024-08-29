usuarios = [
    ["Chanchito", 4], 
    ["Felipe", 1], 
    ["Pulga", 5]
    ]

nombres = []
for user in usuarios:
    nombres.append(user[0])
print(nombres)

# Map
nombres.clear()
nombres = [user[0] for user in usuarios]
print(nombres)

# Filtar - filter
nombres.clear()
nombres = [user for user in usuarios if user[1] > 2]
print(nombres)

# Map
nombres.clear()
nombres = list(map(lambda user: user[0], usuarios))
print(nombres)

# Filter
nombres.clear()
nombres = list(filter(lambda user: user[1] > 2, usuarios))
print(nombres)
