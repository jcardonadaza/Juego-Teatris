import random

ANCHO_VENTANA = 300
ALTO_VENTANA = 600
TAM_BLOQUE = 30
COLUMNAS = ANCHO_VENTANA // TAM_BLOQUE

COLORES = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]

class Pieza:
    def __init__(self, forma):
        self.forma = forma
        self.color = random.choice(COLORES)
        self.x = COLUMNAS // 2 - len(forma[0]) // 2
        self.y = 0

    def rotar(self):
        self.forma = [list(fila) for fila in zip(*self.forma[::-1])]