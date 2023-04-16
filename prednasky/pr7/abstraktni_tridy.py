from abc import ABC, abstractmethod

class Mnohouhelnik(ABC):

    @abstractmethod
    def vypis_pocet_stran(self):
        raise 

class Trojuhelnik(Mnohouhelnik):

    def vypis_pocet_stran(self):
        print("ma 3 strany")


class Ctverec(Mnohouhelnik):
    
    def vypis_pocet_stran(self):
        print("pocet stran je 4")


#NELZE JEDNA SE O ABSTRAKTNI TRIDU
# p = Mnohouhelnik()
# p.vypis_pocet_stran()

d = Trojuhelnik()
d.vypis_pocet_stran()


########################
#VLASTNOSTI TRIDY
########################


class Trida:
    vlastnost_tridy = 0

    def __init__(self, cislo):
        self.cislo = cislo 

print(Trida.vlastnost_tridy)
Trida.vlastnost_tridy = 10
print(Trida.vlastnost_tridy)

class Trida2:
    pocet_instanci = 0

    def __init__(self):
        Trida2.pocet_instanci += 1

    def __del__(self):
        Trida2.pocet_instanci -= 1

    @staticmethod
    def staticka_methoda():
        print("tohle je staticka metoda")

    @classmethod
    def class_f(cls):
        print("metoda tridy:" + str(cls))


t1 = Trida2()
t2 = Trida2()
print("pocet instanci je:", Trida2.pocet_instanci)
del t1
print("pocet instanci je:", Trida2.pocet_instanci)
Trida2.staticka_methoda()
t2.staticka_methoda()
Trida2.class_f()
t2.class_f()


######################
# @property          #
######################

class Bod:
    def __init__(self, x, y) -> None:
        self.__x = x
        self.__y = y


    #GETery
    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y

    #SETery
    @x.setter
    def x(self, hodnota):
        self.__x = hodnota
    
    @y.setter
    def y(self, hodnota):
        self.__y = hodnota
    
bod = Bod(5,4)
print(bod.x)
print(bod.y)
bod.y = 9
print(bod.y)

####################
# BUILD-IN ATRIBUTY#
####################

class Neco:
    pass

print(Neco.__name__)
print(Neco.__module__)
print(Neco.__dict__)
z = Neco()
print(z.__class__.__name__)


#######################
# pristup k atributum #
#######################

class Pristup_k_atributum:
    def __init__(self) -> None:
        self.atribut = "ahoj"

    def __getattribute__(*args):
        print("pristupuji k atributu: ")
        return object.__getattribute__(*args)
    
    def __getattr__(self, item):
        print("pristupuju k atributu: " + item)

r = Pristup_k_atributum()
print(hasattr(r, "atribut"))
print(getattr(r, "atribut"))
print(setattr(r, "atribut", 7000))
print(getattr(r, "atribut"))
delattr(r, "atribut")
print(hasattr(r, "atribut"))
r.neexistujici_atribut

#vytvareni behem runtime
class RunTime:
    pass

def fce(self):
    print("funkce", self.atribut)

RunTime.atribut = "a"
RunTime.funkce = fce

tt = RunTime()
tt.atribut
tt.funkce()

###########
#   DOC   #
###########

class Doc:
    'tohle je moje prvni trida'

    def __init__(self):
        pass



if __name__ == "__main__":
    k = Doc()
    print(Doc.__doc__)
    print(k.__doc__)