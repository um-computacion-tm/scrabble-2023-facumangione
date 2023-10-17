
from typing import List
from game.game_cell import Cell

class Calculate_word_value:
    @staticmethod
    def calculate_word_value(word: List[Cell]) -> int:
        value: int = 0
        multiplier_word = None
        for cell in word:
            value = value + cell.calculate_value()
            if cell.multiplier_type == "word" and cell.active:
                multiplier_word = cell.multiplier
        if multiplier_word:
            value = value * multiplier_word
        return value