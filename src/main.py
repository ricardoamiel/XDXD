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
##button_radius = 50

# Radio de las notas (círculos)
note_radius = 20

# Velocidad de las notas
note_speed = 2

# Notas iniciales
notes = []

# Puntuación
score = 0

# Botones asignados a teclas
button_keys = {'Q': 0, 'W': 1, 'E': 2}

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

# Función para verificar la colisión de una nota con un botón
def check_collision(note, button_index):
    button_x, button_y = button_positions[button_index]
    distance = ((note['x'] - button_x) ** 2 + (note['y'] - button_y) ** 2) ** 0.5
    return distance <= note_radius

# Función principal del juego
def game_loop():
    pygame.mixer.music.play(-1)  # Reproduce la música de fondo en bucle

    running = True
    score = 0  # Definimos la variable de puntuación al comienzo

    next_note_time = time.time() + random.uniform(1, 3)  # Tiempo de aparición de la próxima nota

    bar_note_active = False  # Estado de la nota tipo barra
    bar_note_score = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Lógica del juego

        current_time = time.time()

        # Genera una nota aleatoria en la parte superior
        if current_time > next_note_time:
            if random.randint(1, 100) < 85:  # 85% de probabilidad de generar una nota
                notes.append({'x': random.choice([200, 420, 640]), 'y': 0})
                next_note_time = current_time + random.uniform(1, 3)
            else:
                bar_note_active = True
                bar_note_start_time = current_time
                bar_note_score = 0

        # Si hay una nota tipo barra activa, verifica si la tecla está presionada
        if bar_note_active:
            if pygame.key.get_pressed()[ord('R')]:  # Reemplaza 'R' por la tecla que desees
                bar_note_score += 1

        # Mueve las notas hacia abajo y verifica colisiones
        for note in notes:
            note['y'] += note_speed

            for key, value in button_keys.items():
                if key in ['Q', 'W', 'E']:
                    if pygame.key.get_pressed()[ord(key)] and check_collision(note, value):
                        notes.remove(note)
                        score += 300

            if note['y'] > screen_height:
                notes.remove(note)
                score += 50

        # Dibuja la imagen de fondo
        screen.blit(background, (0, 0))

        # Dibuja los botones (círculos)
        for i in range(3):
            pygame.draw.circle(screen, [GREEN, RED, YELLOW][i], button_positions[i], note_radius)

        # Dibuja y verifica colisiones de las notas
        for note in notes:
            pygame.draw.circle(screen, WHITE, (note['x'], note['y']), note_radius)
            for key, value in button_keys.items():
                if key in ['Q', 'W', 'E']:
                    if pygame.key.get_pressed()[ord(key)] and check_collision(note, value):
                        notes.remove(note)
                        score += 300
                        break
            if note['y'] > screen_height:
                notes.remove(note)
                score += 50

        # Dibuja la puntuación en la pantalla
        font = pygame.font.Font(None, 36)
        text = font.render(f'Puntuación: {score}', True, RED)
        screen.blit(text, (10, 10))

        # Actualiza la pantalla
        pygame.display.update()

    pygame.quit()
    quit()

game_loop()