import math
def fact(n):
    ans = 1
    for i in range(1,n+1):
        ans = ans * i
    return ans

class permutation:
    def per(self,n,r):
        if r < n:
            return fact(n)/fact(n-r)
        elif n == r:
            return fact(n)
        elif r == 1:
            return n 
        else:
            print('Value Error')

class combination:
    def comb(self,n,r):
        return fact(n)/(fact(r)*fact(n-r))