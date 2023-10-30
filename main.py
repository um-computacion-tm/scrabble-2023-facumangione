from game.scrabble import ScrabbleGame
from game.game_board import Board
from configure_game import Configure
from game.models import Tile

class Main:
    def __init__(self):
        print ("¡Bienvenido a Scrabble!")
        self.player_count = Configure.get_player_count
        self.game = ScrabbleGame(self.player_count)
        self.board = self.game.get_board()
        self.config = Configure
    
    def init_game(self):
        self.config.iniciar_juego
        self.config.get_player_count
        self.config.show_board
        self.config.show_current_player



if __name__ == "__main__":
    main = Main()
    main.init_game()

    def play_game(self):
        print('¡VAMOS A JUGAR!')
        self.initial_tiles()
        self.game.players[0].rack = [Tile('H', 4), Tile('O',1), Tile('L',1), Tile('A',1)]
        self.game.show_board(self.board)
        while not self.game.game_over():
            self.next_turn()
            self.show_current_player()
            self.take_turn()
        print('¡SE ACABO LO QUE SE DABA!')
        self.display_final_scores()