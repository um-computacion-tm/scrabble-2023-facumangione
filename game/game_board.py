from game.game_cell import Cell
from game.models import Tile


class Board:
    def __init__(self):
        self.grid = [[ Cell(1, '') for _ in range(15) ]for _ in range(15)]
        self.is_empty = True
        self.word_is_valid = True
        

    def validate_word_inside_board(self, word, location: tuple, orientation):
        position_x = location[0]
        position_y = location[1]
        len_word = len(word)
        orientation = orientation.upper()
        if orientation == "H":
            if position_x + len_word > 15:
                return False
            elif position_y + len_word > 1:
                return True 
        elif orientation == "V":
            if position_y + len_word > 15:
                return False
            elif position_x + len_word > 1:
                return True     
            
    def add_letter(self, x, y, letter):
        self.grid[x][y].add_letter(letter)
        # Después de agregar una letra, el tablero ya no está vacío
        self.is_empty = False

    def validate_word_out_of_board(self, word, location, orientation):
        return not self.validate_word_inside_board(word, location, orientation)

    def validate_word_place_board(self, word, location, orientation):
        row, col = location
        if orientation == "H":
            for letter in word:
                if self.grid[row][col].letter != ' ' and self.grid[row][col].letter != letter:
                    return False
            col += 1
        
        return True
