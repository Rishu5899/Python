def find_hcf(x, y):
    while y:
        x, y = y, x % y
    return x

def find_lcm(x, y):
    hcf = find_hcf(x, y)
    return (x * y) // hcf

# Input from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

hcf = find_hcf(num1, num2)
lcm = find_lcm(num1, num2)

print("HCF of", num1, "and", num2, "is:", hcf)
print("LCM of", num1, "and", num2, "is:", lcm)

def find_hcf(x, y):  # x and y are the two numbers whose HCF we want
    while y != 0:
        x, y = y, x % y  # Euclidean algorithm
    return x

# Take one number from user
num = int(input("Enter a number: "))

# Fixed second number to find HCF with
fixed = 100

# Call the function with num and fixed
hcf = find_hcf(num, fixed)

print("The HCF of", num, "and", fixed, "is", hcf)
