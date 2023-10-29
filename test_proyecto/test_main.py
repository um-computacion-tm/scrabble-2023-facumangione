import unittest
import sys
import io
from unittest.mock import patch
from unittest.mock import call
from game.models import Tile
from game.game_cell import Cell
from io import StringIO
from configure_game import Configure

class TestScrabbleGame(unittest.TestCase):
    def setUp(self):
        self.main_output = StringIO()
        self.real_stdout = sys.stdout
        sys.stdout = self.main_output

    def tearDown(self):
        sys.stdout = self.real_stdout

    @patch('builtins.input', side_effect=['3'])
    def test_vaild_player_count_input(self, mock_input):
        main = Configure()
        number = "2"
        self.assertEqual(main.valid_player_count(number), True)
        number = "name"
        self.assertEqual(main.valid_player_count(number), False)
    

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=['2'])
    def test_show_current_player(self, mock_input, mock_stdout):
        main = Configure()
        main.next_turn()
        main.show_current_player()
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "¡Bienvenido a Scrabble!\nTurno del jugador 1")

    @patch('builtins.input', side_effect=['2'])
    def test_next_turn_main(self, mock_input):
        main = Configure()
        self.assertEqual(main.game.turn, 0)
        main.next_turn()
        self.assertEqual(main.game.turn, 1)

    @patch('builtins.input', side_effect=['2', '2', '1', '3'])
    def test_exchange_tiles(self, mock_input):
        main = Configure()
        main.game.players[0].rack = [Tile('H', 4), Tile('O',1), Tile('L',1), Tile('A',1)]
        main.next_turn()
        main.exchange_tiles()
        self.assertEqual(len(main.game.players[0].rack), 4)

    @patch('builtins.input', side_effect=['2', 'x', 'y'])
    def test_reorganize(self, mock_input):
        main = Configure()
        main.game.players[0].rack = [Tile('H', 4), Tile('O',1), Tile('L',1), Tile('A',1)]
        main.next_turn()
        self.assertEqual(len(main.game.players[0].rack), 4)
        main.reorganize()
        self.assertEqual(len(main.game.players[0].rack), 4)

    @patch('builtins.input', side_effect=['2'])
    def test_add_score(self, mock_input):
        main = Configure()
        word = "Hola"
        location = (7, 7)
        orientation = "H"
        main.next_turn()
        self.assertEqual(main.game.current_player.score, 0)
        main.add_score(word, location, orientation)
        self.assertEqual(main.game.current_player.score, 14)

    @patch('builtins.input', side_effect=['2'])
    def test_initial_tiles(self, mock_input):
        main = Configure()
        self.assertEqual(len(main.game.bag_tiles.tiles), 29)
        self.assertEqual(len(main.game.players[0].rack), 0)
        self.assertEqual(len(main.game.players[1].rack), 0)
        main.initial_tiles()
        self.assertEqual(len(main.game.bag_tiles.tiles), 100-14)
        self.assertEqual(len(main.game.players[0].rack), 7)
        self.assertEqual(len(main.game.players[1].rack), 7)

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['2'])
    def test_show_board(self, mock_input, mock_print):
        main = Configure()
        main.board.grid = [ [Cell(), Cell()],[Cell(), Cell()]]
        main.show_board(main.board)
        expected_output = [ 
            call('\n  |  0   1 '),
            call(' 0|  -   - '),
            call(' 1|  -   - ')]
        mock_print.assert_has_calls(expected_output, any_order=False) 

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['4'])
    def test_show_scores(self, mock_input, mock_print):
        main = Configure()
        main.game.players[0].score = 90
        main.game.players[1].score = 172
        main.game.players[2].score = 78
        main.game.players[3].score = 134
        main.show_scores()
        expected_output = [
            call("¡Bienvenido a Scrabble!"),
            call("Puntajes de los jugadores:"),
            call("Jugador 2: Puntaje = 172"),
            call("Jugador 4: Puntaje = 134"),
            call("Jugador 1: Puntaje = 90"),
            call("Jugador 3: Puntaje = 78")
        ]
        mock_print.assert_has_calls(expected_output, any_order=False)


if __name__ == '__main__':
    unittest.main()