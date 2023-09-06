import unittest
from game.game_board import Board
from game.models import Tile

class TestBoard(unittest.TestCase):
    def test_init(self):
        board = Board()
        self.assertEqual(
            len(board.grid),
            15,
        )
        self.assertEqual(
            len(board.grid[0]),
            15,
        )
        self.assertEqual(
            len(board.grid[0]),
            15,
        )

    def test_board_cell_00(self):
        board = Board()
        cell = board.grid
        self.assertEqual(cell[0][0].multiplier,3 )
        self.assertEqual(cell[0][0].multiplier_type,'word' )
    
    def test_board_cell_77(self):
        board = Board()
        cell = board.grid
        self.assertEqual(cell[7][7].multiplier,2 )
        self.assertEqual(cell[7][7].multiplier_type,'word' )

    def test_place_tile(self):
        board = Board()
        tile = Tile('A', 1)
        self.assertTrue(board.place_tile(7, 7, tile))
        self.assertFalse(board.place_tile(7, 7, tile))
        
    def test_validate_word(self):
        board = Board()
        tile_a = Tile('A', 1)
        tile_b = Tile('B', 2)
        tile_c = Tile('C', 3)

        board.place_tile(7, 7, tile_a)
        board.place_tile(7, 8, tile_b)
        board.place_tile(7, 9, tile_c)

        self.assertTrue(board.validate_word(7, 7, 'ABC', 'horizontal'))
        self.assertFalse(board.validate_word(7, 7, 'ACB', 'horizontal'))
        self.assertTrue(board.validate_word(7, 7, 'A', 'vertical'))
        self.assertFalse(board.validate_word(7, 7, 'AB', 'vertical'))


if __name__ == '__main__':
    unittest.main()