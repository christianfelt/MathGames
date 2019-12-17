# Implements the game of Krypto.
# Christian Felt, December 2019


import random
import re
import operator


class Krypto:
    """A popular math game."""

    operator_table = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }

    def __init__(self):
        self.deck = []
        self.populate_deck()

    def populate_deck(self):
        """Fill deck with standard Krypto card values."""
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
    def read_answer(answer_string):
        answer_string = answer_string.replace(" ", "")
        numbers = re.split('\+|-|\*|/', answer_string)
        operators = re.split('\d+', answer_string)
        operators = operators[1:-1] # Remove "" at beginning and end of list.
        first_operation = Krypto.operator_table[operators[0]](int(numbers[0]), int(numbers[1]))
        result = first_operation
        return result
        # for i in range(0, len(numbers)):



if __name__ == '__main__':
    krypto = Krypto()
    print("Find a way to add, subtract, multiply, or divide (without remainder) the numbers on the following playing\n "
          "cards to produce the number on the target card. Each playing card must be used exactly once. When\n "
          "evaluating your solution, all arithmetic operations will be performed from left to right. In your solution, "
          "\nonly the numbers on the playing cards and the symbols +, -, *, and / are allowed. No negative numbers \n"
          "are allowed.")
    print("Playing Cards:")
    for i in range(0, 5):
        print(krypto.draw(), end=" ")
    print("\nTarget Card:")
    print(krypto.draw())
    answer = input("Do you have a solution?\n")
    print(Krypto.read_answer(answer))
