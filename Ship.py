import pygame
from random import randint, choice
from GameObject import GameObject
# pygame.init()

# Define lanes
lanes = [93, 218, 340]


# -------------------------------------------
# Create a spaceship class that will extend GameObject, subclass
# Should appear in the background moving vertically
class Ship(GameObject):
    def __init__(self):
        super(Ship, self).__init__(0, 0, './images/spaceship.png')
        self.dx = 0
        self.reset()

    def move(self):
        """
        :desc: Move the sprite or image based on dx/dy, resets if larger than screen
        :return: None
        """
        self.x += self.dx
        if self.x > 500:
            self.reset()

    def reset(self):
        """
        :desc: reset ship
        :return: None
        """
        self.x = -64
        self.y = randint(0, 220 - 64)
        self.dx = randint(0, 200) / 100
        self.surf = pygame.image.load('./images/spaceship.png')