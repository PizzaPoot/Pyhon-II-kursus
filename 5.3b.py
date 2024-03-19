def juhuslik_bingo():
    import random
    bingo = []
    rida1 = []
    rida2 = []
    rida3 = []
    rida4 = []
    rida5 = []
    for i in range(5):
        start = (i * 15) + 1
        end = (i * 15) + 16
        randtulp = random.sample(range(start, end), 5)
        rida1.append(randtulp[0])
        rida2.append(randtulp[1])
        rida3.append(randtulp[2])
        rida4.append(randtulp[3])
        rida5.append(randtulp[4])
    bingo.append(rida1)
    bingo.append(rida2)
    bingo.append(rida3)
    bingo.append(rida4)
    bingo.append(rida5)
    return bingo
#Horrible code