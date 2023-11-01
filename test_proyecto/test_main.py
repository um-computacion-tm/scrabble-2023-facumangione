import unittest
from unittest.mock import patch
from game.main import *
import io, sys

class TestMain(unittest.TestCase):
    @patch('builtins.input', side_effect = [2])
    def test_main(self, mock_input):
        main = Main()
        result = main.main()
        self.assertEqual(result, 2)

    @patch('builtins.input', side_effect = [5,2])
    def test_main(self, mock_input):
        main = Main() 
        output_buffer = io.StringIO()
        sys.stdout = output_buffer
        result = main.main()
        sys.stdout = sys.__stdout__
        printed_output = output_buffer.getvalue()
        output_buffer.close()
        expected = 'Bienvenido a Scrabble\nValor no valido\n'
        self.assertEqual(printed_output, expected)
        self.assertEqual(result, 2)

    def test_view_menu(self):
        main = Main()
        scrabble_game = ScrabbleGame(2)
        scrabble_game.players[0].name = 'Jugador 1'
        scrabble_game.players[1].name = 'Jugador 2'
        scrabble_game.next_turn()
        result = main.menu('menu', scrabble_game)
        expected = '''Turno del jugador Jugador 1

    Menu
    1) Tablero
    2) Atril
    3) Jugar 
    4) Puntuaciones
    5) Salir del juego
    Seleccion: '''
        self.maxDiff = None
        self.assertEqual(result, expected)

    def test_view_menu_board(self):
        main = Main()
        scrabble_game = ScrabbleGame(2)
        scrabble_game.players[0].name = 'Jugador 1'
        scrabble_game.players[1].name = 'Jugador 2'
        scrabble_game.next_turn()
        result = main.menu('board', scrabble_game)
        expected = '''Turno del jugador Jugador 1

    Menu
    1) Ver Tablero
    2) Volver
    Seleccion: '''
        self.assertEqual(result, expected)

    def test_view_menu_rack(self):
        main = Main()
        scrabble_game = ScrabbleGame(2)
        scrabble_game.players[0].name = 'Jugador 1'
        scrabble_game.players[1].name = 'Jugador 2'
        scrabble_game.next_turn()
        result = main.menu('lectern', scrabble_game)
        expected = '''Turno del jugador Jugador 1

    Menu
    1) Ver Atril
    2) Volver
    Seleccion: '''
        self.assertEqual(result, expected)

    def test_view_menu_actions(self):
        main = Main()
        scrabble_game = ScrabbleGame(2)
        scrabble_game.players[0].name = 'Jugador 1'
        scrabble_game.players[1].name = 'Jugador 2'
        scrabble_game.next_turn()
        result = main.menu('actions', scrabble_game)
        expected = '''Turno del jugador Jugador 1

    Acciones
    1) Colocar palabra
    2) Cambiar fichas
    3) Pasar turno
    4) Volver
    Seleccion: '''
        self.assertEqual(result, expected)

    def test_view_menu_put_word(self):
        main = Main()
        scrabble_game = ScrabbleGame(2)
        scrabble_game.players[0].name = 'Jugador 1'
        scrabble_game.players[1].name = 'Jugador 2'
        scrabble_game.next_turn()
        result = main.menu('put_word', scrabble_game)
        expected = '''Turno del jugador Jugador 1

    Colocar palabra
    1) Colocar palabra
    2) Volver
    Seleccion: '''
        self.assertEqual(result, expected)

    def test_view_menu_change_tiles(self):
        main = Main()
        scrabble_game = ScrabbleGame(2)
        scrabble_game.players[0].name = 'Jugador 1'
        scrabble_game.players[1].name = 'Jugador 2'
        scrabble_game.next_turn()
        result = main.menu('change_tiles', scrabble_game)
        expected = '''Turno del jugador Jugador 1

    Cambiar fichas
    1) Cambiar fichas
    2) Volver
    Seleccion: '''
        self.assertEqual(result, expected)

    def test_view_menu_next_turn(self):
        main = Main()
        scrabble_game = ScrabbleGame(2)
        scrabble_game.players[0].name = 'Jugador 1'
        scrabble_game.players[1].name = 'Jugador 2'
        scrabble_game.next_turn()
        result = main.menu('next_turn', scrabble_game)
        expected = '''Turno del jugador Jugador 1

    Pasar turno
    1) Pasar turno
    2) Volver
    Seleccion: '''
        self.assertEqual(result, expected)


    def test_view_menu_scores(self):
        main = Main()
        scrabble_game = ScrabbleGame(2)
        scrabble_game.players[0].name = 'Jugador 1'
        scrabble_game.players[1].name = 'Jugador 2'
        scrabble_game.next_turn()
        result = main.menu('scores', scrabble_game)
        expected = '''Turno del jugador Jugador 1

    Puntuaciones
    1) Ver puntuaciones
    2) Volver
    Seleccion: '''    
        self.assertEqual(result, expected)

    @patch('builtins.input', side_effect=[7,2])
    def test_menu_actions_change_tiles_exception(self, mock_input):
        main = Main()
        scrabble_game = ScrabbleGame(2)
        scrabble_game.players[0].name = 'Jugador 1'
        scrabble_game.players[1].name = 'Jugador 2'
        scrabble_game.next_turn()
        output_buffer = io.StringIO()
        sys.stdout = output_buffer
        main.menu_change_tiles(scrabble_game)
        sys.stdout = sys.__stdout__
        printed_output = output_buffer.getvalue()
        output_buffer.close()
        expected = '''Valor no valido\n'''
        self.maxDiff = None
        self.assertEqual(printed_output, expected)

    @patch('builtins.input', side_effect=[1,2])
    def test_menu_actions_next_turn(self, mock_input):
        main = Main ()
        scrabble_game = ScrabbleGame (2)
        scrabble_game.players [0] .name = 'Jugador 1'
        scrabble_game.players [1] .name = 'Jugador 2'
        scrabble_game.next_turn ()
        self.assertEqual(main.menu_next_turn (scrabble_game), 'Cambio de turno')
    
    @patch('builtins.input', side_effect=[7,2])
    def test_menu_actions_next_turn_exception(self, mock_input):
        main = Main()
        scrabble_game = ScrabbleGame(2)
        scrabble_game.players[0].name = 'Jugador 1'
        scrabble_game.players[1].name = 'Jugador 2'
        scrabble_game.next_turn()
        output_buffer = io.StringIO()
        sys.stdout = output_buffer
        main.menu_next_turn(scrabble_game)
        sys.stdout = sys.__stdout__
        printed_output = output_buffer.getvalue()
        output_buffer.close()
        expected = '''Valor invalido\n'''
        self.maxDiff = None
        self.assertEqual(printed_output, expected)

    @patch('builtins.input', side_effect=[1,2])
    def test_menu_actions_scores(self,mock_input):
        main = Main()
        scrabble_game = ScrabbleGame(2)
        scrabble_game.players[0].name = 'Jugador 1'
        scrabble_game.players[1].name = 'Jugador 2'
        scrabble_game.next_turn()
        output_buffer = io.StringIO()
        sys.stdout = output_buffer
        main.menu_scores(scrabble_game)
        sys.stdout = sys.__stdout__
        printed_output = output_buffer.getvalue()
        output_buffer.close()
        expected = '''Jugador 1: 0\nJugador 2: 0\n
'''
        self.maxDiff = None
        self.assertEqual(printed_output, expected)

    @patch('builtins.input', side_effect=[7,2])
    def test_menu_actions_scores_exception(self, mock_input):
        main = Main()
        scrabble_game = ScrabbleGame(2)
        scrabble_game.players[0].name = 'Jugador 1'
        scrabble_game.players[1].name = 'Jugador 2'
        scrabble_game.next_turn()
        output_buffer = io.StringIO()
        sys.stdout = output_buffer
        main.menu_scores(scrabble_game)
        sys.stdout = sys.__stdout__
        printed_output = output_buffer.getvalue()
        output_buffer.close()
        expected = '''Valor no valido\n'''
        self.maxDiff = None
        self.assertEqual(printed_output, expected)

    @patch('builtins.input', side_effect=[1,2])
    def test_menu_board(self,mock_input):
        main = Main()
        scrabble_game = ScrabbleGame(2)
        scrabble_game.players[0].name = 'Jugador 1'
        scrabble_game.players[1].name = 'Jugador 2'
        scrabble_game.next_turn()
        output_buffer = io.StringIO()
        sys.stdout = output_buffer
        main.menu_board(scrabble_game)
        sys.stdout = sys.__stdout__
        printed_output = output_buffer.getvalue()
        output_buffer.close()
        expected = ''' 
    0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 
A   3W|  |  |2L|  |  |  |3W|  |  |  |2L|  |  |3W|
B     |2W|  |  |  |3L|  |  |  |3L|  |  |  |2W|  |
C     |  |2W|  |  |  |2L|  |2L|  |  |  |2W|  |  |
D   2L|  |  |2W|  |  |  |2L|  |  |  |2W|  |  |2L|
E     |  |  |  |2W|  |  |  |  |  |2W|  |  |  |  |
F     |3L|  |  |  |3L|  |  |  |3L|  |  |  |3L|  |
G     |  |2L|  |  |  |2L|  |2L|  |  |  |2L|  |  |
H   3W|  |  |2L|  |  |  |2W|  |  |  |2L|  |  |3W|
I     |  |2L|  |  |  |2L|  |2L|  |  |  |2L|  |  |
J     |3L|  |  |  |3L|  |  |  |3L|  |  |  |3L|  |
K     |  |  |  |2W|  |  |  |  |  |2W|  |  |  |  |
L   2L|  |  |2W|  |  |  |2L|  |  |  |2W|  |  |2L|
M     |  |2W|  |  |  |2L|  |2L|  |  |  |2W|  |  |
N     |2W|  |  |  |3L|  |  |  |3L|  |  |  |2W|  |
O   3W|  |  |2L|  |  |  |3W|  |  |  |2L|  |  |3W|

'''
        self.maxDiff = None
        self.assertEqual(printed_output, expected)


    @patch('builtins.input', side_effect=[7,2])
    def test_menu_lectern_exception(self, mock_input):
        main = Main()
        scrabble_game = ScrabbleGame(2)
        scrabble_game.players[0].name = 'Jugador 1'
        scrabble_game.players[1].name = 'Jugador 2'
        scrabble_game.next_turn()
        output_buffer = io.StringIO()
        sys.stdout = output_buffer
        main.menu_lectern(scrabble_game)
        sys.stdout = sys.__stdout__
        printed_output = output_buffer.getvalue()
        output_buffer.close()
        expected = '''Valor invalido\n'''
        self.maxDiff = None
        self.assertEqual(printed_output, expected)
    
    @patch('builtins.input', side_effect=[1,4])
    def test_menu_actions_1(self,mock_input):
        main = Main()
        scrabble_game = ScrabbleGame(2)
        scrabble_game.players[0].name = 'Jugador 1'
        scrabble_game.players[1].name = 'Jugador 2'
        scrabble_game.next_turn()
        with patch.object(main, 'menu_put_word') as mock_put_word:
            main.menu_actions(scrabble_game)
            mock_put_word.assert_called_once()


    @patch('builtins.input', side_effect=[2,4])
    def test_menu_actions_2(self,mock_input):
        main = Main()
        scrabble_game = ScrabbleGame(2)
        scrabble_game.players[0].name = 'Jugador 1'
        scrabble_game.players[1].name = 'Jugador 2'
        scrabble_game.next_turn()
        with patch.object(main, 'menu_change_tiles') as mock_change_tiles:
            main.menu_actions(scrabble_game)
            mock_change_tiles.assert_called_once()
    
    @patch('builtins.input', side_effect=[3,4])
    def test_menu_actions_3(self,mock_input):
        main = Main()
        scrabble_game = ScrabbleGame(2)
        scrabble_game.players[0].name = 'Jugador 1'
        scrabble_game.players[1].name = 'Jugador 2'
        scrabble_game.next_turn()
        with patch.object(main, 'menu_next_turn') as mock_next_turn:
            main.menu_actions(scrabble_game)
            mock_next_turn.assert_called_once()

    @patch('builtins.input', side_effect=[3,3,4])
    @patch('game.main.Main.menu_next_turn', return_value='cambio de turno')
    def test_menu_actions_3_next_turn(self,mock_input, mock_next_turn):
        main = Main()
        scrabble_game = ScrabbleGame(2)
        scrabble_game.players[0].name = 'Jugador 1'
        scrabble_game.players[1].name = 'Jugador 2'
        scrabble_game.next_turn()
        main.menu_actions(scrabble_game)

    @patch('builtins.input', side_effect=[7,4])
    def test_menu_actions_exception(self, mock_input):
        main = Main()
        scrabble_game = ScrabbleGame(2)
        scrabble_game.players[0].name = 'Jugador 1'
        scrabble_game.players[1].name = 'Jugador 2'
        scrabble_game.next_turn()
        output_buffer = io.StringIO()
        sys.stdout = output_buffer
        main.menu_actions(scrabble_game)
        sys.stdout = sys.__stdout__
        printed_output = output_buffer.getvalue()
        output_buffer.close()
        expected = '''Valor no valido\n'''
        self.maxDiff = None
        self.assertEqual(printed_output, expected)

    def test_play_game_valid_option(self):
        main = Main()
        scrabble_game = ScrabbleGame(2)
        scrabble_game.next_turn()
        with unittest.mock.patch('builtins.input', side_effect=[1,2,2,2,3,4,4,2,5]):
            main.play_game(scrabble_game)


    def test_play_game_invalid_option(self):
        main = Main()
        scrabble_game = ScrabbleGame(2)
        scrabble_game.next_turn()
        output_buffer = io.StringIO()
        sys.stdout = output_buffer
        with unittest.mock.patch('builtins.input', side_effect=['abc',5]):
            self.assertFalse(main.play_game(scrabble_game))
        sys.stdout = sys.__stdout__
        output_buffer.close()

    @patch('builtins.input', side_effect=[2, 'Player1', 'Player2', 5])
    def test_play(self, mock_input):
        main = Main()
        main.play()

    @patch('builtins.input', side_effect=[1,2,2,2,3,4,4,2,5,1])
    def test_play_game(self, mock_input):
        main = Main()  
        scrabble_game = ScrabbleGame(2) 
        scrabble_game.players[0].name = 'Jugador 1'
        scrabble_game.players[1].name = 'Jugador 2'
        scrabble_game.next_turn()
        output_buffer = io.StringIO()
        sys.stdout = output_buffer
        main.play_game(scrabble_game)
        sys.stdout = sys.__stdout__
        printed_output = output_buffer.getvalue()
        output_buffer.close()

    @patch('builtins.input', side_effect=[7,5,1])
    def test_menu_play_game_exception(self, mock_input):
        main = Main()
        scrabble_game = ScrabbleGame(2)
        scrabble_game.players[0].name = 'Jugador 1'
        scrabble_game.players[1].name = 'Jugador 2'
        scrabble_game.next_turn()
        output_buffer = io.StringIO()
        sys.stdout = output_buffer
        main.play_game(scrabble_game)
        sys.stdout = sys.__stdout__
        printed_output = output_buffer.getvalue()
        output_buffer.close()
        expected = '''Valor no valido\n'''
        self.maxDiff = None
        self.assertEqual(printed_output, expected)

    @patch('builtins.input', side_effect=[2, 'Player1', 'Player2', 5,1])
    def test_play(self, mock_input):
        output_buffer = io.StringIO()
        sys.stdout = output_buffer
        main = Main()
        main.play()
        sys.stdout = sys.__stdout__
        printed_output = output_buffer.getvalue()
        output_buffer.close()


if __name__ == '__main__':
    unittest.main()