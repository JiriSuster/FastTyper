#PICKLE
import pickle
mujDict = {"klic": "hodnota", "pole": [1,2,3]}

pickle.dump(mujDict, open("mujPICKLE.p", "wb"))
load = pickle.load(open("mujPICKLE.p", "rb"))
print("pickle: ", load)

#JSON
import json

f = json.dumps(mujDict)
print(f)
json.loads(f)
print("json: ",f)

#csv
import csv

with open("data.csv") as csvfile:
    csv_reader = csv.reader(csvfile)
    for line in csv_reader:
        print(line)

########################
####OOP
########################

class Sportovec:
    def __init__(self, jmeno):
        self.jmeno = jmeno
        self.pocetKm = 0

    def behej(self, km):
        self.pocetKm += km

    def getKm(self):
        return self.pocetKm

pepa = Sportovec("pepa")
pepa.behej(50)
pepa.pocetKm = 80
print(pepa.jmeno, pepa.getKm())

print(pepa)
print(Sportovec)

pepa.pocetKm2 = 9
print(pepa.pocetKm2)


#private vlastnost pomoci prefixu __
class Trida:
    def __init__(self):
        self.__hodnota = 1

    def __vypis_hodnotu(self):
        print(self.__hodnota)

    def vypisHodnotu(self):
        print(self.__hodnota)


t = Trida()
t.vypisHodnotu()
#t.__vypis_hodnotu() <-- privatni metoda
#print(t.__hodnota) <-- privatni promenna

#konstruktor a destruktor
class Trida2:
    def __init__(self):
        print("ahoj")

    def __del__(self):
        print("smazano")

t2 = Trida2()

#je instanci nebo ne vraci bool
print(isinstance(t2,Trida))
print(isinstance(t2,Trida2))
#typ t2 vraci nazev typu
print(type(t2))
del t2

class Kniha:
    def __init__(self, nazev, autor, text):
        self.nazev = nazev
        self.autor = autor
        self.text = text

    def vypisInfo(self):
        print(f"{self.nazev} - {self.autor}")

class Knihovna:
    def __init__(self):
        self.list_knih = []

    def pridejKnihu(self, kniha):
        self.list_knih.append(kniha)

    def vypisKnih(self):
        for kniha in self.list_knih:
            kniha.vypisInfo()


kniha1 = Kniha("1", "1", "1")
kniha2 = Kniha("2", "2", "2")
kniha3 = Kniha("3", "3", "3")
knihovna = Knihovna()
knihovna.pridejKnihu(kniha1)
knihovna.pridejKnihu(kniha2)
knihovna.pridejKnihu(kniha3)
knihovna.vypisKnih()














