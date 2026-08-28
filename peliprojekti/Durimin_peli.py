#Kysytään pelaajan nimi ja ikä

nimi = input("Mikä on nimesi?")
ikä = int(input("Mikä on ikäsi?"))

#Tulostetaan pelaajan nimi ja ikä
print("Nimesi: ", nimi)
print("Ikäsi: ", ikä)

#Ikäraja
if ikä > 12:
    print("Tervetuloa pelaamaan.")
else:
    print("Valitettavasti olet liian nuori pelaamaan")

                                                                