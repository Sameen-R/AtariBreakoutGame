import pygame

class Button:
    def __init__(self, screen, x, y, width, height, text, text_size, button_color, text_color):
        self.screen=screen
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.text=text
        self.text_size=text_size
        self.button_color=button_color
        self.text_color=text_color
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self):
        pygame.draw.rect(self.screen, self.button_color, self.rect)

        txt_font = pygame.font.SysFont(None, self.text_size)
        txt_img = txt_font.render(self.text, True, self.text_color, self.button_color)
        txt_rect = txt_img.get_rect()
        txt_rect.center = self.rect.center

        self.screen.blit(txt_img, txt_rect)


