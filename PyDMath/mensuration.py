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
        
    def error_finder_four(self,valA,valB,valC,valD):
        if (isinstance(valA,int) or isinstance(valA,float)) and (isinstance(valB,int) or isinstance(valB,float)) and (isinstance(valC,int) or isinstance(valC,float)):
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
            return f'Error at value1 = {valA}, Error at value2 = {valB}, Error at value3 = {valC}, Error at value4 = {valD}'

    def error_finder_two(self,valA,valB):
        if isinstance(valA,int) or isinstance(valA,float):
            return f'Error ar value2 = {valB}'
        elif isinstance(valB,int) or isinstance(valB,float):
            return f'Error at value1 = {valA}'
        else:
            return f'Value1 = {valA}, value2 = {valB}'

    def error_finder_three(self,valA,valB,valC):
        if (isinstance(valA,int) or isinstance(valA,float)) and (isinstance(valB,int) or isinstance(valB,float)):
            return f'Error ar value3 = {valC}'
        elif (isinstance(valB,int) or isinstance(valB,float)) and (isinstance(valC,int) or isinstance(valC,float)):
            return f'Error at value1 = {valA}'
        elif (isinstance(valA,int) or isinstance(valA,float)) and (isinstance(valC,int) or isinstance(valC,float)):
            return f'Error ar value3 = {valB}'
        elif isinstance(valA,int) or isinstance(valA,float):
            return f'Error at value2 = {valB}, Error at value3 = {valC}'
        elif isinstance(valB,int) or isinstance(valB,float):
            return f'Error at value1 = {valA}, Error at value3 = {valC}'
        elif isinstance(valC,int) or isinstance(valC,float):
            return f'Error at value1 = {valA}, Error at value2 = {valB}'
        else:
                return f'Value1 = {valA}, value2 = {valB}, value3 = {valC}'

class perimeter(validation):
    pi = 22/7
    def circle(self,r=0):
        # r = Radius of the circle
        if r != 0:
            R = self.splitting(r)
            val1 = self.checking(R)
            if isinstance(val1,int) or isinstance(val1,float):
                return f'{2*self.pi*val1} meters'
            else:
                return val1
        else:
            return 'It requires one value and not equal to zero'
        

    def rectangle(self,l=0,b=0):
        # l = Length of the 
        # b = Breath of the Rectangle
        if l != 0 and b != 0:
            L = self.splitting(l)
            valL = self.checking(L)
            B = self.splitting(b)
            valB = self.checking(B)
            if (isinstance(valL,int) or isinstance(valL,float)) and (isinstance(valB,int) or isinstance(valB,float)):
                return f'{2*(valL+valB)} meters'
            else:
                result = self.error_finder_two(valL,valB)
                return result
        else:
            return 'It requires two values and not equal to zero'

    
    def square(self,l=0):
        # Length of the square
        if l != 0:
            L = self.splitting(l)
            valL = self.checking(L)
            if isinstance(valL,int) or isinstance(valL,float):
                return f'{4*valL} meters'
            else:
                return valL
        else:
            return 'It requires one value and not equal to zero'


    def triangle(self,a=0,b=0,c=0):
        # Height, Slanting height and base
        if a != 0 and b != 0 and c != 0:
            A = self.splitting(a)
            valA = self.checking(A)
            B = self.splitting(b)
            valB = self.checking(B)
            C = self.splitting(c)
            valC = self.checking(C)
            if (isinstance(valA,int) or isinstance(valA,float)) and (isinstance(valB,int) or isinstance(valB,float)) and (isinstance(valC,int) or isinstance(valC,float)):
                return f'{valA+valB+valC} meters'
            else:
                result = self.error_finder_three(valA,valB,valC)
                return result
        else:
            return 'It requires three values and not equal to zero'

    
    def eq_triangle(self,a=0):
        # eq_triangle all sides are equal
        if a != 0 :
            A = self.splitting(a)
            valA = self.checking(A)
            if isinstance(valA,int) or isinstance(valA,float):
                return f'{2*valA} meters'
            else:
                return valA
        else:
            return 'It requires one value and not equal to zero'

    def parallelogram(self,a=0,b=0):
        # Breath and Height
        if a != 0 and b != 0:
            A = self.splitting(a)
            valA = self.checking(A)
            B = self.splitting(b)
            valB = self.checking(B)
            if (isinstance(valA,int) or isinstance(valA,float)) and (isinstance(valB,int) or isinstance(valB,float)):
                return f'{2*(valA+valB)} meters'
            else:
                result = self.error_finder_two(valA,valB)
                return result
        else:
            return 'It requires two values and not equal to zero'

    
    def trapezium(self,a=0,b=0,c=0,d=0):
        # Lenth of four different sides
        if a != 0 and b != 0 and c != 0 and d != 0:
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
            else:
                result = self.error_finder_four(valA,valB,valC,valD)
                return result
        else:
            return 'It requires four values and not equal to zero'

    def isosceles_triangle(self,a=0,b=0):
        # Base and Slanting height 
        if a != 0 and b != 0:
            A = self.splitting(a)
            valA = self.checking(A)
            B = self.splitting(b)
            valB = self.checking(B)
            if (isinstance(valA,int) or isinstance(valA,float)) and (isinstance(valB,int) or isinstance(valB,float)):
                return f'{(2*valA)+valB} meters'
            else:
                result = self.error_finder_two(valA,valB)
                return result
        else:
            return 'It requires two values and not equal to zero'


