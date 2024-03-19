def nurkademanguks_vaja(matrix):
    indices = []
    corners = [(0, 0), (0, 4), (4, 0), (4, 4)]
    for i, j in corners:
        if matrix[i][j] != "X":
            indices.append(matrix[i][j])
    return indices        

def diagonaalidemanguks_vaja(matrix):
    elements = set()
    size = len(matrix)
    for i in range(size):
        if matrix[i][i] != "X":
            elements.add(matrix[i][i])
        if matrix[i][size - i - 1] != "X":
            elements.add(matrix[i][size - i - 1])
    return list(elements)

def taismanguks_vaja(matrix):
    vaja = []
    for row in matrix:
        for element in row:
            if element != "X":
                vaja.append(element)
    return vaja