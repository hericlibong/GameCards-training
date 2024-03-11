
# def multiply(first, second = 1):
#     """Multiplie deux nombres.

#     Args:
#         first -- le multiplicande
#         second -- le multiplicateur (défaut 1)
#     """
#     return first * second


# print(multiply(13, 13))
# print(multiply.__doc__)


# def search_film(name):
#     films = Film.filter_by_name(name)
#     if films:
#         return films.pop(0)
#     return None



import random

RBG_COLORS = ["Red", "Green", "Blue"]

class BagOfMarbles:
    """Sac de billes."""

    def __init__(self, colors=[]):
        """Initialise les billes et les couleurs."""
        self.marbles = []
        self.stats = {}
        for color in colors:
            self.stats[color] = 0


    def add_marbles(self, color, count):
        """Ajoute des billes de la couleur souhaitée."""
        if color in self.stats:
            self.stats[color] += count
            for _ in range(count) :
                self.marbles.append(color)
            return True
        return False
    
    def select_marble(self):
        """Récupère une bille au hasard."""
        random.shuffle(self.marbles)
        color = self.marbles.pop()
        self.stats[color] -= 1
        return color
    
    def print_stats(self):
        """Affiche les statistiques des billes."""

        for color_ in self.stats:
            print(color_, str(self.stats[color_]))
    
    def count_marbles(self):
        return len(self.marbles)

bag = BagOfMarbles(RBG_COLORS)
for color in RBG_COLORS:
    if bag.add_marbles(color, 3) is False:
        print("Failed to add", color, "to bag...")

bag.print_stats()

while bag.count_marbles() > 4:
    print("Removing", bag.select_marble())

bag.print_stats()