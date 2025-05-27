#Write a program to calculate grades based on percentage using if-else ladder6


percentage = int(input("Write Your Percentage = "))

if (percentage <= 100 and percentage >= 90):
         print("Grade A+")
elif(percentage <= 89 and percentage >= 71):
          print("Grade A")
elif(percentage <= 70 and percentage >= 61):
        print("Grade B+")
elif(percentage <= 60 and percentage >= 51):
        print("Grade B")
elif(percentage <= 50 ):
        print("Grade C")
