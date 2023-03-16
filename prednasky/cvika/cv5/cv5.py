#JSON
import json
from collections import Counter

f = open("orders.json", "r")
json_file = json.load(f)


polozky_list = []
for item in json_file:
        polozky_list += [item["Item Name"]]*item["Quantity"]

cnt = Counter(polozky_list) # counter bere list a udela list tuplu
print(cnt.most_common(10))


#OOP

class Weapon:
    def __init__(self, weapon_type, bonus):
        self._type = weapon_type
        self._bonus = bonus

    @property
    def type(self):
        return self._type

    @property
    def bonus(self):
        return self._bonus

class Creature:
    def __init__(self, power):
        self.power = power
        self.health = 100

    def attack(self, enemy):
        if enemy.isAlive() and self is not enemy: #aby nemohl utocit sam na sebe
            enemy.health -= self.power

    def isAlive(self):
        return self.health > 0


class Hero(Creature):
    def __init__(self, power, name):
        super().__init__(power)
        #privatni promenna
        self._name = name
        self._weapon = None
    
    #dekorator neco jako geter v c++
    @property
    def name(self):
        return self._name

    #jako seter v c++
    @name.setter
    def name(self, name):
        self._name = name

    def attack(self, enemy):
         return super().attack(enemy)

    def info(self):
        print(f'{self.name} se zivotem {self.health} a silou {self.power}')

    @property
    def weapon(self):
        return self._weapon

    @weapon.setter
    def weapon(self, weapon):
        self._weapon = weapon



class Monster(Creature):
    def __init__(self, power, poison):
         super().__init__(power)
         self.poison = poison

    def attack(self, enemy):
         super().attack(enemy)
         if enemy.isAlive():
            enemy.health -= self.poison
         

    def info(self):
        print(f'prisera s zivotem {self.health}, silou {self.power} a jedovatosti {self.poison}')

##########################################################
artus = Hero(power=50, name="artus")
artus.info()
snake = Monster(power=50, poison=10)

artus.attack(snake)
snake.info()
snake.attack(artus)
artus.name = "pepa"
artus.info()