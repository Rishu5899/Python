# Write a Python program to check if a person is eligible to donate blood 

age = int(input("Enter your age = "))
weight = float(input("Enter your Weight"))
if age > 18:
    print("you can donate blood")
if weight > 50:
    print("you can donate blood")
else:
    print("you can donate but check your blood percentage")

r = int(input("Enter your number = "))

match r:


     case 100:
        print("Your grade is A+")
     case 70:
        print("Your percentage is B+")
     case _:
        print(r)

     