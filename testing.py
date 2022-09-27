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
    if len(li) == 2:
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
        return math.prod(prime_factors)

    if len(li) == 3:
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
        return math.prod(prime_factors)

    if len(li) == 4:
        while li[0] > 1.0 or li[1] > 1.0 or li[2] > 1 or li[3] > 1:
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
                if li[3]%i == 0:
                    li[3] = li[3]/i
                    count += 1
                if count >= 1:
                    prime_factors.append(i)
                    break
        return math.prod(prime_factors)

    if len(li) == 5:
        while li[0] > 1.0 or li[1] > 1.0 or li[2] > 1 or li[3] > 1 or li[4] > 1:
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
                if li[3]%i == 0:
                    li[3] = li[3]/i
                    count += 1
                if li[4]%i == 0:
                    li[4] = li[4]/i
                    count += 1
                if count >= 1:
                    prime_factors.append(i)
                    break
        return math.prod(prime_factors)

print(lcm2([45,8,25,81,111]))