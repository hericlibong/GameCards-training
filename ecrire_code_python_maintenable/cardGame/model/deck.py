import random
from .cards import Card


class Deck:
    """Représente un jeu de 52 cartes"""
    def __init__(self):
        self.cards = [Card(rank, suit) for suit in Card.suits for rank in Card.ranks] 
        self.shuffle()

    def shuffle(self):
        """Mélange les cartes dans le jeu"""
        random.shuffle(self.cards)

    
    def draw_card(self):
        """Pioche la carte du dessus du jeu mélangé."""
        try:
            return self.cards.pop()
        except IndexError:
            return None
    