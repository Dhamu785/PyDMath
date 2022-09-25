# import PyDMath
# a = PyDMath.perimeter()
# x = input()
# # y = input()
# # z = input()
# print(a.circle(x))


import math
def lcm2(li):
    prime_no = [2,3,5,7,11,13,17,19,23,29,31,37,41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    prime_factors = []
    while li[0] > 1.0 or li[1] > 1.0:
        for i in prime_no:
            count = 0
            if li[0]%i == 0:
                li[0] = li[0]/i
                count += 1
            if li[1]%i == 0:
                li[1] = li[1]/i
                count += 1
            if count >= 1:
                prime_factors.append(i)
                break
    print(math.prod(prime_factors))

def lcm3(li):
    prime_no = [2,3,5,7,11,13,17,19,23,29,31,37,41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    prime_factors = []
    while li[0] > 1.0 or li[1] > 1.0 or li[2] > 1:
        for i in prime_no:
            count = 0
            if li[0]%i == 0:
                li[0] = li[0]/i
                count += 1
            if li[1]%i == 0:
                li[1] = li[1]/i
                count += 1
            if li[2]%i == 0:
                li[2] = li[2]/i
                count += 1
            if count >= 1:
                prime_factors.append(i)
                break
    print(math.prod(prime_factors))
lcm3([15,17,89])