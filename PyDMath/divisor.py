class divisor:
    @staticmethod
    def cvt_lst(n):
        li = []
        for i in n:
            try:
                li.append(int(i))
            except:
                return 'All inputs must be a number'
        return li

    def div(self,n):
        cvted_lst = self.cvt_lst(n)
        if isinstance(cvted_lst,list):
            if cvted_lst[-1]%2 == 0:
                return 'divided by 2'
            elif sum(cvted_lst) % 3 == 0:
                return 'divided by 3'
            else:
                return 'Null'
        else:
            return cvted_lst

