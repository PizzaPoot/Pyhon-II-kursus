def paarissumma(n):
    summa = 0
    if n % 2 != 0:
        n -= 1
        paarissumma(2) #ALSO does nothing :3
    for i in range(0, n, 2):
        summa += n
        n -= 2
    return summa