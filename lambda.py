def appl(fx,value):
    return 6 + fx(value)

double = lambda x: x * 2
cube = lambda x: x * x * x
avgy = lambda  e,r,s:(e+r+s)/3
print(double(5))
print(cube(5))
print(avgy(14,57,15))
print(appl(lambda x: x * 6,7))