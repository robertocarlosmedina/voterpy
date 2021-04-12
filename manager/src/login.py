from support.buttons import verticalButtonsDisplay
import pygame
from support.color import Color
from support.buttons import verticalButtonsDisplay
from support.inputBoxs import drawInputBoxs
from src.textInput import Textinput


class Login:
    pygame.init()

    def __init__(self, screen, screen_size):
        self.screen, self.screen_size = screen, screen_size
        self.font = pygame.font.SysFont("arial", 40)
        self.font1 = pygame.font.SysFont("arial", 12)
        self.surface = pygame.Surface((300,300))
        self.surface.fill(Color.grey3.value)
        self.components = ["Login"]
        self.inputBoxs = {"Poll name.":["", False],"Password / Access code":["",False]}
        self.mouse_pos=None
        self.events=None
        self.active = ''
  
    
    def run(self, events):
        self.mouse_pos = pygame.mouse.get_pos()
        self.events = events

        size = pygame.font.Font.size(self.font, 'Voterpy')
        line = self.font.render('Voterpy', True, Color.white3.value)
        self.screen.blit(line, (self.screen_size[0]/2-size[0]/2, 30))

        size = pygame.font.Font.size(self.font1, 'Manager-App')
        line = self.font1.render('Manager-App', True, Color.white.value)
        self.screen.blit(line, (self.screen_size[0]/2-size[0]/2, 70))

        # bliting the box input surface
        self.screen.blit(self.surface,(self.screen_size[0]/2-150,110))

        # calling the method to add the boxs
        self.inputBoxs = drawInputBoxs(self.screen,self.inputBoxs,20,self.events,self.mouse_pos,170,int(self.screen_size[0]/2-125)\
                                            ,(250, 40), 80)
        
        # Called Method that draw the button on the screen
        self.active = verticalButtonsDisplay(self.screen, self.components,330,(225, 337),(250, 40), self.mouse_pos,self.active,\
             pygame.font.SysFont("arial", 25))
        return "login"

    def verifyInput(self):
        pass
    
    def sendToServer(self):
        pass      
        