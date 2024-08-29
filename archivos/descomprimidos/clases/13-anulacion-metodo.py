class Ave:
    def __init__(self):
        self.volador = True

    def vuela(self):
        print("vuela ave")

class Pato(Ave):
    def __init__(self):
        super().__init__()
        self.nadador = True

    def vuela(self):
        print("vuela pato")
        super().vuela()


pato = Pato()
pato.vuela()
print(pato.volador)
print(pato.nadador)