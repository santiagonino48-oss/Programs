import pygame
import random
import sys
import os

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
ANCHO = 800
ALTO = 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Space Invaders con Sprites Completos")

# Colores (RGB)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
BLANCO = (255, 255, 255)

# Reloj para controlar los FPS
reloj = pygame.time.Clock()
FPS = 60

# =====================================================
# --- CARGA DE IMÁGENES ---
# =====================================================
carpeta_juego = os.path.dirname(__file__)

ruta_img_jugador = os.path.join(carpeta_juego, "Nave.png")
ruta_img_enemigo = os.path.join(carpeta_juego, "Alien.png")
ruta_img_bala = os.path.join(carpeta_juego, "Bala.png") # Asegúrate de tener este archivo

try:
    # 1. Imagen del JUGADOR
    surface_jugador = pygame.image.load(ruta_img_jugador).convert_alpha()
    IMAGEN_JUGADOR = pygame.transform.scale(surface_jugador, (50, 40))

    # 2. Imagen del ENEMIGO
    surface_enemigo = pygame.image.load(ruta_img_enemigo).convert_alpha()
    IMAGEN_ENEMIGO = pygame.transform.scale(surface_enemigo, (40, 30))

    # 3. Imagen de la BALA
    surface_bala = pygame.image.load(ruta_img_bala).convert_alpha()
    IMAGEN_BALA = pygame.transform.scale(surface_bala, (10, 25))

except pygame.error as e:
    print(f"Error cargando imágenes. Verifica que 'Nave.png', 'Alien.png' y 'Bala.png' estén en la misma carpeta.\nDetalles: {e}")
    pygame.quit()
    sys.exit()

# =====================================================
# --- CLASES DEL JUEGO ---
# =====================================================

class Jugador:
    def __init__(self, imagen):
        self.image = imagen 
        self.ancho = 50
        self.alto = 40
        self.x = ANCHO // 2 - self.ancho // 2
        self.y = ALTO - 70
        self.velocidad = 7

    def dibujar(self):
        pantalla.blit(self.image, (self.x, self.y))

    def mover(self):
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT] and self.x > 0:
            self.x -= self.velocidad
        if teclas[pygame.K_RIGHT] and self.x < ANCHO - self.ancho:
            self.x += self.velocidad


class Enemigo:
    def __init__(self, x, y, imagen):
        self.image = imagen 
        self.ancho = 40
        self.alto = 30
        self.x = x
        self.y = y
        self.velocidad = 2

    def dibujar(self):
        pantalla.blit(self.image, (self.x, self.y))

    def mover(self, direccion):
        self.x += self.velocidad * direccion


class Bala:
    def __init__(self, x, y, imagen):
        self.image = imagen # Guardamos la imagen de la bala
        self.ancho = 10
        self.alto = 25
        self.x = x
        self.y = y
        self.velocidad = -10

    def dibujar(self):
        # Ahora dibujamos el sprite en lugar de un rectángulo plano
        pantalla.blit(self.image, (self.x, self.y))

    def mover(self):
        self.y += self.velocidad


# =====================================================
# --- Configuración y Generación de Elementos ---
# =====================================================

jugador = Jugador(IMAGEN_JUGADOR)
balas = []
enemigos = []

def crear_enemigos():
    for fila in range(3):
        for col in range(10):
            x = 80 + col * 60
            y = 50 + fila * 50
            enemigos.append(Enemigo(x, y, IMAGEN_ENEMIGO))

crear_enemigos()
direccion_enemigos = 1
puntuacion = 0
fuente = pygame.font.SysFont("Arial", 24)
juego_terminado = False

# =====================================================
# --- BUCLE PRINCIPAL ---
# =====================================================
ejecutando = True
while ejecutando:
    reloj.tick(FPS)
    pantalla.fill(NEGRO)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE and not juego_terminado:
                # CREACIÓN DE BALA CORREGIDA: Le pasamos IMAGEN_BALA y ajustamos el centrado (x - 5)
                balas.append(Bala(jugador.x + jugador.ancho // 2 - 5, jugador.y, IMAGEN_BALA))
            if evento.key == pygame.K_r and juego_terminado:
                jugador = Jugador(IMAGEN_JUGADOR)
                balas = []
                enemigos = []
                crear_enemigos()
                direccion_enemigos = 1
                puntuacion = 0
                juego_terminado = False

    if not juego_terminado:
        jugador.mover()

        # Actualizar balas
        for bala in balas[:]:
            bala.mover()
            if bala.y < 0:
                balas.remove(bala)

        # Movimiento de los enemigos
        bajar_nivel = False
        for enemigo in enemigos:
            enemigo.mover(direccion_enemigos)
            if enemigo.x <= 0 or enemigo.x >= ANCHO - enemigo.ancho:
                bajar_nivel = True

        if bajar_nivel:
            direccion_enemigos *= -1
            for enemigo in enemigos:
                enemigo.y += 15

        # Colisiones Bala-Enemigo
        for bala in balas[:]:
            for enemigo in enemigos[:]:
                if (bala.x < enemigo.x + enemigo.ancho and
                    bala.x + bala.ancho > enemigo.x and
                    bala.y < enemigo.y + enemigo.alto and
                    bala.y + bala.alto > enemigo.y):
                    
                    if bala in balas:
                        balas.remove(bala)
                    if enemigo in enemigos:
                        enemigos.remove(enemigo)
                    puntuacion += 10

        # Siguiente oleada
        if len(enemigos) == 0:
            crear_enemigos()

        # Condición de Game Over
        for enemigo in enemigos:
            if enemigo.y >= jugador.y - enemigo.alto:
                juego_terminado = True

    # --- DIBUJAR TODO ---
    jugador.dibujar()
    for enemigo in enemigos:
        enemigo.dibujar()
    for bala in balas:
        bala.dibujar()

    # Puntos
    texto_puntos = fuente.render(f"Puntos: {puntuacion}", True, BLANCO)
    pantalla.blit(texto_puntos, (10, 10))

    # Game Over
    if juego_terminado:
        fuente_grande = pygame.font.SysFont("Arial", 48)
        texto_game_over = fuente_grande.render("GAME OVER", True, ROJO)
        texto_reiniciar = fuente.render("Presiona 'R' para reiniciar o 'ESC' para salir", True, BLANCO)
        
        pantalla.blit(texto_game_over, (ANCHO // 2 - 120, ALTO // 2 - 50))
        pantalla.blit(texto_reiniciar, (ANCHO // 2 - 180, ALTO // 2 + 20))
        
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_ESCAPE]:
            ejecutando = False

    pygame.display.flip()

pygame.quit()
sys.exit()