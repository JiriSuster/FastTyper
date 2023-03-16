class Automobil:
    def __init__(self, model, znacka):
        self.model = model
        self.tachometer = 5
        self.znacka = znacka

class OsobniAuto(Automobil):
    def __init__(self, model, tachometer, pocetSedacek, znacka):
        super().__init__(model,tachometer, znacka)
        self.pocetSedacek = pocetSedacek

class Nakladak(Automobil):
    def __init__(self, model, nosnost, znacka):
        super().__init__(model, znacka)
        self.nosnost = nosnost

lorry = Nakladak("model", 1000, "fajso")
print(lorry.model)
print(lorry.nosnost)
print(lorry.tachometer)
print(lorry.znacka)

class RodicA:
    def __init__(self):
        self.x = 10

class RodicB:
    def __init__(self):
        self.y = 20

class Potomek(RodicA,RodicB):
    def __init__(self):
        super().__init__()
        self.z = 30

a = Potomek()
print(a.x)
#print(a.y) <--vypise error
print(a.z)