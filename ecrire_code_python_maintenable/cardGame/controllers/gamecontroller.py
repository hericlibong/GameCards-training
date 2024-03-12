
from model.game import Game

class GameController:
    def __init__(self, interface):
        """
        Initialise le contrôleur du jeu.
        
        Args:
            interface: Une instance de la classe d'interface utilisateur qui sera utilisée
                       pour communiquer avec l'utilisateur.
        """
        self.game = None
        self.interface = interface
        self.player_name = []

    def start_new_game(self):
        """
        Démarre un nouveau jeu en demandant les noms des joueurs et en initialisant le jeu.
        """
        names = self.interface.get_player_names()
        self.game = Game(names)

    def play_round(self):
        """
        Joue une manche du jeu en distribuant une carte à chaque joueur,
        en affichant les cartes distribuées, et en annonçant le vainqueur.
        """
        for player in self.game.players:
            player.card = self.game.deck.draw_card()
            self.interface.show_player_card(player.name, player.card)
        winner = self.game.determine_winner()
        self.interface.show_winner(winner)

    
        
    def run(self):
        """
        Exécute la boucle principale du jeu, affiche le menu principal et traite
        les actions de l'utilisateur jusqu'à ce que le jeu soit quitté.
        """
        while True:
            if not self.game:
                self.interface.show_start_menu()
                choice = self.interface.get_menu_choice()
                if choice == '1':
                    self.start_new_game()
            else:
                self.interface.show_post_game_menu()
                choice = self.interface.get_menu_choice()

            if choice == '1' and self.game:
                self.play_round()
            elif choice == '2':
                self.start_new_game()
            elif choice == '3' or (choice == '2' and not self.game):
                self.interface.quit_game()
                break
            self.play_round()   
