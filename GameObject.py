import pygame
# pygame.init()


# ----------------------------------------
# GameObject class that inherits from the Sprite class, parent class
class GameObject(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super(GameObject, self).__init__()
        self.surf = pygame.image.load(image)
        self.x = x
        self.y = y
        self.rect = self.surf.get_rect()

    def move(self):
        """
        :desc: Move GameObject
        :return:
        """
        self.x += self.dx
        self.y += self.dy

    def render(self, screen):
        """
        :desc: renders an image to the screen
        :param screen: Displays the frame
        :return: None
        """
        self.rect.x = self.x
        self.rect.y = self.y
        screen.blit(self.surf, (self.x, self.y))
