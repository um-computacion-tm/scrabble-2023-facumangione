from game.models import BagTiles

class Player:
    def __init__(self, id:int):
        self.id = id
        self.tiles = None
        self.board = None
        self.score = 0
        self.rack = []

    def get_score(self):
        return sum(cell.calculate_value() for cell in self.board.played_cells)

    def validate_word(self, word):
        rack_letters = [tile.letter for tile in self.tiles]
        return all(word.count(letter) <= rack_letters.count(letter) for letter in set(word))

    def has_letters(self, tiles_to_check, bag_tile):
        # Tomar 7 fichas del "rack" (bag_tile)
        self.tiles = bag_tile.take(7)
        # Obtener las letras del "rack"
        rack_letters = [tile.letter for tile in self.tiles]
        # Comprobar si todas las letras requeridas están en el "rack"
        return all(rack_letters.count(tile.letter) >= tiles_to_check.count(tile) for tile in tiles_to_check)

    def pass_turn(self, bag_tile= BagTiles()):
        # Devuelve las fichas utilizadas al BagTiles
        bag_tile.return_tiles(self.tiles)
        # Limpia el rack del jugador
        self.tiles = []