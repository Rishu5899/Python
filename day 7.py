# Initialize variable to store the largest number
largest = 1

# Loop from 2 to 100 to find the largest number
for num in range(2, 101):
    if num > largest:
        largest = num

# Print the largest number
print("The largest number from 1 to 100 is:", largest)
