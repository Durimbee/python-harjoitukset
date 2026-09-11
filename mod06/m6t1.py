import random

arpakuutiot = int(input("Arpakuutioiden lukumäärä?"))
summa = 0
for i in range(arpakuutiot):
    silmäluku = random.randint(1,6)
    summa = summa + silmäluku
print(summa)