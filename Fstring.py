price = 57.0999
txt = f"For only {price:.2f} dollars!"
print(txt)
print (type(f"{3*60}"))
print(f"{43*21}")
go = "Rishu"
print (f"{{go}}")

table = int(input("Enter your number for table"))  
for i in range(1,11):
      print(table,"*",i,"=",table*i)



def addition(i,f):
    '''This the code of Addition'''
    print(i+f)

i=9
f=8
addition(i,f)
print(addition.__doc__)