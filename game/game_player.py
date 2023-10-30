from game.models import BagTiles

class Player:

    def __init__(self, id=0):
        self.rack = []
        self.score = 0
        self.id = id

    def get_tiles(self, amount, bag=BagTiles):
        new_tiles = bag.take(amount)
        self.rack.extend(new_tiles)


    def exchange_tiles(self, index, bag=BagTiles):
        tile_to_exchange = self.rack.pop(index)
        new_tile = bag.take(1)
        bag.put([tile_to_exchange])
        self.rack.append(new_tile)
        print(f'Exchanged tile in rack: [{tile_to_exchange.letter}] with new tile: [{new_tile.letter}]')

    def has_letters(self, tiles):
        rack = set(tile.letter for tile in self.rack)
        return set(tile.letter for tile in tiles).issubset(rack)

    def display_rack(self):
        rack_str = ' '.join(f'[{tile.letter}]' for tile in self.rack)
        return rack_str #funcion!


if __name__ == "__main__":
    player = Player(id=1)  # Crear una instancia de Player
    player.get_tiles(7, BagTiles())  # Llamar a get_tiles con un argumento count
    player.display_rack()
   
    
    
   
    
    