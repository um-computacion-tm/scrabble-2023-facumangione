from game_cell import Cell

def rotate(mat):
    N = len(mat)

class Board:
    def __init__(self):
        self.grid = [
            [Cell(1, '') for _ in range(15)]
            for _ in range(15)
        ]
        for i in range(4):           
            for i in range(7):
                  for j in range (7):
                        if i == 0:
                            self.grid[i][i] = Cell(' ', 3, 'word') 
                        elif i == 5:
                            self.grid[i][i] = Cell(' ', 3, 'letter')
                        elif i == 6:
                            self.grid[i][i] = Cell(' ', 2, 'letter')  
                        else:
                            self.grid[i][i] = Cell(' ', 2, 'word') 
            self.grid[7][0] = Cell(' ', 3, 'word')    
            self.grid[5][1] = Cell(' ', 3, 'letter') 
            self.grid[1][5] = Cell(' ', 3, 'letter')
            self.grid[0][3] = Cell(' ', 2, 'letter') 
            self.grid[3][0] = Cell(' ', 2, 'letter')
            self.grid[6][2] = Cell(' ', 2, 'letter')
            self.grid[2][6] = Cell(' ', 2, 'letter')
            self.grid[7][3] = Cell(' ', 2, 'letter')
            rotate(self.grid)
            self.grid[7][7] = Cell(' ', 2, 'word')

    def place_tile(self, row, col, tile):
        if 0 <= row < 15 and 0 <= col < 15:
            cell = self.grid[row][col]
            if cell.letter is None:
                cell.add_letter(tile)
                return True
        return False

    def validate_word(self, start_row, start_col, word, direction):
        if direction == 'horizontal':
            for i, letter in enumerate(word):
                col = start_col + i
                if col >= 15 or (self.grid[start_row][col].letter is None or self.grid[start_row][col].letter.letter != letter):
                    return False
            return True
        elif direction == 'vertical':
            for i, letter in enumerate(word):
                row = start_row + i
                if row >= 15 or (self.grid[row][start_col].letter is None or self.grid[row][start_col].letter.letter != letter):
                    return False
            return True