from PyDMath import intrest,year
a= year()
c = input()
b = c.split('-')
print(a.find_day(b[0],b[1],b[2]))