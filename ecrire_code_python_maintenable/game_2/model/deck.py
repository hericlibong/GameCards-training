import random
from .cards import Card
from game_2.helpers import RANKS, SUITS




class Deck:
    """Deck of cards."""

    def __init__(self):
        """Has some cards."""
        self.cards = [Card(suit, rank) for rank in RANKS for suit in SUITS]
        self.shuffle()

    def shuffle(self):
        """Shuffle the deck."""
        random.shuffle(self.cards)

    def draw_card(self):
        """Draw the top card."""
        try:
            return self.cards.pop()
        except IndexError:
            return None