import pygame
from support.color import Color

# class that control the initial painel 
class Start:
    pygame.init()
    def __init__(self, screen, screen_size):
        self.font = pygame.font.SysFont("arial", 50)
        self.font1 = pygame.font.SysFont("arial", 12)
        self.screen = screen
        self.screen_size = screen_size
        self.delay = self.highCircle  = self.count = 0

    # Method that control this class
    def run(self):
        size = pygame.font.Font.size(self.font, 'Voterpy')
        line = self.font.render('Voterpy', True, Color.white3.value)
        self.screen.blit(line, (self.screen_size[0]/2-size[0]/2, (self.screen_size[1]/2-size[1]/2)-40))

        size = pygame.font.Font.size(self.font1, 'Voter App')
        line = self.font1.render('Voter App', True, Color.white.value)
        self.screen.blit(line, (self.screen_size[0]/2-size[0]/2, (self.screen_size[1]/2-size[1]/2)-10))
        
        self.animation()
        if self.count >= 6:    
            return "login"
        return "start"

    # Method that control the circle animation display and the time 
    def animation(self):
        pos_x, pos_y = int(self.screen_size[0]/2), int(self.screen_size[1]/2)+20
        for i in range(0, 7):
            if i == self.highCircle:
                pygame.draw.circle(self.screen, Color.green1.value, (pos_x-60, pos_y), 6)
            elif i == self.highCircle + 1:
                pygame.draw.circle(self.screen, Color.green1.value, (pos_x-60, pos_y), 3)
            elif i == self.highCircle - 1:
                pygame.draw.circle(self.screen, Color.green1.value, (pos_x-60, pos_y), 3)
            else:
                pygame.draw.circle(self.screen, Color.green2.value, (pos_x-60, pos_y), 2)
            pos_x +=20

        if self.delay >= 100:
            self.highCircle += 1
            self.delay = 0
        self.delay += 1

        if self.highCircle > 7:
            self.highCircle = 0
            self.count += 1
