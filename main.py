import pygame
from juego import Juego

# Inicialización
pygame.init()

if __name__ == "__main__":
    juego = Juego()
    juego.ejecutar()
    pygame.quit()