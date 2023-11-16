import pygame
from random import randint, choice
from GameObject import GameObject
# pygame.init()

# Define lanes
lanes = [93, 218, 340]


# -------------------------------------------
# Apple class that inherits from GameObject
class Apple(GameObject):
    def __init__(self):
        super(Apple, self).__init__(0, 0, './images/apple.png')
        self.dx = 0
        self.dy = (randint(0, 320) / 100) + 1
        self.reset()

    # ------------------------------------
    def move(self):
        """
        :desc: Updates the player's position in each frame
        :return: None
        """
        super().move()
        # Check the y position of the apple
        if self.y > 500:
            self.reset()

    # ------------------------------------
    def reset(self):
        """
        :desc: Moves sprite to the center of the screen. This is the player's starting position.
        :return: None
        """
        self.x = choice(lanes)
        self.y = -64
