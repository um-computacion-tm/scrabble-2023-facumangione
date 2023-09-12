import random

class Tile:
    def __init__(self, letter, value):
        self.letter = letter
        self.value = value


class BagTiles:
    def __init__(self):
        self.tiles = [
            Tile('A',1),
            Tile('A',1),
            Tile('A',1),
            Tile('A',1),
            Tile('A',1),
            Tile('A',1),
            Tile('A',1),
            Tile('A',1),
            Tile('A',1),
            Tile('A',1),
            Tile('A',1),
            Tile('A',1),     
            Tile('E',1),
            Tile('E',1),
            Tile('E',1),
            Tile('E',1),
            Tile('E',1),
            Tile('E',1),
            Tile('E',1),
            Tile('E',1),
            Tile('E',1),
            Tile('E',1),
            Tile('E',1),
            Tile('E',1),
            Tile('I',1),
            Tile('I',1),
            Tile('I',1),
            Tile('I',1),
            Tile('I',1),
            Tile('I',1),
            Tile('L',1),
            Tile('L',1),
            Tile('L',1),
            Tile('L',1),
            Tile('N',1),
            Tile('N',1),
            Tile('N',1),
            Tile('N',1),
            Tile('N',1),
            Tile('O',1),
            Tile('O',1),
            Tile('O',1),
            Tile('O',1),
            Tile('O',1),
            Tile('O',1),
            Tile('O',1),
            Tile('O',1),
            Tile('O',1),
            Tile('R',1),
            Tile('R',1),
            Tile('R',1),
            Tile('R',1),
            Tile('R',1),
            Tile('S',1),
            Tile('S',1),
            Tile('S',1),
            Tile('S',1),
            Tile('S',1),
            Tile('S',1),
            Tile('T',1),
            Tile('T',1),
            Tile('T',1),
            Tile('T',1),
            Tile('U',1),
            Tile('U',1),
            Tile('U',1),
            Tile('U',1),
            Tile('U',1),
            Tile('D',1),
            Tile('D',1),
            Tile('D',1),
            Tile('D',1),
            Tile('D',1),
            Tile('G',1),
            Tile('G',1),
            Tile('B',1),
            Tile('B',1),
            Tile('C',1),
            Tile('C',1),
            Tile('C',1),
            Tile('C',1),
            Tile('M',1),
            Tile('M',1),
            Tile('P',1),
            Tile('P',1),
            Tile('F',1),
            Tile('H',1),
            Tile('H',1),
            Tile('V',1),
            Tile('Y',1),
            Tile('C',1),
            Tile('H',1),
            Tile('X',1),
            Tile('Q',1),
            Tile('J',1),
            Tile('L',1),
            Tile('L',1),
            Tile('Ñ',1),
            Tile('R',1),
            Tile('R',1),
            Tile('X',1),
            Tile('Z',1)

                                         
        ]
        random.shuffle(self.tiles)

    def take(self, count):
        tiles = []
        for _ in range(count):
            tiles.append(self.tiles.pop())
        return tiles

    def put(self, tiles):
        self.tiles.extend(tiles)