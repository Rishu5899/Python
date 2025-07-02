e = int(input("Enter the number"))
e += int(input("Enter the second number"))
print(e)
q = int(input("Enter the number"))
q -= int(input("Enter the second number"))
print(q)
w = 3
t = 5
print(w!=t)
y = 3
c = 3 
print(y>=c)
# # how IS operator works 
r = ["Rabbit","Rat"]
u = ["Rabbit","Rat"]
i = r
print(i is r)
print(id(r))
print(id(u))
print(id(i))
# Membership Operator
o = ["Eagle","Sparrow"]
print ( "Eagle"  in o)
print("Dad" not in o)

#  Operator Precedence
l = 5
x = 6
b = 12
g = 18
w = (l+x)*b/g   #(5+6*12/18)
print(w)
z = l+(x*b)/g
print(z)
# Write a program to print a string "Hello Python".
print("hello Python")
#  Write a program to store one value in variable and print that variable.
q = "Hello Python"
print(q)
# Write a program to take value from user input and print that value.
x = input("Enter the input")
print(x)
# Write a program to do a sum of two value
r = 54 + 47
print(r)
#  Write a program division using variables
v = 1254
n = 544
h = v/n
print(h)
#  Write a program to print multiple value of variables
p = "Vibrant"
i = "Technology"
print(p, i)
# Write a program to find a type of variable
lf = 2.44
print(type(lf))
# Write a program to take two integer value from the user and check both the values are same.
ew = int(input("Enter the number"))
ve = int(input("Enter the number"))
print(ew == ve)