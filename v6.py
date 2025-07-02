# Q: Write a Python program that asks the user to enter a number from a list and displays the square of that number.
no = [1,2,3,4,5,6,7,8,9,10,11,12]
print(no)
try:
 f = int(input("Enter the number from the list"))
 if f in no: 
  for j in range(1):   
    print(f*f)
except ValueError:
  print("You didn't enter the integer")

