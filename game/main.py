from game.scrabble import ScrabbleGame
from io import StringIO
from game.get_player_count import show_board, show_player, get_player_count, get_inputs


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

#INICIAR JUEGO

def main():

    player_count = get_player_count()
    game = ScrabbleGame(player_count)
    while game.is_playing():
        show_board(game.get_board())
        show_player(*game.get_current_player())
        word, coords, orientation = get_inputs()
        try:
            game.play(word, coords, orientation)
        except Exception as e:
            print(e)
    
    print('Bienvenido') 
    
    
if __name__ == '__main__':
    main()