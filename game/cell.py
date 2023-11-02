from game.models import Tile

class Cell:
    def __init__(self, multiplier=1, multiplier_type='letter', active=True):
        self.multiplier = multiplier
        self.multiplier_type = multiplier_type
        self.tile = None
        self.active = active

    def add_letter(self, tile:Tile):
        self.tile = tile

    def calculate_value(self):
        if self.tile is None:
            return 0
        if self.multiplier_type == 'letter':
            return self.tile.value * self.multiplier
        else:
            return self.tile.value