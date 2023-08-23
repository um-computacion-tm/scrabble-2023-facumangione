import random

class Tile:
    def __init__(self, letter, value):
        self.letter = letter
        self.value = value


class BagTiles:
    def __init__(self):
        self.tiles = [
            ('A', 1, 7), ('E', 1, 12), ('I', 1, 6), ('L', 1, 4), ('N', 1, 5),
    ('O', 1, 9), ('R', 1, 6), ('S', 1, 5), ('T', 1, 4), ('U', 1, 5),
    ('D', 2, 5), ('G', 2, 2), ('B', 3, 2), ('C', 3, 4), ('M', 3, 2),
    ('P', 3, 2), ('F', 4, 2), ('H', 4, 2), ('V', 4, 2), ('Y', 4, 2),
    ('CH', 5, 1), ('Q', 5, 1), ('J', 8, 1), ('LL', 8, 1), ('Ñ', 8, 1),
    ('RR', 8, 1), ('X', 8, 1), ('Z', 10, 1),
        ]
        random.shuffle(self.tiles)

    def take(self, count):
        tiles = []
        for _ in range(count):
            tiles.append(self.tiles.pop())
        return tiles

    def put(self, tiles):
        self.tiles.extend(tiles)
