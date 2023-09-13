import unittest
from game.game_board import Board
from game.models import Tile



class TestBoard(unittest.TestCase):
    def test_init(self):
        board = Board()
        self.assertEqual(len(board.grid),15,)
        self.assertEqual(len(board.grid[5]),15,)

    def test_H_True_word_inside_board(self):
        board = Board()
        word = "Facultad"
        location = (3,10)
        orientation = 'H'
        word_is_valid = board.validate_word_inside_board(word,location,orientation)
        self.assertEqual(word_is_valid, True)

    def test_H_False_word_inside_board(self):
        board = Board()
        word = "Universidad"
        location = (6,10)
        orientation = 'h'
        word_is_valid = board.validate_word_inside_board(word,location,orientation)
        self.assertEqual(word_is_valid, False)

    def test_V_True_word_inside_board(self):
        board = Board()
        word = 'Terreno'
        location = (9,8)
        orientation = 'v'
        word_is_valid = board.validate_word_inside_board(word,location,orientation)
        self.assertEqual(word_is_valid, True)

    def test_V_False_word_inside_board(self):
        board = Board()
        word = 'Sierra'
        location = (15,10)
        orientation = 'V'
        word_is_valid = board.validate_word_inside_board(word,location,orientation)
        self.assertEqual(word_is_valid, False)

    def test_word_out_of_board(self):
        board = Board()
        word = "Facultad"
        location = (14,4)
        orientation = "H"

        word_is_valid = board.validate_word_inside_board(word, location, orientation)
        assert word_is_valid == False
    
    def test_board_is_empty(self):
        board = Board()
        assert board.is_empty == True

    def test_board_is_not_empty(self):
        board = Board()
        board.grid[7][7].add_letter(Tile('C', 1))
        return board.is_empty == False

    
    


    
if __name__ == '__main__':
    unittest.main()