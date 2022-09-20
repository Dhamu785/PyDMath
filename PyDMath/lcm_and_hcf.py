import numpy as np
def hcf(*args):
    q = []
    for i in args:
        try:
            q.append(int(i))
        except:
            return 'It accepts only numbers'
    q.sort()
    if len(q) == 2:
        for j in range(q[0],0,-1):
            if (q[0] % j == 0) and (q[1] % j == 0):
                return j
    elif len(q) == 3:
        for j in range(q[0],0,-1):
            if (q[0]%j == 0) and (q[1]%j == 0) and (q[2]% j == 0):
                return j
    
    elif len(q) == 4:
        for j in range(q[0],0,-1):
            if (q[0]%j == 0) and (q[1]%j == 0) and (q[2]% j == 0) and (q[3]% j == 0):
                return j
            
    else:
        return 'It accepts only 4 values'
            

def lcm(*args):
    hcf1 = hcf(*args)
    r = []
    for i in args:
        try:
            r.append(int(i))
        except:
            return 'It accepts only numbers'
    r.sort()
    if len(r) == 2:
        lcm1 = np.product(r) / int(hcf1)
        return int(lcm1)
    elif len(r) == 3:
        x = []
        y = []
        z = []
        pre_extend = 1
        extend = 5
        while True:
            for i in range(pre_extend,extend):
                x.append(r[0]*i)
                y.append(r[1]*i)
                z.append(r[2]*i)
            for j in x:
                if (j in y) and (j in z):
                    return j
            pre_extend = extend
            extend = extend+5
        
    elif len(r) == 4:
        w = []
        x = []
        y = []
        z = []
        pre_extend = 1
        extend = 5
        while True:
            for i in range(pre_extend,extend):
                w.append(r[0]*i)
                x.append(r[1]*i)
                y.append(r[2]*i)
                z.append(r[3]*i)
            for j in w:
                if (j in x) and (j in y) and (j in z):
                    return j
            pre_extend = extend
            extend = extend+5

    else:
        return 'It accepts only 4 values'
