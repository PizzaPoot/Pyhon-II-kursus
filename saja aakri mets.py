fail = open(input("Failinimi: "), encoding="UTF-8")
metsapindalad = []
for rida in fail:
    metsapindalad.append(float(rida.strip()))
fail.close()
aastanejuurdekasv = float(input("Aastane juurdekasv: "))
piir = float(input("Piir: "))

def juurdekasv(aakrid, juurdekasv):
    hektarid = aakrid * 0.4047
    juurdekasv = hektarid * juurdekasv
    return round(juurdekasv, 2)


i = 0

for aakrid in metsapindalad:
    if aakrid > piir:
        i += 1
        print("Metsatüki aastane juurdekasv on ", juurdekasv(aakrid, aastanejuurdekasv))
    else:
        print("Metsatükki ei võeta arvesse")
print(f"Arvutati {i} metsatüki juurdekasv.")
