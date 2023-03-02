#DICT

#preved list studentu a loginu do dvojic v dictionary
studenti = ["xlogin1","jmeno1","xlogin2","jmeno2","xlogin3","jmeno3"]

studenti_dict = {}
for i in range(0,len(studenti),2):
    studenti_dict[studenti[i]] = studenti[i+1]
print("dictionary je: ", studenti_dict)


st = [
  {"xlogin": "xvalovic", "jmeno": "Roman", "predmety": ["PYT", "ALG"]},
  {"xlogin": "xhavlik", "jmeno": "Jan", "predmety": ["AI", "ALG"]},
  {"xlogin": "xnadule", "jmeno": "Nada", "predmety": ["WD", "PYT"]},
  {"xlogin": "xmuron", "jmeno": "Mikulas", "predmety": ["TZI", "PTN"]},
  {"xlogin": "xpernes", "jmeno": "Petr", "predmety": ["PYT", "MAT"]}
]

#vypiste loginy studentu s predmetem ALG
print("studenti s predmetem ALG: ")
for student in st:
    if "ALG" in student["predmety"]:
        print(student["xlogin"])

#vypiste unikatni seznam vsech predmetu
unikatni_predmety = set()
for student in st:
    for predmet in student["predmety"]:
        unikatni_predmety.add(predmet)
print("unikatni predmety jsou: ", unikatni_predmety)

#predmety jako klice a seznam studentu studujici dany predmet bude ulozeny jako hodnota pod timto klicem
predmety_studenti = {p: [] for p in unikatni_predmety}
for p in unikatni_predmety:
    for studenti in st:
        if p in studenti["predmety"]:
            predmety_studenti[p].append(studenti["xlogin"])
print("seznam predmetu a jejich studentu: ")
print(predmety_studenti)

#MODULY
#hra kamen,nuzky,papir s pomoci modulu random ze souboru kmn.py

#import kmn
#result =kmn.play()

#from kmn import play
#result = play()
#print(result)

#vytvorte program jenz spocita vek osoby
import datetime
narozeni = datetime.datetime(2001,9,3) #parametry rok mesic den
dnes = datetime.datetime.now()
vek = dnes - narozeni
print(vek.days)

today = datetime.datetime.strptime("2023-03-02", "%Y-%m-%d")
print(today)
print(today.year)

#funkce ktera prevezne libovolny pocet parametru
def scitacka( *params, operace):
    #je to ve formatu tuple
    print(params)
    print("soucet je: ", sum(params))
    print("max je: ", operace(params))

scitacka(1,2,3,4,5, operace=max) #operace musi operace=...


#pojmenovat si muzeme i parametry
def zapis_studenti(jmeno,prijmeni,vek):
    print("jmeno: ",jmeno)
    print("prijmeni: ",prijmeni)
    print("vek: ", vek)

zapis_studenti(jmeno="david", vek=15,prijmeni="krcmar") # dokonce parametry nemusi dodrzovat svoje poradi


#faktorial
def fakt(cislo):
    if cislo < 1:
        return 1
    else:
        return cislo * fakt(cislo-1)

print(fakt(5))






