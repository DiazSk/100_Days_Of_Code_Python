import random
from hangman_words import word_list
from hangman_art import logo, stages

print(logo)

chosen_word = random.choice(word_list)
lives = 6

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(f"\nGuess the word: {placeholder}")

end_of_game = False
correct_letters = []

while not end_of_game:

    print(f"\n****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You've already guessed {guess}")

    display = ""

    # Check if the guess is correct and add to correct_letters
    if guess in chosen_word and guess not in correct_letters:
        correct_letters.append(guess)

    for letter in chosen_word:
        if letter == guess:
            display += letter
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(f"Word to guess: {display}")

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f"***********************IT WAS {chosen_word}! YOU LOSE**********************")
            
    if "_" not in display:
        end_of_game = True
        print(f"***********************YOU GUESSED THE WORD! YOU WIN**********************")

    print(stages[lives])
