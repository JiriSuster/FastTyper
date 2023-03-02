#cviceni 2 struktury

seznam = []
seznam.append("rohlik")
seznam.append("jogurt")
seznam.append("pivo")
print(seznam)
odebrano = seznam.pop(0)
print("odebrali jsme ", odebrano)
seznam.pop((len(seznam)-1))
print(seznam)
#insert na prvni pozici v listu
#pokud dame vyssi index nez je pocet elementu tak to proste vlozi na konec
seznam.insert(0,"mleko")
print(seznam)

#pridejte do seznamu 10 rohliku
seznam2 = ["rohlik"] * 10
print(seznam2)

#cisla delitelna peti od 0 do 100
print(list(range(0,101,5)))

#sortovani podle delky jmena
studenti = [["mikulas",70],
            ["stepan", 50],
            ["roman",60]]

def getValue(item):
    return len(item[0])


studenti.sort(key=getValue)
print("nejkratsi jmeno ma: ",studenti[0][0])
print("nejdelsi jmeno ma: ", studenti[-1][0])
#od nejdelsiho jmeno po nejkratsi
studenti.sort(key=getValue, reverse=True)
print("nejdelsi jmeno ma: ", studenti[0][0])


#SET - mnozina
#mejme list s duplicitnimi hodnotami
duplicitList = [1,2,2,3,3,0]
print(set(duplicitList))

mzk = {"harry", "Catch", "Trainspotting"}
mahenka = {"harry", "Babicka", "Macbeth"}
prunik = mzk.intersection(mahenka)
sjednoceni = mzk.union(mahenka)
print("prunik mnozin", prunik)
print("sjednoceni mnozin: ", sjednoceni)
print("knihy co jsou v mzk ale nejsou v mahence",mzk - mahenka)

mahenka.add("Kytice")
mahenka.remove("harry")
print(mahenka)

#jmeno tymu bude spojeni dvou prvnich pismem kazdeho v tymu
listJmen = ["tadeas","oldrich","monika"]
jmenoTymu = ""
for jmeno in listJmen:
    jmenoTymu += jmeno[:2]
print(jmenoTymu)

#slouzi pro meneni hodnot primo v iterovanem listu
for i,jmena in enumerate(listJmen):
    print(i,".index je ",jmena)


#kalkulacka
znamenka = ["+","-","*","/"]
cislo1 = input("zadej prvni cislo: ")
cislo2 = input("zadej druhe cislo: ")

while not(cislo1.isdigit() and cislo2.isdigit()):
    print("-----zadej znovu hodnoty-----")
    cislo1 = input("zadej prvni cislo: ")
    cislo2 = input("zadej druhe cislo: ")
print("vyber si operaci: ")
cislo1 = float(cislo1)
cislo2 = float(cislo2)
operace = None

while operace not in znamenka:
    for i in range(len(znamenka)):
        print(str(i)+". je operace", znamenka[i])
    operace = input("zadej operaci: ")

if operace is znamenka[0]:
    print(cislo1+cislo2)
elif operace is znamenka[1]:
    print(cislo1-cislo2)
elif operace is znamenka[2]:
    print(cislo1*cislo2)
elif cislo2 != 0 and operace is znamenka[3]:
    print(cislo1/cislo2)
else:
    print("nelze vyresit")


