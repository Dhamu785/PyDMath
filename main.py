from PyDMath import intrest,year
a= year()
c = input()
b = c.split('-')
res = a.find_day(b[0],b[1],b[2])
print(res)