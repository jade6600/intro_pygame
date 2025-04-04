import pygame
# Inicializamos los módulos de pygame
pygame.init()

# Establecer título a la ventana
pygame.display.set_caption("Bandera de colombia")

# Establecemos las dimensiones de la ventana
ventana = pygame.display.set_mode((400, 400))

# seleciionar un color
amarillo = (255,250,0)
azul = (0,0,255)
rojo = (255,0,0)
superficie_aleatoria = pygame.Surface((300, 300))

# creamos una superficie
amarillo_Superficie = pygame.Surface((400,200))
azul_Superficie = pygame.Surface((400,100))
rojo_Superficie = pygame.Surface((400,100))

# Rellenamos la superficie de azul
amarillo_Superficie.fill(amarillo)
azul_Superficie.fill(azul)
rojo_Superficie.fill(rojo)


# Inserto o muevo la superficie en la ventana
ventana.blit(amarillo_Superficie, (0, 0))
ventana.blit(azul_Superficie, (0, 200))
ventana.blit(rojo_Superficie, (0, 300))
# Actualiza la visualización de la ventana
pygame.display.flip()

# Bucle del juego
while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        break

# Salimos de pygame
pygame.quit()
