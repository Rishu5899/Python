# Program to find the largest number in a list

numbers = [12, 45, 78, 34, 89, 23, 67]

# Assume the first number is the largest
largest = numbers[0]

# Loop through the list
for num in numbers:
    if num > largest:
        largest = num

print("The largest number is:", largest)
