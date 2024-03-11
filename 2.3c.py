def vahimatest_suurim(maatriks):
    arvud = []
    for element in maatriks:
        arvud.append(min(element))
    return max(arvud)