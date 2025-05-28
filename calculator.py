x = int(input("Enter your First Number"))
y = int(input("Enter your Second Number"))

a = print("Enter 1 for Addition")
s = print("Enter 2 for Subtraction")
m = print("Enter 3 for Multiplication")
d = print("Enter 4 for Division")



# g = int(input("Enter the option"))
raghu = int(input("Enter Digit only"))

match raghu:

     case 1:
      print(x+y,a,raghu)
     case 2: 
       print(x-y,s,raghu)
     case 3:
      print(x*y,m,raghu)
     case 4:
      print(x//y,d,raghu)
     case _:
      print("nvjitji")