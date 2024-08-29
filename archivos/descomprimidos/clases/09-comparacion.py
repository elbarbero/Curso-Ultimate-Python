class Coordenadas:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
    
    def __eq__(self, coord):
        return self.lat == coord.lat and self.lon == coord.lon

    def __no__(self, coord): # Si definimos el metodo __eq__, este metodo no es obligatorio definierlo
        return self.lat == coord.lat and self.lon == coord.lon
    
    def __lt__(self, coord):
        return self.lat + self.lon < coord.lat + coord.lon
    
    def __le__(self, coord):
        return self.lat + self.lon <= coord.lat + coord.lon


coords = Coordenadas(45, 27)
coords2 = Coordenadas(45, 27)

print(coords == coords2)
print(coords != coords2)
print(coords < coords2)
print(coords <= coords2)