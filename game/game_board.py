from game.models import Tile
from game.game_cell import Cell

class Board:
    
    def __init__(self):
        self.grid = [[Cell() for _ in range(15)] for _ in range(15)]  # Representa el tablero como una matriz de celdas
        self.initialize_board_multipliers()  # Inicializa los multiplicadores del tablero

    def __iter__(self):
        return iter(self.grid)

    def initialize_board_multipliers(self):
        # Establece los multiplicadores de palabras (DP y TP)
        word_multipliers = [
            (0, 0), (0, 7), (0, 14),
            (7, 0), (7, 14),
            (14, 0), (14, 7), (14, 14)
        ]

        for position in word_multipliers:
            x, y = position
            self.grid[x][y].multiplier_type = 'word'
            self.grid[x][y].multiplier = 2 if (x, y) != (7, 7) else 3  # Casilla central es TP, el resto son DP

        # Establece los multiplicadores de letras (DL y TL)
        letter_multipliers = [
            (1, 1), (1, 13),
            (2, 2), (2, 12),
            (3, 3), (3, 11),
            (4, 4), (4, 10),
            (13, 1), (13, 13),
            (12, 2), (12, 12),
            (11, 3), (11, 11),
            (10, 4), (10, 10)
        ]

        for position in letter_multipliers:
            x, y = position
            self.grid[x][y].multiplier_type = 'letter'
            self.grid[x][y].multiplier = 2 if (x, y) != (7, 7) else 3  # Casilla central es TL, el resto son DL


    def validate_word_inside_board(self, word, location, orientation):
        position_x, position_y = location  #<--Cambiar nombre de variable para que sea mas facil de entender
        word_length = len(word)

        if orientation == "H":
            if position_y + word_length <= 15:
                return True
        elif orientation == "V":
            if position_x + word_length <= 15:
                return True

        return False

    @property
    def is_empty(self):
        # Verificar si el tablero está completamente vacío
        for row in self.grid:
            for cell in row:
                if not cell.is_empty():
                    return False
        return True

    def validate_word_place_board(self, word, location, orientation):
        position_x, position_y = location
        word_length = len(word)

        if not self.validate_word_inside_board(word, location, orientation):
            return False

        for i in range(word_length):
            if orientation == "H":
                current_tile = self.grid[position_x + i][position_y]
            elif orientation == "V":
                current_tile = self.grid[position_x][position_y + i]

            if current_tile.letter is not None:
                return False

        return True

    def put_words_board(self, word, location, orientation):
        position_x, position_y = location
        word_length = len(word)

        if not self.validate_word_place_board(word, location, orientation):
            return False

        for i in range(word_length):
            if orientation == "H":
                self.grid[position_x + i][position_y].add_letter(word[i])
            elif orientation == "V":
                self.grid[position_x][position_y + i].add_letter(word[i])

        return True
    
    def generate_row_string(self, row, positions, row_index):
        row_values = []

        for cell in row:
            if isinstance(cell, Cell):
                if cell.letter:
                    row_values.append(cell.letter.letter)
                else:
                    if cell.multiplier_type == 'DL':
                        row_values.append('DL')
                    elif cell.multiplier_type == 'TL':
                        row_values.append('TL')
                    elif cell.multiplier_type == 'DP':
                        row_values.append('DP')
                    elif cell.multiplier_type == 'TP':
                        row_values.append('TP')
            else:
                row_values.append('-')

        row_string = ' '.join(row_values)

        return row_string