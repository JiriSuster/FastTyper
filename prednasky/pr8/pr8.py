#OOP
#demeterin zakon -> pravidla nejmensi znalosti (ukryti vnitrni stukruty objektu)
#SRP -> kazda trida resi jen jednu vec
#OCP -> tridy by meli byt otevrene pro rozsirovani, ale uzavrene pro zmeny

#dynamicke vlastnosti
class Bod:

    def __init__(self, x, y) -> None:
        self.__x = x
        self.__y = y

    @property
    def x(self):
        #kontrola
        return self.__x
    
    @property
    #kontrola
    def y(self):
        return self.__y
    
    @x.setter
    def x(self, value):
        #kontrola
        if value < 0:
            raise ValueError("x must be positive")
        self.__x = value

    @y.setter
    def y(self, value):
        #kontrola
        if value < 0:
            raise ValueError("x must be positive")
        self.__y = value
    

b1 = Bod(1,2)
print(b1.x)
b1.x = 3
print(b1.x)


class Kniha:
    def __init__(self, autor, text) -> None:
        self.autor = autor
        self.text = text

    #definovali jsme si vlastni chovani pro len, int, str
    #je to ciste na nas jak si to nadefinujeme
    def __len__(self):
        return int(len(self.text))
    
    def __int__(self):
        return int(len(self.text))
    
    def __str__(self):
        return self.text+" -- "+self.autor
    
    def __add__(self, other):
        nova_kniha = Kniha(self.autor+other.autor, self.text+other.text)
        return nova_kniha
    
    def __eq__(self, other):
        return (other.autor==self.autor and other.text==self.text)

k1 = Kniha("rowling", "Harry")
k2 = Kniha("Tolkien", "Hobbit")
print("pocet znaku: ",len(k1))
print(int(k1))
print(str(k1))
k3 = k1+k2
print(k3)
print(k3==k2)

#anonymni funkce (lambda funkce)

def secti(a,b):
    return a + b

b = secti #jenom jako reference ulozi se jako by to byla promenna
print(b(5,5))
a = secti(5,5)

secti2 = lambda a, b: a + b
print(secti2(3,3))

#jiny zpusob jak manipulovat s hodnotama
cisla = [1,2,3,4,5,6,7,8,9]

for i, cislo in enumerate(cisla):
    cisla[i] = cislo*2
print(cisla)

def vynasob2(x):
    return x*2

print(list(map(vynasob2, cisla)))

print(list(map(lambda x:x*2, cisla)))

c = [1,2,3,4,5,6,7,8,9]
print(list(filter(lambda x:x%2==0, c)))



#testovani
assert(5==5)

def secti(a, b):
    return a+b

#unit testy
def test_secti(a,b):
    assert secti(2,3) == 5
    assert secti(3,3) == 6
    assert secti(-2,0) == -2



