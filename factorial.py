def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

number = int(input("Enter a number: "))

if number < 0:
    print("Factorial is not defined for negative numbers.")
elif number == 0:
    print("The factorial of 0 is 1.")
else:
    result = factorial(number)
    print("The factorial of", number, "is:", result)
