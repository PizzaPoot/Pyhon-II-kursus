def failist_sonastik(failinimi):
    fail = open(failinimi, encoding="UTF-8")
    sonastik = {}
    for rida in fail:
        osad = rida.split()
        sonastik[osad[0]] = osad[1]
    fail.close()
    return sonastik

def tahised_nimedeks(tahised, sonastik):
    nimed = []
    for tahis in tahised:
        if tahis in sonastik:
            nimed.append(sonastik[tahis])
        else:
            nimed.append(None)
    return nimed

sonastik = failist_sonastik(input("Sisestage failinimi: "))
tahised = input("Piiriületajad: ").split()

for nimi in tahised_nimedeks(tahised, sonastik):
    if nimi is not None:
        print(nimi)
    else:
        print("Tundmatu maa")