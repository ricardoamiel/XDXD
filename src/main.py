import pygame
import random
import time

# Inicializa Pygame
pygame.init()

# Configuración de la pantalla
screen_width = 960
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Skibidi Toilet x Peso Pluma Game")

# Colores
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Carga la imagen de fondo
background = pygame.image.load("C:/Users/Godel/Documents/GitHub/XDXD/others/quelepareceesamorra.jpeg")# Reemplaza "background.jpg" con tu imagen de fondo
background = pygame.transform.scale(background, (screen_width, screen_height))

# Carga la música de fondo
pygame.mixer.music.load("C:/Users/Godel/Documents/GitHub/XDXD/others/ella_baila_sola.mp3")  # Reemplaza "background_music.mp3" con tu música
pygame.mixer.music.set_volume(0.05)  # Ajusta el volumen a tu preferencia (de 0.0 a 1.0)

# Radio de los botones (círculos)
button_radius = 50

# Posiciones de los botones (centros de los círculos)
button_positions = [(200, 600), (420, 600), (640, 600)]

# Inicialización de Pygame Mixer para efectos de sonido
pygame.mixer.init()

# Función para mostrar un mensaje en la pantalla
def message_display(text):
    font = pygame.font.Font(None, 36)
    text_surface = font.render(text, True, RED)
    text_rect = text_surface.get_rect()
    text_rect.center = (screen_width // 2, screen_height // 2)
    screen.blit(text_surface, text_rect)
    pygame.display.update()
    time.sleep(2)  # Muestra el mensaje durante 2 segundos

# Función principal del juego
def game_loop():
    pygame.mixer.music.play(-1)  # Reproduce la música de fondo en bucle

    running = True
    score = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Lógica del juego
        # Aquí debes agregar la generación de pixeles al azar y la detección de clics en los botones

        # Dibuja la imagen de fondo
        screen.blit(background, (0, 0))

        # Dibuja los botones (círculos)
        for i in range(3):
            pygame.draw.circle(screen, [GREEN, RED, YELLOW][i], button_positions[i], button_radius)

        # Actualiza la pantalla
        pygame.display.update()

    pygame.quit()
    quit()

game_loop()
