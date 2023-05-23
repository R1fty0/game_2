import pygame
from utility import Image
from utility import Collider


class PlayerControls:
    def __init__(self, up_key, down_key, left_key, right_key):
        self.controls = [up_key, down_key, left_key, right_key]

    def check_for_input(self) -> int:
        """
            Checks each control key for input and returns a corresponding
            value if the key is pressed by the user (0 = Up,
            1 = Down, 2 = Left, Right = 3).
        """
        keyboard_event = pygame.key.get_pressed()
        for key in self.controls:
            if keyboard_event[key]:
                count = self.controls.index(key)
                return count


class Player(Image, Collider, PlayerControls):
    def __init__(self, image_name, folder_name, spawn_x, spawn_y, up, down, left, right, velocity):
        Image.__init__(self, image_name, folder_name)  # loads player image
        Collider.__init__(self, spawn_x, spawn_y, self.image, "Player")  # creates a collider for the player
        PlayerControls.__init__(self, up, down, left, right)   # handles player controls
        self.velocity = velocity

    def movement(self):
        """ Handles Player Movement - NOTE: DOES NOT CHECK FOR COLLISION DETECTION. """
        key = self.check_for_input()
        if key is None:
            return
        else:
            if key == 0:  # Up
                self.rect.y += self.velocity
            if key == 1:  # Down
                self.rect.y -= self.velocity
            if key is 2:  # Left
                self.rect.x += self.velocity
            if key is 3:  # Right
                self.rect.x -= self.velocity
