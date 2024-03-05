fail = open(input("failinimi: "), encoding="UTF-8")
kalapikkused = []
kaalud = []
for rida in fail:
    kalapikkused.append(float(rida.strip()))
puugialammoot = float(input("püügialammõõt: "))
fulton = float(input("fulton: "))

def kala_kaal(pikkus, fulton):
    kaal = (pikkus**3) * fulton / 100
    return round(kaal)

for pikkus in kalapikkused:
    if pikkus >= puugialammoot:
        print(f"Püütud kala kaaluga {kala_kaal(pikkus, fulton)} grammi")
        kaalud.append(kala_kaal(pikkus, fulton))
    else:
        print("Kala lasti vette tagasi")
print(f"Kõige raskem püütud kala: {round(max(kaalud) / 1000), 3} kg")