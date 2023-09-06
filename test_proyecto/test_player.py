import unittest
from game.game_player import Player
from game.models import BagTiles, Tile


class TestPlayer(unittest.TestCase):
    def test_init(self):
        player_1 = Player()
        self.assertEqual(
            len(player_1.tiles),
            0,
        )
def test_draw_tiles(self):
    # Crea un jugador y una bolsa de letras
    player = Player()
    bag_tiles = BagTiles()

    # El jugador toma 5 letras de la bolsa
    player.draw_tiles(bag_tiles, 5)
    
    # Verifica que el jugador tenga 5 ,letras después de tomarlas
    self.assertEqual(len(player.tiles), 5)

def test_exchange_tiles(self):
    # Crea un jugador y una bolsa de letras
    player = Player()
    bag_tiles = BagTiles()
    player.draw_tiles(bag_tiles, 5)
    bag_tiles_count_before = len(bag_tiles.tiles)
    tiles_to_exchange = player.tiles[:2]
    tiles_count_before = len(player.tiles)
    player.exchange_tiles(bag_tiles, tiles_to_exchange)
    
    # Verifica que el jugador tenga la cantidad correcta de letras después del intercambio
    self.assertEqual(len(player.tiles), tiles_count_before - 2 + len(tiles_to_exchange))
    self.assertEqual(len(bag_tiles.tiles), bag_tiles_count_before)

def test_calculate_score(self):
    player = Player()

    # Clase simulada para representar una celda en el tablero
    class MockCell:
        def __init__(self, letter, multiplier, multiplier_type):
            self.letter = letter
            self.multiplier = multiplier
            self.multiplier_type = multiplier_type

        def calculate_value(self):
            return self.letter.value

    # Crea una lista de celdas simuladas con letras y multiplicadores
    cells = [
        MockCell(Tile('A', 1), 1, ''),
        MockCell(Tile('B', 2), 2, 'letter'),
        MockCell(Tile('C', 3), 1, 'word'), 
    ]

    # Calcula la puntuación del jugador usando las celdas simuladas
    score = player.calculate_score(cells)
    
    # Calcula la puntuación esperada basada en los valores y multiplicadores
    expected_score = (1 * 1) + (2 * 2) + (3 * 1)
    
    # Verifica que la puntuación calculada sea igual a la puntuación esperada
    self.assertEqual(score, expected_score)


if __name__ == '__main__':
    unittest.main()      