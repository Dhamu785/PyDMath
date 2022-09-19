def hcf(*kwargs):
    q = []
    for i in kwargs:
        q.append(i)
    q.sort()
    if len(q) == 2:
        for j in range(q[0],0,-1):
            if (int(q[0]) % j == 0) and (int(q[1]) % j == 0):
                print(j)
                break

hcf(45,63)