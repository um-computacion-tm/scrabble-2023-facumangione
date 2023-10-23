import unittest
from game.game_board import Board
from game.models import Tile
from game.game_cell import Cell


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_board_initialization(self):
        self.assertEqual(len(self.board.grid), 15)
        self.assertEqual(len(self.board.grid[0]), 15)

    def test_validate_word_inside_board_horizontal(self):
        self.assertTrue(self.board.validate_word_inside_board("PALABRA", (0, 0), "H"))

    def test_validate_word_inside_board_vertical(self):
        self.assertTrue(self.board.validate_word_inside_board("PALABRA", (0, 0), "V"))

    def test_validate_word_out_of_board_horizontal(self):
        self.assertFalse(self.board.validate_word_inside_board("PALABRA", (0, 14), "H"))

    def test_validate_word_out_of_board_vertical(self):
        self.assertFalse(self.board.validate_word_inside_board("PALABRA", (14, 0), "V"))

    def test_word_placement_empty_board_horizontal(self):
        self.assertTrue(self.board.validate_word_place_board("PALABRA", (0, 0), "H"))

    def test_word_placement_empty_board_vertical(self):
        self.assertTrue(self.board.validate_word_place_board("PALABRA", (0, 0), "V"))

    def test_word_placement_overlap_horizontal(self):
        self.board.grid[0][0].add_letter(Tile("P", 1))
        self.assertFalse(self.board.validate_word_place_board("PALABRA", (0, 0), "H"))

    def test_word_placement_overlap_vertical(self):
        self.board.grid[0][0].add_letter(Tile("P", 1))
        self.assertFalse(self.board.validate_word_place_board("PALABRA", (0, 0), "V"))

    def test_word_placement_valid_horizontal(self):
        self.assertTrue(self.board.put_words_board("PALABRA", (0, 0), "H"))

    def test_word_placement_valid_vertical(self):
        self.assertTrue(self.board.put_words_board("PALABRA", (0, 0), "V"))

    def test_word_placement_invalid_horizontal(self):
        self.board.grid[0][0].add_letter(Tile("P", 1))
        self.assertFalse(self.board.put_words_board("PALABRA", (0, 0), "H"))

    def test_word_placement_invalid_vertical(self):
        self.board.grid[0][0].add_letter(Tile("P", 1))
        self.assertFalse(self.board.put_words_board("PALABRA", (0, 0), "V"))

    def test_generate_row_string_with_letters(self):
        row = [Tile("P", 1), Tile("A", 1), Tile("L", 1), Tile("A", 1), Tile("B", 1), Tile("R", 1), Tile("A", 1)]
        self.board.grid[0] = row
        row_str = self.board.generate_row_string(self.board.grid[0], None, 0)
        self.assertEqual(row_str, "P A L A B R A")

    def test_generate_row_string_with_multipliers(self):
        row = [Cell(multiplier_type="DL"), Cell(), Cell(multiplier_type="2L"), Cell(letter=Tile("A", 1))]
        self.board.grid[1] = row
        row_str = self.board.generate_row_string(self.board.grid[1], None, 1)
        self.assertEqual(row_str, "DL - 2L A")


if __name__ == '__main__':
    unittest.main()