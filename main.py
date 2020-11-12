import pygame
from Button import Button
from Sprites.Player import Player
from Sprites.Ball import Ball
from Sprites.Brick import Brick

pygame.init()

screen_w = 1200
screen_h = 800
screen = pygame.display.set_mode((screen_w, screen_h))

clock = pygame.time.Clock()

homeButton = Button(screen, 1100, 0, 100, 50, "Home", 25, (100,100,100), (0,0,0))

def opening_screen():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill((0,0,0))

        txt_font = pygame.font.SysFont(None, 150)
        txt_img = txt_font.render("Atari Breakout", True, (255,255,255))
        txt_rect = txt_img.get_rect()
        txt_rect.center = (screen_w/2, screen_h/4)

        small_font = pygame.font.SysFont(None, 50)
        small_img = small_font.render("Press the space button to play", True, (255, 255, 0))
        small_rect = small_img.get_rect()
        small_rect.center = (screen_w / 2, screen_h / 2)

        screen.blit(txt_img, txt_rect)
        screen.blit(small_img, small_rect)

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_SPACE]:
            game()

        pygame.display.update()
        clock.tick(100)

def game_over_screen():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill((0,0,0))

        txt_font = pygame.font.SysFont(None, 200)
        txt_img = txt_font.render("GAME OVER", True, (255,0,0))
        txt_rect = txt_img.get_rect()
        txt_rect.center = (screen_w/2, screen_h/4)

        small_font = pygame.font.SysFont(None, 50)
        small_img = small_font.render("Press the space button to play again", True, (0, 255, 0))
        small_rect = small_img.get_rect()
        small_rect.center = (screen_w / 2, screen_h / 2)

        screen.blit(txt_img, txt_rect)
        screen.blit(small_img, small_rect)

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_SPACE]:
            game()

        pygame.display.update()
        clock.tick(100)

def game():
    player = Player(screen, 1200, 800)
    ball = Ball(screen, 1200,800)
    bricks = []
    for x in range(0, 11):
        for y in range(0, 8):
            bricks.append(Brick(screen, 100*x, 50*y, (255,0,0)))


    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()

        #updating player's position
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_RIGHT] and player.x<screen_w-player.w:
            player.x+=player.speed
        if pressed[pygame.K_LEFT] and player.x>0:
            player.x-=player.speed
        player.update(player.x, player.y)

        if ball.x<=0 or ball.x>=screen_w-ball.w: #changed here
            ball.xspeed*=-1
            ball.x+=ball.xspeed
        if ball.y<=0:
            ball.yspeed*=-1
        if ball.y+ball.h>=screen_h:
            game_over_screen()

        if pygame.sprite.collide_rect(ball, player):
            collision_rect = ball.rect.clip(player.rect)
            if collision_rect.width > collision_rect.height:
                ball.yspeed*=-1
            if ball.x >= player.x + player.w / 2:
                ball.xspeed = 0.1 * (ball.x - (player.x + player.w / 2))
            else:
                ball.xspeed = 0.1 * (ball.x + ball.w - (player.x + player.w / 2))
        ball.update()

        #updating mouse events
        mouse_pos = pygame.mouse.get_pos()
        clicked = pygame.mouse.get_pressed()

        if homeButton.x<mouse_pos[0]<homeButton.x+homeButton.width and homeButton.y<mouse_pos[1]<homeButton.y+homeButton.height:
            if clicked[0]==1:
                opening_screen()


        for brick in bricks.copy():
            if pygame.sprite.collide_rect(ball, brick):
                collision_rect = ball.rect.clip(brick.rect)
                if collision_rect.width > collision_rect.height:
                    ball.yspeed*=-1
                else:
                    ball.xspeed*=-1
                bricks.remove(brick)

        screen.fill((0,0,0))
        ball.draw()
        for brick in bricks:
            brick.draw()
        player.draw()
        homeButton.draw()

        pygame.display.update()
        clock.tick(100)

opening_screen()
