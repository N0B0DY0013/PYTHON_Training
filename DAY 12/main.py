import random
from art import logo

EASY = 10
HARD = 5

print(logo)

rand_number = random.randint(1,100)

print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == "easy":
    attempts = EASY
else:
    attempts = HARD

guessed = False

while attempts > 0 and guessed == False:
    print(f"You have {attempts} remaining to guess the number.")
    guessed_number = int(input(f"make a guess: "))
    
    if guessed_number == rand_number:
        guessed = True
    else:
        attempts -= 1
        if guessed_number > rand_number:
            print("Too high. \nGuess again.\n")
        else:
            print("Too low. \nGuess again.\n")

if guessed:
    print(f"You got it! The answer is {guessed_number}.")
else:
    print(f"You've run out of guesses. The answer is {rand_number}. You lose.")