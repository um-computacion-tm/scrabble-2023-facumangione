from game.models import Tile 

class Cell:
    def __init__(self, multiplier=1, multiplier_type=None, letter=None, active=True):  # Agregamos letter como argumento opcional
        self.multiplier = multiplier
        self.multiplier_type = multiplier_type
        self.letter = letter  # Establecemos el atributo letter con el valor pasado o None
        self.active = active

    def add_letter(self, letter: Tile):
        self.letter = letter

    def calculate_value(self):
        if self.letter is None:
            return 0
        if self.multiplier_type == 'letter':
            return self.letter.value * self.multiplier
        else:
            return self.letter.value