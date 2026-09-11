yritykset = 0

while yritykset < 5:
    tunnus = input("Anna tunnus: ")
    salasana = input("Anna salasana: ")
    if tunnus == "python" and salasana == "rules":
        print("Tervetuloa!")
        break
    else:
        yritykset = yritykset + 1
        if yritykset == 5:
            print("Pääsy evätty.")
            break