
from model.game import Game

class GameController:
    def __init__(self, interface):
        self.game = None
        self.interface = interface

    def start_new_game(self):
        names = self.interface.get_player_names()
        self.game = Game(names)
        

    def play_round(self):
        for player in self.game.players:
            player.card = self.game.deck.draw_card()
            #Affiche la carte de chaque joueur après la distribution
            self.interface.show_player_card(player.name, player.card)
        winner = self.game.determine_winner()
        self.interface.show_winner(winner)

    def run(self):
        while True:
            self.interface.show_main_menu()
            choice = self.interface.get_menu_choice()
            if choice == 'start':
                self.start_new_game()
                self.play_round()
            elif choice == 'quit':
                self.interface.quit_game()
                break
