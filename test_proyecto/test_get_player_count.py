import unittest
from unittest.mock import patch
from game.get_player_count import GetPlayerCount

class TestGetPlayerCount(unittest.TestCase):

    @patch('builtins.input', side_effect=['2'])
    def test_get_player_count_valid(self, mock_input):
        game = GetPlayerCount()
        game.get_player_count()
        self.assertEqual(game.player_count, 2)

    @patch('builtins.input', side_effect=['5', '3'])
    def test_get_player_count_invalid_then_valid(self, mock_input):
        game = GetPlayerCount()
        game.get_player_count()
        self.assertEqual(game.player_count, 3)

    @patch('builtins.input', side_effect=['a', '1'])
    def test_get_player_count_invalid_then_valid_type_error(self, mock_input):
        game = GetPlayerCount()
        game.get_player_count()
        self.assertEqual(game.player_count, 1)

    @patch('builtins.input', side_effect=['0', '4'])
    def test_get_player_count_invalid_then_valid_out_of_range(self, mock_input):
        game = GetPlayerCount()
        game.get_player_count()
        self.assertEqual(game.player_count, 4)

if __name__ == "__main__":
    unittest.main()