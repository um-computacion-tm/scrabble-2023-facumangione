from game.scrabble import ScrabbleGame

def get_player_count():
        while True:
            try:
                player_count = int(input('cantidad de jugadores (1-3): '))
                if player_count <= 3:
                    break
            except Exception as e:
                print('ingrese un numero por favor')

        return player_count



def player_number(): #lleva un seguimiento del turno del jugador actual

    for player_number in range(1, ScrabbleGame.add_player + 1):
        print(f"Turno del jugador {player_number}")
        word = input('Ingrese palabra: ')
        location_x = input('Ingrese posición X: ')
        location_y = input('Ingrese posición Y: ')
        location = (location_x, location_y)
        orientation = input('Ingrese orientación (V/H): ')

        # Debo llamar al método que valida la palabra y realiza las acciones del juego:

        ScrabbleGame.validate_word(player_number, word, location, orientation)

        # Luego, continuo con el siguiente jugador en el bucle."""