import pygame
import random
from pieza import Pieza


# Constantes
ANCHO_VENTANA = 300
ALTO_VENTANA = 600
TAM_BLOQUE = 30
COLUMNAS = ANCHO_VENTANA // TAM_BLOQUE
FILAS = ALTO_VENTANA // TAM_BLOQUE
NEGRO = (0, 0, 0)
GRIS = (128, 128, 128)

# Formas de piezas
PIEZAS = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[0, 1, 0], [1, 1, 1]],  # T
    [[1, 1, 0], [0, 1, 1]],  # S
    [[0, 1, 1], [1, 1, 0]],  # Z
]


class Juego:
    def __init__(self):
        self.pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
        pygame.display.set_caption("Teatris")
        pygame.mixer.init()
        self.sonido_linea = pygame.mixer.Sound("sonidos/linea.wav")
        self.sonido_gameover = pygame.mixer.Sound("sonidos/gameover.wav")
        self.velocidad = 30
        self.reloj = pygame.time.Clock()
        self.tablero = self.crear_tablero()
        self.pieza_actual = Pieza(random.choice(PIEZAS))
        self.puntuacion = 0
        self.contador_caida = 0

    def hay_colision(self, pieza, tablero, dx=0, dy=0):
        for y, fila in enumerate(pieza.forma):
            for x, celda in enumerate(fila):
                if celda:
                    nx = pieza.x + x + dx
                    ny = pieza.y + y + dy
                    if nx < 0 or nx >= COLUMNAS or ny >= FILAS:
                        return True
                    if ny >= 0 and tablero[ny][nx] != NEGRO:
                        return True
        return False
    
    def crear_tablero(self):
        return [[NEGRO for _ in range(COLUMNAS)] for _ in range(FILAS)]

    def dibujar_tablero(self):
        for y in range(FILAS):
            for x in range(COLUMNAS):
                pygame.draw.rect(
                    self.pantalla,
                    self.tablero[y][x],
                    (x * TAM_BLOQUE, y * TAM_BLOQUE, TAM_BLOQUE, TAM_BLOQUE),
                    0,
                )
                pygame.draw.rect(
                    self.pantalla,
                    GRIS,
                    (x * TAM_BLOQUE, y * TAM_BLOQUE, TAM_BLOQUE, TAM_BLOQUE),
                    1,
                )

    def dibujar_pieza(self):
        for y, fila in enumerate(self.pieza_actual.forma):
            for x, celda in enumerate(fila):
                if celda:
                    pygame.draw.rect(
                        self.pantalla,
                        self.pieza_actual.color,
                        (
                            (self.pieza_actual.x + x) * TAM_BLOQUE,
                            (self.pieza_actual.y + y) * TAM_BLOQUE,
                            TAM_BLOQUE,
                            TAM_BLOQUE,
                        ),
                    )

    def eliminar_lineas(self):
        nuevas_filas = [
            fila for fila in self.tablero if any(color == NEGRO for color in fila)
        ]
        lineas_eliminadas = FILAS - len(nuevas_filas)
        for _ in range(lineas_eliminadas):
            nuevas_filas.insert(0, [NEGRO for _ in range(COLUMNAS)])
        self.tablero = nuevas_filas
        if lineas_eliminadas > 0:
            self.sonido_linea.play()
        return lineas_eliminadas

    def ejecutar(self):
        corriendo = True
        while corriendo:
            self.pantalla.fill(NEGRO)
            self.dibujar_tablero()
            self.dibujar_pieza()

            self.contador_caida += 1
            if self.contador_caida >= 30:
                if not self.hay_colision(self.pieza_actual, self.tablero, dy=1):
                    self.pieza_actual.y += 1
                else:
                    for y, fila in enumerate(self.pieza_actual.forma):
                        for x, celda in enumerate(fila):
                            if celda:
                                self.tablero[self.pieza_actual.y + y][
                                    self.pieza_actual.x + x
                                ] = self.pieza_actual.color
                    eliminadas = self.eliminar_lineas()
                    self.puntuacion += eliminadas * 100
                    if self.puntuacion >= 500 and self.velocidad > 5:
                        self.velocidad -= 5
                    if any(self.tablero[0][x] != NEGRO for x in range(COLUMNAS)):
                        corriendo = False
                    self.pieza_actual = Pieza(random.choice(PIEZAS))
                self.contador_caida = 0

            fuente = pygame.font.SysFont(None, 36)
            texto = fuente.render(f"Puntos: {self.puntuacion}", True, (255, 255, 255))
            self.pantalla.blit(texto, (10, 10))

            pygame.display.flip()

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    corriendo = False
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_LEFT and not self.hay_colision(
                        self.pieza_actual, self.tablero, dx=-1
                    ):
                        self.pieza_actual.x -= 1
                    elif evento.key == pygame.K_RIGHT and not self.hay_colision(
                        self.pieza_actual, self.tablero, dx=1
                    ):
                        self.pieza_actual.x += 1
                    elif evento.key == pygame.K_DOWN and not self.hay_colision(
                        self.pieza_actual, self.tablero, dy=1
                    ):
                        self.pieza_actual.y += 1
                    elif evento.key == pygame.K_UP:
                        self.pieza_actual.rotar()
                        if self.hay_colision(self.pieza_actual, self.tablero):
                            for _ in range(3):
                                self.pieza_actual.rotar()

            self.reloj.tick(self.velocidad)

        fuente = pygame.font.SysFont(None, 72)
        texto = fuente.render("Game Over", True, (255, 0, 0))
        self.pantalla.blit(texto, (40, ALTO_VENTANA // 2 - 36))
        pygame.display.flip()
        self.sonido_gameover.play()
        pygame.time.wait(3000)
