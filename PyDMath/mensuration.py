import math

class validation:
    def splitting(self,x):
        y = x.split('-')
        try:
            int(y[0])
        except Exception:
            return 'Type Error'
        if len(y) == 2:
            if y[1].lower() == 'cm' or y[1].lower() == 'cms':
                return int(y[0])/100
            elif y[1].lower() == 'm':
                return int(y[0])
            elif y[1].lower() == 'km' or y[1].lower() == 'kms':
                return int(y[0])*1000
            elif y[1].lower() == 'mm':
                return int(y[0])/1000
            else:
                return 'Unit Invalid'
        elif len(y) < 2:
            return 'one bar'
        else:
            return '"-" Error'


    def checking(self,val):
        try:
                if val == '"-" Error':
                    return 'Only one "-" allowed'
                elif val == 'Type Error':
                    return 'It accepts only the integer at first'
                elif val == 'Unit Invalid':
                    return 'Invalid Unit'
                elif val == 'one bar':
                    return 'Please specify value and unit seperated by "-". Eg:3-cm'
                elif isinstance(val,int) or isinstance(val,float):
                    return val
                else:
                    return 'Something went wrong'
        except Exception:
                return Exception

class perimeter(validation):
    pi = 22/7
    def circle(self,r):
        # r = Radius of the circle
        R = self.splitting(r)
        val1 = self.checking(R)
        if isinstance(val1,int) or isinstance(val1,float):
            return f'{2*self.pi*val1} meters'
        else:
            return val1
        

    def rectangle(self,l,b):
        # l = Length of the 
        # b = Breath of the Rectangle
        L = self.splitting(l)
        valL = self.checking(L)
        B = self.splitting(b)
        valB = self.checking(B)
        if (isinstance(valL,int) or isinstance(valL,float)) and (isinstance(valB,int) or isinstance(valB,float)):
            return f'{2*(valL+valB)} meters'
        elif isinstance(valL,int) or isinstance(valL,float):
            return f'Error ar value2 = {valB}'
        elif isinstance(valB,int) or isinstance(valB,float):
            return f'Error at value1 = {valL}'
        else:
            return f'Value1 = {valL}, value2 = {valB}'
    
    def square(self,l):
        # Length of the square
        L = self.splitting(l)
        valL = self.checking(L)
        if isinstance(valL,int) or isinstance(valL,float):
            return f'{4*valL} meters'
        else:
            return valL

    def triangle(self,a,b,c):
        # Height, Slanting height and base
        A = self.splitting(a)
        valA = self.checking(A)
        B = self.splitting(b)
        valB = self.checking(B)
        C = self.splitting(c)
        valC = self.checking(C)
        if (isinstance(valA,int) or isinstance(valA,float)) and (isinstance(valB,int) or isinstance(valB,float)) and (isinstance(valC,int) or isinstance(valC,float)):
            return f'{valA+valB+valC} meters'
        elif (isinstance(valA,int) or isinstance(valA,float)) and (isinstance(valB,int) or isinstance(valB,float)):
            return f'Error ar value3 = {valC}'
        elif (isinstance(valB,int) or isinstance(valB,float)) and (isinstance(valC,int) or isinstance(valC,float)):
            return f'Error at value1 = {valA}'
        elif (isinstance(valA,int) or isinstance(valA,float)) and (isinstance(valC,int) or isinstance(valC,float)):
            return f'Error ar value3 = {valB}'
        else:
            return f'Value1 = {valA}, value2 = {valB}, value3 = {valC}'
    
    def eq_triangle(self,a):
        # eq_triangle all sides are equal
        A = self.splitting(a)
        valA = self.checking(A)
        if isinstance(valA,int) or isinstance(valA,float):
            return f'{2*valA} meters'
        else:
            return valA

    def parallelogram(self,a,b):
        # Breath and Height
        A = self.splitting(a)
        valA = self.checking(A)
        B = self.splitting(b)
        valB = self.checking(B)
        if (isinstance(valA,int) or isinstance(valA,float)) and (isinstance(valB,int) or isinstance(valB,float)):
            return f'{2*(valA+valB)} meters'
        elif isinstance(valA,int) or isinstance(valA,float):
            return f'Error ar value2 = {valB}'
        elif isinstance(valB,int) or isinstance(valB,float):
            return f'Error at value1 = {valA}'
        else:
            return f'Value1 = {valA}, value2 = {valB}'
    
    def trapezium(self,a,b,c,d):
        # Lenth of four different sides
        A = self.splitting(a)
        valA = self.checking(A)
        B = self.splitting(b)
        valB = self.checking(B)
        C = self.splitting(c)
        valC = self.checking(C)
        D = self.splitting(d)
        valD = self.checking(D)
        if (isinstance(valA,int) or isinstance(valA,float)) and (isinstance(valB,int) or isinstance(valB,float)) and (isinstance(valC,int) or isinstance(valC,float)) and (isinstance(valD,int) or isinstance(valD,float)):
            return f'{valA+valB+valC+valD} meters'

        elif (isinstance(valA,int) or isinstance(valA,float)) and (isinstance(valB,int) or isinstance(valB,float)) and (isinstance(valC,int) or isinstance(valC,float)):
            return f'Error at value4 = {valD}'
        elif (isinstance(valB,int) or isinstance(valB,float)) and (isinstance(valA,int) or isinstance(valA,float)) and (isinstance(valD,int) or isinstance(valD,float)):
            return f'Error ar value3 = {valC}'
        elif (isinstance(valA,int) or isinstance(valA,float)) and (isinstance(valC,int) or isinstance(valC,float)) and (isinstance(valD,int) or isinstance(valD,float)):
            return f'Error ar value2 = {valB}'
        elif (isinstance(valB,int) or isinstance(valB,float)) and (isinstance(valC,int) or isinstance(valC,float)) and (isinstance(valD,int) or isinstance(valD,float)):
            return f'Error at value1 = {valA}'
        
        elif (isinstance(valA,int) or isinstance(valA,float)) and (isinstance(valB,int) or isinstance(valB,float)):
            return f'Error at value3 = {valC}, Error at value4 = {valD}'
        elif (isinstance(valA,int) or isinstance(valA,float)) and (isinstance(valC,int) or isinstance(valC,float)):
            return f'Error at value2 = {valB}, Error at value4 = {valD}'
        elif (isinstance(valA,int) or isinstance(valA,float)) and (isinstance(valD,int) or isinstance(valD,float)):
            return f'Error at value2 = {valB}, Error at value3 = {valC}'
        elif (isinstance(valB,int) or isinstance(valB,float)) and (isinstance(valC,int) or isinstance(valC,float)):
            return f'Error at value1 = {valA}, Error at value4 = {valD}'
        elif (isinstance(valB,int) or isinstance(valB,float)) and (isinstance(valD,int) or isinstance(valD,float)):
            return f'Error at value1 = {valA}, Error at value3 = {valC}'
        elif (isinstance(valC,int) or isinstance(valC,float)) and (isinstance(valD,int) or isinstance(valD,float)):
            return f'Error at value1 = {valA}, Error at value2 = {valB}'
            
        elif (isinstance(valA,int) or isinstance(valA,float)):
            return f'Error at value2 = {valB}, Error at value3 = {valC}, Error at value4 = {valD}'
        elif (isinstance(valB,int) or isinstance(valB,float)):
            return f'Error at value1 = {valA}, Error at value3 = {valC}, Error at value4 = {valD}'
        elif (isinstance(valC,int) or isinstance(valC,float)):
            return f'Error at value1 = {valA}, Error at value2 = {valB}, Error at value4 = {valD}'
        elif (isinstance(valD,int) or isinstance(valD,float)):
            return f'Error at value1 = {valA}, Error at value2 = {valB}, Error at value3 = {valC}'
        else:
            return f'Value1 = {valA}, value2 = {valB}, value3 = {valC}, value4 = {valD}'

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