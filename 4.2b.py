fail = open("maalähedane.csv", encoding="UTF-8")
kokkunimed = []
kokkunum = []
for rida in fail:
    osad = rida.split(";")
    nimi = osad[0]
    osalejad = osad[1:]
    kokkunum.append(sum(map(int, osalejad)))
    kokkunimed.append([nimi, sum(map(int, osalejad))])

suurim = ""
max = 0
for rida in kokkunimed:
    if rida[1] > max:
        max = rida[1]
        suurim = rida[0]
print(f"Kõige rohkem osalejaid - {suurim}, {max} inimest.")
print(f"Kokku on kursusel osalenud {sum(map(int, kokkunum))} inimest.")