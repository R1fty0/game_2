import pygame
import os
import random


class Image:
    def __init__(self, image_name, folder_name=None):
        """ Loads in a new image and provides other useful image related functions. """
        self.image = self.load_image(folder_name, image_name)

    def load_image(self, folder_name, image_name):
        """ Loads a new image into the game. """
        if folder_name is None:
            image = pygame.image.load(image_name)
        else:
            image = pygame.image.load(os.path.join(folder_name, image_name))
        return image

    def scale_image(self, width, height):
        """ Scales the class's image. """
        self.image = pygame.transform.scale(self.image, (width, height))


class UI:
    def create_window(self, width, height, name):
        """ Creates a new window. """
        window = pygame.display.set_mode((width, height))
        pygame.display.set_caption(name)
        return window


class Collider:
    def __init__(self, spawn_x, spawn_y, image, name):
        """ Creates a new collider and handles collision detection of said collider if required. """
        self.rect = pygame.Rect(spawn_x, spawn_y, image.get_width(), image.get_height())
        self.name = name

    def check_window_bounds(self, window_width, window_height) -> int:
        """
        Checks if the Collider has any part of the window and returns a value representing the result.
        (0 = No Collision, 1 = Hit Top, 2 = Hit Bottom, 3 = Hit Left, 4 = Hit Right)
        """
        value = 0
        # Check if collider hit top of game window
        if self.rect.top <= 0:
            value = 1
        # Check if collider hit bottom of game window
        elif self.rect.bottom >= window_height:
            value = 2
        # Check if collider hit left side of game window
        if self.rect.left <= 0:
            value = 3
        # Check if collider hit right side of game window
        elif self.rect.right >= window_width:
            value = 4
        return value


class Spawner:
    def generate_random_cooridnates(self, x_max, x_min, y_max, y_min) -> tuple:
        """ Generates a random set of coordinates. """
        x = random.randint(x_min, x_max)
        y = random.randint(y_min, y_max)
        return x, y
