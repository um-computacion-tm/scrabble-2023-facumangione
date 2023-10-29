import unittest
from game.game_player import Player
from game.models import BagTiles, Tile

class TestPlayer(unittest.TestCase):
    def test_player(self):
        player_1 = Player()
        self.assertEqual(player_1.rack,[])

    def test_player_get_tile(self):
        bag_tile = BagTiles()
        player = Player()
        player.get_tiles(3,bag_tile)
        self.assertEqual(len(player.rack),3)

    def test_player_exchange(self):
        bag_tile = BagTiles()
        player = Player()
        player.rack = [Tile('A', 1), Tile('B',3), Tile('C',2)]
        player.exchange_tiles(2,bag_tile)
        self.assertEqual(len(player.rack),3)
        self.assertEqual(len(bag_tile.tiles),29)
    
    def test_validate_rack_true(self):
        player_1 = Player()
        tiles = [Tile("H",1),Tile("O",1),Tile("L",1),Tile("A",1)]
        player_1.rack = [Tile("H",1),Tile("O",1),Tile("L",1),Tile("A",1), Tile("Z",1), Tile("Z",1), Tile("Z",1)]
        is_valid = player_1.has_letters(tiles)
        assert is_valid == True
    
    def test_validate_rack_false(self):
        player_1 = Player()
        tiles = [Tile("H",1),Tile("O",1),Tile("L",1),Tile("A",1)]
        player_1.rack = [Tile("H",1),Tile("O",1),Tile("E",1),Tile("A",1), Tile("Z",1), Tile("Z",1), Tile("Z",1)]
        is_valid = player_1.has_letters(tiles)
        assert is_valid == False
    

    def test_display_rack(self):
        player = Player()
        player.rack = [Tile('A', 1), Tile('B',3), Tile('C',2)]
        self.assertEqual(player.display_rack(), "[A] [B] [C]")

if __name__ == '__main__':
    unittest.main()