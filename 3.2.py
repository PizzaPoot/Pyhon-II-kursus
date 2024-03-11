def keskmised(hinded):
    keskmised = []
    for aine in hinded:
        keskmine = sum(aine[1:]) / len(aine[1:])
        keskmised.append([aine[0], round(keskmine, 1)])
    return keskmised