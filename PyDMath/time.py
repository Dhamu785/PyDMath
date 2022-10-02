class year:
    def leap_year(self,y):
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