class area(validation):
    pi = 22/7
    def circle(self,r=0):
        # radius of circle
        if r != 0:
            R = self.splitting(r)
            valR = self.checking(R)
            if isinstance(valR,int) and (isinstance(valR,float)):
                return f'{self.pi*(valR**2)} meters'
            else:
                return valR
        else:
            return 'It requires one value and not equal to zero'

    def rectangle(self,w=0,l=0):
        # Length and width
        if w != 0 and l != 0:
            W = self.splitting(w)
            valW = self.checking(W)
            L = self.splitting(l)
            valL = self.checking(L)
            if (isinstance(valW,int) or isinstance(valW,float)) and (isinstance(valL,int) or isinstance(valL,float)):
                return f'{valW*valL} meters'
            else:
                result = self.error_finder_two(valW,valL)
                return result
        else:
            return 'It requires two values and not equal to zero'

    def square(self,a=0):
        # Length of the sides
        if a != 0:
            A = self.splitting(a)
            valA = self.checking(A)
            if isinstance(valA,int) and (isinstance(valA,float)):
                return f'{valA**2} meters'
            else:
                return valA
        else:
            return 'It requires one value and not equal to zero'

    def triangle(self,b=0,h=0):
        # Bash and Height
        if b != 0 and h != 0:
            B = self.splitting(b)
            valB = self.checking(B)
            H = self.splitting(h)
            valH = self.checking(H)
            if (isinstance(valB,int) or isinstance(valB,float)) and (isinstance(valH,int) or isinstance(valH,float)):
                return f'{(1/2)*(valB*valH)} meters'
            else:
                result = self.error_finder_two(valB,valH)
                return result
        else:
            return 'It requires two values and not equal to zero'
            
    
    def eq_triangle(self,a=0):
        # Length of all sides
        if a != 0:
            A = self.splitting(a)
            valA = self.checking(A)
            if isinstance(valA,int) or isinstance(valA,float):
                return f'{(math.sqrt(3)/4)*(valA**2)} meters'
            else:
                return valA
        else:
            return 'It requires one value and not equal to zero'

    def parallelogram(self,b=0,h=0):
        # bash and height
        if b != 0 and h != 0:
            B = self.splitting(b)
            valB = self.checking(B)
            H = self.splitting(h)
            valH = self.checking(H)
            if (isinstance(valB,int) or isinstance(valB,float)) and (isinstance(valH,int) or isinstance(valH,float)):
                return f'{valB*valH} meters'
            else:
                result = self.error_finder_two(valB,valH)
                return result
        else:
            return 'It requires two values and not equal to zero'

    def trapezium(self,a=0,b=0,h=0):
        # opposite sides are equal
        # h = Height
        if a != 0 and b != 0 and h != 0:
            A = self.splitting(a)
            valA = self.checking(A)
            B = self.splitting(b)
            valB = self.checking(B)
            H = self.splitting(h)
            valH = self.checking(H)
            if (isinstance(valA,int) or isinstance(valA,float)) and (isinstance(valB,int) or isinstance(valB,float) and isinstance(valH,int) or isinstance(valH,float)):
                num = (valA+valB)/2
                return f'{num*valH} meters'
            else:
                result = self.error_finder_three(valA,valB,valH)
                return result
        else:
            return 'It requires three values and not equal to zero'

    def isosceles_triangle(self,b=0,h=0):
        # slanting heights are same 
        # b = Base
        if b != 0 and h != 0:
            B = self.splitting(b)
            valB = self.checking(B)
            H = self.splitting(h)
            valH = self.checking(H)
            if (isinstance(valB,int) or isinstance(valB,float)) and (isinstance(valH,int) or isinstance(valH,float)):
                return f'{(valB*valH)/2} meters'
            else:
                result = self.error_finder_two(valB,valH)
                return result
        else:
            return 'It requires two values and not equal to zero'

    
    def rhombus(self,d=0):
        if d != 0:
            D = self.splitting(d)
            valD = self.checking(D)
            if isinstance(valD,int) or isinstance(valD,float):
                return f'{(1/2)*valD*valD} meters'
            else:
                return valD
        else:
            return 'It requires one value and not equal to zero'

