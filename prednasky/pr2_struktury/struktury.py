#LIST
a = [1,"ahoj",1.2]
b = list()
a[0] = "pepa"
b.append("prvni")
a.pop(0)  #muze mit i index jaky chceme vyhodit
print("delka a je: ", len(a))
print(a[0])
print(b[0])

#vicerozmerny
list1 = [[0,5,6],[1,21,5]]
print("vicerozmerny list:", list1[1])
print("vicerozmerny list:", list1[1][1])

L = [123,'abc',1.23]
print(L+["pokracovani", "dalsi"])
K = [1,2,3]
print(K*3)
#list sort/reverse
P = [5,2,9,0]
P.reverse()
print("reversed: ", P)
P.sort()
print("sorted: ", P)
#list range(start,stop,po kolika)
print(list(range(4)))
print(list(range(-6,7,2)))
#KOPIROVANI LISTUU!!!!!
Q = [1,2,3]
#W = list(Q)
W = Q.copy()
W.pop()
print(Q)
print(W)


#TUPLE
#konstanty, ktere nemuzeme premenit
tup1 = ("a",1,"c")
tup2 = tuple(tup1)
print(tup2)

#SET
s1 = {'a', 'b', 5}
s2 = set(s1)
s2.discard("b") #smaze co chceme smazat
s2.add("ahooj")
print(s2)
#prvku z s1 i s2
print("prvky z s1 a s2", s2.union(s1))
#spolecne prvky
print("spolecne prvky z s1 a s2", s1.intersection(s2))

#FROZENSET
a = {'a','b','c','d'}
fset = frozenset(a)
#nema metodu add!!!


#DICTIONARY
dic1 = dict(one=45, two=55, three=65)
dic2 = {'one': 5, 'two': 6,'three': 7}
dic2['four']=8
dic2["one"] = 20
print("hodnota klice one: ", dic2["one"])
print(dic1.get('one'))
print(dic2.values())
print(dic2.keys())

for value, key in dic2.items():
    print("hodnota: ",value, " klic: ", key)