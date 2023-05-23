import sys
import pygame
from utility import UI

""" Program Constants """
FPS = 60
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 800
WINDOW_NAME = "Game 2"
WINDOW = UI().create_window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_NAME)


def game():
    game_clock = pygame.time.Clock()
    is_running = True
    while is_running:
        game_clock.tick(FPS)
        for event in pygame.event.get():  # closes the window
            if event.type == pygame.QUIT:
                sys.exit()


if __name__ == "__main__":
    game()