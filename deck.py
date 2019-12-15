# Represents an ordinary deck of 52 face cards.
# Christian Felt, December 2019


import random


class Deck:
    def __init__(self):
        self.cards = [
            "Ace of hearts",
            "Ace of diamonds",
            "Ace of clubs",
            "Ace of spades",

            "Two of hearts",
            "Two of diamonds",
            "Two of clubs",
            "Two of spades",

            "Three of hearts",
            "Three of diamonds",
            "Three of clubs",
            "Three of spades",

            "Four of hearts",
            "Four of diamonds",
            "Four of clubs",
            "Four of spades",

            "Five of hearts",
            "Five of diamonds",
            "Five of clubs",
            "Five of spades",

            "Six of hearts",
            "Six of diamonds",
            "Six of clubs",
            "Six of spades",

            "Seven of hearts",
            "Seven of diamonds",
            "Seven of clubs",
            "Seven of spades",

            "Eight of hearts",
            "Eight of diamonds",
            "Eight of clubs",
            "Eight of spades",

            "Nine of hearts",
            "Nine of diamonds",
            "Nine of clubs",
            "Nine of spades",

            "Ten of hearts",
            "Ten of diamonds",
            "Ten of clubs",
            "Ten of spades",

            "Jack of hearts",
            "Jack of diamonds",
            "Jack of clubs",
            "Jack of spades",

            "Queen of hearts",
            "Queen of diamonds",
            "Queen of clubs",
            "Queen of spades",

            "King of hearts",
            "King of diamonds",
            "King of clubs",
            "King of spades"
        ]

        self.card_values = {
            "Ace of hearts" : 1,
            "Ace of diamonds" : 1,
            "Ace of clubs" : 1,
            "Ace of spades" : 1,

            "Two of hearts" : 2,
            "Two of diamonds" : 2,
            "Two of clubs" : 2,
            "Two of spades" : 2,

            "Three of hearts" : 3,
            "Three of diamonds" : 3,
            "Three of clubs" : 3,
            "Three of spades" : 3,

            "Four of hearts" : 4,
            "Four of diamonds" : 4,
            "Four of clubs" : 4,
            "Four of spades" : 4,

            "Five of hearts" : 5,
            "Five of diamonds" : 5,
            "Five of clubs" : 5,
            "Five of spades" : 5,

            "Six of hearts" : 6,
            "Six of diamonds" : 6,
            "Six of clubs" : 6,
            "Six of spades" : 6,

            "Seven of hearts" : 7,
            "Seven of diamonds" : 7,
            "Seven of clubs" : 7,
            "Seven of spades" : 7,

            "Eight of hearts" : 8,
            "Eight of diamonds" : 8,
            "Eight of clubs" : 8,
            "Eight of spades" : 8,

            "Nine of hearts" : 9,
            "Nine of diamonds" : 9,
            "Nine of clubs" : 9,
            "Nine of spades" : 9,

            "Ten of hearts" : 10,
            "Ten of diamonds" : 10,
            "Ten of clubs" : 10,
            "Ten of spades" : 10,

            "Jack of hearts" : 10,
            "Jack of diamonds" : 10,
            "Jack of clubs" : 10,
            "Jack of spades" : 10,

            "Queen of hearts" : 10,
            "Queen of diamonds" : 10,
            "Queen of clubs" : 10,
            "Queen of spades" : 10,

            "King of hearts" : 10,
            "King of diamonds" : 10,
            "King of clubs" : 10,
            "King of spades" : 10
        }

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop(0)

    def get_card_value(self, card):
        return self.card_values[card]


if __name__ == '__main__':
    deck = Deck()
    deck.shuffle()
    card = deck.draw()
    score = deck.get_card_value(card)


