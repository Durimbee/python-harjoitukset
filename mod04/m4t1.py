kuhan_pituus = int(input("Anna kuhan pituus senttimetreinä: "))

if kuhan_pituus < 37:
    puuttuu = 37 - kuhan_pituus
    print("Mitasta puuttuu", puuttuu,  "cm")
    print("Kuha on alamittainen, laske se takaisin järveen.")
else:
    print("Wau, hieno saalis!")