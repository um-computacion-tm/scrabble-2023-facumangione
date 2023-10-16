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
        self.word_calculator = Calculate_word_value()

        for _ in range(players_count):
            self.players.append(Player(id=len(self.players) + 1))
        
        if self.players:
            self.current_player = self.players[0]  # Inicializar con el primer jugador

    def add_player(self):
        if len(self.players) >= 4:
            raise ValueError("El máximo número de jugadores permitido es 4")
        self.players.append(Player(id=len(self.players) + 1))

    def next_turn(self):
        current_index = self.players.index(self.current_player)
        if current_index == len(self.players) - 1:
            self.current_player = self.players[0]
        else:
            self.current_player = self.players[current_index + 1]

    def play(self, word, location, orientation):
        self.validate_word(word, location, orientation)
        words = self.board.put_words(word, location, orientation)
        total = self.word_calculator.calculate_word_value(words)
        self.current_player.score += total
        self.next_turn()

    def validate_word(self, word, location, orientation):
        if not Dictionary().verify_word(word):
            raise ValueError("Su palabra no existe en el diccionario")
        if not self.board.validate_word_inside_board(word, location, orientation):
            raise ValueError("Su palabra excede el tablero")
        if not self.board.validate_word_place_board(word, location, orientation):
            raise ValueError("Su palabra está mal puesta en el tablero")

    def is_playing(self):
        return any(player.rack or self.bag_tiles.tiles for player in self.players)

    def get_board(self):
        return self.board
    
    def get_current_player(self):
        return self.current_player
    
    def get_players(self):
        return self.players

    def start_game(self):
        while self.is_playing():
            self.show_board()  # Muestra el tablero antes de cada turno
            self.show_current_player()  # Muestra el turno del jugador actual
            word = input('Ingrese palabra (o "PASAR" para saltar el turno): ')
            if word.lower() == "pasar":
                self.pass_turn()
            else:
                location_x = int(input('Ingrese posición X: '))
                location_y = int(input('Ingrese posición Y: '))
                orientation = input('Ingrese orientación (V/H): ')
                try:
                    self.play(word, (location_x, location_y), orientation)
                except Exception as e:
                    print(e)
            self.show_scores()  # Muestra los puntajes después de cada turno

    def show_board(self):
        board = self.get_board()
        for row in board:
            print(' '.join([cell.letter for cell in row]))
        print()

    def show_current_player(self):
        current_player = self.get_current_player()
        print(f"Turno del jugador {current_player.id}")

    def show_scores(self):
        players = self.get_players()
        for player in players:
            print(f"Jugador {player.id}: Puntos = {player.score}")
        print()