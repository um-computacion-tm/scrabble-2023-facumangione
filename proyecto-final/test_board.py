import unittest
from board import Board


class TestBoard(unittest.TestCase):
    def test_init(self):
        board = Board()
        self.assertEqual(
            len(board.grid),
            15,
        )
        
        
if __name__ == "__main__":
    unittest.main()        