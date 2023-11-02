import unittest
from game.board import *
from game.cell import *
from unittest.mock import patch


class TestBoard(unittest.TestCase):
    def test_init(self):
        board = Board()
        self.assertEqual(len(board.grid),15)
        self.assertEqual(len(board.grid[0]),15)

    def test_board_is_empty(self):
        board = Board()
        self.assertEqual( board.is_empty(), True)

    def test_board_is_not_empty(self):
        board = Board()
        board.grid[7][7].add_letter(Tile('C', 1))
        assert board.is_empty() == False

    @patch('game.board.dle.search_by_word')
    def test_word_inside_board_h(self, mock_rae):
        mock_rae.return_value.meta_description = 'casa | Definición | Diccionario de la lengua española | RAE - ASALE'
        board = Board()
        word = 'CASA'
        location = (7, 7)
        horizontal = 'H'
        word_is_valid = board.validate(word, location, horizontal)
        self.assertEqual(word_is_valid, True)
    
    @patch('game.board.dle.search_by_word')
    def test_word_out_of_board_h(self, mock_rae):
        mock_rae.return_value.meta_description = 'facultades | Definición | Diccionario de la lengua española | RAE - ASALE'
        board = Board()
        word = 'FACULTADES'
        location = (7, 7)
        horizontal = 'H'
        word_is_valid = board.validate(word, location, horizontal)
        self.assertEqual(word_is_valid, False)

    @patch('game.board.dle.search_by_word')
    def test_word_inside_board_v(self, mock_rae):
        mock_rae.return_value.meta_description = 'casa | Definición | Diccionario de la lengua española | RAE - ASALE'
        board = Board()
        word = 'CASA'
        location = (7, 7)
        horizontal = 'V'
        word_is_valid = board.validate(word, location, horizontal)
        self.assertEqual(word_is_valid, True)
    
    @patch('game.board.dle.search_by_word')
    def test_word_out_of_board_v(self, mock_rae):
        mock_rae.return_value.meta_description = 'facultades | Definición | Diccionario de la lengua española | RAE - ASALE'
        board = Board()
        word = 'FACULTADES'
        location = (7, 7)
        horizontal = 'V'
        word_is_valid = board.validate(word, location, horizontal)
        self.assertEqual(word_is_valid, False)
   
    @patch('game.board.dle.search_by_word')
    def test_validate_intersection_v(self, mock_rae):
        mock_rae.return_value.meta_description = 'laso | Definición | Diccionario de la lengua española | RAE - ASALE'
        board = Board()
        board.grid[7][7].tile = Tile("C",1)
        board.grid[7][8].tile = Tile("A",1)
        board.grid[7][9].tile = Tile("S",2)
        board.grid[7][10].tile = Tile("A",1)
        word = "LASO"
        orientation = "V"
        location = (6,8)
        self.assertEqual(board.validate(word, location, orientation), False)

    @patch('game.board.dle.search_by_word')
    def test_validate_intersection_v_fail(self, mock_rae):
        mock_rae.return_value.meta_description != 'Versión electrónica 23.6 del «Diccionario de la lengua española», obra lexicográfica académica por excelencia.' 
        board = Board()
        board.grid[7][7].tile = Tile("C",1)
        board.grid[7][8].tile = Tile("A",1)
        board.grid[7][9].tile = Tile("S",2)
        board.grid[7][10].tile = Tile("A",1)
        word = "LSSO"
        orientation = "V"
        location = (6,8)
        self.assertEqual(board.validate(word, location, orientation), False)

    @patch('game.board.dle.search_by_word')
    def test_invalidate_intersection_h(self, mock_rae):
        mock_rae.return_value.meta_description = 'laso | Definición | Diccionario de la lengua española | RAE - ASALE'
        board = Board()
        board.grid[7][7].tile = Tile("C",1)
        board.grid[8][7].tile = Tile("A",1)
        board.grid[9][7].tile = Tile("S",2)
        board.grid[10][7].tile = Tile("A",1)
        word = "LASO"
        orientation = "H"
        location = (8,6)
        self.assertEqual(board.validate(word, location, orientation), False)

    @patch('game.board.dle.search_by_word')
    def test_validate_intersection_h_fail(self, mock_rae):
        mock_rae.return_value.meta_description = 'Versión electrónica 23.6 del «Diccionario de la lengua española», obra lexicográfica académica por excelencia.' 
        board = Board()
        board.grid[7][7].tile = Tile("C",1)
        board.grid[8][7].tile = Tile("A",1)
        board.grid[9][7].tile = Tile("S",2)
        board.grid[10][7].tile = Tile("A",1)
        word = "LSSO"
        orientation = "H"
        location = (8,6)
        self.assertEqual(board.validate(word, location, orientation), False)

    @patch('game.board.dle.search_by_word')
    def test_validate_intersection_in_right(self, mock_rae):
        mock_rae.return_value.meta_description = 'cosa | Definición | Diccionario de la lengua española | RAE - ASALE'
        board = Board()
        board.grid[7][7].tile = Tile("C",1)
        board.grid[7][8].tile = Tile("A",1)
        board.grid[7][9].tile = Tile("S",2)
        board.grid[7][10].tile = Tile("A",1)
        board.grid[6][10].tile = Tile("L",1)
        board.grid[8][10].tile = Tile("S",2)
        board.grid[9][10].tile = Tile("O",1)
        board.grid[9][8].tile = Tile("O",1)
        board.grid[9][9].tile = Tile("S",2)
        word = "COSA"
        orientation = "V" 
        location = (7,7)
        self.assertEqual(board.validate_right(word, location, orientation), True)

    @patch('game.board.dle.search_by_word')
    def test_validate_intersection_in_right_invalid(self, mock_rae):
        mock_rae.return_value.meta_description = 'Versión electrónica 23.6 del «Diccionario de la lengua española», obra lexicográfica académica por excelencia.' 
        board = Board()
        board.grid[7][7].tile = Tile("C",1)
        board.grid[7][8].tile = Tile("A",1)
        board.grid[7][9].tile = Tile("S",2)
        board.grid[7][10].tile = Tile("A",1)
        board.grid[6][10].tile = Tile("L",1)
        board.grid[7][10].tile = Tile("A",1)
        board.grid[8][10].tile = Tile("S",2)
        board.grid[9][10].tile = Tile("O",1)
        board.grid[9][8].tile = Tile("O",1)
        board.grid[9][9].tile = Tile("S",2)
        board.grid[9][10].tile = Tile("O",1)
        word = "CAOS"
        orientation = "V" 
        location = (7,7)
        self.assertEqual(board.validate_right(word, location, orientation), False)    

    @patch('game.board.dle.search_by_word')
    def test_validate_intersection_in_left(self, mock_rae):
        mock_rae.return_value.meta_description = 'caso | Definición | Diccionario de la lengua española | RAE - ASALE'
        board = Board()
        board.grid[7][7].tile = Tile("C",1)
        board.grid[7][8].tile = Tile("A",1)
        board.grid[7][9].tile = Tile("S",2)
        board.grid[7][10].tile = Tile("A",1)
        board.grid[6][8].tile = Tile("L",1)
        board.grid[7][8].tile = Tile("A",1)
        board.grid[8][8].tile = Tile("S",2)
        board.grid[9][8].tile = Tile("O",1)
        board.grid[9][8].tile = Tile("O",1)
        board.grid[9][9].tile = Tile("S",2)
        board.grid[9][10].tile = Tile("O",1)
        word = "CASO"
        orientation = "V" 
        location = (5,11)
        self.assertEqual(board.validate_left(word, location, orientation), True) 

    @patch('game.board.dle.search_by_word')
    def test_validate_intersection_in_left_invalid(self, mock_rae):
        mock_rae.return_value.meta_description = 'Versión electrónica 23.6 del «Diccionario de la lengua española», obra lexicográfica académica por excelencia.' 
        board = Board()
        board.grid[7][7].tile = Tile("C",1)
        board.grid[7][8].tile = Tile("A",1)
        board.grid[7][9].tile = Tile("S",2)
        board.grid[7][10].tile = Tile("A",1)
        board.grid[6][8].tile = Tile("L",1)
        board.grid[7][8].tile = Tile("A",1)
        board.grid[8][8].tile = Tile("S",2)
        board.grid[9][8].tile = Tile("O",1)
        board.grid[9][8].tile = Tile("O",1)
        board.grid[9][9].tile = Tile("S",2)
        board.grid[9][10].tile = Tile("O",1)
        word = "CAOS"
        orientation = "V" 
        location = (5,11)
        self.assertEqual(board.validate_left(word, location, orientation), False) 

    def test_put_word_v(self):
        board = Board()
        word = [Tile('C',1),Tile('O',1),Tile('S',2),Tile('A',1)]
        orientation = 'V'
        location = (4,5)
        board.put_word(word, location, orientation)
        word_in_board = ''
        for i in range(4):
            word_in_board += board.grid[4+i][5].tile.letter
        self.assertEqual(word_in_board , 'COSA')

    def test_put_word_h(self):
        board = Board()
        word = [Tile('C',1),Tile('O',1),Tile('S',2),Tile('A',1)]
        orientation = 'H'
        location = (5,4)
        board.put_word(word, location, orientation)
        word_in_board = ''
        for i in range(4):
            word_in_board += board.grid[5][4+i].tile.letter
        self.assertEqual(word_in_board , 'COSA')

    def test_valid_accent_word(self):
        board = Board()
        word = "Árbol"
        self.assertEqual(board.words_with_accent(word), 'ARBOL')

    def test_valid_accent_rest_of_words(self):
        board = Board()
        word1 = "Éste"
        word2 = "ahí"
        word3 = "cocción"
        word4 = "última"
        self.assertEqual(board.words_with_accent(word1), 'ESTE')
        self.assertEqual(board.words_with_accent(word2), 'AHI')
        self.assertEqual(board.words_with_accent(word3), 'COCCION')
        self.assertEqual(board.words_with_accent(word4), 'ULTIMA') 

    def test_board_in_terminal_empty(self):
        board = Board()
        result = board.board_in_terminal()
        expected = """ 
    0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 
A   3W|  |  |2L|  |  |  |3W|  |  |  |2L|  |  |3W|
B     |2W|  |  |  |3L|  |  |  |3L|  |  |  |2W|  |
C     |  |2W|  |  |  |2L|  |2L|  |  |  |2W|  |  |
D   2L|  |  |2W|  |  |  |2L|  |  |  |2W|  |  |2L|
E     |  |  |  |2W|  |  |  |  |  |2W|  |  |  |  |
F     |3L|  |  |  |3L|  |  |  |3L|  |  |  |3L|  |
G     |  |2L|  |  |  |2L|  |2L|  |  |  |2L|  |  |
H   3W|  |  |2L|  |  |  |2W|  |  |  |2L|  |  |3W|
I     |  |2L|  |  |  |2L|  |2L|  |  |  |2L|  |  |
J     |3L|  |  |  |3L|  |  |  |3L|  |  |  |3L|  |
K     |  |  |  |2W|  |  |  |  |  |2W|  |  |  |  |
L   2L|  |  |2W|  |  |  |2L|  |  |  |2W|  |  |2L|
M     |  |2W|  |  |  |2L|  |2L|  |  |  |2W|  |  |
N     |2W|  |  |  |3L|  |  |  |3L|  |  |  |2W|  |
O   3W|  |  |2L|  |  |  |3W|  |  |  |2L|  |  |3W|
"""
        self.maxDiff = None
        self.assertEqual(result, expected)

    def test_board_in_terminal_word_v(self):
        board = Board()
        board.grid[7][7].tile = 'CH'
        board.grid[8][7].tile = 'A'
        board.grid[9][7].tile = 'S'
        board.grid[10][7].tile = 'A'
        result = board.board_in_terminal()
        expected = """ 
    0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 
A   3W|  |  |2L|  |  |  |3W|  |  |  |2L|  |  |3W|
B     |2W|  |  |  |3L|  |  |  |3L|  |  |  |2W|  |
C     |  |2W|  |  |  |2L|  |2L|  |  |  |2W|  |  |
D   2L|  |  |2W|  |  |  |2L|  |  |  |2W|  |  |2L|
E     |  |  |  |2W|  |  |  |  |  |2W|  |  |  |  |
F     |3L|  |  |  |3L|  |  |  |3L|  |  |  |3L|  |
G     |  |2L|  |  |  |2L|  |2L|  |  |  |2L|  |  |
H   3W|  |  |2L|  |  |  |CH|  |  |  |2L|  |  |3W|
I     |  |2L|  |  |  |2L|A |2L|  |  |  |2L|  |  |
J     |3L|  |  |  |3L|  |S |  |3L|  |  |  |3L|  |
K     |  |  |  |2W|  |  |A |  |  |2W|  |  |  |  |
L   2L|  |  |2W|  |  |  |2L|  |  |  |2W|  |  |2L|
M     |  |2W|  |  |  |2L|  |2L|  |  |  |2W|  |  |
N     |2W|  |  |  |3L|  |  |  |3L|  |  |  |2W|  |
O   3W|  |  |2L|  |  |  |3W|  |  |  |2L|  |  |3W|
""" 
        self.maxDiff = None
        self.assertEqual(result, expected)
       
