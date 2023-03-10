#IS and ==
a = [1,2,3]
b = [1,2,3]
c = a
print(a is b)
print(a is c)
print(a == b == c)

#IN
print("tady je in: ")
print("tup" in "vstup")
print("z" in "vstup")
print(1 in a)

decision = input("zadej rozhodnuti: ")
if decision in ["souhlasim", "ano", "ok"]:
    print("souhlas")
elif decision in ["nesouhlas", "ne"]:
    print("nesouhlas")
else:
    print("spatny input")

cisla = range(0,50,10)
for x in cisla:
    print("cislo je: ",x)

data = []
for i in range(5):
    data.append(input("zadej text:  "))
data.reverse()
for element in data:
    print(element)
#zpet otocit
for i in range(len(data)-1,-1,-1):
    print(data[i])

enu = ["a","b","c","d"]
for i,v in enumerate(enu):
    print("index: " + str(i) +" value: " + str(v))

#while
vstup = input("vstup: ")
vstup_list = list()
while vstup != "konec":
    vstup_list.append(vstup)
    vstup = input("vstup: ")
vstup_list.sort()
print(vstup_list)