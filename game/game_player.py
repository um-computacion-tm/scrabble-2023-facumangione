class Player:
    def __init__(self, id:int):
        self.id = id
        self.tiles = None
        self.board = None

    @property
    def rack(self):
        return self.tiles

    def get_score(self):
        return sum(cell.calculate_value() for cell in self.board.played_cells)

    def validate_word(self, word):
        rack_letters = [tile.letter for tile in self.tiles]
        return all(word.count(letter) <= rack_letters.count(letter) for letter in set(word))

    def pass_turn(self):
        pass