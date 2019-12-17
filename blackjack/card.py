# Represents an ordinary face card.
# Christian Felt, December 2019


class Card:
    """A playing card."""
    def __init__(self, name, suit, value):
        """Create card."""
        self.name = name
        self.suit = suit
        self.value = value
