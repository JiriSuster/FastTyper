#dict
adresar = {"david": 11111111,"pepa": 123456, "ada": 987654}

for jmeno,cislo in adresar.items():
    print(jmeno ," ", cislo)

print(list(adresar.keys()))
print(list(adresar.values()))

users = dict()
users["xdavid"] = dict()
users["xdavid"]["prijmeni"] = "krcmar"
users["xdavid"]["telefon"] = 1111
users["xadela"] = dict()
users["xadela"]["prijmeni"] = "kuliskova"
users["xadela"]["telefon"] = [1111,2222]
print(users)

#funkce
#muze vracet vice hodnot
def sectiAnasob(a,b):
    return a+b,a*b

print(sectiAnasob(1,5))

vysledek = print("ahoj")
print("vysledek z print je: ", vysledek)

#funkce s libovolnym poctem parametru
def secti(*args):
    return sum(args)

print("soucet je: ", secti(5,5,5,5,5))

#pojmenovane parametry
print("ahoj", end="@\n")

#argument s vychozi hodnotou
def pozdrav(jmeno, prijmeni="novak"):
    print("ahoj", jmeno, prijmeni)

pozdrav("david", "krcmar")
pozdrav("david")

#uchovani pojmenovanych parametru za pomoci **kwargs
def funkce(a,*args, **kwargs):
    print(a, args, kwargs)
#kdyz je tam a parametr nelze volat prazdna
#do a se ulozi vzdy prvni hodnota
funkce(1,2,3,b=5,c="ahoj")

#ulozeni odkazu funkce print do hej, ktera se pak chova jako print
hej = print
hej("ahoj chovam se ted jako print")

#moduly
#import math as m -> pak staci print(m.pi)
import math
print(math.pi)

#moduly se daji sdruzit do package
import package.pack
#import package.pack as p
package.pack.zkouska_package()


#requirements
#pres pip install nainstalujeme nebo pres pycharm
#potom do requirements dame pip freeze