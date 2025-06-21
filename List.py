# animal = ["Tiger","Lion","Giraffe","Deer","Camel","Ant"]
# Alochol = ["Red Label","Monkey Shoulder","Magic Moment","Jaisalmer","100 Pipers","Teacher's","MC Dowells"]
# print (type(len(animal)))
# print("\n" ,animal)
# print (Alochol[0])
# print (Alochol[-6])
# print (Alochol[len(Alochol)-6])
# print (Alochol[6-6])
# print (Alochol[0])
# print (Alochol[:])
# print (Alochol[0:7:2])
Fruit = ["Apple","Banana","Pineapple","Chickoo"]
for Fruits in range(3):
    s = str(input("Enter your option"))
if "Banana" in Fruit:
    print("yes")
else:
    print("no")

if "Apple" in Fruit:
    print("yes")
else:
    print("no")

if "Pineapple" in Fruit:
    print("yes")
else:
    print("no")

# Same thing applies for strings as well!
if "app" in "Pineapple":
    print("yes")
else:
    print("no")


print ("Range of Bottle is Between 1000 to 5000")
Drink = int(input("Enter Your Budget"))
if (Drink<=2000 and Drink >= 1000):
    print("1.Blender","2.Offical Choice","3.All Season")
else:
 print("You enter out of range amount")
select = int(input("Enter your Choice "))
match select:
    case 1:
         print("1100")
    case 2:
        print("1200")
    case 3:
        print("1500") 
 


     
