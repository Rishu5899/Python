s = open('file.txt', 'r')  # Open file in read mode
x = s.read()               # Read contents
print(x)                   # Print contents
s.close()                  # ✅ Properly close the file


