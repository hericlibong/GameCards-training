import random

class Card:
    """Représente une carte avec un rang et une couleur"""
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['Trèfles', 'Piques', 'Cœurs', 'Carreaux']

    def __init__(self, rank, suit):
        """Initialise une nouvelle carte avec le rang et la couleur spécifié"""
        self.rank = rank
        self.suit = suit
        # Détermine le score de rang en trouvant l'index du rang dans la liste des rangs.
        self.rank_score = self.ranks.index(rank)
        # Détermine le score de couleur en trouvant l'index de la couleur dans la liste des couleurs.
        self.suit_score = self.suits.index(suit)

    def __str__(self):
        return f"{self.rank} de {self.suit}"
    
    def __repr__(self):
        return self.__str__()
    
    def __lt__(self, other):
        """Permet la comparaison de deux cartes basée sur leur rang et leur couleur."""
        if self.rank_score == other.rank_score:
            return self.suit_score < other.suit_score
        return self.rank_score < other.rank_score

class Deck:
    """Représente un jeu de 52 cartes"""
    def __init__(self):
        self.cards = [Card(rank, suit) for suit in Card.suits for rank in Card.ranks] 

    def shuffle(self):
        "Mélange les cartes dans le jeu"
        random.shuffle(self.cards)

class Player:
    """Représente un joueur"""
    def __init__(self, name):
        self.name = name
        self.card = None

class Game:
    """Gère la logique du jeu"""
    def __init__(self, player_names):
        self.deck = Deck()
        self.players = [Player(name) for name in player_names]
