# s = int(input("Enter the number of the table"))
# for a in range(11):
#     print(s,  "*",a,"=",s*a )
# a = 12
# print(a*a)
# def cube(x):
#     return x+2
# print (cube(4))
# def x(cube):
#     return cube * cube * cube 
# print(x(int(input("Enter the number")) ))
# def cube(x):
#     return x * x * x
# print(cube(4))
# li = [14,12,5,8,7]
# newa = list(map(lambda x: x * x,li))
# print(newa)
# fd = lambda x: x / 2
# print(fd(5))
# def Filter_Function(numb):
#     return numb>2
# da = list(filter(Filter_Function,li))
# print(da)
from functools import reduce
# List of numbers
numbers = [1,5,6,14,25]
sum = reduce(lambda x, y: x + y, numbers)
print(sum)