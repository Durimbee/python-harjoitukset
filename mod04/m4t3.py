sukupuoli = input("Anna sukupuoli (mies, nainen):")
hemoglobiini = int(input("Anna hemoglobiini (g/l): "))

if sukupuoli == "mies":
    if hemoglobiini < 134:
        print("Hemoglobiini on alhainen")
    elif hemoglobiini > 195:
        print("Hemoglobiini on korkea")
    else:
        print("Hemoglobiini on normaali")

if sukupuoli == "nainen":
    if hemoglobiini < 117:
        print("Hemoglobiini on alhainen")
    elif hemoglobiini > 175:
        print("Hemoglobiini on korkea")
    else:
        print("Hemoglobiini on normaali")

