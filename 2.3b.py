fail = open("raamatud.txt", encoding="UTF-8")
import math
kirjandus_tabel = [] # Tühi järjend, kuhu lisame raamatud

for rida in fail:    # Iga rea jaoks failist
    raamat = []     # Kogume reas olevad raamatu pealkirja ja lehekülgede arvu järjendisse
    osad = rida.split(":") # Jupitame rea semikooloni koha pealt

    pealkiri = osad[0].strip() # Eraldame pealkirja
    leheküljed = int(osad[1].strip()) # Eraldame lehekülgede arvu

    raamat.append(pealkiri) # Lisame reas olevad raamatu pealkirja ja lehekülgede arvu järjendisse
    raamat.append(leheküljed)

    kirjandus_tabel.append(raamat) # Lisame raamatute järjendi kirjanduse tabelisse

fail.close()
tunnid = 0
for raamat in kirjandus_tabel:
    minutid = raamat[1] * 2
    paev = minutid / 60 / 2
    tunnid += minutid / 60
    if paev >  4:
        print(f"{raamat[0]} - {math.ceil(paev)} päeva")
print(f"Kõigi raamatute lugemiseks kulub {round(tunnid, 1)} h.")