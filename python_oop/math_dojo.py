# class MathDojo(object):
#     def __init__(self, num):
#         self.num = num
    
#     def add(self, *num):   
#             self.num += sum(num)
#             return self

#     def subtract(self, *num):
#         self.num -= sum(num)
#         return self

#     def result(self):
#         print self.num
#         return self


# md = MathDojo(0)
# md.add(4).result()


x = [1,2,3]
for i in x:
    temp = sum(i)
    print temp