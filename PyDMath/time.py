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

    def year_diff(self,yrs):
        if int(yrs[2:]) == 0:
            return 0
        else:
            diff = int(yrs[2:])
            leap_yr = 0
            nml_yr = 0
            for i in range(1,diff+1):
                if i%4 == 0:
                    leap_yr += 1
                else:
                    nml_yr += 1
            return leap_yr*2 + nml_yr

    def find_day(self,date,month,year):
        # year calculation
        yr = self.year(str(int(year)-1))

        # year difference
        yrs = self.year_diff(str(int(year)-1))

        # Month calculation
        month_days = [3,1,3,2,3,2,3,3,2,3,2,3]
        if self.leap_year(year) == 'Leap year':
            month_days[1] = 1
        else:
            month_days[1] = 0
        month_total_days = 0
        for i in range(0,int(month)-1):
            month_total_days = month_total_days + month_days[i]

        print('year:',yr)
        print('diff',yrs%7)
        print('month',month_total_days)
        print('day',int(date)%7)

        return yr + (month_total_days%7) + (int(date))%7 + yrs%7