fail = open("hinded.csv", encoding="UTF-8")
for rida in fail:
    osad = rida.split(",")
    nimi = osad[0]
    hinded = osad[1:]
    keskmine = sum(map(int, hinded)) / len(hinded)
    print(nimi, round(keskmine, 1))