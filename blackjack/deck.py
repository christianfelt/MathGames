# Represents an ordinary deck of 52 face cards.
# Christian Felt, December 2019


import random
import card


class Deck:
    """A deck of cards."""
    def __init__(self, deck_type="standard"):
        """Create deck of cards."""
        if deck_type == "standard":
            self.card_values = {
                "ace": 1,
                "two": 2,
                "three": 3,
                "four": 4,
                "five": 5,
                "six": 6,
                "seven": 7,
                "eight": 8,
                "nine": 9,
                "ten": 10,
                "jack": 10,
                "queen": 10,
                "king": 10
            }
            self.cards = []
            self.fill_standard_deck()
        else:
            raise Exception("Only standard deck type is supported right now.")

    def fill_standard_deck(self):
        """Add 52 regular face cards to the deck."""
        for name in ["ace", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack",
                     "queen", "king"]:
            for suit in ["hearts", "diamonds", "spades", "clubs"]:
                self.cards.append(card.Card(name, suit, self.card_values[name]))

    def shuffle(self):
        """Shuffle deck."""
        random.shuffle(self.cards)

    def reshuffle(self):
        """Discard any existing cards in deck and add 52 new ones, then shuffle."""
        self.cards = []
        self.fill_standard_deck()
        self.shuffle()

    def draw(self):
        """Draw a card. If deck is empty, reshuffle then draw."""
        if len(self.cards) > 0:
            return self.cards.pop(0)
        else:
            self.reshuffle()
            return self.cards.pop(0)


if __name__ == '__main__':
    # Tests
    deck = Deck()
    deck.shuffle()
    this_card = deck.draw()
    assert (card not in deck.cards)
    for i in range(0, 51):
        deck.draw()
    assert (len(deck.cards) == 0)
    deck.draw()
    assert (len(deck.cards) == 51)

