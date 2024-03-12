

class Card:
    """Représente une carte avec un rang et une couleur"""
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Reine', 'Roi', 'As']
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