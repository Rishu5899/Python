# Write a program to print the Fibonacci Sequence

n = int(input("Enter the number: ")) 
a, b = 0, 1
sum = 0
for d in range(n):
    print(f"Fibonacci: {a}", end=" ")
    sum += a
    print("sum")
    a, b = b, a + b 
