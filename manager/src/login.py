from support.buttons import verticalButtonsDisplay
import pygame
from support.color import Color
from support.buttons import verticalButtonsDisplay
from src.textInput import Textinput


class Login:
    pygame.init()
    textinput = Textinput()
    textinput1 = Textinput()

    def __init__(self, screen, screen_size):
        self.screen, self.screen_size = screen, screen_size
        self.font = pygame.font.SysFont("arial", 40)
        self.font1 = pygame.font.SysFont("arial", 12)
        self.surface = pygame.Surface((300,300))
        self.surface.fill(Color.grey3.value)
        self.components = ["Login"]
        self.inputBoxs = {1:False,2:False}
        self.mouse_pos=None
        self.active = ''
        self.electionName = ''
        self.electionState = False
        self.password = ''        
    
    def run(self):
        self.mouse_pos = pygame.mouse.get_pos()
        size = pygame.font.Font.size(self.font, 'Voterpy')
        line = self.font.render('Voterpy', True, Color.white3.value)
        self.screen.blit(line, (self.screen_size[0]/2-size[0]/2, 30))

        size = pygame.font.Font.size(self.font1, 'Manager-App')
        line = self.font1.render('Manager-App', True, Color.white.value)
        self.screen.blit(line, (self.screen_size[0]/2-size[0]/2, 70))

        self.drawBoxLogin()

        # Called Method that draw the button on the screen
        self.active = verticalButtonsDisplay(self.screen, self.components,330,(225, 337),(250, 40), self.mouse_pos,self.active,\
             pygame.font.SysFont("arial", 25))
        return "login"

    def verifyInput(self):
        pass
    
    def sendToServer(self):
        pass
    
    # Method that draw the input's box ont he screen 
    def drawBoxLogin(self):
        self.screen.blit(self.surface,(self.screen_size[0]/2-150,110))
        self.electionNams = self.textinput.getInputText(pygame.event.get(), self.screen,250,200, self.screen_size)
        self.password = self.textinput1.getInputText(pygame.event.get(), self.screen,250, 260,self.screen_size)

        # if self.mouse_pos[0] in range(self.screen_size[0]/2-125, self.screen_size[0]/2+125)\
            # and self.mouse_pos[1]in range(200,240):
        
        