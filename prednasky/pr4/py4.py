import sys

if "-help" in sys.argv:
    print("vypis do terminalu: -n <cislo>")
elif "-n" in sys.argv:
    if len(sys.argv) > 2:
        print(int(sys.argv[sys.argv.index("-n")+1])*10)
    else:
        print("nezadana hodnota parametru n")
else:
    print("neznamy parametr")

#knihovna os
import os

muj_adresar = os.getcwd()
print(muj_adresar)

#os.makedir("nova_slozka")
#os.rename("nova_slozka","nova_slozka2")
#os.rmdir("nova_slozka2")

r_code = os.system("dir") #"ls -l"
print(r_code)

#knihovna subprocess
import shutil

memory = shutil.disk_usage("/")

print("pouzita pamet: ", memory)

#datumy
from datetime import date
dnes = date.today()
narozeni = date(int(input("rok: ")), int(input("mesic: ")), int(input("den: ")))
print((dnes-narozeni).days)

#knihovna timeit
import timeit
t1 = timeit.timeit("print('cau')", number=10) #number udava pocet kolikrat se to ma provest
print(t1)

import logging
logging.basicConfig(level=logging.DEBUG)
logging.info("informational message")
logging.debug("debugging message")
logging.warning("warning message")

#knihovna json
import json

d = {"a":1,"b":2}

with open("data.json", "w") as f:
    json.dump(d,f)

with open("data.json", "r") as f:
    x = json.load(f)

print(x)