#Kysytään pelaajan nimi ja ikä
nimi = input("Mikä on nimesi?")
ikä = int(input("Mikä on ikäsi?"))

#Tulostetaan pelaajan nimi ja ikä
print("Pelaajan nimi: ", nimi)
print("Pelaajan ikä: ", ikä)

#Ikäraja
if ikä <12:
    print("Olet liian nuori pelaamaan.")
else:
    print("Tervetuloa pelaamaan", nimi + "!")
    print(" PÄÄVALIKKO ")
    print("1) Aloita peli")
    print("2) Ohjeet")
    print("3) Lopeta peli")

while True:
    komento = input("Anna komento: ")
    if komento == "Lopeta peli":
        print("Peli keskeytetään. Kiitos pelaamisesta!")
        break
    elif komento == "Aloita peli":
        print("Aloitetaan peliä...")
    elif komento == "Ohjeet":
        print("Tässä ohjeet...")
    else:
        print("Saatavilla olevat komennot: Aloita peli, Ohjeet, Lopeta peli")

print(" PÄÄVALIKKO ")
print("1) Aloita peli")
print("2) Ohjeet")
print("3) Lopeta")