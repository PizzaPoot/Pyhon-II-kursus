def nummerda(korrused, korterid):
    korrus = []
    for i in range(0, korrused):
        korter = []
        for j in range(0, korterid):
            korter.append(str(i + 1) + str(j + 1))
        korrus.append(korter)
    return korrus