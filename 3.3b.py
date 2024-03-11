def on_bingo_tabel_extra(matrix):
    arvud = []
    for rida in matrix:
        for i, arv in enumerate(rida):
            if i * 15 < arv <= (i + 1) * 15 and arv not in arvud:
                arvud.append(arv)
            else:
                return False
    return True