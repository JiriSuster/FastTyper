###################
# identita objektu#
###################

a="text1"
b="text2"
print(id(a))
print(id(b))

import weakref, gc
class Object:
    pass

aa = Object()
r = weakref.ref(aa)
b = r()
print(aa is b)

del aa
gc.collect()

if r() is None:
    print("objekt byl smazan")
else:
    print("objekt stale existuje")

###############
# iteratory   #
###############

import random

class MujIter:
    def __iter__(self):
        self.count = 10
        return self
    
    def __next__(self):
        if self.count > 0:
            self.count -= 1
            return random.random()
        else:
            raise StopIteration
        
iter = MujIter()
for i in iter:
    print(i)

class MujSeznam:
    def __init__(self) -> None:
        self.list = [1,2,3,4,5]

    def __iter__(self):
        return self.list.__iter__()
    
seznam = MujSeznam()
for i in seznam:
    print(i)


###############
# dekoratory
###############

def decorate(func):
    print("poustim funkci: ")
    return func

@decorate
def f():
    print("f()")

f()

#################
# generatory
#################

def generator():
    yield 1
    yield 2

for i in generator():
    print(i)


###############
# deskriptory
###############

class Celsius:
    def __get__(self, instance, owner):
        return 5*(instance.fahrenheit - 32)/9
    
    def __set__(self, instance, value):
        instance.fahrenheit = 32 + 9 * value / 5

class Temperature:
    celsius = Celsius()

    def __init__(self, initial_f) -> None:
        self.fahrenheit = initial_f

t = Temperature(212)
print(t.celsius)
t.celsius = 0
print(t.fahrenheit)

###############
# closures
###############

def nasobek_cisla(n):
    def multiplier(x):
        return x*n
    
    return multiplier

krat3 = nasobek_cisla(3)
print(krat3(5))

krat5 = nasobek_cisla(5)
print(krat5(5))