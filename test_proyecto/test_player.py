import unittest
from game.game_player import Player
from game.game_cell import Cell
from game.models import Tile
from game.game_board import Board


class TestPlayer(unittest.TestCase):
    def test_init(self):
        player_1 = Player(1)
        player_2 = Player(2)
        player_3 = Player(3)
        self.assertEqual(player_1.id,1)
        self.assertEqual(player_2.id,2)
        self.assertEqual(player_3.id,3)

    def setUp(self):
        self.player = Player(1)
        self.player.tiles = [Tile('A', 1), Tile('B', 2), Tile('C', 3), Tile('D', 4)]
        self.player.board = Board()
        
    def test_get_score(self):
        # Simula una lista de celdas jugadas en el tablero
        self.player.board.played_cells = [Cell(1), Cell(2), Cell(3)]  # Ajusta esto según tu implementación

        # Simula el valor de las celdas jugadas
        self.player.board.played_cells[0].calculate_value = lambda: 5
        self.player.board.played_cells[1].calculate_value = lambda: 10
        self.player.board.played_cells[2].calculate_value = lambda: 3

        self.assertEqual(self.player.get_score(), 18)  # Ajusta esto según tus cálculos esperados

    def test_validate_word(self):
        self.player.tiles = [Tile('A', 1), Tile('B', 2), Tile('C', 3), Tile('D', 4)]
        # Caso de prueba válido
        self.assertTrue(self.player.validate_word('ABCD'))

        # Caso de prueba inválido
        self.assertFalse(self.player.validate_word('ABE'))

if __name__ == '__main__':
    unittest.main()
    