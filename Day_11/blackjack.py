import random as rdm
import os

# ASCII art logo for the game
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \\/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \\  /|K /\\  |     | '_ \\| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \\/ | /  \\ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \\  / |     |_.__/|_|\\__,_|\\___|_|\\_\\ |\\__,_|\\___|_|\\_\\
      |  \\/ K|                            _/ |                
      `------'                           |__/           
"""

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_cards = []
computer_cards = []


def deal_card():
    """
    Draw a random card from the deck.

    Returns:
        int: The value of the drawn card.
    """
    return rdm.choice(cards)


def calculate_score(cards):
    """
    Calculate the score of a given list of cards.

    This function sums the values of the cards in the list to calculate the total score.
    It also handles special cases for Blackjack and the Ace card:
    - If the score is 21 with exactly two cards, it returns 0 to indicate a Blackjack.
    - If the score exceeds 21 and there is an Ace (value 11), it converts the Ace to 1
      and recalculates the score to avoid busting.

    Args:
        cards (list of int): The list of card values to calculate the score for.

    Returns:
        int: The calculated score.
    """
    score = sum(cards)

    if score == 21 and len(cards) == 2:
        return 0

    if score > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
        score = sum(cards)

    return score


def compare(user_score, computer_score):
    """
    Compare the user's score and the computer's score to determine the game outcome.

    Args:
        user_score (int): The score of the user.
        computer_score (int): The score of the computer.

    Returns:
        str: A message indicating the result of the game.
    """
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack! 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def play_game():
    """
    Play a game of Blackjack.

    This function initiates and manages the flow of a single game of Blackjack.
    It handles dealing cards to the user and the computer, calculating scores,
    and determining the winner based on the rules of Blackjack. The game continues
    until the user decides to stop playing.

    The function also displays the current status of the game, including the user's
    and computer's cards and scores, and prompts the user for input to continue
    drawing cards or to pass.
    """
    print(logo)

    # Clear previous cards
    user_cards.clear()
    computer_cards.clear()

    # Deal initial cards
    user_cards.extend([deal_card(), deal_card()])
    computer_cards.extend([deal_card(), deal_card()])

    game_over = False

    # User's turn
    while not game_over:
        # Calculate scores
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        # Display current status
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        # Check for game ending conditions
        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            # Ask user if they want to draw another card
            should_continue = input("Type 'y' to get another card, type 'n' to pass: ")
            if should_continue.lower() == 'y':
                user_cards.append(deal_card())
            else:
                game_over = True

    # Computer's turn - only if user didn't go over 21
    if user_score <= 21:
        while computer_score < 17 and computer_score != 0:
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)

    # Show final hands
    print(f"\nYour final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


# Main game loop
while True:
    play_game()
    play_again = input("\nDo you want to play again? Type 'y' or 'n': ")
    if play_again.lower() != 'y':
        break
    # Clear the console
    os.system('cls' if os.name == 'nt' else 'clear')

