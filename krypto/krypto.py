# Implements the game of Krypto.
# Christian Felt, December 2019

# TODO: Implement time limit
# TODO: Implement solution checking
# TODO: Implement computer opponent who finds correct solution after handicap time (random deviation around
#  an average, selected according to player's chosen difficulty level.)
# TODO: Implement custom parser to catch all potential rule breaking.
# TODO: Implement saving high scores with username between runs

import random
import re
import threading
import os


class Krypto:
    """A popular math game."""

    rules = "\nFind a way to add, subtract, multiply, or divide the numbers on the following playing cards to produce\n " \
            "the number on the target card. Each playing card must be used exactly once. In your solution,\n " \
            "only the numbers on the playing cards and the symbols +, -, *, /, and parentheses are allowed.\n "

    allowed_characters = ['+', '-', '/', '*', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '(', ')']

    def __init__(self, time_limit=60):
        """Fill and shuffle deck and initialize game stats."""
        self.deck = []
        self.populate_deck()
        self.games_won = 0
        self.games_lost = 0
        self.timer = threading.Timer(time_limit, self.time_up)

    def time_up(self):
        print("Time's up!")
        print("Games won:", self.games_won)
        print("Games lost:", self.games_lost)
        total_score = self.games_won - self.games_lost
        print("Total score:", total_score)
        os._exit(0)

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

    def play_krypto(self):
        self.timer.start()
        print(Krypto.rules)
        while True:
            print("\nPlaying Cards:")
            playing_cards = []
            for i in range(0, 5):
                playing_cards.append(self.draw())
                print(playing_cards[-1], end=" ")
            print("\nTarget Card:")
            target_card = self.draw()
            print(target_card)
            answer = input("Do you have a solution?\n")
            evaluation = Krypto.evaluate_answer(answer, playing_cards, target_card)
            print(evaluation)
            if evaluation == "Correct!":
                self.games_won += 1
            else:
                self.games_lost += 1
            print("Games won:", self.games_won)
            print("Games lost:", self.games_lost)

    @staticmethod
    def evaluate_answer(answer_string, playing_cards, target_card):
        """Check if answer is correct."""
        answer_string = answer_string.replace(" ", "")  # Get rid of spaces.
        if len(answer_string) > len(playing_cards) + 20: # Some basic security checks on input to eval()
            return "Solution is too long."
        for char in answer_string:
            if char not in Krypto.allowed_characters:
                return "Solution contains invalid characters."
        try:
            result = eval(answer_string)
        except SyntaxError:
            return "Solution has incorrect syntax."
        answer_string = answer_string.replace("(", "")
        answer_string = answer_string.replace(")", "")
        numbers = re.split('\+|-|\*|/', answer_string)
        if len(numbers) != len(playing_cards):
            return "Solution contains wrong number of numbers."
        operators = re.split('\d+', answer_string)
        operators = operators[1:-1] # Remove "" at beginning and end of list.
        if len(operators) + 1 != len(numbers):
            return "Solution uses wrong number of operators"
        for card in playing_cards:
            if str(card) not in numbers:
                return "Solution does not use all the playing cards."
        for number in numbers:
            if int(number) not in playing_cards:
                return "Solution uses numbers not in playing cards."
        if result == target_card:
            return "Correct!"
        else:
            return "= " + str(result) + ". Incorrect."


if __name__ == '__main__':
    krypto = Krypto()
    krypto.play_krypto()

