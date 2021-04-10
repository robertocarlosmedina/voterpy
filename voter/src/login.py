import pygame
from support.color import Color
from src.textInput import Textinput


class Login:
    pygame.init()
    textinput = Textinput()

    def __init__(self, screen, screen_size):
        self.screen, self.screen_size = screen, screen_size
        self.font = pygame.font.SysFont("arial", 40)
        self.font1 = pygame.font.SysFont("arial", 12)
        self.surface = pygame.Surface((300,300))
        self.surface.fill(Color.grey3.value)
        self.electionName = ''
        self.electionState = False
        self.password = ''        
    
    def run(self):
        size = pygame.font.Font.size(self.font, 'Voterpy')
        line = self.font.render('Voterpy', True, Color.white3.value)
        self.screen.blit(line, (self.screen_size[0]/2-size[0]/2, 30))

        size = pygame.font.Font.size(self.font1, 'Voter App')
        line = self.font1.render('Voter App', True, Color.white.value)
        self.screen.blit(line, (self.screen_size[0]/2-size[0]/2, 70))

        self.drawBoxLogin()
        return "login"

    def verifyInput(self):
        pass
    
    def sendToServer(self):
        pass
    
    def drawBoxLogin(self):
        self.screen.blit(self.surface,(self.screen_size[0]/2-150,110))
        self.electionName = self.textinput.getInputText(pygame.event.get(), self.screen,250,200, self.screen_size)
        self.password = self.textinput.getInputText(pygame.event.get(), self.screen,250, 260,self.screen_size)
        
        