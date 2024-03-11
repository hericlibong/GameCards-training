from .deck import Deck
from .players import Player

class Game:
    """Gère la logique du jeu"""
    def __init__(self, player_names):
        self.deck = Deck()
        self.players = [Player(name) for name in player_names]

    def determine_winner(self):
        # Supposons que chaque joueur a une seule carte.
        # La logique peut devenir plus complexe si les joueurs ont plusieurs cartes.
        winning_player = None
        highest_card = None
        for player in self.players:
            if highest_card is None or player.card > highest_card:
                highest_card = player.card
                winning_player = player
        return winning_player