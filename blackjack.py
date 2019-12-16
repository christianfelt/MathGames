# Implements the game of blackjack.
# Christian Felt, December 2019

import deck


class Blackjack:
    """A well-known card game."""

    def __init__(self, max_score=21):
        """Set up basic game parameters."""
        self.player_bank = 100
        self.dealer_bank = 100
        self.player_score = 0
        self.game_in_progress = True
        self.dealer_score = 0
        self.games_won = 0
        self.games_lost = 0
        self.games_drawn = 0
        self.player_name = "Anonymous"
        self.deck = deck.Deck()
        self.max_score = max_score
        self.latest_result = "none"
        self.dealer_max_score = 14  # Point at which dealer stops drawing new cards.

    def renew_deck(self):
        """Draw and shuffle a new deck."""
        self.deck = deck.Deck()
        self.deck.shuffle()

    def set_player_name(self, name):
        """Set player's name."""
        self.player_name = name

    def do_dealer_turn(self):
        """Draw a card, record the score, and display results."""
        this_card = self.deck.draw()
        print("The dealer drew the", this_card.name, "of", this_card.suit)
        if this_card.name.lower() == "ace":
            if self.dealer_score < 11:
                this_card.value = 11
            else:
                this_card.value = 1
        this_score = this_card.value
        self.dealer_score += this_score
        print("The dealer's score is", self.dealer_score)
        if self.dealer_score > self.max_score:
            print("The dealer's score exceeds the max score. Therefore, you win.")
            self.games_won += 1
            self.latest_result = "win"
            self.game_in_progress = False

    def do_player_turn(self):
        """Draw a card, record the score, and display results."""
        this_card = self.deck.draw()
        print("You drew the", this_card.name, "of", this_card.suit)
        if this_card.name.lower() == "ace":
            choice = int(input("Would you like this ace to count as 1 or 11? "))
            while choice != 1 and choice != 11:
                choice = input("Invalid input. Please enter 1 or 11. ")
            this_card.value = choice
        this_score = this_card.value
        self.player_score += this_score
        print("Your score is", self.player_score)
        if self.player_score > self.max_score:
            print("Your score exceeds the max score. Therefore, you lose.")
            self.game_in_progress = False
            self.games_lost += 1
            self.latest_result = "lose"

    def play_game(self):
        name = input("What is your name? ")
        self.set_player_name(name)
        print("Hello,", self.player_name)
        print("Player's money =", self.player_bank)
        print("Dealer's money =", self.dealer_bank)
        keep_playing = True
        while keep_playing:
            bet_amount = int(input("How much would you like to wager that you will win this game? "
                                   "(0-" + str(self.player_bank) + ") "))
            while bet_amount < 0 or bet_amount > self.player_bank:
                bet_amount = int(
                    input("Invalid input. Please enter a number between 0 and " + str(self.player_bank) + " "))
            self.renew_deck()
            self.player_score = 0
            self.dealer_score = 0
            self.game_in_progress = True
            self.do_player_turn()
            self.do_dealer_turn()
            self.latest_result = "none"
            while self.game_in_progress:
                response = input("Would you like to draw another card? (y/n) ")
                while response.lower() == "" or response.lower() not in "yn":
                    response = input("Input not recognized. Please enter 'y' or 'n'. ")
                if response.lower() == "y":
                    self.do_player_turn()
                    if self.game_in_progress:
                        if self.dealer_score < self.dealer_max_score:
                            self.do_dealer_turn()
                        else:
                            print("The dealer did not draw a card. The dealer's score is still", self.dealer_score)
                elif response.lower() == "n":
                    while self.dealer_score < self.dealer_max_score:
                        self.do_dealer_turn()
                    if self.game_in_progress:
                        print("Your final score is", self.player_score)
                        print("The dealer's final score is", self.dealer_score)
                        if self.player_score > self.dealer_score:
                            print("You win!")
                            self.games_won += 1
                            self.latest_result = "win"
                        elif self.player_score < self.dealer_score:
                            print("You lose.")
                            self.games_lost += 1
                            self.latest_result = "lose"
                        else:
                            print("The game was a draw.")
                            self.games_drawn += 1
                            self.latest_result = "draw"
                        self.game_in_progress = False
                else:
                    print("Did you enter 'yn'? You loser. You lose.")
                    self.games_lost += 1
                    self.latest_result = "lose"
                    self.game_in_progress = False
            if self.latest_result == "win":
                self.player_bank += bet_amount
                self.dealer_bank -= bet_amount
            elif self.latest_result == "lose":
                self.player_bank -= bet_amount
                self.dealer_bank += bet_amount
            elif self.latest_result == "draw":
                pass
            else:
                raise Exception("self.latest_result was not set properly.")
            print("Games won:", self.games_won)
            print("Games lost:", self.games_lost)
            print("Games drawn:", self.games_drawn)
            print("Player's money =", self.player_bank)
            print("Dealer's money =", self.dealer_bank)
            if self.player_bank == 0:
                print("You are bankrupt!")
                keep_playing = False
            elif self.dealer_bank == 0:
                print("You bankrupted the casino!")
                keep_playing = False
            else:
                keep_playing = input("Would you like to keep playing? (y/n) ")
                while keep_playing.lower() != "y" and keep_playing.lower() != "n":
                    keep_playing = input("Invalid input. Please enter y or n. ")
                if keep_playing.lower() == "y":
                    keep_playing = True
                elif keep_playing.lower() == "n":
                    keep_playing = False
                else:
                    raise Exception("Invalid 'keep playing?' input.")
        print("Goodbye,", self.player_name)


if __name__ == '__main__':
    blackjack = Blackjack()
    blackjack.play_game()
