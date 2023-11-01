import unittest
from game.models import (
    BagTiles,
    Tile,
    Joker,
)
from unittest.mock import patch

class TestTiles(unittest.TestCase):
    def test_tile(self):
        tile = Tile('A', 1)
        self.assertEqual(tile.letter, 'A')
        self.assertEqual(tile.value, 1)
        tile = Tile("B",3)
        self.assertEqual(tile.letter,"B")
        self.assertEqual(tile.value,3)
        tile = Tile("C",3)
        self.assertEqual(tile.letter,"C")

class TestBagTiles(unittest.TestCase):
    @patch('random.shuffle')
    def test_bag_tiles(self, patch_shuffle):
        bag = BagTiles()
        self.assertEqual(len(bag.tiles),100,)
        self.assertEqual(patch_shuffle.call_count,1,)
        self.assertEqual(patch_shuffle.call_args[0][0],bag.tiles,)

    def test_take(self):
        bag = BagTiles()
        tiles = bag.take(2)
        self.assertEqual(len(bag.tiles),98,)
        self.assertEqual(len(tiles),2,)

    def test_put(self):
        bag = BagTiles()
        put_tiles = [Tile('Z', 1), Tile('Y', 1)]
        bag.put(put_tiles)
        self.assertEqual(len(bag.tiles),100,)

    def test_put(self):
        bag = BagTiles()
        put_tiles = [Tile('Z', 1), Tile('Y', 1)]
        bag.take(3)
        bag.put(put_tiles)
        self.assertEqual(len(bag.tiles),99,)

class TestJoker(unittest.TestCase):
    def test_joker_creation(self):
        comodin = Joker()
        self.assertEqual(comodin.letter,"")
        self.assertEqual(comodin.value,0)
    
    def test_joker_selection(self):
        comodin = Joker()
        comodin.select_letter("A")
        self.assertEqual(comodin.letter,"A")
        self.assertEqual(comodin.value,1)

if __name__ == '__main__':
    unittest.main()