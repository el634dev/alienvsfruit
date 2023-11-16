import pygame
from random import randint, choice
from GameObject import GameObject
# pygame.init()

# Define lanes
lanes = [93, 218, 340]


# ---------------------------------------------
# Create Bomb class this will extend GameObject, subclass
class Bomb(GameObject):
    def __init__(self):
        super(Bomb, self).__init__(0, 0, './images/bomb.png')
        self.dx = 0
        self.dy = (randint(0, 310) / 100) + 1
        self.reset()

    def move(self):
        """
        :desc: Move the sprite or image based on dx/dy, resets if larger than screen
        :return: None
        """
        super().move()
        # Check the x and y position
        if self.x > 500 or self.x < -64 or self.y > 500 or self.y < -64:
            self.reset()

    def reset(self):
        """
        :desc: resets the sprite if the sprite goes over 500 on the y-axis
        :return: None
        """
        self.x = choice(lanes)
        self.y = -64
