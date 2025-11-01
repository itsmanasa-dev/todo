import random

secret_number = random.randint(1, 100)
attempts=3

print("I am thinking of number between 1 and 100.")

while attempts > 0:
    guess = int(input("Make a guess: "))
    if guess < secret_number:
        print("Too low.")
    elif guess > secret_number:
        print("Too high.")
    else:
        print(f"Congratulations! You've guessed the number {secret_number} correctly!")
    attempts-= 1
    
    if attempts > 0 and guess != secret_number:
        print(f"You have {attempts} attempts remaining. Try again.")
    elif attempts == 0 and guess != secret_number:
        print(f"Sorry, you've run out of attempts. The number was {secret_number}.")