rahat = float(input("Anna rahamäärä: "))
if rahat >= 5:
    print("Voit ostaa latten")
else:
    jäljellä = 5 - rahat
    print ("Tarvitset vielä", jäljellä , "€" , "jotta saat latten")