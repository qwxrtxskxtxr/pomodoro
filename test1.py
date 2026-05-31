def d(n, m):
    return n % m == 0
ans = []
for a in range(1, 500):
    flag = True
    for x in range(1, 500):
        if not (d(70, a) and (d(x, 28) <= ((not(d(x, a))) <= (not(d(x, 21)))))):
            flag = False
            break
    if flag:
        ans.append(a)
print(max(ans))