from game.game_board import Board
from game.game_player import Player
from game.models import BagTiles
from game.several import Several
from game.dictionary import Dictionary
import uuid
import random

class ScrabbleGame:
    def __init__(self, players_count):
        self.board = Board()
        self.bag_tiles = BagTiles()
        self.players = []
        self.gameid = str(uuid.uuid4())
        for index in range(players_count):
            self.players.append(Player(id=index +1))
        self.current_player = None
        self.turn = 0
        self.dic = Dictionary()
        self.grid = [[' ' for _ in range(15)] for _ in range(15)] 

    def playing(self):
        return True
    
    def next_turn(self):
        if self.current_player is None:
            self.current_player = self.players[0]
        else:
            current_index = self.players.index(self.current_player)
            next_index = (current_index + 1) % len(self.players)
            self.current_player = self.players[next_index]
        self.turn += 1

    def current_player_name(self):
        if self.current_player:
            return f'Jugador {self.current_player.id}'
        else:
            return 'No hay jugador actual'


    ###
    def scrabble_validate_word(self, word, location, orientation):
        if self.dic.verify_word(word) is True:
            return self.board.validate_word_place_board(word, location, orientation)
        else:
            return False
   
    def scrabble_word_calculate_score(self, word, location, orientation):
        sev = Several()
        board = self.board
        new_word = sev.converter_word_to_cells(word, location, orientation, board)
        score = sev.calculate_word_value(new_word)
        self.current_player.score += score
    ###
    def get_board(self):
        sev = Several()
        return self.board
    ###
    def show_rack(self):
        return self.current_player.display_rack()

    def put_word(self, word, location, orientation):
        self.board.insert(word, location, orientation)

    def show_amount_tiles_bag(self):
        return len(self.bag_tiles.tiles)

    def shuffle_rack(self):
        random.shuffle(self.current_player.rack)

    def game_over(self):
        if len(self.bag_tiles.tiles) == 0:
            return True
        return False

    def put_tiles_in_rack(self, amount=7):
        bag = self.bag_tiles
        if self.turn == 0:
            for i in range(len(self.players)):
                self.players[i].get_tiles(amount, bag)#get_tiles
        else:
            self.current_player.get_tiles(amount, bag)

    def put_initial_tiles_bag(self):
        self.bag_tiles.initial_tiles()

    def show_board(self, board):
        print('\n  |' + ''.join([f' {str(row_index).rjust(2)} ' for row_index in range(len(board.grid))]))
        for row_index, row in enumerate(board.grid):
            print(
                str(row_index).rjust(2) +
                '| ' +
                ' '.join([repr(cell) for cell in row])
            )