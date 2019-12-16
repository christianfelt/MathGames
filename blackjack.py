# Implements the game of blackjack.
# Christian Felt, December 2019
# TODO: Implement choosing Ace score
# TODO: Implement betting

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
        this_score = this_card.value
        self.dealer_score += this_score
        print("The dealer drew the", this_card.name, "of", this_card.suit)
        print("The dealer's score is", self.dealer_score)
        if self.dealer_score > self.max_score:
            print("The dealer's score exceeds the max score. Therefore, you win.")
            self.games_won += 1
            self.game_in_progress = False

    def do_player_turn(self):
        """Draw a card, record the score, and display results."""
        this_card = self.deck.draw()
        this_score = this_card.value
        self.player_score += this_score
        print("You drew the", this_card.name, "of", this_card.suit)
        print("Your score is", self.player_score)
        if self.player_score > self.max_score:
            print("Your score exceeds the max score. Therefore, you lose.")
            self.game_in_progress = False
            self.games_lost += 1

    def play_game(self):
        name = input("What is your name? ")
        self.set_player_name(name)
        print("Hello,", self.player_name)
        keep_playing = True
        while keep_playing:
            self.renew_deck()
            self.player_score = 0
            self.dealer_score = 0
            self.game_in_progress = True
            first_card = self.deck.draw()
            print("Your first card is the", first_card.name, "of", first_card.suit)
            first_score = first_card.value
            self.player_score += first_score
            print("Your score is", self.player_score)
            self.do_dealer_turn()
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
                        elif self.player_score < self.dealer_score:
                            print("You lose.")
                            self.games_lost += 1
                        else:
                            print("The game was a draw.")
                            self.games_drawn += 1
                        self.game_in_progress = False
                else:
                    print("Did you enter 'yn'? You loser. You lose.")
                    self.games_lost += 1
                    self.game_in_progress = False
            print("Games won:", self.games_won)
            print("Games lost:", self.games_lost)
            print("Games drawn:", self.games_drawn)
            keep_playing = input("Would you like to keep playing? (y/n)")
            while keep_playing.lower() != "y" and keep_playing.lower() != "n":
                keep_playing = input("Invalid input. Please enter y or n.")
            if keep_playing.lower() == "y":
                keep_playing = True
            elif keep_playing.lower() == "n":
                keep_playing = False
            else:
                raise Exception("Invalid 'keep playing?' input.")


if __name__ == '__main__':
    blackjack = Blackjack()
    blackjack.play_game()
