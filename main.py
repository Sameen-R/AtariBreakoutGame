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
player = Player(screen, 1200, 800)


def opening_screen():
    global player
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                player.reset_high_score()
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
    global player
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                player.reset_high_score()
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
    #creating objects
    global player
    player = Player(screen, 1200, 800)
    ball = Ball(screen, 1200,800)
    bricks = []

    #inserting bricks
    for x in range(0, 11):
        for y in range(0, 8):
            bricks.append(Brick(screen, 100*x, 50*y, (255,0,0)))


    while True:

        #checking if the user wants to quit
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                player.reset_high_score()
                pygame.quit()
                quit()

        #updating player's position
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_RIGHT] and player.x<screen_w-player.w:
            player.x+=player.speed
        if pressed[pygame.K_LEFT] and player.x>0:
            player.x-=player.speed
        player.update(player.x, player.y) #updates the player's rectangle position

        #ball's collision with the edges of the screen
        if ball.x<=0 or ball.x>=screen_w-ball.w:
            ball.xspeed*=-1
            ball.x+=ball.xspeed
        if ball.y<=0:
            ball.yspeed*=-1
        if ball.y+ball.h>=screen_h:
            player.score = 0
            game_over_screen()

        #ball's collision with the player (deflecting left or right)
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

        #ball's collisions with the bricks
        for brick in bricks.copy():
            if pygame.sprite.collide_rect(ball, brick):
                collision_rect = ball.rect.clip(brick.rect)
                if collision_rect.width > collision_rect.height:
                    ball.yspeed*=-1
                else:
                    ball.xspeed*=-1
                bricks.remove(brick)
                player.score += 10
                if player.score>player.high_score:
                    player.high_score = player.score
                    player.update_high_score()

        #drawing all te sprites and updating the game
        screen.fill((0,0,0))
        ball.draw()
        for brick in bricks:
            brick.draw()
        player.draw()
        homeButton.draw()

        #drawing the high score text
        high_score_txt = pygame.font.SysFont(None, 25)
        high_score_img = high_score_txt.render("High Score: " + str(player.high_score), True, (255, 255, 255))
        high_score_rect = high_score_img.get_rect()
        high_score_rect.x = 10
        high_score_rect.y = 10
        screen.blit(high_score_img, high_score_rect)

        #drawing the current score text
        score_txt = pygame.font.SysFont(None, 25)
        score_img = score_txt.render("Score: "+str(player.score), True, (255,255,255))
        score_rect = score_img.get_rect()
        score_rect.x = 10
        score_rect.y = 30
        screen.blit(score_img, score_rect)

        pygame.display.update()
        clock.tick(100)

opening_screen()
