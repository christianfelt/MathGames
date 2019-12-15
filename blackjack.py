# Implements the game of blackjack.
# Christian Felt, December 2019

import deck

class Blackjack:
    def __init__(self, max_score = 21):
        self.player_score = 0
        self.dealer_score = 0
        self.games_played = 0
        self.games_won = 0
        self.games_lost = 0
        self.games_drawn = 0
        self.player_name = "Anonymous"
        self.current_deck = deck.Deck()
        self.max_score = max_score
        self.dealer_max_score = 14

    def set_player_name(self, name):
        self.player_name = name

    def do_dealer_turn(self):
        this_card = self.current_deck.draw()
        this_score = self.current_deck.get_card_value(this_card)
        self.dealer_score += this_score
        print("The dealer drew", this_card)
        print("The dealer's score is", self.dealer_score)

    def do_player_turn(self):
        this_card = self.current_deck.draw()
        this_score = self.current_deck.get_card_value(this_card)
        self.player_score += this_score
        print("You drew", this_card)
        print("Your score is", self.player_score)



if __name__ == '__main__':
    blackjack = Blackjack()
    name = input("What is your name? ")
    blackjack.set_player_name(name)
    print("Hello,", blackjack.player_name)
    first_card = blackjack.current_deck.draw()
    print("Your first card is", first_card)
    first_score = blackjack.current_deck.get_card_value(first_card)
    blackjack.player_score += first_score
    game_in_progress = True
    blackjack.do_dealer_turn()
    while game_in_progress:
        response = input("Would you like to draw another card? (y/n) ")
        while response.lower() == "" or response.lower() not in "yn":
            response = input("Input not recognized. Please enter 'y' or 'n'. ")
        if response.lower() == "y":
            blackjack.do_player_turn()
            if blackjack.player_score > blackjack.max_score:
                print("Your score exceeds the max score. Therefore, you lose.")
                game_in_progress = False
            if blackjack.dealer_score < blackjack.dealer_max_score:
                blackjack.do_dealer_turn()
                if blackjack.dealer_score > blackjack.max_score:
                    print("The dealer's score exceeds the max score. Therefore, you win.")
                    game_in_progress = False
        elif response.lower() == "n":
            game_in_progress = False
            print("Your final score is", blackjack.player_score)
            print("The dealer's final score is", blackjack.dealer_score)
            if blackjack.player_score > blackjack.dealer_score:
                print("You win!")
                blackjack.games_won += 1
            elif blackjack.player_score < blackjack.dealer_score:
                print("You lose.")
                blackjack.games_lost += 1
            else:
                print("The game was a draw.")
                blackjack.games_drawn += 1
        else:
            print("Did you enter 'yn'? You loser. You lose.")
            game_in_progress = False
    blackjack.games_played += 1


