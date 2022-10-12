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

    def find_day(self,date,month,year):
        year = int(year) - int(year[2:])
        print(year)
        y = None
        if year/100 == 0.25:
            y = 5
        elif year/100 == 0.5:
            y = 3
        elif year/100 == 0.75:
            y = 1
        elif year/100 == 0:
            y = 0
        else:
            y = 'Error'
        return y