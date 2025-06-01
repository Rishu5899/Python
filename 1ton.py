n = int(input("Enter a positive integer (n): "))

if n <= 0:
    print("Please enter a positive integer.")
else:

    total_sum = 0

    
    for num in range(1, n + 1):
        total_sum += num

   
    print("The sum of natural numbers from 1 to", n, "is:", total_sum)
