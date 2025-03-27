# filepath: /teatris-game/teatris-game/src/main.py

import pygame
from game.board import Board
from game.tetromino import Tetromino
from game.game_logic import GameLogic

def main():
    pygame.init()
    
    # Configuración de la ventana del juego
    screen_width = 300
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Teatris Game")

    # Inicialización de componentes del juego
    board = Board()
    tetromino = Tetromino()
    game_logic = GameLogic(board, tetromino)

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Manejo de entradas del jugador
            game_logic.handle_input(event)

        # Actualización de la lógica del juego
        game_logic.update()

        # Dibujo del estado del juego
        screen.fill((0, 0, 0))  # Limpiar pantalla
        board.draw(screen)
        tetromino.draw(screen)
        pygame.display.flip()

        clock.tick(60)  # Limitar a 60 FPS

    pygame.quit()

if __name__ == "__main__":
    main()