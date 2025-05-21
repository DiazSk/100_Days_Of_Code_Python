from deal_card import DealCard
from calculate_score import CalculateScore
from compare import Compare
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

class PlayGame:
    def __init__(self):
        self.deal_card = DealCard()
        self.calculate_score = CalculateScore()
        self.compare = Compare()
        self.user_cards = []
        self.computer_cards = []

    def play_game(self):
        print(logo)

        self.user_cards.clear()
        self.computer_cards.clear()

        # Deal initial cards
        self.user_cards.extend([self.deal_card.deal_card(), self.deal_card.deal_card()])
        self.computer_cards.extend([self.deal_card.deal_card(), self.deal_card.deal_card()])

        game_over = False

        while not game_over:
            user_score = self.calculate_score.calculate_score(self.user_cards)
            computer_score = self.calculate_score.calculate_score(self.computer_cards)

            print(f"Your cards: {self.user_cards}, current score: {user_score}")
            print(f"Computer's first card: {self.computer_cards[0]}")

            if user_score == 0 or computer_score == 0 or user_score > 21:
                game_over = True
            else:
                user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
                if user_should_deal == "y":
                    self.user_cards.append(self.deal_card.deal_card())
                else:
                    game_over = True

        if user_score <= 21:
            while computer_score < 17 and computer_score != 0:
                self.computer_cards.append(self.deal_card.deal_card())
                computer_score = self.calculate_score.calculate_score(self.computer_cards)

        print(f"\nYour final hand: {self.user_cards}, final score: {user_score}")
        print(f"Computer's final hand: {self.computer_cards}, final score: {computer_score}")
        print(self.compare.compare(user_score, computer_score))
                    

while True:
    play_game = PlayGame()
    play_game.play_game()
    play_again = input("Do you want to play again? Type 'y' or 'n': ")
    if play_again.lower() != 'y':
        break
    # Clear the console
    os.system('cls' if os.name == 'nt' else 'clear')
