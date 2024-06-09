# class divisor:
#     @staticmethod
#     def cvt_lst(n):
#         li = []
#         for i in n:
#             try:
#                 li.append(int(i))
#             except:
#                 return 'All inputs must be a number'
#         return li

#     def div(self,n):
#         cvted_lst = self.cvt_lst(n)
#         if isinstance(cvted_lst,list):
#             if cvted_lst[-1]%2 == 0:
#                 return 'The number is divided by 2'
#             elif sum(cvted_lst) % 3 == 0:
#                 return 'The number is divided by 3'
#             elif int(str(cvted_lst[-2]) + str(cvted_lst[-1])) % 4 == 0:
#                 return 'The number is divided by 4'
#             elif (cvted_lst[-1] == 0) or (cvted_lst[-1] == 5):
#                 return 'The number is divided by 5'
#             elif (cvted_lst[-1]%2 == 0) and (sum(cvted_lst) % 3 == 0):
#                 return 'The number is divided by 6'
#             elif int(str(cvted_lst[-3]) + str(cvted_lst[-2]) + str(cvted_lst[-1])) % 8 == 0:
#                 return 'The number is divided by 8'
#             elif sum(cvted_lst) % 9 == 0:
#                 return 'The number is divided by 9'
#             elif cvted_lst[-1] == 0:
#                 return 'The number is divided by 10'
#             else:
#                 return 'Null'
#         else:
#             return cvted_lst