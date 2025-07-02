# s = open("file.txt", "r")  
# x = s.read()              
# print(x)                   
# s.close()                  
# with open('file.txt', 'r') as s:
#     x = s.read()
#     print(x)
# # No need to call s.close()
s = open('file.txt', 'r')  # Open file in read mode
x = s.read()               # Read contents
print(x)                   # Print contents
s.close()                  # ✅ Properly close the file
