pienin = None
suurin = None

while True:
    syöte = input("Anna luku: ")

    if syöte == "":
        break

    luku = int(syöte)

    if pienin is None:
        pienin = luku
        suurin = luku
    else:
        if luku < pienin:
            pienin = luku

        if luku > suurin:
            suurin = luku
print("Pienin luku on:", pienin)
print("Suurin luku on:", suurin)
