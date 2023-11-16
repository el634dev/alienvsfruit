import pygame


class ScoreBoard(pygame.sprite.Sprite):
    def __init__(self, x, y, score):
        super(ScoreBoard, self).__init__()
        self.score = score
        self.font = pygame.font.SysFont('Courier New', 45)
        self.surf = self.font.render(f"{self.score}", False, (0, 0, 0))
        self.dx = 0
        self.dy = 0
        self.x = x
        self.y = y

    def update(self, points):
        """
        :Desc: Update the score, call this when updating the score
        :param points: Integer
        :return: None
        """
        self.score += points

    def move(self):
        """
        :desc: Most likely will not move but just in case
        :return: None
        """
        self.x += self.dx
        self.y += self.dy

    def render(self, screen):
        """
        :desc: Rendering the text
        :param screen: The frame of the pygame window
        :return: None
        """
        self.surf = self.font.render(f"{self.score}", False, (0, 0, 0))
        screen.blit(self.surf, (self.x, self.y))

    def reset(self):
        """
        :desc: Reset score to 0
        :return: None
        """
        self.score = 0
