import pygame
import sys
import random

rojo = (255, 0, 0)
rojo = (255, 0, 0)
rojo = (255, 0, 0)
azul = (0, 0, 255)
rosita = (200, 0, 55)
amarillo = (210, 45, 0)
verde = (0, 250, 5)
negro = (0, 0, 0)
cian = ( 0,200,250)

pygame.init()

ventana = pygame.display.set_mode((500, 500))

pygame.display.set_caption("El Cuadrado que rebota")

clock = pygame.time.Clock()

XX = 300
MOVIMIENTO = 3

# cuadrado1
while True:
    clock.tick(50)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    ventana.fill(azul)

    XX += MOVIMIENTO

    if XX >= 451:
        XX = 451
        MOVIMIENTO = -3
    elif XX <= 0:
        XX = 0
        MOVIMIENTO = 3

    pygame.draw.rect(ventana, rojo, (XX, 0, 50, 50))

    pygame.draw.rect(ventana, rosita, (XX, 450, 50, 50))

    pygame.draw.rect(ventana, cian , (200, 250, 100, 100))

    pygame.draw.rect(ventana, verde, (0, XX, 50, 50))

    pygame.draw.rect(ventana, negro, (450,XX, 50, 50))


    
    pygame.display.flip()

