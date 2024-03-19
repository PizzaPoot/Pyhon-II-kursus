def kooslubajad(sets):
    max_similar = 0
    max_indexes = (0, 1)
    for i in range(len(sets)):
        for j in range(i+1, len(sets)):
            similar_elements = len(sets[i] & sets[j])
            if similar_elements > max_similar:
                max_similar = similar_elements
                max_indexes = (i, j)
    
    return max_indexes