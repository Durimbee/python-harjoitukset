import random

pisteiden_määrä = int(input("Kuinka monta pistettä arvotaan?"))

ympyrän_sisällä = 0
arvottu = 0

while arvottu < pisteiden_määrä:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x**2 + y**2 < 1:
        ympyrän_sisällä = ympyrän_sisällä + 1

    arvottu = arvottu + 1

pii = 4 * ympyrän_sisällä / pisteiden_määrä
print(pii)