class TestDiccionary(unittest.TestCase):
    @patch(
        'pyrae.dle.search_by_word',
        return_value=unittest.mock.MagicMock(
            meta_description='1. interj. U. como salutación familiar.'
        )
    )
    def test_valid(self, search_by_word_patched):
        board = Board()
        self.assertTrue(board.validate_word('hola'))

    @patch(
        'pyrae.dle.search_by_word',
        return_value=unittest.mock.MagicMock(
            meta_description='Versión electrónica 23.6 del «Diccionario de la lengua española», obra lexicográfica académica por excelencia.'
        )
    )
    def test_invalid(self, search_by_word_patched):
        board = Board()
        self.assertFalse(board.validate_word('asd'))

    @patch(
        'pyrae.dle.search_by_word',
        return_value=None
    )
    def test_connection_error(self, search_by_word_patched):
        board = Board()
        with self.assertRaises(DictionaryConnectionError):
            board.validate_word('hola')


    def test_put_word_v_intersections(self):
        board = Board()
        board.grid[7][6].tile = Tile('C',3)
        board.grid[7][7].tile = Tile('A',1)
        board.grid[7][8].tile = Tile('S',1)
        board.grid[7][9].tile = Tile('A',1)
        word = [Tile('L',3), Tile('S',6), Tile('O',1)]
        location = (6, 7)
        horizontal = 'V'
        board.put_word(word,location,horizontal)
        word_in_board = ''
        for i in range(4):
            word_in_board += board.grid[6+i][7].tile.letter
        self.assertEqual('LASO',word_in_board)

