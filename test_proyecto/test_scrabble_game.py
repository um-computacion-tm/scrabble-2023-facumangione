import unittest
from unittest.mock import patch
from game.scrabble import ScrabbleGame
from game.models import Tile

class TestScrabbleGame(unittest.TestCase):
    def test_init(self):
        scrabble_game = ScrabbleGame(players_count=3)
        self.assertIsNotNone(scrabble_game.board)
        self.assertEqual(
            len(scrabble_game.players),
            3,
        )
        self.assertIsNotNone(scrabble_game.bag_tiles)
    
    def test_next_turn_when_game_is_starting(self):
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.current_player = None
        scrabble_game.next_turn()
        assert scrabble_game.current_player == scrabble_game.players[0]

    def test_next_turn_when_game_is_not_the_first(self):
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.current_player = scrabble_game.players[0]
        scrabble_game.next_turn()
        assert scrabble_game.current_player == scrabble_game.players[1]
    
    def test_next_turn_when_player_is_last(self):
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.current_player = scrabble_game.players[2]
        scrabble_game.next_turn()
        assert scrabble_game.current_player == scrabble_game.players[0]

    def test_end_game_when_tilebag_is_empty_and_player_tiles_are_empty(self):
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.bag_tiles.tiles = []
        scrabble_game.players[0].tiles = []
        scrabble_game.players[1].tiles = []
        scrabble_game.players[2].tiles = []
        self.assertTrue(scrabble_game.end_game())

    def test_end_game_when_tilebag_is_empty(self):
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.bag_tiles.tiles = []
        scrabble_game.players[0].tiles = ['A']
        scrabble_game.players[1].tiles = ['A']
        scrabble_game.players[2].tiles = ['A']
        self.assertFalse(scrabble_game.end_game())

    def test_end_game_when_player_tiles_are_empty(self):
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.bag_tiles.tiles = ['A']
        scrabble_game.players[0].tiles = []
        scrabble_game.players[1].tiles = []
        scrabble_game.players[2].tiles = []
        self.assertFalse(scrabble_game.end_game())\
        
    def test_change_tiles(self):
        scrabble = ScrabbleGame(2)
        a = Tile('A',1)
        b = Tile('B',1)
        scrabble.bag_tiles.tiles = [b,b,b,b,b,b,b ,b,b,b,b,b,b,b ,b,b,b,b,b,b,b]
        scrabble.next_turn()
        scrabble.current_player.lectern = [a,a,a,a,a,a,a]
        result = scrabble.change_tiles((2,3))
        self.assertEqual(result, [a,a])
        self.assertEqual(len(scrabble.bag_tiles.tiles), 21)
        self.assertEqual([a,a,b,b,a,a,a], scrabble.current_player.lectern)

if __name__ == '__main__':
    unittest.main()