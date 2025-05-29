x = int(input("Enter your First Number"))
y = int(input("Enter your Second Number"))

print("Enter 1 for Addition")
print("Enter 2 for Subtraction")
print("Enter 3 for Multiplication")
print("Enter 4 for Division")



# g = int(input("Enter the option"))
raghu = int(input("Enter Digit only"))

match raghu:

     case 1:
      print(x+y)
     case 2: 
       print(x-y)
     case 3:
      print(x*y)
     case 4:
      print(x//y)
     case _:
      print("nvjitji")