import pygame
from support.color import Color
from support.buttons import verticalButtonsDisplay

class Voted():
    def __init__(self, screen, screen_size):
        self.screen, self.screen_size = screen, screen_size
        self.font = pygame.font.SysFont("arial", 50)
        self.font1 = pygame.font.SysFont("arial", 12)
        self.font2 = pygame.font.SysFont("arial", 24)
        self.button = ["Finish"]
        self.active = ""
        self.events = None
        self.mouse_pos = None
        self.id = None
        self.delay = self.highCircle  = 0

    def run(self, events, id):
        self.id = id
        self.events = events
        self.mouse_pos = pygame.mouse.get_pos()
        # draw the tittle
        size = pygame.font.Font.size(self.font, 'Voterpy')
        line = self.font.render('Voterpy', True, Color.white3.value)
        self.screen.blit(line, (self.screen_size[0]/2-size[0]/2, 130))
        # draw the sub tittle
        size = pygame.font.Font.size(self.font1, 'Voter App')
        line = self.font1.render('Voter App', True, Color.white.value)
        self.screen.blit(line, (self.screen_size[0]/2-size[0]/2, 175))

        # draw the text
        size = pygame.font.Font.size(self.font2, 'Your vote was successfully registered.')
        line = self.font2.render('Your vote was successfully registered.', True, Color.white.value)
        self.screen.blit(line, (self.screen_size[0]/2-size[0]/2, 230))
        # Drawing the animation
        self.animation()
        # Called Method that draw the button on the screen
        self.active = verticalButtonsDisplay(self.screen, self.button,300,(int(self.screen_size[0]/2-100), 317),(200, 60), self.mouse_pos,self.active,\
                                                pygame.font.SysFont("arial", 25))
        if self.active == "Finish" and self.id == None:
            self.active = ""
            return "login", self.id

        # Turning the id to None
        self.id = None

        return "voted", self.id
    
    def animation(self):
        pos_x, pos_y = int(self.screen_size[0]/2), int(self.screen_size[1]/2)-40
        for i in range(0, 7):
            if i == self.highCircle:
                pygame.draw.circle(self.screen, Color.grey1.value, (pos_x-60, pos_y), 6)
            elif i == self.highCircle + 1:
                pygame.draw.circle(self.screen, Color.green1.value, (pos_x-60, pos_y), 3)
            elif i == self.highCircle - 1:
                pygame.draw.circle(self.screen, Color.green1.value, (pos_x-60, pos_y), 3)
            else:
                pygame.draw.circle(self.screen, Color.green2.value, (pos_x-60, pos_y), 2)
            pos_x +=20

        # Controling the delay to change the higher circle
        if self.delay >= 100:
            self.highCircle += 1
            self.delay = 0
        self.delay += 1

        # COntroling the if the higher  circle is in the end to return it to the start
        if self.highCircle > 7:
            self.highCircle = 0