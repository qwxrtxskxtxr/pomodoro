for a in range(300):
    flag = True
    for x in range(500):
        for y in range(500):
            f = (((3 * x + 7 * y) < a) or (x >= y) or (y > 6))
            if not f:
                flag = False
                break
    if flag:
            print(a)
            break
            