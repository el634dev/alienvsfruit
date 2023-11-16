# import pygame
from random import randint, choice
from GameObject import GameObject
# pygame.init()

# Define lanes
lanes = [93, 218, 340]


# -------------------------------------------
# Strawberry class that inherits from GameObject
class Strawberry(GameObject):
    def __init__(self):
        super(Strawberry, self).__init__(0, 0, './images/strawberry.png')
        self.dx = 0
        self.dy = (randint(0, 310) / 100) + 1
        self.reset()

    def move(self):
        """
        :desc: Move the sprite or image based on dx/dy, resets if larger than screen
        :return: None
        """
        super().move()
        # Check the y position of the apple
        if self.x > 500:
            self.reset()

    def reset(self):
        """
        :desc: resets the sprite if the sprite goes over 500 on the y-axis
        :return: None
        """
        self.x = choice(lanes)
        self.y = 64
