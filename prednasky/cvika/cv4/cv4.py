#zkuste vyvolat exception a vypsat ji v bloku except
try:
    #number = int(input("zadej cislo: "))
    number = int("ahoj")
except ValueError:
    print("this is not a number")


#prvni vychyta uplne vsechny chyby
#NENI VHODNE POUZIVAT JEN EXCEPTION
try:
    5/0
except Exception:
    print("Exception vychyta vsechny druhy chyb")


#vychyta jenom chyby typu zero division a file not found
# pokud chceme vyvolat nejaky typ erroru
# udelame to pomoci: raise ZeroDivisionError
try:
    raise IndexError("chybova hlaska")
    5/0
    open("foo.txt", "r")
except ZeroDivisionError:
    print("nulou se neda delit")
except FileNotFoundError:
    print("soubor neexistuje")
except Exception as error:
    print("neznama chyba", error)


#fce nacitajici cislo. bude to delat dokud to cislo nezada
def nacti_cislo():
    while(True):
        try:
            num = int(input("zadej cislo: "))
            break
        except ValueError:
            print("nezadal jsi cislo")
    return num

def nacti_cislo_rekurzivne():
    try:
        return int(input("zadej cislo: "))
    except ValueError:
        print("nezadal jsi cislo")
        return nacti_cislo_rekurzivne()

#print(nacti_cislo_rekurzivne())

#---------------------------------------
#---------------------------------------
#---------------------------------------

#SOUBORY

vstup = "tohle je text ktery se ma ulozit do souboru\n"

file = open("soubor1.txt", "w") 
# "a" - prida na konec souboru, "r" - read, "w" - write (vymaze puvodni obsah, nebo vytvori novy)
file.write(vstup)
file.close()


file = open("soubor1.txt", "r")
obsah = file.read()
file.close()
print(obsah)

#cte po radcich
# for lines in file.readlines():
#     print(lines)


#najdete nejdelsi souvisly retezec v hamlet.txt
longest_word = ""
longest_word_len = 0
with open("hamlet.txt", "r") as file2:
    for line in file2.readlines():
        for word in line.split():
            word_len = len(word)
            if longest_word_len < word_len:
                longest_word = word
                longest_word_len = word_len
#nemusi se zavirat soubor pri tomto zapise v bloku
print("nejdelsi slovo je: ", longest_word)

#nejcetnejsi vyskyt slova a dane slovo s hamlet.txt
word_dict = dict()
with open("hamlet.txt", "r") as f:
     for line in f.readlines():
        for word in line.split():
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1
#...
#print(word_dict)

#NEBO
#pretvori list na dictionary a seradi hodnoty
from collections import Counter

with open("hamlet.txt", "r") as f:
     content = f.read()
     words = content.split()
     cnt = Counter(words)

print(cnt.most_common(10))

print()
print()
print()
#nacitani souboru JSON
#upravi hodnoty treba z true pro python na True
import json
#load - nacita json ze souboru
#loads - nacita json z retezce

f = open("orders.json", "r")
data = json.load(f)
f.close()
print(data[:2])