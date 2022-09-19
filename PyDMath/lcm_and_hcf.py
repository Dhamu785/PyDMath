def hcf(*args):
    q = []
    for i in args:
        q.append(i)
    q.sort()
    if len(q) == 2:
        for j in range(q[0],0,-1):
            if (int(q[0]) % j == 0) and (int(q[1]) % j == 0):
                return j
            

def lcm(*args):
    hcf1 = hcf(*args)
    r = []
    for i in args:
        r.append(int(i))
    if len(r) == 2:
        lcm1 = (r[0]*r[1]) / int(hcf1)
        print(lcm1)

lcm(18,15)