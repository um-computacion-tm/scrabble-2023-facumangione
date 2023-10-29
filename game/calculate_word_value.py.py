from game.game_cell import Cell

class Calculate_word_value:
    def calculate_word_value(self,cells: list[Cell]): 
        value: int = 0
        multiplier_word = None
        for cell in cells:
            value = value + cell.calculate_value()
            if cell.multiplier_type == 'word':
                multiplier_word = cell.multiplier
                cell.multiplier = 1
        if multiplier_word != None:
            value = (value * multiplier_word)
        return value