class volume(validation):
    pi = 22/7
    def sphere(self,r=0):
        # r = Radius
        if r != 0:
            R = self.splitting(r)
            valR = self.checking(R)
            if isinstance(valR,int) or isinstance(valR,float):
                return (4/3)*self.pi*(valR**3)
            else:
                return valR
        else:
            return 'It requires one value and not equal to zero'

    def cylinder(self,r=0,h=0):
        # r = Radius
        # h = Height
        if r != 0 and h != 0:
            R = self.splitting(r)
            valR = self.checking(R)
            H = self.splitting(h)
            valH = self.checking(H)
            if (isinstance(valH,int) or isinstance(valH,float)) and (isinstance(valR,int) or isinstance(valR,float)):
                return f'{self.pi*(valR**2)*valH} meters'
            else:
                result = self.error_finder_two(valR,valH)
                return result
        else:
            return 'It requires two values and not equal to zero'

    def cube(self,a=0):
        # a = Length of four sides
        if a != 0:
            A = self.splitting(a)
            valA = self.checking(A)
            if isinstance(valA,int) or isinstance(valA,float):
                return f'{valA**3} meters'
            else:
                return valA
        else:
            return 'It requires one value and not equal to zero'

    def rectangular_prism(self,l=0,b=0,h=0):
        # l = length
        # b = Base
        # h = Height
        if l != 0 and b != 0 and h != 0:
            L = self.splitting(l)
            valL = self.checking(L)
            B = self.splitting(b)
            valB  = self.checking(B)
            H = self.splitting(h)
            valH = self.checking(H)
            if (isinstance(valL,int) or isinstance(valL,float)) and (isinstance(valB,int) or isinstance(valB,float)) and (isinstance(valH,int) or isinstance(valH,float)):
                return f'{valL*valB*valH} meters'
            else:
                result = self.error_finder_three(valL,valB,valH)
                return result
        else:
            return 'It requires three values and not equal to zero'


    def cone(self,r=0,h=0):
        # r = Radius
        # h = Height
        if h != 0 and r != 0:
            R = self.splitting(r)
            valR = self.checking(R)
            H = self.splitting(h)
            valH = self.checking(H)
            if (isinstance(valR,int) or isinstance(valR,float)) and (isinstance(valH,int) or isinstance(valH,float)):        
                return f'{(1/3)*self.pi*(valR**2)*valH} meters'
            else:
                result = self.error_finder_two(valR,valH)
                return result
        else:
            return 'It requires two values and not equal to zero'


    def right_rectangular_pyramid(self,l=0,w=0,h=0):
        # l = length 
        # w = width
        # h = height
        if l != 0 and w != 0 and h != 0:
            L = self.splitting(l)
            valL = self.checking(L)
            W = self.splitting(w)
            valW = self.checking(W)
            H = self.splitting(h)
            valH = self.checking(H)
            if (isinstance(valL,int) or isinstance(valL,float)) and (isinstance(valW,int) or isinstance(valW,float)) and (isinstance(valH,int) or isinstance(valH,float)):
                return f'{(valL*valW*valH)/3} meters'
            else:
                result = self.error_finder_three(valL,valW,valH)
                return result
        else:
            return 'It requires three values and not equal to zero'


    def hemi_sphere(self,r=0):
        # r = Radius of sphere
        if r != 0:
            R = self.splitting(r)
            valR = self.checking(R)
            if isinstance(valR,int) or isinstance(valR,float):
                return f'{(2/3)*self.pi*(valR**3)} meters'
            else:
                return valR
        else:
            return 'It requires one value and not equal to zero'
