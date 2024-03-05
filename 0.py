fail = open("konto.txt", encoding="UTF-8")
tehingud = []
for rida in fail:
    if float(rida.strip()) > 0:
        print(rida.strip())
#bruh too easy