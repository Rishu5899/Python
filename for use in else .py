e = int(input("Enter your number"))
for a in  range(1,11):
    print(e,"*",a,"=",a*e)
    if e == 2:
        break   
else:
    print("You didn't input the integer")


q  = int(input("Enter your number"))   
while q<=20:
    q = q * 2 
    print(q)
    if q == 20:
        print("stop")
        break
else:
    print("no number")
