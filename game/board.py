from game.cell import *
from pyrae import dle
from game.models import D as DATA
from game.player import Player

class Board:
    def __init__(self):
        self.grid = [[Cell(1, '') for _ in range(15)] for _ in range(15)]
        self.add_multipliers()

    def add_multipliers(self):
        WORD_MULTIPLIERS = ((0, 0), (7, 0), (0, 7), (7, 7), (0, 14), (7, 14), (14, 0), (14, 7), (14, 14), (1, 1), (2, 2), (3, 3), (4, 4), (10, 10), (11, 11), (12, 12), (13, 13), (1, 13), (2, 12), (3, 11), (4, 10), (10, 4), (11, 3), (12, 2), (13, 1))
        LETTER_MULTIPLIERS = ((1, 5), (1, 9), (5, 1), (5, 5), (5, 9), (5, 13), (9, 1), (9, 5), (9, 9), (9, 13), (13, 5), (13, 9),(0, 3), (0, 11), (2, 6), (2, 8), (3, 0), (3, 7), (3, 14), (6, 2), (6, 6), (6, 8), (6, 12), (7, 3), (7, 11), (8, 2), (8, 6), (8, 8), (8, 12), (11, 0), (11, 7), (11, 14), (12, 6), (12, 8), (14, 3), (14, 11))
        for row in range(15):
            for col in range(15):
                cell = self.grid[row][col]
                if (row, col) in LETTER_MULTIPLIERS:
                    multiplier = 3 if (row, col) in ((1, 5), (1, 9), (5, 1), (5, 5), (5, 9), (5, 13), (9, 1), (9, 5), (9, 9), (9, 13), (13, 5), (13, 9)) else 2
                    cell.multiplier = multiplier
                    cell.multiplier_type = 'letter'
                elif (row, col) in WORD_MULTIPLIERS:
                    multiplier = 3 if (row, col) in ((0, 0), (7, 0), (0, 7), (0, 14), (7, 14), (14, 0), (14, 7), (14, 14)) else 2
                    cell.multiplier = multiplier
                    cell.multiplier_type = 'word'

    def calculate_word_value(self, word, pos, orientation, first=True):
        horizontal = True if orientation.upper() == 'H' else False
        word = Player().split_word(word)
        points = 0
        word_multiplier = 1
        i = 0
        for letter in word:
            cell, invert_cell, side_cell = self.get_cells(pos, i, horizontal)
            available = not cell.tile and first
            j = 1
            if invert_cell and invert_cell.tile and available:
                side_word, j = self.get_side_word(invert_cell, i, (horizontal,True), pos, letter)
                points += self.calculate_word_value(side_word, (pos[0] - j + 1, pos[1] + i) if horizontal else (pos[0] + i, pos[1] - j + 1), not horizontal, False)
            elif side_cell and side_cell.tile and available:
                side_word, j = self.get_side_word(side_cell, i, (horizontal,False), pos, letter)
                points += self.calculate_word_value(side_word, (pos[0], pos[1] + i) if horizontal else (pos[0] + i, pos[1]), not horizontal, False)
            letter_value = self.get_letter_value(letter)
            word_multiplier, points = self.update_multipliers(cell, letter_value, word_multiplier, points, first)
            i += 1
        points = points * word_multiplier
        return points

    def get_cells(self, pos, i, horizontal):
        cell = self.grid[pos[0]][pos[1] + i] if horizontal else self.grid[pos[0] + i][pos[1]]
        if pos[0] > 0 and pos[1] > 0:
            invert_cell = self.grid[pos[0] - 1][pos[1] + i] if horizontal else self.grid[pos[0] + i][pos[1] - 1]
        else:
            invert_cell = None
        try:
            side_cell = self.grid[pos[0] + 1][pos[1] + i] if horizontal else self.grid[pos[0] + i][pos[1] + 1]
        except:
            side_cell = None
        return cell, invert_cell, side_cell

    def get_side_word(self, cell, i, orientation, pos, letter):
        horizontal = orientation[0]
        inverted = orientation[1]
        k = -1 if inverted else 1
        side_word = letter
        j = 1
        while cell.tile:
            side_word += cell.tile.letter
            cell = self.grid[pos[0] + (1 + j)*k][pos[1] + i] if horizontal else self.grid[pos[0] + i][pos[1] + (1 + j)*k]
            j += 1
        if inverted:
            side_word = side_word[::-1]
        return side_word, j

    def get_letter_value(self, letter):
        for tile in DATA:
            if letter == tile['letter']:
                return tile['value']
        return 0

    def update_multipliers(self, cell, letter_value, word_multiplier, points, first):
        if not (cell.multiplier_type == 'letter' ) and cell.active:
            word_multiplier *= cell.multiplier
        points += (letter_value * cell.multiplier) if cell.multiplier_type == 'letter' and cell.active else letter_value
        if first:
            cell.active = False
        return word_multiplier, points
    
    def validate_word_inside_board(self, word, location, orientation):
        if orientation == "H":
            return len(word) <= len(self.grid)-location[0]
        else:
            return len(word) <= len(self.grid)-location[1]

    def is_empty(self):
        return self.grid[7][7].tile == None
    
    def validate_empty(self, word, location, orientation):
        h_space = len(word) <= len(self.grid)-location[0]
        v_space = len(word) <= len(self.grid)-location[1]
        if orientation=='H' and h_space and location[0]==7:
            for i in range(len(word)):
                if location[1] + i == 7:
                    return True
        elif (orientation !='H' and v_space and location[1]==7):
            for i in range(len(word)):
                if location[0] + i == 7:
                    return True
        return False
    
    def validate_side_cell(self, parameters, validators, cell, index_increment):
        word, pos, i = parameters[0], parameters[1], parameters[2]
        is_valid, intersections = validators[0], validators[1]
        grid, word2, index = self.grid, word[i], 1
        while cell:
            word2 += cell.lower()
            cell = grid[pos[0] + i + index_increment * index][pos[1] + i].tile
            index += 1
        word2_is_valid = self.rae_search(word2)
        if not word2_is_valid:
            is_valid = -9999
        else:
            is_valid += 1
            intersections += 1
        return [is_valid, intersections]

    def check_cells(self, cells, parameters, validators):
        cell, sidecell, invertsidecell = cells[0], cells[1], cells[2]
        word, pos, i = parameters[0], parameters[1], parameters[2]
        is_valid, intersections = validators[0], validators[1]
        if cell:
            intersections += 1
            is_valid += 1 if cell == word[i].upper() else 0
        elif sidecell:
            result = self.validate_side_cell([word, pos, i], [is_valid, intersections], sidecell, 1)
            is_valid, intersections = result[0], result[1]
        elif invertsidecell:
            result = self.validate_side_cell([word, pos, i], [is_valid, intersections], invertsidecell, -1)
            is_valid, intersections = result[0], result[1]
        return [is_valid, intersections]
    
    def validate_not_empty(self, word, pos, orientation):
        horizontal = True if orientation.upper() == 'H' else False
        intersections = 0
        is_valid = 0
        grid = self.grid
        for i in range(len(word)):
            cell = grid[pos[0] + (i if not horizontal else 0)][pos[1] + (i if horizontal else 0)].tile
            sidecell = grid[pos[0] + i][pos[1] + 1].tile if not horizontal else grid[pos[0] + 1][pos[1] + i].tile
            invertsidecell = grid[pos[0] + i][pos[1] - 1].tile if not horizontal else grid[pos[0] - 1][pos[1] + i].tile
            checked = self.check_cells([cell, sidecell, invertsidecell], [word, pos, i], [is_valid, intersections])
            is_valid, intersections = checked[0], checked[1]
        return is_valid != 0 and is_valid == intersections
        
    def validate(self, word, location, orientation):
        if self.validate_word(word):
            if self.grid[7][7].tile is None:
                return self.validate_empty(word, location, orientation)
            return self.validate_not_empty(word, location, orientation)
        return False
            
    def validate_right(self, word, location, orientation):
        row = location[0]
        column = location[1]
        for i in range (len(word)):
            cell = self.grid[row+i][column]
            right_cell = self.grid[row+i][column+1]
            if cell.tile == None:
                if right_cell.tile is not None:
                    temporal_word = word[i]
                    j = 1
                    temporal_rcell = right_cell
                    while temporal_rcell.tile != None:
                        temporal_word += temporal_rcell.tile.letter
                        temporal_rcell = self.grid[row+i][column + 1 + j]
                        j += 1
                    if self.validate_word(temporal_word):
                        return True
        return False     

    def validate_left(self, word, location, orientation):
        row = location[0]
        column = location[1]
        for i in range (len(word)):
            cell = self.grid[row+i][column]
            left_cell = self.grid[row+i][column-1]
            if cell.tile == None:
                if left_cell.tile is not None:
                    temporal_word = word[i]
                    j = 1
                    temporal_lcell = left_cell
                    while temporal_lcell.tile != None:
                        temporal_word += temporal_lcell.tile.letter
                        temporal_lcell = self.grid[row+i][column - 1 - j]
                        j += 1
                    temporal_word = temporal_word[::-1]
                    if self.validate_word(temporal_word):
                        return True
        return False       
            
    def put_word(self,word,location,orientation):
        horizontal = True if orientation.upper() == 'H' else False
        j=0
        for i in range(len(word)):
            cell = self.grid[location[0]][location[1]+i+j] if horizontal else self.grid[location[0]+i+j][location[1]]
            while cell.tile:
                j+=1
                cell = self.grid[location[0]][location[1]+i+j] if horizontal else self.grid[location[0]+i+j][location[1]]
            cell.tile = word[i]

    def words_with_accent(self, word):
        word = word.lower()
        for letter in word:
            if letter == 'á':
                word = word.replace('á', 'a')
            elif letter == 'é':
                word = word.replace('é', 'e')
            elif letter == 'í':
                word = word.replace('í', 'i')
            elif letter == 'ó':
                word = word.replace('ó', 'o')
            elif letter == 'ú':
                word = word.replace('ú', 'u')
        return word.upper()

    def board_in_terminal(self):
        view = ' \n'
        view += '    0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 \n'
        letters = 'ABCDEFGHIJKLMNO'
        for i, row in enumerate(self.grid):
            view += f"{letters[i]}   "
            for cell in row:
                if cell.tile is None:
                    if cell.multiplier_type == 'letter' and cell.multiplier == 3:
                        view += f"3L|"
                    elif cell.multiplier_type == 'letter' and cell.multiplier == 2:
                        view += f"2L|"
                    elif cell.multiplier_type == 'word' and cell.multiplier == 3:
                        view += f"3W|"
                    elif cell.multiplier_type == 'word' and cell.multiplier == 2:
                        view += f"2W|"
                    else:
                        view += f"  |"
                else:
                    if len(cell.tile) == 2:
                        view += f"{cell.tile}|"
                    else:
                        view += f"{cell.tile} |"
            view += "\n"
        return view
    
    def get_word_without_intersections(self,word,pos,horizontal):
        result = ''
        for i in range(len(word)):
            cell = self.grid[pos[0] + (i if not horizontal else 0)][pos[1] + (i if horizontal else 0)].tile
            if not cell:
                result += word[i]
        return result

    
    def validate_word(self, word):
        dle.set_log_level(log_level = 'CRITICAL')
        search = dle.search_by_word(word=word)
        if search is None:
            raise DictionaryConnectionError()
        return search.meta_description != 'Versión electrónica 23.6 del «Diccionario de la lengua española», obra lexicográfica académica por excelencia.'
        
class DictionaryConnectionError(Exception):
    ...