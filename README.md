# Estructura de un juego en pygame

## Inicializacion

Como en todo programa en python, se deben importar los modulos o librerias a utilizar.

`import pygame`

- inicializar pygame usando la funcion init(). Inicializa todos los modulos de pygame importados.

``pygame.init()``

## Visualizacion de la ventanz

``ventana= pygame.display.set_mode((600,400))``

- set_mode es la funcon encargada de definir el tamaño de la ventana. En el ejemplo se esta definiendo una ventana de 600 pixeles de ancho y 400 pixeles de alto. 

``pygame.display.set_caption("mi ventana")``

- set_caption es la funcion que añade un titulo a la ventana.

### Funcion set_mode()

``set_mode(size =(0,0), flags = 0, depth = 0, display = 0)``

- size = (600,400) : define el tamaño de la ventana
- flags : define uno o mas comportamientos para la ventana
    - valores:
        - pygame.FULLSCREEN
        - pygame.RESIZABLE
    - Ejemplo:
        - flags = pygame.FULLSCREEN | pygame.RESIZABLE: pantalla completa, dimensiones modificables.

## Bucle de juego - game loop

- bucle infinito quese interrumpira al cumplir ciertos criterios 

- reloj interno del juego

- en cada interacion del buce del juego podemos mover a un personaje, o tener en cuenta que un objeto a alcanzado a otro, o que se a cruzado la linea de llegada lo que quiere decir que la partida ha terminado.

- cada iteracion es una oportunidad para actualizar todos los datos relacionados con el estado de la partida.

- en cada iteracion se realisan las siguientes tareas:
    1. comprobar que no se alcanzan las condiciones de parada, en cuyo caso se interrumpe el bucle.
    2. Actualizar los recursos necesarios para la iteracion actual
    3. Obtener las entradas del sistemas, o de interaccion con el jugador.
    4. actualizar todas las identidades que
    caracterizan el juego.
    5. refrescar la pantalla.

## Superficies pygame

- Superficie: 
    - elemento geometrico 
    - linea , poligono, imagen, texto, que se muestra en la pantalla.
    - El poligono se puede o no rellenar de color.
    - Las supericies se crean de diferente manera dependiendo del tipo:
        - imagen: image.load()
        - texto: font.render()
        - superficie generica: con pygame.surface()
        - ventana del juego: pygame.display.set_mode()

# Ejemplo bandera de colombia 
```# importamos la libreria pygame

import pygame

# inicializamos los modulos de pygame

pygame.init()

# Establecer titulo a la ventana

pygame.display.set_caption("surface")

# Establecemos las dimenciones de la ventana

ventana = pygame.display.set_mode((400,400))

# definimos un color
amarillo = (255,255,0)
azul = (0,0,255)
rojo = (255,0,0)
# creamos una superficie

amarillo_superficie = pygame.Surface((400,200))
azul_superficie = pygame.Surface((400,100))
rojo_superficie = pygame.Surface((400,100))

# rellenamos la superficie de azul

amarillo_superficie.fill((amarillo))
azul_superficie.fill((azul))
rojo_superficie.fill((rojo))

# inserto o muevo la superficie en la ventana

ventana.blit(amarillo_superficie, (0,0))
ventana.blit(azul_superficie, (0,200))
ventana.blit(rojo_superficie, (0,300))

# actualiza la visualizacion de la ventana

pygame.display.flip()

# bucle del juego

while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        break
pygame.quit()
```
![imagen bandera](screen02.png)


## Bandera Colombia

## Gestion del tiempo y los eventos

### Modulo time

- Ofrece varias funciones que permiten cronometrar la sesion actual (desde el init()) o pausar, la ejecucion, por ejemplo.
- Funciones:
    - pygame.time.get_ticks
    - pygame.time.waitpygame.time.delay

- Objeto clock
    - La funcion tick permite actualizar el reloj asociado con el juego actual.
    - Se llama cada vez que se actualiza la pantalla del juego.
    - Permite especificar el numero maximo de fotograma que se muuestran por segundo, y por tanto,limitar y controlar la velocidad de ejecucion del juego.
    - Si insertamos en un bucle de juego la siguiente linea, garantizamos que nunca sera mas rapido de 58 fotogramas por segundo: `Clock.tick[50]`

### Gestion de eventos 
- Hay diferentes formas para que el programa sepa que se ha desencadenado un evento
- Es ensencial qe lo programas puedan conocer inmediatamente las acciones del jugador a traves del teclado, el mouse, el joysticik o cualquier otro periferico.

#### Funcion pygame.event.get
- Permite obtener todos los eventos en espera de ser procesados y que estan disponibles en una cola.
- Si no hay ninguno, entonces se obtiene una coleccion vacia.
```Python
#Usamos un ucle for para recorrer todos los eventos de la coleccion obtenida al llamar a la funccion get.
for event in pygame.event.get()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            PARAR_JUEGO = True
``` 
#### Funcion pygame.event.wait
- Esta funcion espera a que ocurra un evento, y en cuento sucede esta disponible.

```Python
while True:
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        break
``` 
#### Funcion pygame.event.poll 
- Devuelve solo uno de los eventos que estan en la cola de espera.


## sonidos en Pygame
- Pygame.mixer: Modulo que permite la gestion del sonido.
-music: submodulo que gestiona lamusica de fondo solo hay uno a la vez.
- Sound: Objeto de mixer que se puede instanciar varias veces para usarlo en efectos de sonido del juego.

### Archivos de sonido
- Se recomienda usar dosfromatos principalmente:
    - Formato WAV (WaveFrom Audio File Format)
    - Formato y gratuito ODG.

### Channel (canal) en Pygame
- Un juego tienen varios canales de sonido.
- Se puede asignar al canal numero 1 y otro al numero 2.
- Entonces es posible reproducir sonidos simultaneamente activando la lectura en diferentes canales.

## Sprites
- Objeto que asocia una ubicacion, una representacion grafica(esta o aquell imagen, por ejemplo)y un conjunto de propiedades.
- Estas propiedades pueden ser un nombre, un texto, valores boleanos que caracterizan el objetoen cuestion(por ejemplo si el objeto se puede mover o no)
- Una posible traduccion del termino sprite podria ser "imagen-objeto" que se actualiza con cada iteracion del juego.
- Cuanto mas complejo es el juego, mas objetos graficos tiene que gestionar y actualizar, lo que puede ser tedioso.
- Pygame usa no solo la nocion de sprite, sino tambien la nocion del grupo de sprites (grupo) 
- La nocion de grupo permite agrupar los objetos del mismo tipo. Ejemplo: todos los soldados del eercito lo que se entiende como una coleccion de estancias de una clase Soldado.
- Un determinado procesamiento se puede aplicar a un conjunto o subconjunto de sprites. Ejemplo: cambiar el color de todos losenemigos o hacer invisibles algunos objetos.