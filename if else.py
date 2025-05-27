a = int(input("Enter the age"))
print("Your age is",a)
print(a<18)
print(a<=18)
print(a>=18)
print(a==18)
if (a>=18):
    print("You are not allowed")
else:
    print("You are child")

fees = int(input("Enter your fees"))
budget = 50000
if (fees <= budget):
    print("The collage is selected")
else:
    print("Collage is Expensive")

#Write a program of elif

fees = int(input("Enter your Collage Fees"))
examfees = int(input("Enter your Examfee"))

if (fees + examfees < 50000):
    #print("Collage is Expensive")
    if (fees + examfees < 10000):
        print("Collage")

elif (fees + examfees > 80000):
    print("Collage is Selected")

else:
    print("Collage is not budgetfriendly")