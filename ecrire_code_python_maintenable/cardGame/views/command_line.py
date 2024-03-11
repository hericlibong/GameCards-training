
class CommandLineInterface:
    def show_main_menu(self):
        print("1. Start a new game")
        print("2. Quit")

    def get_menu_choice(self):
        choice = input("Enter your choice: ")
        if choice == '1':
            return 'start'
        elif choice == '2':
            return 'quit'
        else:
            print("Invalid choice.")
            return 'invalid'

    def get_player_names(self):
        names = []
        player_count = int(input("Enter number of players: "))
        for i in range(player_count):
            name = input(f"Enter player {i+1} name: ")
            names.append(name)
        return names
    
    def show_player_card(self, player_name, card):
        print(f"{player_name} a tiré la carte {card}.")

    def show_winner(self, winner):
        print(f"The winner is {winner.name} with the {winner.card}.")

    def quit_game(self):
        print("Thank you for playing!")


