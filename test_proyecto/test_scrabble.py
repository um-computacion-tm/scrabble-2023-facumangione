import unittest
from game.scrabble import ScrabbleGame
from game.models import Tile

class TestScrabble(unittest.TestCase):
    def test_scrabble(self):
        scrabble_1 = ScrabbleGame(3)
        self.assertIsNotNone(scrabble_1.board, None)
        self.assertEqual(len(scrabble_1.players),3)
        self.assertEqual(scrabble_1.turn, 0)
    
    def test_unique_id(self):
        game_1 = ScrabbleGame(1)
        game_2 = ScrabbleGame(1)
        self.assertNotEqual(game_1.gameid, game_2.gameid)

    def test_next_turn_when_game_is_starling(self):
        game = ScrabbleGame(2)
        game.next_turn()
        self.assertEqual(game.current_player,game.players[0])

    def test_next_turn_when_game_is_not_the_first_and_is_last(self):
        game = ScrabbleGame(2)    
        game.current_player = game.players[0]
        game.next_turn()
        self.assertEqual(game.current_player, game.players[1])   
        game.current_player = game.players[1]
        game.next_turn()
        self.assertEqual(game.current_player, game.players[0])

    def test_next_turn(self):
        game = ScrabbleGame(2)
        self.assertEqual(game.turn, 0)
        game.next_turn()
        self.assertEqual(game.turn, 1)

    def test_playing(self):
        game = ScrabbleGame(1)
        self.assertEqual(game.playing(), True)

    def test_validate_word(self):
        game = ScrabbleGame(2)
        word = "Facultad"
        location = (7, 7)
        orientation = "H"
        self.assertEqual(game.scrabble_validate_word(word,location,orientation), True)


    def test_calculate_score_word_with_single_letter(self):
        game = ScrabbleGame(2)
        # Define una palabra que contiene una única letra 'A' en una casilla con multiplicador de palabra 1 y valor de letra 1.
        word = "Facu"
        location = (4,0)
        orientation = "H"
        game.next_turn()
        # Verifica que la puntuación del jugador actual sea 0 al inicio.
        self.assertEqual(game.current_player.score, 0)
        game.scrabble_word_calculate_score(word, location, orientation)
        self.assertEqual(game.current_player.score, 8)

    def test_calculate_score_word_with_existing_score(self):
        game = ScrabbleGame(2)
        word = "Facu"
        location = (0,0)
        orientation = "H"
        game.next_turn()
        self.assertEqual(game.current_player.score, 0)
        game.scrabble_word_calculate_score(word, location, orientation)
        self.assertEqual(game.current_player.score, 27)

    def test_validate_word_false(self):
        game = ScrabbleGame(2)
        word = "Kadabra"
        location = (0,0)
        orientation = "H"
        self.assertEqual(game.scrabble_validate_word(word, location, orientation), False)

    def test_show_rack(self):
        game = ScrabbleGame(2)
        game.next_turn()
        game.current_player.rack = [Tile('A', 1), Tile('B',3), Tile('C',2)]
        self.assertEqual(game.show_rack(), "[A] [B] [C]")

    def test_put_word(self):
        game = ScrabbleGame(2)
        word = "Hola"
        location = (5, 4)
        orientation = "H"
        game.put_word(word, location, orientation)
        self.assertEqual(game.board.grid[5][4].letter.letter, "H")
        self.assertEqual(game.board.grid[5][5].letter.letter, "O")
        self.assertEqual(game.board.grid[5][6].letter.letter, "L")
        self.assertEqual(game.board.grid[5][7].letter.letter, "A")

    def test_show_amount_tiles_bag(self):
        game = ScrabbleGame(2)
        self.assertEqual(game.show_amount_tiles_bag(), 29)

    def test_shuffle_rack(self):
        game = ScrabbleGame(2)
        game.next_turn()
        game.current_player.rack = [Tile('A', 1), Tile('B',3), Tile('C',2)]
        game.shuffle_rack()
        self.assertEqual(len(game.current_player.rack), 3)

    def test_game_over_true(self):
        game = ScrabbleGame(2)
        game.bag_tiles.tiles = []
        self.assertEqual(game.game_over(), True)

    def test_game_over_false(self):
        game = ScrabbleGame(2)
        self.assertEqual(game.game_over(), False)

    def test_put_tiles_in_rack_all_players(self):
        game = ScrabbleGame(2)
        self.assertEqual(len(game.players[0].rack), 0)
        self.assertEqual(len(game.players[1].rack), 0)
        game.put_tiles_in_rack()
        self.assertEqual(len(game.players[0].rack), 7)
        self.assertEqual(len(game.players[1].rack), 7)

    def test_put_tiles_in_rack_one_player(self):
        game = ScrabbleGame(2)
        self.assertEqual(len(game.players[0].rack), 0)
        self.assertEqual(len(game.players[1].rack), 0)
        game.next_turn()
        game.next_turn()
        game.put_tiles_in_rack(1)
        self.assertEqual(len(game.players[0].rack), 0)
        self.assertEqual(len(game.players[1].rack), 1)

    def test_put_initial_tiles_bag(self):
        game = ScrabbleGame(2)
        self.assertEqual(len(game.bag_tiles.tiles), 29)
        game.put_initial_tiles_bag()
        self.assertEqual(len(game.bag_tiles.tiles), 100)


if __name__ == '__main__':
    unittest.main()