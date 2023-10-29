import unittest
from game.game_cell import Cell
from game.calculate_word_value import Calculate_word_value

class TestCalculateWordValue(unittest.TestCase):
    def test_calculate_word_value_no_multipliers(self):
        # Prueba cuando no hay multiplicadores de palabra
        cells = [Cell(1), Cell(2), Cell(3)]
        calculator = Calculate_word_value()
        result = calculator.calculate_word_value(cells)
        self.assertEqual(result, 6)

    def test_calculate_word_value_with_multiplier(self):
        # Prueba cuando hay un multiplicador de palabra
        cells = [Cell(1), Cell(2, 'word', 2), Cell(3)]
        calculator = Calculate_word_value()
        result = calculator.calculate_word_value(cells)
        self.assertEqual(result, 12)

if __name__ == '__main__':
    unittest.main()