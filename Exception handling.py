# u = input("Enter the number")
# try:
#  for w in range(1,11):
#     print(f"{int(u)}*{w}={int(u)*w}")
# except:
#   print("Invalid Input")

# print("Your Program is done")

try:
  y = int(input("Enter the number"))
  t = [4,8]
  print(t[y])
except ValueError:
  print("You enter wrong input")

except IndexError:
  print("You Entered Wrong Index")