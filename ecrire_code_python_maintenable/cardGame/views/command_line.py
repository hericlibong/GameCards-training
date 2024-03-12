
class CommandLineInterface:

    def show_start_menu(self):
        print("1. Commencer une nouvelle partie")
        print("2. Quitter")

    def show_post_game_menu(self):
        print("1. Rejouer avec les mêmes joueurs")
        print("2. Commencer une nouvelle partie")
        print("3. Quitter")
    
    def get_menu_choice(self):
        return input("Entrez votre choix : ")

            

    def get_player_names(self):
        """
        Demande et retourne les noms des joueurs.
        
        Returns:
            list of str: Une liste contenant les noms des joueurs.
        """
        names = []
        player_count = int(input("Enter number of players: "))
        for i in range(player_count):
            name = input(f"Enter player {i+1} name: ")
            names.append(name)
        return names
    
    def show_player_card(self, player_name, card):
        """
        Affiche la carte tirée par un joueur.
        
        Args:
            player_name (str): Le nom du joueur.
            card (Card): L'objet carte tiré par le joueur.
        """
        print(f"{player_name} a tiré la carte {card}.")

    def show_winner(self, winner):
        """
        Annonce le gagnant de la manche.
        
        Args:
            winner (Player): Le joueur qui a gagné la manche.
        """
        print(f"{winner.name} gagne avec {winner.card}.")
        

    def quit_game(self):
        """
        Affiche un message de fin lorsque l'utilisateur quitte le jeu.
        """
        print("Merci d'avoir joué!")


