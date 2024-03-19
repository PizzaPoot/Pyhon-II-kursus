def alla_ules(sisend):
    if sisend < 0:
        return
    elif sisend == 0:
        print("Põhi!")
        return
    if sisend % 2 != 0:
        for i in range(sisend, 0, -2):
            print(i)
        print("Põhi!")
        for i in range(0, sisend + 1, 2):
            print(i)
    elif sisend % 2 == 0:
        for i in range(sisend, 0, -2):
            print(i)
        print("Põhi!")
        for i in range(1, sisend + 1, 2):
            print(i)
    alla_ules(-1) #does nothing :p