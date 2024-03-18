def voitis_nurkademangu(matrix):
    if matrix[0][0] == "X" and matrix[0][4] == "X" and matrix[4][0] == "X" and matrix[4][4] == "X":
        return True
    else:
        return False

def x_peadiagonaalil(matrix):
    xarv = 0
    for i, rida in enumerate(matrix):
        if rida[i] == "X":
            xarv += 1
    return xarv

def x_korvaldiagonaalil(matrix):
    xarv = 0
    for i, rida in enumerate(matrix):
        if rida[4-i] == "X":
            xarv += 1
    return xarv

def voitis_diagonaalidemangu(matrix):
    if x_peadiagonaalil(matrix) == 5 and x_korvaldiagonaalil(matrix) == 5:
        return True
    else:
        return False
    
def voitis_taismangu(matrix):
    xarv = 0
    for rida in matrix:
        for element in rida:
            if element == "X":
                xarv += 1
    if xarv == 25:
        return True
    else: 
        return False