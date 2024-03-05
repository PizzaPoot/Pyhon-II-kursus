fail = open("tulemused.txt", encoding="UTF-8")

tulemuste_tabel = []

for rida in fail: # iga rea jaoks failist
    seti_punktid = [] # kogume ühe seti punkte
    osad = rida.split() # tühikute kohalt osadeks

    for osa in osad: # osade kaupa
        seti_punktid.append(int(osa)) # järjekordsed punktid juurde

    tulemuste_tabel.append(seti_punktid) # seti punktide järjend juurde
fail.close()
eestipunktid = 0
soomempunktid = 0
riigi_nimi = ""
võitja_punktid = 0
kaotaja_punktid = 0

for mang in tulemuste_tabel: # iga mängu kohta
    if mang[0] > mang[1]:
        eestipunktid += 1
    else:
        soomempunktid += 1

if eestipunktid > soomempunktid:
    riigi_nimi = "Eesti"
    võitja_punktid = eestipunktid
    kaotaja_punktid = soomempunktid
else:
    riigi_nimi = "Soome"
    võitja_punktid = soomempunktid
    kaotaja_punktid = eestipunktid

print(f"{riigi_nimi} võitis {võitja_punktid}-{kaotaja_punktid}")