print("hello david")
print(40+32)
print(2**4)
print(2/3) #vzdy vraci float
print(10//3) #deleni celociselne

mojecislo = 3
print(mojecislo)

a, b = 1, 2
print(a, b)
a, b = b, a
print(a, b)

c = d = e = 2
print(c, d, e)

pravda = True
nic = None

#zaokrouhleni
x = float(input("zadej cislo 1"))
y = float(input("zadej cislo 2"))
print(int(x/y))

ahoj = """
viceradkovy
string
"""
print(ahoj)

delka = len("ahojjakje")
print(delka)

#raw text
print(r"C:\some\name")

slovo = "python"
print(slovo[-1])
print(slovo[0:2])
print(slovo[-2:])

print(slovo.find("kul"))
print(slovo.find("pyt")) #napise na jakem indexu jinak 1

slovo.replace("pyt", "PYT")
print(slovo)
print(slovo.isalpha())
print(slovo.isdigit())

vstup = input("zadej cislo")
while not vstup.isdigit():
    print("zadal jsi spatne")
    vstup = input("zadej cislo")
print("cislo je " + vstup)