from game.scrabble import ScrabbleGame
from io import StringIO


class Main:
    def __init__(self):
        print('Bienvenido')
        self.player_count = self.get_player_count()
        self.game = ScrabbleGame(self.player_count)
        self.main_output = StringIO()

    def valid_player_count(self,player_count):
        try:
            count = int(player_count)
            if 2 <= count <= 4:
                return True
        except ValueError:
            pass
        return False
    def get_player_count(self):
        while True:
            player_count = input('Cantidad de jugadores: ')
            if self.valid_player_count(player_count) is True:
                return int(player_count)
            print('Valor inválido')
    
    def play(self):
        print(f'La cantidad de jugadores es: {self.player_count}')
        self.game.next_turn()
        print(f"Turno del jugador 1")

"""
def main():
    print('Bienvenido')
    while True:
        try:
            player_count = int(input('cantidad de jugadores '))
            if player_count < 2 or player_count > 4:
                raise ValueError
            else:
                break
        except ValueError:
            print('Valor invalido')
    game = Scrabble(player_count)
    print('La cantidad de jugadores es: ' + str(player_count))
    game.next_turn()
    print(f"Turno del jugador 1")
    word = input('Ingrese palabra: ')
    location_x = input('Ingrese posición X: ')
    location_y = input('Ingrese posición Y: ')
    location = (location_x, location_y)
    orientation = input('Ingrese orientación (V/H): ')
    game.validate_word"""