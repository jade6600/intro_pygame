## Sprite permite representar cualquier cosa que se ve en tu juego (como personajes o objetos) como una imagen con una posición en la pantalla, facilitando que Pygame los dibuje y detecte si chocan entre sí. Es como tener una plantilla para todos los "actores" visuales de tu juego.

import pygame
from pygame.sprite import Sprite

# Inicializar Pygame
pygame.init()

# Dimensiones de la pantalla
ancho = 300
alto = 200
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Sprite Básico Sin Group")

# Color verde
verde = (0, 255, 0)
blanco = (255, 255, 255)

# Clase para un círculo simple (hereda de Sprite)
class Circulo(Sprite):
    def __init__(self, x, y, radio, color):
        super().__init__()
        self.radio = radio
        self.image = pygame.Surface((radio * 2, radio * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, color, (radio, radio), radio)
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        # En este ejemplo, el círculo no se mueve
        pass

# Crear un círculo (instancia de nuestro Sprite)
mi_circulo = Circulo(ancho // 2, alto // 2, 20, verde)

# Bucle principal del juego
ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    # Actualizar el sprite directamente
    mi_circulo.update()

    # Dibujar el fondo
    pantalla.fill(blanco)

    # Dibujar el sprite directamente usando su image y rect
    pantalla.blit(mi_circulo.image, mi_circulo.rect)

    # Actualizar la pantalla
    pygame.display.flip()

# Finalizar Pygame
pygame.quit()