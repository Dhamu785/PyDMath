import math
def ins(x):
    y = x.split('-')
    if y[1].lower() == 'cm':
        return int(y[0])/100
class perimeter:
    pi = 22/7
    def circle(self,r):
        # r = Radius of the circle
        return 2*self.pi*r

    def rectangle(self,l,b):
        # l = Length of the 
        # b = Breath of the Rectangle
        return 2*(l+b)
    
    def square(self,l):
        # Length of the square
        return 4*l

    def triangle(self,a,b,c):
        # Height, Slanting height and base
        return a+b+c
    
    def eq_triangle(self,a):
        # eq_triangle all sides are equal
        return 3*a

    def parallelogram(self,a,b):
        # Breath and Height
        return 2*(a+b)
    
    def trapezium(self,a,b,c,d):
        # Lenth of four different sides
        return a+b+c+d

    def isosceles_triangle(self,a,b):
        # Base and Slanting height 
        A = 2*a
        return A+b

class area:
    pi = 22/7
    def circle(self,r):
        # radius of circle
        return self.pi*(r**2)

    def rectangle(self,w,l):
        # Length and width
        return w*l

    def square(self,a):
        # Length of the sides
        return a**2

    def triangle(self,b,h):
        # Bash and Height
        return (1/2)*(b*h)
    
    def eq_triangle(self,a):
        # Length of all sides
        return (math.sqrt(3)/4)*(a**2)

    def parallelogram(self,b,h):
        # bash and height
        return b*h

    def trapezium(self,a,b,h):
        # opposite sides are equal
        # h = Height
        num = (a+b)/2
        return num*h

    def isosceles_triangle(self,b,h):
        # slanting heights are same 
        # b = Base
        return (b*h)/2
    
    def rhombus(self,d):
        return (1/2)*d*d

class volume:
    pi = 22/7
    def sphere(self,r):
        # r = Radius
        return (4/3)*self.pi*(r**3)

    def cylinder(self,r,h):
        # r = Radius
        # h = Height
        return self.pi*(r**2)*h

    def cube(self,a):
        # a = Length of four sides
        return a**3

    def rectangular_prism(self,l,b,h):
        # l = length
        # b = Base
        # h = Height
        return l*b*h

    def cone(self,r,h):
        # r = Radius
        # h = Height
        return (1/3)*self.pi*(r**2)*h

    def right_rectangular_pyramid(self,l,w,h):
        # l = length 
        # w = width
        # h = height
        return (l*w*h)/3

    def hemi_sphere(self,r):
        # r = Radius of sphere
        return (2/3)*self.pi*(r**3)