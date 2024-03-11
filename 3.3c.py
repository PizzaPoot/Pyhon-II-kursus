fail = open(input("failinimi: "), encoding="UTF-8")
reasummad = []
for reanum, rida in enumerate(fail):
    rida.split()
    reasumma = 0
    for i in rida.split():
        reasumma += int(i)
    reasummad.append([reanum + 1, reasumma])
fail.close()
suurim = -1000000
suurimarida = 0
for element in reasummad:
    if element[1] > suurim:
        suurim = element[1]
        suurimarida = element[0]
print(f"Suurim summa on failis {suurimarida}. real ja see on {suurim}.")
#kohutav kood :skull: