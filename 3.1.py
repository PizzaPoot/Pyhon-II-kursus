fail = open("toad.txt", encoding="UTF-8")

tubade_tabel = []

for rida in fail: # iga rea jaoks failist
    korruse_toad = [] # kogume ühe korruse tubasid
    osad = rida.split() # tühikute kohalt osadeks

    for osa in osad: # osade kaupa
        korruse_toad.append(int(osa)) # järjekordne tuba juurde

    tubade_tabel.append(korruse_toad) # korruse tubade järjend juurde

fail.close()

for i, korrus in enumerate(tubade_tabel):
    i += 1
    if i % 2 == 0:
        for tuba in korrus:
            if tuba % 2 == 0:
                print(tuba)