import pygame

class Ball(pygame.sprite.Sprite):
    def __init__(self, screen, screen_w, screen_h):
        self.screen = screen
        self.screen_w = screen_w
        self.screen_h = screen_h

        self.w = 50
        self.h = 50
        self.x = (self.screen_w - self.w) / 2
        self.y = self.screen_h - 100
        self.color = (0, 0, 255)
        self.xspeed = 0
        self.yspeed = 10
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)

    def update(self):
        self.x += self.xspeed
        self.y += self.yspeed
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (int(self.x+25), int(self.y+25)), 25)
