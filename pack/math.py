class perimeter:
    pi = 22/7
    def circle(self,r):
        return 2*self.pi*r

    def rectangle(self,l,b):
        return 2*(l+b)
    
    def square(self,l):
        return 4*l

    def triangle(self,a,b,c):
        return a+b+c
    
    def eq_triangle(self,a):
        return 3*a

    def parallelogram(self,a,b):
        return 2*(a+b)
    
    def trapezium(self,a,b,c,d):
        return a+b+c+d

    def isosceles_triangle(self,a,b):
        A = 2*a
        return A+b

class area:
    pi = 22/7
    def circle(self,r):
        return self.pi*(r**2)