# Implements the game of Krypto.
# Christian Felt, December 2019

# TODO: Implement time limit
# TODO: Implement solution checking
# TODO: Implement computer opponent who finds correct solution after handicap time (random deviation around
#  an average, selected according to player's chosen difficulty level.)

import random
import re
import operator


class Krypto:
    """A popular math game."""

    operator_table = {
        """All operators allowed in the game. Map from strings to operators."""
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }

    rules = "Find a way to add, subtract, multiply, or divide (without remainder) the numbers on the following " \
            "playing\n cards to produce the number on the target card. Each playing card must be used exactly once. " \
            "When\n evaluating your solution, all arithmetic operations will be performed from left to right. In your " \
            "solution, \nonly the numbers on the playing cards and the symbols +, -, *, and / are allowed. No " \
            "negative numbers \n are allowed. "

    def __init__(self):
        """Fill and shuffle deck and initialize game stats."""
        self.deck = []
        self.populate_deck()
        self.games_won = 0
        self.games_lost = 0


    def populate_deck(self):
        """Fill deck with standard Krypto card values and shuffle."""
        self.deck = [
            1, 1, 1,
            2, 2, 2,
            3, 3, 3,
            4, 4, 4,
            5, 5, 5,
            6, 6, 6,
            7, 7, 7,
            8, 8, 8,
            9, 9, 9,
            10, 10, 10,
            11, 11,
            12, 12,
            13, 13,
            14, 14,
            15, 15,
            16, 16,
            17, 17,
            18,
            19,
            20,
            21,
            22,
            23,
            24,
            25
        ]
        random.shuffle(self.deck)

    def draw(self):
        """Draw a card and reshuffle deck if empty."""
        if len(self.deck) > 0:
            return self.deck.pop(0)
        else:
            self.populate_deck()
            return self.deck.pop(0)

    @staticmethod
    def evaluate_answer(answer_string, playing_cards, target_card):
        """Check if answer is correct."""
        answer_string = answer_string.replace(" ", "") # Get rid of spaces.
        numbers = re.split('\+|-|\*|/', answer_string)
        if len(numbers) != len(playing_cards):
            return "Solution contains wrong number of numbers."
        operators = re.split('\d+', answer_string)
        operators = operators[1:-1] # Remove "" at beginning and end of list.
        if len(operators) + 1 != len(numbers):
            return "Solution uses wrong number of operators"
        result = int(numbers[0])
        for i in range(0, len(operators)):
            try:
                intermediate_result = Krypto.operator_table[operators[i]](result, int(numbers[i+1]))
            except KeyError:
                return "Solution uses invalid operators."
            if intermediate_result < 0:
                return "Negative numbers are not allowed."
            if intermediate_result % 1 != 0:
                return "Division with remainders is not allowed."
            result = intermediate_result
        for card in playing_cards:
            if card not in numbers:
                return "Solution does not use all the playing cards."
        if result == target_card:
            return "Correct!"
        else:
            return "Incorrect."


if __name__ == '__main__':
    krypto = Krypto()
    print(Krypto.rules)
    keep_playing = True
    while keep_playing:
        print("Playing Cards:")
        playing_cards = []
        for i in range(0, 5):
            playing_cards.append(krypto.draw())
            print(playing_cards[-1], end=" ")
        print("\nTarget Card:")
        target_card = krypto.draw()
        print(target_card)
        answer = input("Do you have a solution?\n")
        evaluation = Krypto.evaluate_answer(answer, playing_cards, target_card)
        print(evaluation)
        if evaluation == "Correct!":
            krypto.games_won += 1
        elif evaluation == "Incorrect.":
            krypto.games_lost += 1
        print("Games won:", krypto.games_won)
        print("Games lost:", krypto.games_lost)
        keep_playing = input("Would you like to keep playing? (y/n) ").lower() == "y"
