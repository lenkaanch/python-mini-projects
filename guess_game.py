import random

secret_number = random.randint(1, 10)
print("Guess the number between 1 and 10")
guess = int(input("Enter your guess: "))
if guess == secret_number:
    print("Correct!")
else:
    print("Wrong!")
# Simple guessing game
# User tries to guess a random number
