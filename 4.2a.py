fail = open("tehnika.txt", encoding="UTF-8")
for rida in fail:
    osad = rida.split()
    nimi = osad[0]
    esmane = int(osad[1])
    teine = int(osad[7])
    if teine - esmane > 10:
        print(f"{nimi} - {teine - esmane}%")