class TestCalculateWordValue(unittest.TestCase):
    def test_simple(self):
        board = Board()        
        word = 'casa'
        pos=(10,6)
        value = board.calculate_word_value(word, pos, 'H')
        self.assertEqual(value, 6)

    def test_simple_with_double_letter(self):
        board = Board()
        word = 'lluvia'
        pos=(10,5)
        value = board.calculate_word_value(word, pos, 'H')
        self.assertEqual(value, 8+1+4+1+1)
        
    def test_with_word_multiplier_2(self):
        board = Board()        
        word = 'casa'
        pos=(7,6)
        value = board.calculate_word_value(word, pos, 'H')
        self.assertEqual(value, 12)

    def test_with_word_multiplier_3(self):
        board = Board()        
        word = 'casa'
        pos=(14,6)
        value = board.calculate_word_value(word, pos, 'H')
        self.assertEqual(value, 18)

    def test_with_letter_multiplier_2(self):
        board = Board()        
        word = 'casa'
        pos=(8,8)
        value = board.calculate_word_value(word, pos, 'H')
        self.assertEqual(value, 9)

    def test_with_letter_multiplier_3(self):
        board = Board()        
        word = 'casa'
        pos=(9,8)
        value = board.calculate_word_value(word, pos, 'H')
        self.assertEqual(value, 8)

    def test_with_letter_multiplier_and_word_multiplier(self):
        board = Board()        
        word = 'casa'
        pos=(14,0)
        value = board.calculate_word_value(word, pos, 'H')
        self.assertEqual(value, 21)

    def test_with_letter_multiplier_and_word_multiplier_no_active(self):
        board = Board()        
        word = 'casa'
        pos=(14,0)
        value = board.calculate_word_value(word, pos, 'H')
        value = board.calculate_word_value(word, pos, 'H')
        self.assertEqual(value, 6)

    # def test_simple_intersection(self):
    #     board = Board()
    #     board.grid[7][2].tile = Tile('E', 1)
    #     board.grid[7][3].tile = Tile('S', 1)
    #     board.grid[7][4].tile = Tile('T', 1)
    #     board.grid[7][5].tile = Tile('R', 1)
    #     board.grid[7][6].tile = Tile('E', 1)
    #     board.grid[7][7].tile = Tile('N', 1)
    #     board.grid[7][8].tile = Tile('O', 1)
    #     board.grid[7][7].active = False
    #     word = 'mes'
    #     pos=(6,6)
    #     value = board.calculate_word_value(word, pos, 'H')
    #     self.assertEqual(value, 21)

    # def test_simple_intersection_inverted(self):
    #     board = Board()
    #     board.grid[7][2].tile = Tile('E', 1)
    #     board.grid[7][3].tile = Tile('S', 1)
    #     board.grid[7][4].tile = Tile('T', 1)
    #     board.grid[7][5].tile = Tile('R', 1)
    #     board.grid[7][6].tile = Tile('E', 1)
    #     board.grid[7][7].tile = Tile('N', 1)
    #     board.grid[7][8].tile = Tile('O', 1)
    #     board.grid[7][7].active = False
    #     word = 'mes'
    #     pos=(8,6)
    #     value = board.calculate_word_value(word, pos, 'H')
    #     self.assertEqual(value, 21)

    # def test_simple_intersection_2(self):
    #     board = Board()
    #     board.grid[7][5].tile = Tile('C', 3)
    #     board.grid[7][6].tile = Tile('A', 1)
    #     board.grid[7][7].tile = Tile('S', 1)
    #     board.grid[7][8].tile = Tile('A', 1)
    #     board.grid[6][8].tile = Tile('L', 1)
    #     board.grid[8][8].tile = Tile('S', 1)
    #     board.grid[9][8].tile = Tile('O', 1)
    #     board.grid[9][7].tile = Tile('S', 1)
    #     board.grid[9][6].tile = Tile('O', 1)
    #     word = 'cosa'
    #     pos=(7,5)
    #     value = board.calculate_word_value(word, pos, 'V')
    #     self.assertEqual(value, 14)

    # def test_simple_intersection_inverted_2(self):
    #     board = Board()
    #     board.grid[7][5].tile = Tile('C', 3)
    #     board.grid[7][6].tile = Tile('A', 1)
    #     board.grid[7][7].tile = Tile('S', 1)
    #     board.grid[7][8].tile = Tile('A', 1)
    #     board.grid[8][5].tile = Tile('O', 1)
    #     board.grid[9][5].tile = Tile('S', 1)
    #     board.grid[10][5].tile = Tile('A', 1)
    #     board.grid[9][7].tile = Tile('S', 1)
    #     board.grid[9][6].tile = Tile('O', 1)
    #     board.grid[9][8].tile = Tile('O', 1)
    #     board.grid[7][7].active = False
    #     word = 'laso'
    #     pos=(5,9)
    #     value = board.calculate_word_value(word, pos, 'V')
    #     self.assertEqual(value, 13)

    # def test_simple_intersection_inverted_3(self):
    #     board = Board()
    #     board.grid[7][5].tile = Tile('C', 3)
    #     board.grid[7][6].tile = Tile('A', 1)
    #     board.grid[7][7].tile = Tile('S', 1)
    #     board.grid[7][8].tile = Tile('A', 1)
    #     board.grid[8][5].tile = Tile('O', 1)
    #     board.grid[9][5].tile = Tile('S', 1)
    #     board.grid[10][5].tile = Tile('A', 1)
    #     board.grid[9][7].tile = Tile('S', 1)
    #     board.grid[9][6].tile = Tile('O', 1)
    #     board.grid[9][8].tile = Tile('O', 1)
    #     board.grid[7][7].active = False
    #     board.grid[9][5].active = False
    #     word = 'lasos'
    #     pos=(5,9)
    #     value = board.calculate_word_value(word, pos, 'V')
    #     self.assertEqual(value, 23)

    def test_out_of_range_side(self):
        board = Board()
        word = 'casa'
        pos = (14,10)
        horizontal = 'H'
        value = board.calculate_word_value(word, pos, horizontal)
        pos = (0,0)
        horizontal = 'H'
        value = board.calculate_word_value(word, pos, horizontal)
        self.assertEqual(value!=None, True)

    def test_letter_not_available(self):
        board = Board()
        word = 'c?sa'
        pos = (7,7)
        horizontal = 'H'
        value = board.calculate_word_value(word,pos,horizontal)
        self.assertEqual(value, 10)

if __name__ == '__main__':
    unittest.main()