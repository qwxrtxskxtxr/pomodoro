for a in range(1, 300):
    flag = True
    for x in range(1000):
        f = (((x & 35 != 0) or (x & 22 != 0)) <= ((x & 15 == 0) <= (x & a != 0)))
        if not f:
            flag = False
            break
    if flag:
        print(a)
        break
