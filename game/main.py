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
            player_count = int(input('Cantidad de jugadores (2-4): ')) 
            if player_count < 2 or player_count > 4:
                raise ValueError 
            else:
                break 
        except ValueError:
            print('Valor inválido')

    game = Scrabble(player_count)
    print(f'La cantidad de jugadores es: {player_count}')
    
    for player_number in range(1, player_count + 1):
        print(f"Turno del jugador {player_number}")
        word = input('Ingrese palabra: ')
        location_x = input('Ingrese posición X: ')
        location_y = input('Ingrese posición Y: ')
        location = (location_x, location_y)
        orientation = input('Ingrese orientación (V/H): ')

        # Debo llamar al método que valida la palabra y realiza las acciones del juego:

        game.play_word(player_number, word, location, orientation)

        # Luego, continuo con el siguiente jugador en el bucle."""