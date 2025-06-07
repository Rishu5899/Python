'''number = int(input("Enter your First number"))
numbertwo = int(input("Enter your Second number"))

if (number>1):
    print("Number is BIG",number)
else:
    print("Number is SMALL")'''

year = int(input("Enter your Birth Year: "))

if (year % 4 == 0): 
    print("You were born in a leap year:" ,year)
else:
    print("You were not born in a leap year" ,year)

#and (year % 100 != 0) 
#or (year % 400 == 0):