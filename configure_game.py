from game.scrabble import ScrabbleGame
from game.models import Tile
from game.game_board import Board
import random
from game.models import BagTiles
from game.game_player import Player

class Configure:
    def __init__(self):
        print ("¡Bienvenido a Scrabble!")
        self.player_count = self.get_player_count()
        self.game = ScrabbleGame(self.player_count)
        self.board = self.game.get_board()
        self.bag = BagTiles() 
        self.player = Player()

    def iniciar_juego(self):
       pass
          
    def valid_player_count(self,player_count):
        try:
            count = int(player_count)
            return 2<= count <= 4
        except ValueError:
            return False
        
    def get_player_count(self):
        while True:
            player_count = input('Número de participantes es(2-4):')
            if self.valid_player_count(player_count) is True:
                return int(player_count)
            print('Valor ingresado no valido')
  
    def show_board(self, board):
        print('\n  |' + ''.join([f' {str(row_index).rjust(2)} ' for row_index in range(len(board.grid))]))
        for row_index, row in enumerate(board.grid):
            print(
                str(row_index).rjust(2) +
                '| ' +
                ' '.join([repr(cell) for cell in row])
            )



    def show_current_player(self):
        total_players = self.player_count  # Utiliza el número de jugadores ya almacenado
        player_number = self.game.current_player.id
        print(f'Turno del jugador {player_number} de {total_players} jugadores')


    

    def initial_tiles(self):
        self.game.put_initial_tiles_bag()
        self.game.put_tiles_in_rack()
    ###

    def take_turn(self):
        current_player = self.game.current_player  # Obtener el jugador actual
        print(f'{self.game.current_player_name()}: Tienes las siguientes fichas: {current_player.display_rack()}')
        while True:
            action = int(input('¿Qué vas hacer? JUGAR(1) / CAMBIAR LETRA (2) / PASAR(3) / RENDIRTE(4): '))  #hasta acá funciona 
            action = action
            if action == 1:
                while True:
                    word = input('Ingresar palabra: ')
                    location_x = int(input('Ingresar columna (0-14): '))
                    location_y = int(input('Ingrese fila (0-14): '))
                    location = (location_x, location_y)
                    orientation = input('Ingresar (V/H): ')
                    if self.game.scrabble_validate_word(word, location, orientation):
                        self.game.put_word(word, location, orientation)
                        self.add_score(word, location, orientation)
                        break
                    elif word == 0:
                        break
                    else:
                        print("Valor ingresado no válido, ¿Desea volver al menú principal? y/n")
                        while True:
                            choice = input().strip().lower()
                            if choice == "y":
                                return  # Esto saldrá de la función y volverá al menú principal
                            elif choice == "n":
                                break  # Continuar jugando dentro del bucle
                            else:
                                print("Opción no válida. Por favor, ingrese 'y' para volver al menú principal o 'n' para continuar jugando.") #funciona


                    
            elif action == 2:
                pass
                #terminar
            elif action == 3:
                self.game.next_turn
                break
            elif action == 4:
                self.surrender()
                #terminar
            else:
                print("Opción no válida. Por favor, elige una opción válida.")

        if self.game.game_over():
            print('¡SE ACABÓ EL JUEGO!')
            self.display_final_scores()

    def show_scores(self):
        sorted_players = sorted(self.game.players, key=lambda player: player.score, reverse=True) 
        print("Puntajes de los jugadores:")
        for _, player in enumerate(sorted_players, start=1):
            print(f"Jugador {player.id}: Puntaje = {player.score}")

    def place_word(self):
        while True:
            word = input('Ingresar palabra: ')
            location_x = int(input('Ingresar columna (0-14): '))
            location_y = int(input('Ingrese fila (0-14): '))
            location = (location_x, location_y)
            orientation = input('Ingresar (V/H): ')
            if self.game.scrabble_validate_word(word, location, orientation):
                self.game.put_word(word, location, orientation)
                self.add_score(word, location, orientation)
                break
            elif word == 0:
                break
            else:
                print("Valor ingresado no valido ")

    def exchange_tiles(self):
        amount = int(input("¿Cuántas fichas quieres intercambiar? (1-7): "))
        for i in range(amount):
            index = int(input("Elige la ficha que vas a intercambiar (1-7): "))
            self.game.current_player.exchange_tiles(index, self.game.bag_tiles)

    def surrender(self):
        print(f'Jugador {self.game.current_player.id} se ha rendido. ¡Fin del juego!')
        self.display_final_scores()

    def display_final_scores(self):
        sorted_players = sorted(self.game.players, key=lambda player: player.score, reverse=True)
        print("Puntajes finales de los jugadores:")
        for player in sorted_players:
            print(f"Jugador {player.id}: Puntaje = {player.score}")
            


    def add_score(self, word, location, orientation):
        self.game.scrabble_word_calculate_score(word, location, orientation)

    def play_game(self):
        play_again = 'y'  # Inicializa play_again como 'y' para comenzar el juego

        while play_again.lower() == 'y':
            self.initial_tiles()
            for player in self.game.players:
                player.rack = self.bag.take(7)  # Asignar 7 letras aleatorias a cada jugador
            self.game.show_board(self.board)
            while not self.game.game_over():
                self.game.next_turn()  # Cambiar el turno utilizando self.game
                self.show_current_player()
                self.take_turn()
                self.game.show_board(self.board)  # Muestra el tablero después de cada turno

            print('¡SE ACABO LO QUE SE DABA!')
            self.display_final_scores()

            # Pregunta si los jugadores desean volver a jugar
            play_again = input("¿Quieres volver a jugar? (y/n): ").strip().lower()

        print("¡Gracias por jugar al Scrabble!")






if __name__ == "__main__":
    main = Configure()
    main.play_game()