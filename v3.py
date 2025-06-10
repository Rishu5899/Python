#WAP to find particular string using simple for loop and simple if condition.
Fruit = ["Apple","Banana","Pineapple","Chickoo"]
print(Fruit)
search_string = str(input("Enter your string"))
print(search_string)
for n in Fruit:
 if search_string in Fruit:
    print("yes")
    break
else:
    print("no")