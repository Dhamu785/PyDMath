def fact(n):
    ans = 1
    for i in range(1,n+1):
        ans = ans * i
    return ans

def type_check(a):
    try:
        int(a)
        return 'ok'
    except:
        return 'Type Error'

class permutation:
    def per(self,n='d',r='d'):
        if n != 'd' and r != 'd':
            res1 = type_check(n)
            res2 = type_check(r)
            if res1 == 'ok' and res2 == 'ok':
                if int(n) >= int(r):
                    return fact(n)/fact(n-r)
                else:
                    return '"r" must be less than or equal to "n"'
            elif res1 == 'ok':
                return '"r" accepts numbers only'
            elif res2 == 'ok':
                return '"n" accepts numbers only'
            else:
                return 'Both must be numbers'
        else:
            return 'It requires two values'

class combination:
    def comb(self,n='d',r='d'):
        if n != 'd' and r != 'd':
            res1 = type_check(n)
            res2 = type_check(r)
            if res1 == 'ok' and res2 == 'ok':
                if int(n) >= int(r):
                    return fact(int(n))/(fact(int(r))*fact(int(n)-int(r)))
                else:
                    return '"r" must be less than or equal to "n"'
            elif res1 == 'ok':
                return '"r" accepts numbers only'
            elif res2 == 'ok':
                return '"n" accepts numbers only'
            else:
                return 'Both must be numbers'
        else:
            return 'It requires two values'