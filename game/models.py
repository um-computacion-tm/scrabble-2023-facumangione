import random

class Tile:
    def __init__(self, letter, value):
        self.letter = letter
        self.value = value

    def __repr__(self):
        return self.letter

class Joker(Tile):
    def __init__(self):
        super().__init__(letter = "",value = 0)

    def select_letter(self, selection):
        for tile in D:
            if selection == tile["letter"]:
                self.letter = tile["letter"]
                self.value = tile["value"]
        
D = [
    {
        "letter":"A",
        "value":1,
        "quantity":12
    },
    {
        "letter":"B",
        "value":3,
        "quantity":2
    },
    {
        "letter":"C",
        "value":3,
        "quantity":4
    },
    {
        "letter":"CH",
        "value":5,
        "quantity":1
    },
    {
        "letter":"D",
        "value":2,
        "quantity":5
    },
    {
        "letter":"E",
        "value":1,
        "quantity":12
    },
    {
        "letter":"F",
        "value":4,
        "quantity":1
    },
    {
        "letter":"G",
        "value":2,
        "quantity":2
    },
    {
        "letter":"H",
        "value":4,
        "quantity":2
    },
    {
        "letter":"I",
        "value":1,
        "quantity":6
    },
    {
        "letter":"J",
        "value":8,
        "quantity":1
    },
    {
        "letter":"L",
        "value":1,
        "quantity":4
    },
    {
        "letter":"LL",
        "value":8,
        "quantity":1
    },
    {
        "letter":"M",
        "value":3,
        "quantity":2
    },
    {
        "letter":"N",
        "value":1,
        "quantity":5
    },
    {
        "letter":"Ñ",
        "value":8,
        "quantity":1
    },
    {
        "letter":"O",
        "value":1,
        "quantity":9
    },
    {
        "letter":"P",
        "value":3,
        "quantity":2
    },
    {
        "letter":"Q",
        "value":5,
        "quantity":1
    },
    {
        "letter":"R",
        "value":1,
        "quantity":5
    },
    {
        "letter":"RR",
        "value":8,
        "quantity":1
    },
    {
        "letter":"S",
        "value":1,
        "quantity":6
    },
    {
        "letter":"T",
        "value":1,
        "quantity":4
    },
    {
        "letter":"U",
        "value":1,
        "quantity":5
    },
    {
        "letter":"V",
        "value":4,
        "quantity":1
    },
    {
        "letter":"X",
        "value":8,
        "quantity":1
    },
    {
        "letter":"Y",
        "value":4,
        "quantity":1
    },
    {
        "letter":"Z",
        "value":10,
        "quantity":1
    }]

class BagTiles:
    def __init__(self):
        self.tiles = []
        for i in D:
            for j in range(i.get("quantity")):
                self.tiles.append(i.get("letter"))
        self.tiles.append(Joker())
        self.tiles.append(Joker())

        random.shuffle(self.tiles)

    def take(self, count):
        tiles = []
        if count <= len(self.tiles):
            for _ in range(count):
                tiles.append(self.tiles.pop())
        else:
            print("No hay suficientes fichas")
        return tiles
        
    def put(self, hand):
        if len(hand) + len(self.tiles) <= 100:
            self.tiles.extend(hand)
        else:
            print("Hay mas tiles de las que se puede tener")