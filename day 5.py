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
