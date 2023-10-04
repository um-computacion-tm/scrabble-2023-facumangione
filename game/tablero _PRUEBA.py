import pygame
import sys
from models import BagTiles

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
ANCHO, ALTO = 800, 800
VENTANA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Scrabble")

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

# Crear un tablero
tablero = [[' ' for _ in range(15)] for _ in range(15)]

# Función para llenar el tablero con letras disponibles
def llenar_tablero():
    # Crea una instancia de la clase BagTiles
    bolsa = BagTiles()

    for fila in range(15):
        for columna in range(15):
            # Coloca una letra en cada celda del tablero
            if bolsa.tiles:  # Asegúrate de que haya letras disponibles
                letra = bolsa.tiles.pop(0).letter  # Obtén una letra disponible
                tablero[fila][columna] = letra

# Llenar el tablero con letras disponibles
llenar_tablero()

# Función para dibujar el tablero en la ventana de Pygame
def dibujar_tablero():
    for fila in range(15):
        for columna in range(15):
            pygame.draw.rect(VENTANA, BLANCO, (columna * 50, fila * 50, 50, 50))
            letra = tablero[fila][columna]
            texto = pygame.font.Font(None, 36).render(letra, True, NEGRO)
            VENTANA.blit(texto, (columna * 50 + 15, fila * 50 + 15))

# Bucle principal del juego
ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    # Llamar a la función para dibujar el tablero
    dibujar_tablero()

    # Actualizar la pantalla
    pygame.display.update()

# Finalizar Pygame
pygame.quit()
sys.exit()
