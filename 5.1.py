def symbolite_sagedus(string):
    sagedus = {}
    for letter in string:
        if letter in sagedus:
            sagedus[letter] += 1
        else:
            sagedus[letter] = 1
    return sagedus