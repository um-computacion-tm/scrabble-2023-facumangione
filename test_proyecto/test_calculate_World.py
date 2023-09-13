import unittest
from game.game_calcute import Calculate_word_value
from game.game_cell import Cell
from game.models import Tile

class TestsCalculateWordValue(unittest.TestCase):
    def test_simple(self):
        # Prueba simple con multiplicadores de letra
        # Comentario explicativo
        word = [
            Cell(multiplier=1, multiplier_type='letter'),
            Cell(multiplier=1, multiplier_type='letter'),
            Cell(multiplier=1, multiplier_type='letter'),
            Cell(multiplier=1, multiplier_type='letter'),
        ]
        
        letters = ["C", "A", "S", "A"]
        for i, cell in enumerate(word):
            cell.add_letter(Tile(letter=letters[i], value=1))

        value = Calculate_word_value.calculate(word)
        self.assertEqual(value, 4)

    # Agregar más pruebas aquí para cubrir otros casos y ramas del código

if __name__ == '__main__':
    unittest.main()