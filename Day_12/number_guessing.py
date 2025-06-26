import random
import os

def guess():
    print("Welcome to the Number Guessing Game")
    print("I'm thinking of a number between 1 and 100")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if difficulty == 'easy':
        attempts = 10
    else:
        attempts = 5

    number = random.randint(1, 100)

    while attempts > 0:
        guess = int(input("Make a guess: "))

        if guess > number:
            print("Too high.")
            attempts -= 1
            if attempts > 0:
                print(f"You have {attempts} attempts remaining to guess the number.")
        elif guess < number:
            print("Too low.")
            attempts -= 1
            if attempts > 0:
                print(f"You have {attempts} attempts remaining to guess the number.")
        else:
            print(f"You got it! The answer was {number}.")
            break

    if attempts == 0:
        print(f"You've run out of guesses, you lose. The number was {number}.")

# Main game loop
while True:
    guess()
    play_again = input("\nDo you want to play again? Type 'y' or 'n': ")
    if play_again.lower() != 'y':
        break
    # Clear the console
    os.system('cls' if os.name == 'nt' else 'clear')



