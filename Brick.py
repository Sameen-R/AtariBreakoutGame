import pygame

class Brick(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, color):
        self.screen = screen
        self.x = x
        self.y = y

        self.r, self.g, self.b = color

        self.color = color

        self.rect = pygame.Rect(x, y, 100, 50)

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
