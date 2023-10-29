from game.models import Tile
from game.several import Several
class Cell:
    def __init__(self, multiplier=1, multiplier_type='', letter=None, status='active'):
        self.multiplier = multiplier
        self.multiplier_type = multiplier_type
        self.letter = letter
        self.status = status
        
    def add_letter(self, letter:Tile):
        self.letter = letter
        

    def calculate_value(self):
        if self.letter is None:
            return 0
        if self.multiplier_type == 'letter':
            return self.letter.value * self.multiplier
        if self.multiplier_type == 'word':
            return self.letter.value
        
    def __repr__(self):
        sev = Several()
        if self.status == "active":
            return sev.format_active_cell(self)
        else:
            return sev.format_cell_contents(self)