# class Menu:
#     use = "Isha is dentist"
#     name = "Dhrumil" # Class attr
#     def __init__(self,name,age,write,mobileno,use):
#         self.name = name #  Oject attr , Object attribuite > class attribute
#         self.age = age
#         self.write = write
#         self.mobileno = mobileno 
    


# c = Menu("Rishu age is",21,"and mobile no is",9023696890,"Python Developer")

# print(c.name,c.age,c.write,c.mobileno)


for q in range(1,100,2):
   print(q*q)

# total = 0 
# for w in range(1,101):
#    total += w
# print(total)

total = 0
for i in range(1, 101):
    total += i
print(total)

class Tution:
 def __init__(self,Name,Fees,Yearly):
     self.Name = Name
     self.Fees = Fees
     self.Yearly = Yearly
 def welcome(self):
   print("Welcome all Students")

 def get_Name(self):
    return self.Name   
Name=int(input("Enter the number "))
Fees=int(input("Enter the number "))
Yearly=Name+Fees

  

s = Tution(Name,Fees,Yearly)
print(s.Name,s.Fees,s.Yearly)

s.welcome()
print(s.Name)
