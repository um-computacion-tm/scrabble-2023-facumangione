"""
from io import StringIO
from game.scrabble import ScrabbleGame
from game.get_player_count import GetPlayerCount

class Main:
    def __init__(self):
        print('¡Bienvenido a Scrabble!')
        self.player_count = self.get_player_count()
        self.game = ScrabbleGame(self.player_count)
        self.main_output = StringIO()

    def get_player_count(self):
        while True:
            try:
                player_count = int(input('Ingrese la cantidad de jugadores (2-4): '))
                if 2 <= player_count <= 4:
                    return player_count
                else:
                    print('Por favor, ingrese un número entre 2 y 4.')
            except ValueError:
                print('Por favor, ingrese un número válido.')

    def play(self):
        print(f'La cantidad de jugadores es: {self.player_count}')
        self.game.start_game()
        while self.game.is_playing():
            self.show_board()
            self.show_current_player()
            word = input('Ingrese palabra (o "PASAR" para saltar el turno): ')
            if word.lower() == "pasar":
                self.game.pass_turn()
            else:
                location_x = int(input('Ingrese posición X: '))
                location_y = int(input('Ingrese posición Y: '))
                orientation = input('Ingrese orientación (V/H): ')
                try:
                    self.game.play(word, (location_x, location_y), orientation)
                except Exception as e:
                    print(e)
            self.show_scores()

    def show_board(self):
        board = self.get_board()
        for row in board:
            print(' '.join([cell.letter or '.' for cell in row]))  # Utiliza '.' para representar celdas vacías
        print()

    def show_current_player(self):
        current_player = self.game.get_current_player()
        print(f"Turno del jugador {current_player.id}")

    def show_scores(self):
        players = self.game.get_players()
        for player in players:
            print(f"Jugador {player.id}: Puntos = {player.score}")
        print()

    def valid_player_count(self, player_count):
        try:
            count = int(player_count)
            if 2 <= count <= 4:
                return True
        except ValueError:
            pass
        return False
if __name__ == '__main__':
    main = Main()
    main.play()
    
"""    