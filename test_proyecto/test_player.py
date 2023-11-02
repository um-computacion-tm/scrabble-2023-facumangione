import unittest
from game.player import Player
from game.models import BagTiles
from game.models import Tile


class TestPlayer(unittest.TestCase):
    def test_init(self):
        player_1 = Player()
        self.assertEqual(
            len(player_1.tiles),
            0,
        )

class TestPlayer(unittest.TestCase):
    def test_player_creation(self):
        player = Player(name='Isaac', number=1, points=3)
        self.assertEqual(player.name, 'Isaac')
        self.assertEqual(player.number, 1)
        self.assertEqual(player.points, 3)
        self.assertEqual(player.lectern, [])

    def test_player_creation_no_parameters(self):
        player = Player()
        self.assertEqual(player.name, '')
        self.assertEqual(player.number, 0)
        self.assertEqual(player.points, 0)
        self.assertEqual(player.lectern, [])

    def test_give_tiles(self):
        player = Player()
        player.give_tiles(['A', 'B'])
        self.assertEqual(player.lectern, ['A', 'B'])

    def test_give_tiles_from_bag(self):
        bag = BagTiles()
        player = Player()
        player.give_tiles(bag.take(7))
        self.assertEqual(len(player.lectern), 7)

    def test_change_tiles(self):
        player = Player()
        player.give_tiles(['A', 'B', 'C'])
        old_tiles = player.change_tiles(old_tiles_index=[2,3], new_tiles=['Z', 'Y'])
        self.assertEqual(player.lectern, ['A', 'Z', 'Y'])
        self.assertEqual(old_tiles, ['B', 'C'])

    def test_split_word(self):
        player = Player()
        splited_word = player.split_word('CASA')
        self.assertEqual(splited_word, ['C','A','S','A'])

    def test_split_word_with_ll(self):
        player = Player()
        splited_word = player.split_word('llano')
        self.assertEqual(splited_word, ['LL','A','N','O'])

    def test_split_word_with_ch(self):
        player = Player()
        splited_word = player.split_word('chamba')
        self.assertEqual(splited_word, ['CH','A','M','B','A'])

    def test_split_word_with_rr(self):
        player = Player()
        splited_word = player.split_word('ferro')
        self.assertEqual(splited_word, ['F','E','RR','O'])

    def test_search_word(self):
        player = Player()
        player.give_tiles([Tile('A',1), Tile('C', 1), Tile('C',1), Tile('S',3), Tile('A',1), Tile('S',3), Tile('G',2)])
        result = player.search_words_in_lectern('casa')
        self.assertEqual(result, True)

    def test_search_word_invalid(self):
        player = Player()
        player.give_tiles([Tile('A',1), Tile('C', 1), Tile('C',1), Tile('S',3), Tile('A',1), Tile('S',3), Tile('G',2)])
        result = player.search_words_in_lectern('losa')
        self.assertEqual(result, False)

    def test_search_word_2_same_letter(self):
        player = Player()
        player.give_tiles([Tile('Y',1), Tile('C', 1), Tile('C',1), Tile('S',3), Tile('A',1), Tile('G',3), Tile('G',2)])
        result = player.search_words_in_lectern('casas')
        self.assertEqual(result, False)

    def test_search_double_letter_tile_word(self):
        player = Player()
        player.give_tiles([Tile('LL',1), Tile('U', 1), Tile('V',1), Tile('I',3), Tile('A',1), Tile('G',3), Tile('G',2)])
        result = player.search_words_in_lectern('lluvia')
        self.assertEqual(result, True)
    
    def test_search_word_invalid2(self):
        player = Player()
        player.give_tiles([Tile('A',1),Tile('B',1),Tile('C',1),Tile('D',1)])
        self.assertFalse(player.search_words_in_lectern('CASA'))

    def test_search_word_valid(self):
        player = Player()
        player.give_tiles([Tile('A',1),Tile('B',1),Tile('C',1),Tile('D',1),])
        self.assertTrue(player.search_words_in_lectern('AB'))
        
    def test_fill(self):
        bag = BagTiles()
        player = Player()
        player.lectern = [Tile('A', 1)]
        player.fill(bag)
        self.assertEqual(len(player.lectern), 7)

    def test_view_lectern(self):
        player = Player()
        player.lectern = [Tile('A', 1),Tile('A', 1),Tile('A', 1),Tile('A', 1),Tile('A', 1),Tile('A', 1),Tile('A', 1)]
        result = player.view_lectern()
        expected = '''                     ATRIL

Letras ->  | A | A | A | A | A | A | A |'''
        self.maxDiff = None
        self.assertEqual(result, expected)

    def test_take(self):
        player = Player()
        player.give_tiles(['C','A','S','A','B','O','U'])
        result = player.take_tiles('casa')
        self.assertEqual(len(result),4)
        self.assertEqual(len(player.lectern),3)

    def test_take_2(self):
        player = Player()
        player.lectern = ['C','A','S','A','R','C','A']
        result = player.take_tiles('casa')
        self.assertEqual(len(result),4)
        self.assertEqual(len(player.lectern),3)

    def test_has_tiles(self):
        player=Player('Simon',0,0,BagTiles())
        tiles=[Tile('A',1),Tile('B',1),Tile('C',1)]
        player.give_tiles(tiles)
        self.assertTrue(player.has_tiles('ABC'))
        self.assertFalse(player.has_tiles('ABD'))

if __name__ == '__main__':
    unittest.main()