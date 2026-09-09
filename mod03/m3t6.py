import random

numero_1 = random.randint(0,9)
numero_2 = random.randint(0,9)
numero_3 = random.randint(0,9)

koodi_1 = str(numero_1) + str(numero_2) + str(numero_3)


numero_4 = random.randint(1,6)
numero_5 = random.randint(1,6)
numero_6 = random.randint(1,6)
numero_7 = random.randint(1,6)

koodi_2 = str(numero_4) + str(numero_5) + str(numero_6) + str(numero_7)

print(str(koodi_1) , str(koodi_2))