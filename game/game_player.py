from game.models import BagTiles


class Player:

    def __init__(self, id=0):
        self.rack = []
        self.score = 0
        self.id = id
  
    def get_tiles(self,amount,bag=BagTiles):
        for _ in range(amount):
            self.rack.append(bag.take(1))

    def exchange_tiles(self,index,bag=BagTiles):
        tile_to_exchange = self.rack.pop(index)
        new_tile = bag.take(1)
        bag.put([tile_to_exchange])
        self.rack.append(new_tile)
    
    def has_letters(self, tiles):
        rack = set(tile.letter for tile in self.rack) 
        return set(tile.letter for tile in tiles).issubset(rack)
    
    def display_rack(self):
        return ' '.join(f'[{tile.letter}]' for tile in self.rack)


   
    
    