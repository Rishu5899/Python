# Write a Python program to print "Hello" using a string.
a = "Hello"
print(a)

#  Write a Python program to allocate a string to a variable and print it
q = "Rishu"
print(q)

# Write a Python program to print a string using triple quotes.
e = '''AI'''
print(e)

# Write a Python program to access the first character of a string using index value
r = "Electronic"
print(r[0])

# Write a Python program to access the string from the second position onwards using slicing
y = "Watch"
print(y[1:]) 

#  Write a Python program to access a string up to the fifth character
t = "December"
print(t[:5])

# Write a Python program to print the substring between index values 1 and 4.
u = "January"
print(u[1:4])

# Write a Python program to print a string from the last character.
i = "March"
print(i[-1])

# Write a Python program to print every alternate character from the string starting from index 1.
o = "Electronic"
print(o[1:8:2])

# Write a Python program to skip 'banana' in a list using the continue statement. 
# List = ['apple', 'banana', 'mango']
# for x in List:
#     if x =='banana':
#         continue
    # print(x)
#  Write a Python program to stop the loop once 'banana' is found using the break statement.
Listone = ['apple', 'banana', 'mango']
for x in Listone:
    if x =='banana':
        print("Banana Found, You are out of the loop")
        break
    print(x)
