from game.main import Main
from game.game_board import Board
from game.game_cell import Cell
from game.models import Tile
import unittest
from unittest.mock import patch
from io import StringIO
from game.scrabble import ScrabbleGame
import sys

class TestMain(unittest.TestCase):
    def setUp(self):
        self.main_output = StringIO()
        self.real_stdout = sys.stdout
        sys.stdout = self.main_output

    def tearDown(self):
        sys.stdout = self.real_stdout

    @patch('builtins.input', side_effect=['3'])   
    def test_valid_player_count(self, mock_input):
        main = Main()
        number = "2"
        self.assertEqual(main.valid_player_count(number), True)

    @patch('builtins.input', side_effect=['3'])
    def test_valid_player_count_error(self, mock_input):
        main = Main()
        number = "name"
        self.assertEqual(main.valid_player_count(number), False)

    @patch('builtins.input', side_effect=['3']) 
    def test_player_count_input_valid(self, mock_input):
        main = Main()
        main.play()
        main_output_value = self.main_output.getvalue()
        self.assertIn('Bienvenido', main_output_value)
        self.assertIn('La cantidad de jugadores es: 3', main_output_value)
        self.assertIn('Turno del jugador 1', main_output_value)

    @patch('builtins.input', side_effect=['5', '3'])
    def test_player_count_input_invalid_then_valid(self, mock_input):
        main = Main()
        main.play()
        main_output_value = self.main_output.getvalue()
        self.assertIn('Bienvenido', main_output_value)
        self.assertIn('Valor inválido', main_output_value)
        self.assertIn('La cantidad de jugadores es: 3', main_output_value)
        self.assertIn('Turno del jugador 1', main_output_value)
    
    def test_add_letter(self):
        board = Board()
        board.add_letter(7, 7, Tile('A', 1))
        self.assertEqual(board.grid[7][7].letter.value, 1)  # Compara con el número 1 en lugar de 'A'
        self.assertEqual(board.is_empty, False)


    def test_validate_word_out_of_board(self):
        board = Board()
        word = "Python"
        location = (13, 1)
        orientation = "H"
        result = board.validate_word_out_of_board(word, location, orientation)
        self.assertEqual(result, True)

    def test_validate_word_place_board_horizontal_overlap(self):
        board = Board()
        board.grid[7][7] = Cell(1, 'A')
        word = "Apple"
        location = (7, 6)
        orientation = "H"
        result = board.validate_word_place_board(word, location, orientation)
        self.assertEqual(result, False)

    def test_validate_word_place_board_vertical_overlap(self):
        board = Board()
        board.grid[7][7] = Cell(1, 'A')
        word = "Apple"
        location = (6, 7)
        orientation = "V"
        result = board.validate_word_place_board(word, location, orientation)
        self.assertEqual(result, True)

    def get_player_count():
        while True:
            try:
                player_count = int(input('cantidad de jugadores (1-3): '))
                if player_count <= 3:
                    break
            except Exception as e:
                print('ingrese un numero por favor')

        return player_count

    @patch('builtins.print')
    @patch.object(ScrabbleGame, 'is_playing', side_effect=[True, False])
    @patch.object(ScrabbleGame, 'get_current_player', return_value=(0, "Player",))
    @patch.object(ScrabbleGame, 'play')

    def test_main(self, *args):
        Main()

if __name__ == '__main__':
    unittest.main()