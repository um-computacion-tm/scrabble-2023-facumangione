import unittest
from game.game_calculate import Calculate_word_value
from game.game_cell import Cell
from game.models import Tile


import unittest  # Agrega esta línea para importar unittest

class TestsCalculateWordValue(unittest.TestCase):
    def test_simple(self):
        word = [
            Cell(multiplier=1, multiplier_type='letter',value=1),
            Cell(multiplier=1, multiplier_type='letter',value=1),
            Cell(multiplier=1, multiplier_type='letter',value=1),
            Cell(multiplier=1, multiplier_type='letter',value=1),
        ]
        
        letters = ["C", "A", "S", "A"]
        for i, cell in enumerate(word):
            cell.add_letter(Tile(letter=letters[i], value=1))

        value = Calculate_word_value.calculate_word_value(word)
        self.assertEqual(value, 4)  


    def test_with_letter_multiplier(self):
        word = [
            Cell(multiplier=1, multiplier_type='letter',value=1),
            Cell(multiplier=1, multiplier_type='letter',value=1),
            Cell(multiplier=2, multiplier_type='letter',value=1),  # Usar multiplier y multiplier_type en lugar de letter y value
            Cell(multiplier=1, multiplier_type='letter',value=1),
        ]
        letters = ["C", "A", "S", "A"]
        for i, cell in enumerate(word):
            cell.add_letter(Tile(letter=letters[i], value=1))

        value = Calculate_word_value.calculate_word_value(word)
        self.assertEqual(value, 5)

    def test_with_word_multiplier(self):
        word = [
            Cell(multiplier=1, multiplier_type='letter'),
            Cell(multiplier=1, multiplier_type='letter'),
            Cell(multiplier=2, multiplier_type='word'),  # Usamos multiplier_type 'word'
            Cell(multiplier=1, multiplier_type='letter'),
        ]
        letters = ["C", "A", "S", "A"]
        for i, cell in enumerate(word):
            cell.add_letter(Tile(letter=letters[i], value=1))

        value = Calculate_word_value.calculate_word_value(word)
        self.assertEqual(value, 8)


    def test_with_word_multiplier(self):
        word = [
            Cell(letter=Tile("C", 1)),
            Cell(letter=Tile("A", 1)),
            Cell(letter=Tile("S", 2), multiplier=2, multiplier_type="word"),
            Cell(letter=Tile("A", 1)),
        ]
        value = Calculate_word_value.calculate_word_value(word)
        self.assertEqual(value, 10)

    def test_with_letter_word_multiplier(self):
        word = [
            Cell(letter=Tile("C", 1), multiplier=3, multiplier_type="letter"),
            Cell(letter=Tile("A", 1)),
            Cell(letter=Tile("S", 2), multiplier=2, multiplier_type="word"),
            Cell(letter=Tile("A", 1)),
        ]
        value = Calculate_word_value.calculate_word_value(word)
        self.assertEqual(value, 14)

        
    def test_with_letter_word_multiplier_active(self):
        word = [
            Cell(letter=Tile("C", 1), multiplier=3, multiplier_type="letter"),
            Cell(letter=Tile("A", 1)),
            Cell(letter=Tile("S", 2), multiplier=2, multiplier_type="word"),
            Cell(letter=Tile("A", 1)),
        ]
        for index in range(4):
            word[index].active = False
        value = Calculate_word_value.calculate_word_value(word)
        self.assertEqual(value, 7)

    def test_with_letter_word_multiplier_no_active(self):
        word = [
            Cell(letter=Tile("C", 1), multiplier=3, multiplier_type="letter"),
            Cell(letter=Tile("A", 1)),
            Cell(letter=Tile("S", 2), multiplier=2, multiplier_type="word"),
            Cell(letter=Tile("A", 1)),
        ]
        value = Calculate_word_value.calculate_word_value(word)
        self.assertEqual(value, 14)


if __name__ == '__main__':
    unittest.main()