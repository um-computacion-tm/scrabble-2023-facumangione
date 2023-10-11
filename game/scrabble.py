from game.game_board import Board
from game.game_player import Player
from game.models import BagTiles 
from game.game_calculate import Calculate_word_value
from game.dictionary import Dictionary

class ScrabbleGame:
    def __init__(self, players_count):
        self.board = Board()
        self.bag_tiles = BagTiles()
        self.players = []   
        self.user_letters= []
        for _ in range(players_count):
             self.players.append(Player(id=len(self.players) + 1))# Quitamos el argumento 'id'
        
        if self.players:  # Verificar si hay jugadores en la lista
            self.current_player = 0  # Inicializar con el primer jugador (puede ser 0 o 1 dependiendo de cómo se indexen los jugadores)
        else:
            self.current_player = None 

    def add_player(self):
        if self.player_count >= 4:
            raise ValueError("El máximo número de jugadores permitido es 4")
        self.players.append(Player(id=len(self.players) + 1))
        self.player_count += 1

    def next_turn(self):
        if self.current_player is None:
            self.current_player = self.players[0]
        elif id(self.current_player) == id(self.players[(len(self.players)) -1]):
            self.current_player = self.players[0]
        else:
            self.current_player = self.players[self.players.index(self.current_player)+ 1]

    def play(self, word, location, orientation):
        self.validate_word(word, location, orientation)
        words = self.board.put_words(word, location, orientation)
        total = Calculate_word_value(words)
        self.players[self.current_player].score += total
        self.next_turn()

    def next_turn(self):
        if self.current_player is None:
            self.current_player = 0  # Inicializar con el primer jugador
        else:
            self.current_player = (self.current_player + 1) % len(self.players)


    def validate_word(self, word, location, orientation):
        if not Dictionary(word):
            raise ValueError("Su palabra no existe en el diccionario")
        if not self.board.validate_word_inside_board(word, location, orientation):
            raise ValueError("Su palabra excede el tablero")
        if not self.board.validate_word_place_board(word, location, orientation):
            raise ValueError("Su palabra esta mal puesta en el tablero")