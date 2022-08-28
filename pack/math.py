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