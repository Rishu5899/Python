import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 20.")

number_to_guess = random.randint(1, 20)
attempts = 5

while attempts > 0:
    guess = int(input("Take a guess: "))
    
    if guess == number_to_guess:
        print("Congratulations! You guessed it right!")
        break
    elif guess < number_to_guess:
        print("Too low!")
    else:
        print("Too high!")
    
    attempts -= 1
    print(f"Attempts left: {attempts}")

if attempts == 0:
    print(f"Sorry! The number was {number_to_guess}. Better luck next time!")
