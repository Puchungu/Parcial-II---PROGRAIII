import pygame
import sys

# Inicializar Pygame
pygame.init()

# Crear una pantalla de 640x480 píxeles
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Vaquero Pequeñito')

# Definir colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
MARRON = (139, 69, 19)
AZUL = (0, 0, 255)
CAFE = (160, 82, 45)
AMARILLO = (255, 255, 0)

# Clase para el vaquero
class Vaquero:
    def __init__(self, x, y):
        self.x = x  # Coordenada base del vaquero
        self.y = y
        self.velocidad = 3  # Velocidad del vaquero (más lenta)

    def dibujar(self, screen):
        
        # Sombrero
        pygame.draw.rect(screen, MARRON, (self.x, self.y, 60, 10))  # Cinturón del sombrero
        pygame.draw.rect(screen, MARRON, (self.x - 20, self.y + 10, 100, 20))  # Ala del sombrero
        
        # Cabeza
        pygame.draw.rect(screen, AMARILLO, (self.x + 10, self.y + 30 , 40, 40))  # Cabeza
        
        # Cuerpo
        pygame.draw.rect(screen, AZUL, (self.x, self.y + 70, 60, 60))  # Torso
        
        # Piernas
        pygame.draw.rect(screen, NEGRO, (self.x, self.y + 130, 20, 40))  # Pierna izquierda
        pygame.draw.rect(screen, NEGRO, (self.x + 40, self.y + 130, 20, 40))  # Pierna derecha

        # Brazos
        pygame.draw.rect(screen, CAFE, (self.x - 20, self.y + 70, 20, 40))   # Brazo izquierdo
        pygame.draw.rect(screen, CAFE, (self.x + 60, self.y + 70, 20, 40))   # Brazo derecho

        # Cinturón
        pygame.draw.rect(screen, NEGRO, (self.x, self.y + 120, 60, 10))  # Cinturón
        
    # Método para mover al vaquero y evitar que se salga de la pantalla
    def mover(self, dx, dy, screen_width, screen_height):
        # Actualizar posición, pero controlar que no se salga de los límites de la pantalla
        nuevo_x = self.x + dx
        nuevo_y = self.y + dy
    
        # Asegurarse de que el vaquero no salga de la pantalla
        if 0 <= nuevo_x <= screen_width - 60:  # Ancho del vaquero es 60
            self.x = nuevo_x
        if 0 <= nuevo_y <= screen_height - 170:  # Alto del vaquero es aproximadamente 170 (sombrero a pies)
            self.y = nuevo_y

# Crear una instancia del vaquero
vaquero = Vaquero(300, 100)

# Configurar el reloj de Pygame para controlar los FPS
clock = pygame.time.Clock()

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Capturar la entrada del teclado para mover al vaquero con W, A, S, D
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        vaquero.mover(-vaquero.velocidad, 0, 640, 480)  # Mover a la izquierda (A)
    if keys[pygame.K_d]:
        vaquero.mover(vaquero.velocidad, 0, 640, 480)  # Mover a la derecha (D)
    if keys[pygame.K_w]:
        vaquero.mover(0, -vaquero.velocidad, 640, 480)  # Mover hacia arriba (W)
    if keys[pygame.K_s]:
        vaquero.mover(0, vaquero.velocidad, 640, 480)  # Mover hacia abajo (S)

    # Rellenar la pantalla de color blanco
    screen.fill(BLANCO)

    # Dibujar el vaquero
    vaquero.dibujar(screen)

    # Actualizar la pantalla
    pygame.display.update()

    # Limitar a 60 fotogramas por segundo (FPS)
    clock.tick(60)

# Salir de Pygame
pygame.quit()
sys.exit()

