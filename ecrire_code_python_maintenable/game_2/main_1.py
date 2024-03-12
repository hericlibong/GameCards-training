import random

# Define the cards.
SUITS = ("diamonds", "coeurs", "piques", "carreaux")
RANKS = (
    "deux",
    "trois",
    "quatre",
    "cinq",
    "six",
    "sept",
    "huit",
    "neuf",
    "dix",
    "valet",
    "reine",
    "roi",
    "ace",
)

class Card:
    """Card class.

    Has a suit and a rank.
    """

    def __init__(self, suit, rank):
        """Init the suit, the rank, is_face_up and the scores."""
        self.suit = suit
        self.rank = rank
        self.is_face_up = False

        self._rank_score = RANKS.index(self.rank)
        self._suit_score = SUITS.index(self.suit)

    def __str__(self):
        """Used in print."""
        return f"{self.rank} de {self.suit}"

    def __repr__(self):
        """Used in print."""
        return str(self)

    def __lt__(self, other: "Card"):
        """Compares the score of the current card with the score of another card."""
        if self._rank_score != other._rank_score:
            return self._rank_score < other._rank_score

        return self._suit_score < other._suit_score

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

class Player:
    def __init__(self, name):
        self.name = name
        self.card = None

        

deck = Deck()
print(deck.cards)

card1 = Card('diamonds', "dix")
card2 = Card("carreaux", "neuf")
card3 = Card("piques", "neuf")
card4 = Card("coeurs", "deux")

print(card1 < card2)
print(card1 > card3)
print(card2 > card3)


