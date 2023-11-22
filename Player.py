import pygame
from random import randint, choice
from GameObject import GameObject
# pygame.init()

# Define lanes
lanes = [93, 218, 340]


# ---------------------------------------------
# Create player class this will extend GameObject, subclass
class Player(GameObject):
    def __init__(self):
        super(Player, self).__init__(0, 0, './images/player.png')
        self.dx = 0
        self.dy = 0
        self.pos_x = 1
        self.pos_y = 1
        self.reset()

    def left(self):
        """
        :desc: move the player when the left key is pressed
        :return: None
        """
        if self.pos_x > 0:
            self.pos_x -= 1
            self.update_dx_dy()

    # ------------------------------------
    def right(self):
        """
        :desc: move the player when the right key is pressed
        :return: None
        """
        if self.pos_x < len(lanes) - 1:
            self.pos_x += 1
            self.update_dx_dy()

    # ------------------------------------
    def up(self):
        """
        :desc: move the player when the up key is pressed
        :return: None
        """
        if self.pos_y > 0:
            self.pos_y -= 1
            self.update_dx_dy()

    # ------------------------------------
    def down(self):
        """
        :desc: move the player when the down key is pressed
        :return: None
        """
        if self.pos_y < len(lanes) - 1:
            self.pos_y += 1
            self.update_dx_dy()

    # ------------------------------------
    def move(self):
        """
        :desc: Updates the player's position in each frame
        :return: None
        """
        # dx is where to go and x is the start
        # Calculates the distance to move
        self.x -= (self.x - self.dx) * 0.25
        self.y -= (self.y - self.dy) * 0.25

    # ------------------------------------
    def update_dx_dy(self):
        """
        :desc: want the player to change lanes
        :return: None
        """
        self.dx = lanes[self.pos_x]
        self.dy = lanes[self.pos_y]

    # ------------------------------------
    def reset(self):
        """
        :desc: Moves sprite to the center of the screen. This is the player's starting position.
        :return: None
        """
        self.x = lanes[self.pos_x]
        self.y = lanes[self.pos_y]
        self.dx = self.x
        self.dy = self.y
