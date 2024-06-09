import numbersD
a = input()
try:
    b = a.split(',')
    print(b)
except:
    print('123')
print(numbersD.lcm(b))