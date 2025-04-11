import pygame
import sys
import random

rojo = (255, 0, 0)
azul = (0, 0, 255)
amarillo = (255,225,0)
moradito = (170, 27, 219)
marron = (255, 0, 255)

pygame.init()

ventana = pygame.display.set_mode((500, 500))

pygame.display.set_caption("El Cuadrado que rebota")

clock = pygame.time.Clock()

XX = 300
MOVIMIENTO = 5

YY = 255
MOVIMIENTO_YY = 5

while 1:
    clock.tick(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    ventana.fill(azul)

    XX = XX + MOVIMIENTO

    if XX >= 450:
        XX = 450
        MOVIMIENTO = -5
    elif XX <= 0:
        XX = 0
        MOVIMIENTO = 5
    
    YY = YY + MOVIMIENTO

    if YY >= 450:
        YY = 450
        MOVIMIENTO_YY= -5
    elif YY <= 0:
        YY = 0
        MOVIMIENTO_YY = 5


    pygame.draw.rect(ventana, rojo, (XX,0, 50, 50))
    pygame.draw.rect(ventana, amarillo,(XX,450, 50, 50))
    pygame.draw.rect(ventana, marron,(0, YY ,50, 50))
    pygame.draw.rect(ventana, moradito,(450, YY ,50, 50))

    color_aleatorio = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    pygame.draw.rect(ventana, color_aleatorio,(200,200,100,100))
   
    pygame.display.flip()