class year:
    def cvt_int(self,yr):
        try:
            return int(yr)
        except:
            return 'Hey Buddy, Please enter a year..!'
    def leap_year(self,a):
        y = self.cvt_int(a)
        if isinstance(y,int):
            if y%100 == 0:
                if y%400 == 0:
                    return 'Leap year'
                else:
                    return 'Not a leap year'
            else:
                if y%4 == 0:
                    return 'Leap year'
                else:
                    return 'Not a leap year'
        else:
            return y
    
    def year(self,y):
        year = int(y) - int(y[2:])
        yr = None
        if str(year/400)[-2:] == '25':
            yr = 5
        elif str(year/400)[-2:] == '.5':
            yr = 3
        elif str(year/400)[-2:] == '75':
            yr = 1
        elif str(year/400)[-2:] == '.0':
            yr = 0
        else:
            yr = 'Error'
        return yr

    def find_day(self,date,month,year):
        yr = self.year(year)
        return yr