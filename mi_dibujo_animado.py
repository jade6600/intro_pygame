import pygame
import sys
import math 

# Colores
gris3 = (98, 101, 127)
gris2 = (144,148, 151)
gris = (208, 211, 212)
rojito = (255, 0, 0)
azul = (0, 0, 255)
verde = (0,255,0)
rosado = (255,192,203)
negro = (0,0,0)
amarillo = (255,255,0)
blanco = (255,255,255)
Naranja = (255,165,0)
cian = (0,255,255)
marroncito = (120,66,18)
PI = math.pi

pygame.init()
ventana = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Trencito")
clock = pygame.time.Clock()

# nubecitas
nube1_x = -100 # Nubecita1
nube2_x = 700 # Nubecita2
pajaro_x = -50 # Pajarito abstracto
# Bucle principal del juego
while 1:
    clock.tick(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    ventana.fill(blanco)

    # Nube 1
    nube1_x += 1
    if nube1_x > 650:
        nube1_x = -100
    pygame.draw.circle(ventana, cian, (nube1_x + 20, 100), 20)
    pygame.draw.circle(ventana, cian, (nube1_x + 40, 90), 25)
    pygame.draw.circle(ventana, cian, (nube1_x + 60, 100), 20)
    pygame.draw.circle(ventana, cian, (nube1_x + 40, 110), 22)

    # Nube 2
    nube2_x -= 1
    if nube2_x < -100:
        nube2_x = 620
    pygame.draw.circle(ventana, cian, (nube2_x + 20, 150), 20)
    pygame.draw.circle(ventana, cian, (nube2_x + 40, 140), 25)
    pygame.draw.circle(ventana, cian, (nube2_x + 60, 150), 20)
    pygame.draw.circle(ventana, cian, (nube2_x + 40, 160), 22)

    # Pajarito: 
    pajaro_x += 2
    if pajaro_x > 650:
        pajaro_x = -50
    pygame.draw.circle(ventana, rojito, (pajaro_x + 40, 180), 8) # cuerpo
    pygame.draw.circle(ventana, rojito, (pajaro_x + 50, 175), 5) # cabeza
    pico = [(pajaro_x + 55, 175), (pajaro_x + 60, 178), (pajaro_x + 55, 180)]# pico
    pygame.draw.polygon(ventana, Naranja, pico)


    # Tren 
    pygame.draw.rect(ventana, rosado, (240,350, 300,150))
    pygame.draw.rect(ventana, negro, (400,490, 60,20))
    pygame.draw.rect(ventana, negro, (300,490, 60,20))
    pygame.draw.rect(ventana, gris2, (220,375, 20,100))
    pygame.draw.rect(ventana, gris2, (195,365, 25,120))
    pygame.draw.rect(ventana, gris2, (370,230,150,120))
    pygame.draw.rect(ventana, blanco, (395,250,100,80))
    pygame.draw.rect(ventana, gris2, (360,210,170,25))
    pygame.draw.rect(ventana, gris3, (370,190,150,20))
    pygame.draw.rect(ventana, gris3, (295,290,40,60))
    pygame.draw.rect(ventana, gris3, (285,265,60,25))
    pygame.draw.rect(ventana, rosado, (20,85, 550,450), 5)
    pygame.draw.rect(ventana, verde, (0,530,600,85))

    # Textos
    fuente_arial = pygame.font.SysFont("Arial", 25, 1, 1)
    texto = fuente_arial.render("Colegio San Jose de guanenta", 3 , negro)
    ventana.blit(texto,(3, 3))
    texto = fuente_arial.render("Especialidad de Sistemas", 3 , negro)
    ventana.blit(texto,(3, 20))
    texto = fuente_arial.render("Soreth Florez", 5 , negro)
    ventana.blit(texto,(310, 400))

    # Ruedas del tren 
    pygame.draw.circle(ventana, gris, (290,500), 30 )
    pygame.draw.circle(ventana, gris, (390,500), 30 )
    pygame.draw.circle(ventana, gris, (490,500), 30 )
    pygame.draw.circle(ventana, amarillo, (445,287), 45 )
    pygame.draw.circle(ventana, blanco, (427,277), 12 )
    pygame.draw.circle(ventana, blanco, (465,277), 12 )
    pygame.draw.circle(ventana, marroncito, (427,277), 7 )
    pygame.draw.circle(ventana, marroncito, (465,277), 7 )
    pygame.draw.circle(ventana, rojito, (448,307), 10 )
    

    pygame.display.flip()