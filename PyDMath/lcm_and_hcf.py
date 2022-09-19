import numpy as np
def hcf(*args):
    q = []
    for i in args:
        try:
            q.append(int(i))
        except:
            return 'It requires only numbers'
    q.sort()
    if len(q) == 2:
        for j in range(q[0],0,-1):
            if (q[0] % j == 0) and (q[1] % j == 0):
                return j
    elif len(q) == 3:
        for j in range(q[0],0,-1):
            if (q[0]%j == 0) and (q[1]%j == 0) and (q[2]% j == 0):
                return j
    else:
        return 'It accepts only 5 values'
            

def lcm(*args):
    hcf1 = hcf(*args)
    r = []
    for i in args:
        r.append(int(i))
    if len(r) == 2:
        lcm1 = np.product(r) / int(hcf1)
        return lcm1

print(hcf(4,6))
print(lcm(4,6))
