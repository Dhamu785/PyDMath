import numpy as np
def hcf(args):
    q = []
    for i in args:
        try:
            q.append(int(i))
        except:
            return 'It accepts only numbers'
    q.sort()
    if len(q) == 1:
        return 'It does not accept single value'
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
    
    elif len(q) == 5:
        for j in range(q[0],0,-1):
            if (q[0]%j == 0) and (q[1]%j == 0) and (q[2]% j == 0) and (q[3]% j == 0) and (q[4]%j ==0):
                return j
            
    else:
        return 'It accepts only 5 values'
            

def lcm(args):
    r = []
    for i in args:
        try:
            r.append(int(i))
        except:
            return 'It accepts only numbers'
    r.sort()
    if len(r) == 1:
        return 'It does not accept single value'
    elif len(r) == 2:
        x = []
        y = []
        pre_extend = 1
        extend = 5
        while True:
            for i in range(pre_extend,extend):
                x.append(r[0]*i)
                y.append(r[1]*i)
            for j in y:
                if j in x:
                    return j
            pre_extend = extend
            extend = extend + 5

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
            for j in z:
                if (j in x) and (j in y):
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
        count = 0
        while count <= 100:
            for i in range(pre_extend,extend):
                w.append(r[0]*i)
                x.append(r[1]*i)
                y.append(r[2]*i)
                z.append(r[3]*i)
            for j in z:
                if (j in w) and (j in x) and (j in y):
                    return j
            count += 1
            if count == 100:
                return 'Error occured'
            print(w,x,y,z)
            pre_extend = extend
            extend = extend+5

    elif len(r) == 5:
        v = []
        w = []
        x = []
        y = []
        z = []
        pre_extend = 1
        extend = 5
        while True:
            for i in range(pre_extend,extend):
                v.append(r[0]*i)
                w.append(r[1]*i)
                x.append(r[2]*i)
                y.append(r[3]*i)
                z.append(r[4]*i)
            for j in z:
                if (j in v) and (j in w) and (j in x) and (j in y):
                    return j
            pre_extend = extend
            extend = extend+5
    else:
        return 'It accepts only 5 values'




# LCM of 45 8 91 6