import unittest
from game.game_player import Player
from game.game_cell import Cell
from game.models import Tile
from game.game_board import Board
from game.models import BagTiles


class TestPlayer(unittest.TestCase):
    def test_init(self):
        player_1 = Player(1)
        player_2 = Player(2)
        player_3 = Player(3)
        self.assertEqual(player_1.id,1)
        self.assertEqual(player_2.id,2)
        self.assertEqual(player_3.id,3)
        self.bag_tile = BagTiles() 
        self.player = Player(1)

    def setUp(self):
        self.player = Player(1)
        self.player.tiles = [Tile('A', 1), Tile('B', 2), Tile('C', 3), Tile('D', 4)]
        self.player.board = Board()
        
    def test_get_score(self):
        # Simula una lista de celdas jugadas en el tablero
        self.player.board.played_cells = [Cell(1), Cell(2), Cell(3)]  # Ajusta esto según tu implementación

        # Simula el valor de las celdas jugadas
        self.player.board.played_cells[0].calculate_value = lambda: 5
        self.player.board.played_cells[1].calculate_value = lambda: 10
        self.player.board.played_cells[2].calculate_value = lambda: 3

        self.assertEqual(self.player.get_score(), 18)  # Ajusta esto según tus cálculos esperados

    def test_validate_word(self):
        self.player.tiles = [Tile('A', 1), Tile('B', 2), Tile('C', 3), Tile('D', 4)]
        # Caso de prueba válido
        self.assertTrue(self.player.validate_word('ABCD'))

        # Caso de prueba inválido
        self.assertFalse(self.player.validate_word('ABE'))
    
    def test_validate_user_has_letters(self):
        bag_tile = BagTiles()
        bag_tile.tiles = [
            Tile(letter='H', value=1),
            Tile(letter='O', value=1),
            Tile(letter='L', value=1),
            Tile(letter='A', value=1),
            Tile(letter='C', value=1),
            Tile(letter='U', value=1),
            Tile(letter='M', value=1),
    ]
        player = Player(bag_tile)
        tiles_to_check = [
            Tile(letter='H', value=1),
            Tile(letter='O', value=1),
            Tile(letter='L', value=1),
            Tile(letter='A', value=1),
    ]

        is_valid = player.has_letters(tiles_to_check, bag_tile)  # Pasar bag_tile también

        self.assertEqual(is_valid, True)
    
    def test_validate_fail_when_user_has_not_letters(self):
        bag_tile = BagTiles()
        bag_tile.tiles = [
            Tile(letter='P', value=1),
            Tile(letter='O', value=1),
            Tile(letter='L', value=1),
            Tile(letter='A', value=1),
            Tile(letter='C', value=1),
            Tile(letter='U', value=1),
            Tile(letter='M', value=1),
    ]
        player = Player(bag_tile)
        tiles_to_check = [
            Tile(letter='H', value=1),
            Tile(letter='O', value=1),
            Tile(letter='L', value=1),
            Tile(letter='A', value=1),
    ]

        is_valid = player.has_letters(tiles_to_check, bag_tile)  # Pasar bag_tile también

        self.assertEqual(is_valid, False)

    def test_directory_word_in_spanish(self):
        bag_tile = BagTiles()
        bag_tile.tiles = [
            Tile(letter='P', value=1),
            Tile(letter='O', value=1),
            Tile(letter='E', value=1),
            Tile(letter='A', value=1),
            Tile(letter='R', value=1),
            Tile(letter='U', value=1),
            Tile(letter='M', value=1),
    ]

        player = Player(bag_tile)
        tiles_to_check = [
            
            #[https://dle.rae.es/]

        ]

    def test_pass_turn(self):
        # Agrega algunas fichas al rack del jugador para el test
        self.player.tiles = [Tile('A',1), Tile('B',1), Tile('C',1)]

        # Verifica que el rack del jugador contenga fichas antes de pasar el turno
        self.assertNotEqual(len(self.player.tiles), 0)

        # Llama a la función pass_turn para pasar el turno
        self.player.pass_turn()

        # Verifica que el rack del jugador esté vacío después de pasar el turno
        self.assertEqual(len(self.player.tiles), 0)

        #completar más



if __name__ == '__main__':
    unittest.main()