# Represents an ordinary deck of 52 face cards.
# Christian Felt, December 2019


import random
import card


class Deck:
    def __init__(self, deck_type="standard"):
        if deck_type == "standard":
            self.card_values = {
                "ace" : 1,
                "two" : 2,
                "three" : 3,
                "four" : 4,
                "five" : 5,
                "six" : 6,
                "seven" : 7,
                "eight" : 8,
                "nine" : 9,
                "ten" : 10,
                "jack" : 10,
                "queen" : 10,
                "king" : 10
            }
            self.cards = []
            for name in ["ace", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack",
                         "queen", "king"]:
                for suit in ["hearts", "diamonds", "spades", "clubs"]:
                    self.cards.append(card.Card(name, suit, self.card_values[name]))

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop(0)


if __name__ == '__main__':
    deck = Deck()
    deck.shuffle()
    card = deck.draw()
    assert(card not in deck.cards)


