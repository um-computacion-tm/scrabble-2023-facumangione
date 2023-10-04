import pygame

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
ANCHO, ALTO = 800, 800
VENTANA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Scrabble")

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

# Función para dibujar el tablero
def dibujar_tablero():
    VENTANA.fill(BLANCO)
    # Dibuja el tablero aquí, por ejemplo, líneas y casillas especiales
    # Puedes usar pygame.draw.rect() para dibujar celdas cuadradas

    # Actualiza la pantalla
    pygame.display.update()

# Bucle principal del juego
ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    # Llamar a la función para dibujar el tablero
    dibujar_tablero()

# Finalizar Pygame
pygame.quit()