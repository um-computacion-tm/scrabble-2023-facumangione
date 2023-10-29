import unittest
from game.game_cell import Cell
from game.models import Tile
from game.several import Several

class TestCell(unittest.TestCase):
    def test_init(self):
        cell = Cell(multiplier=2, multiplier_type='letter')
        self.assertEqual(
            cell.multiplier,2,)
        self.assertEqual(
            cell.multiplier_type,
            'letter',)
        self.assertIsNone(cell.letter)
        self.assertEqual(
            cell.calculate_value(),0,)

    def test_add_letter(self):
        cell = Cell(multiplier=1, multiplier_type='')
        letter = Tile(letter='p', value=3)
        cell.add_letter(letter=letter)
        self.assertEqual(cell.letter, letter)

    def test_cell_value(self):
        cell = Cell(multiplier=2, multiplier_type='letter')
        letter = Tile(letter='p', value=3)
        cell.add_letter(letter=letter)
        self.assertEqual(
            cell.calculate_value(),6,)

    def test_cell_multiplier_word(self):
        cell = Cell(multiplier=2, multiplier_type='word')
        letter = Tile(letter='p', value=3)
        cell.add_letter(letter=letter)
        self.assertEqual(
            cell.calculate_value(),3,)

    def test_repr_active(self):
        cell = Cell(2, "word")
        sev = Several()
        self.assertEqual(repr(cell), sev.format_active_cell(cell))

    def test_repr_deactive(self):
        cell = Cell(2, "word", status="deactive")
        sev = Several()
        self.assertEqual(repr(cell), sev.format_cell_contents(cell))


if __name__ == '__main__':
    unittest.main()