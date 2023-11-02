from game.board import Board
from game.player import Player
from game.models import *
from random import shuffle

class ScrabbleGame:
    def __init__(self, players_count):
        self.players_count = players_count
        self.players = []
        self.board = Board()
        self.bag_tiles = BagTiles()
        self.current_player = None
        self.game_over = False
        self.current_player= None
        for i in range(self.players_count):
            self.players.append(Player())
        self.add_tiles_to_players()

    def add_tiles_to_players(self):
        for player in self.players:
            player.give_tiles(self.bag_tiles.take(7))

    def change_tiles(self, old_tiles_index):
        new_tiles = self.bag_tiles.take(len(old_tiles_index))
        old_tiles = []
        for i in old_tiles_index:
            old_tiles.append(self.current_player.lectern[i])
            self.current_player.lectern[i] = new_tiles.pop(0)
        self.bag_tiles.put(old_tiles)
        random.shuffle(self.bag_tiles.tiles)
        return old_tiles

    def next_turn(self):
        if self.current_player is None:
            self.current_player = self.players[0]
        elif self.players[-1] == self.current_player:
            self.current_player = self.players[0]
        else:
            index=self.players.index(self.current_player) + 1
            self.current_player = self.players[index]
         
    def end_game(self):
        if len(self.bag_tiles.tiles) == 0:
            for player in self.players:
                if player.tiles == []:
                    self.game_over = True
                else:
                    self.game_over = False
                    break
        else:
            self.game_over = False
        return self.game_over
        
    def view_board(self):
        return self.board.board_in_terminal()
    
    def view_scores(self):
        scores = ''
        for player in self.players:
            scores += player.name + ': ' + str  (player.points) + '\n'
        return scores 