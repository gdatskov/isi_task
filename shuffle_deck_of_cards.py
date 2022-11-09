import random


class Deck:
    cards = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']
    card_colors = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

    def __init__(self):
        self.deck = self.create_deck(self.cards, self.card_colors)

    @staticmethod
    def create_deck(cards, card_colors):
        deck_of_cards = []

        for card in cards:
            for color in card_colors:
                deck_of_cards.append(f'{card}-{color}')

        return deck_of_cards

    def shuffle(self):
        return random.shuffle(self.deck)

    def __str__(self):
        return ', '.join(self.deck)

    def __repr__(self):
        return self.deck


deck = Deck()
deck.shuffle()
print(deck)
