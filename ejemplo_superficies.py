import pygame
import random

# Inicializamos los módulos de pygame
pygame.init()

# Establecer título a la ventana
pygame.display.set_caption("Superficie con color aleatorio")

# Establecemos las dimensiones de la ventana
ventana = pygame.display.set_mode((400, 400))

# Función para generar un color aleatorio
def generar_color_aleatorio():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Generamos un color aleatorio
color_aleatorio = generar_color_aleatorio()

# Crear una superficie
superficie_aleatoria = pygame.Surface((300, 300))

# Rellenamos la superficie con el color aleatorio
superficie_aleatoria.fill(color_aleatorio)

# Inserto o muevo la superficie en la ventana
ventana.blit(superficie_aleatoria, (0, 0))

# Actualiza la visualización de la ventana
pygame.display.flip()

# Bucle del juego
while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        break

# Salimos de pygame
pygame.quit()

