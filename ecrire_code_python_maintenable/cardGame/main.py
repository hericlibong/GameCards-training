from views.command_line import CommandLineInterface
from controllers.gamecontroller import GameController

if __name__ == "__main__":
    cli = CommandLineInterface()
    controller = GameController(cli)
    controller.run()