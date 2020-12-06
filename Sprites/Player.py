import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, screen, screen_w, screen_h):
        self.screen = screen
        self.screen_w = screen_w
        self.screen_h = screen_h

        self.w = 400
        self.h = 20
        self.x = (screen_w - self.w) / 2
        self.y = screen_h - self.h
        self.color = (255, 255, 255)
        self.speed = 20
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)

    def update(self, x, y):
        self.x = x
        self.y = y
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

#############