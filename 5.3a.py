def sorteeri(failinimi):
    fail = open(failinimi, encoding="UTF-8")
    laulud = {}
    for rida in fail:
        year = rida.rstrip().split(";")[2]
        decade = int(year) // 10 * 10
        laul = laulud.get(decade, [])
        laul.append(rida.rstrip().split(";"))
        laulud[decade] = laul
    return laulud

def kuva(laulud):
    for key in sorted(laulud.keys()):
        most_sold = max(laulud[key], key=lambda x: int(x[-1]))
        print(f"{key}: {len(laulud[key])} album(it) ({most_sold[0]} - {most_sold[1]})")

kuva(sorteeri("albumid.txt"))