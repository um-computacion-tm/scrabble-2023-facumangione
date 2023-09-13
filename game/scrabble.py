from game.game_board import Board
from game.game_player import Player
from game.models import BagTiles
from game.game_cell import Cell


class ScrabbleGame:
    def __init__(self, players_count):
        self.board = Board()
        self.bag_tiles = BagTiles()
        self.players = []
        for _ in range(players_count):
             self.players.append(Player(id=len(self.players) + 1))# Quitamos el argumento 'id'
        self.current_player = None

    def next_turn(self):
        if self.current_player is None:
            self.current_player = self.players[0]
        elif id(self.current_player) == id(self.players[(len(self.players)) -1]):
            self.current_player = self.players[0]
        else:
            self.current_player = self.players[self.players.index(self.current_player)+ 1]

    def validate_word(self, word, location, orientation):
        '''
        1- Validar que usuario tiene esas letras
        2- Validar que la palabra entra en el tablero
        '''
        self.board.validate_word_inside_board(word, location, orientation)
    
    def get_words():
        '''
        Obtener las posibles palabras que se pueden formar, dada una palabra, ubicacion y orientacion 
        Preguntar al usuario, por cada una de esas palabras, las que considera reales
        '''
    
    def put_words():
        '''
        Modifica el estado del tablero con las palabras consideradas como correctas
        '''