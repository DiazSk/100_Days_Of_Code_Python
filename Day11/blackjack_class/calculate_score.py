class CalculateScore:
    def __init__(self):
        self.cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    def calculate_score(self, cards):
        score = sum(cards)

        if score == 21 and len(cards) == 2:
            return 0
        if score > 21 and 11 in cards:
            cards.remove(11)
            cards.append(1)
        return score
