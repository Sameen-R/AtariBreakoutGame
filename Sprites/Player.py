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

        self.score = 0
        self.high_score = self.get_high_score()

    def update(self, x, y):
        self.x = x
        self.y = y
        self.rect.x = self.x
        self.rect.y = self.y

    def get_high_score(self):
        '''
        This code opens the High_Score.txt file in read-only mode and gets the high score.

        Explanation of this line of code
        int(High_Score_file.readlines()[0].strip('\n'))

            -Strings are the only contents of a text file, so the string must be converted into a number: int()
            -The text_file.readlines() function gets all the lines of the text file in a list. Only the first line of the file contains the score.
            -The string.strip('\n') removes all occurences of the new line character from the string.
        '''
        with open('Sprites/High_Score.txt', 'r') as High_Score_file:
            high_score = int(High_Score_file.readlines()[0].strip('\n'))
        return high_score

    def update_high_score(self):
        '''
        The High_Score.txt file is opened in r+ mode (reading and writing enabled).
        If the self.high_score variable is larger than the high score recorded in the file, the new high score will be replace the old one.
        '''
        with open('Sprites/High_Score.txt', 'r+') as High_Score_file:
            recorded_high_score = int(High_Score_file.readlines()[0].strip('\n'))
            if self.high_score > recorded_high_score:
                '''
                High_Score_file.seek(0): Sets the cursor position to index 0 (the very beginning of the file)
                High_Score_file.truncate(): Clears everything after the cursor position. The cursor position is 0, so the entire file is cleared.
                High_Score_file.write(str(self.high_score)): Writes the high score in the text file. The argument of write() must be a string.
                '''
                High_Score_file.seek(0)
                High_Score_file.truncate()
                High_Score_file.write(str(self.high_score))


    def reset_high_score(self):
        with open('Sprites/High_Score.txt', 'r+') as High_Score_file:
            High_Score_file.seek(0)
            High_Score_file.truncate()
            High_Score_file.write('0')

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
