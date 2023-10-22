from game.scrabble import ScrabbleGame

class GetPlayerCount:

    def __init__(self):
        self.player_count = 0

    def get_player_count(self):
        while True:
            try:
                self.player_count = int(input('Ingrese la cantidad de jugadores (1-4): '))
                if 1 <= self.player_count <= 4:
                    break
                else:
                    print('Por favor, ingrese un número entre 1 y 4.')
            except ValueError:
                print('Por favor, ingrese un número válido.')

    def player_number(self):
        game = ScrabbleGame(self.player_count)  # Crea una instancia de ScrabbleGame
        for player_number in range(1, self.player_count + 1):
            print(f"Turno del jugador {player_number}")
            word = input('Ingrese palabra (o "PASAR" para saltar el turno): ')
            if word.lower() == "pasar":
                game.pass_turn()
            else:
                location_x = int(input('Ingrese posición X: '))
                location_y = int(input('Ingrese posición Y: '))
                orientation = input('Ingrese orientación (V/H): ')
                try:
                    game.play(word, (location_x, location_y), orientation)
                except Exception as e:
                    print(e)
        game.show_scores()  # Muestra los puntajes al final del juego

if __name__ == "__main__":
    game = GetPlayerCount()
    game.get_player_count()
    game.player_number()