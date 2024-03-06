fail = open("kalorid.txt", encoding="UTF-8")

toitude_tabel = []

for rida in fail: # iga rea jaoks failist
    korra_grammid = [] # kogume ühe toidukorra info
    osad = rida.split() # tühikute kohalt osadeks

    for osa in osad: # osade kaupa
        korra_grammid.append(int(osa)) # järjekordne info juurde

    toitude_tabel.append(korra_grammid) # toidukorra järjend juurde

fail.close()
kalorid_kokku = 0
for toidukord in toitude_tabel:
    kalorid1 = toidukord[0] * 4 #süsivesikud
    kalorid2 = toidukord[1] * 4 #valgud
    kalorid3 = toidukord[2] * 9 #rasvad
    kalorid_kokku += kalorid1 + kalorid2 + kalorid3
print(kalorid_kokku)