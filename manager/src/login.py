from support.buttons import verticalButtonsDisplay
import pygame
from support.color import Color
from support.buttons import verticalButtonsDisplay
from support.inputBoxs import drawInputBoxs, verifyInput
from support.client import Client

# Class tha dispkay the login screen 
class Login:
    pygame.init()
    client = Client()

    def __init__(self, screen, screen_size):
        self.screen, self.screen_size = screen, screen_size
        self.font = pygame.font.SysFont("arial", 40)
        self.font1 = pygame.font.SysFont("arial", 12)
        self.surface = pygame.Surface((300,300))
        self.surface.fill(Color.grey3.value)
        self.components = ["Login"]
        self.inputBoxs = {"Poll name.":["", False],"Password / Access code.":["",False]}
        self.mouse_pos=None
        self.events=None
        self.connectionSent =self.error= False
        self.count = 0
        self.active = ''

  
    # Method that control this class
    def run(self, events):
        self.mouse_pos = pygame.mouse.get_pos()
        self.events = events
        
        # Bliting on the screen title name
        size = pygame.font.Font.size(self.font, 'Voterpy')
        line = self.font.render('Voterpy', True, Color.white3.value)
        self.screen.blit(line, (self.screen_size[0]/2-size[0]/2, 30))
        # Bliting on the screen app name
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
        
        # verify the input when submited
        if self.active == "Login":
            if verifyInput(self.inputBoxs):
                self.sendToServer()
                self.refreshInputsAndAtributes()
            self.active = ''

            return "homePage" if self.connectionSent else self.messageNotSentError()
        # show to error message in a period of time
        if self.error:
            if self.count < 350:
                return self.messageNotSentError()
            else:
                self.error = False
                self.count = 0

        return "login"
    
    # Method to show error
    def messageNotSentError(self):
        self.error = True
        text_surface = pygame.font.SysFont("arial", 12).render("Error while making login.", True, Color.red1.value)
        size = pygame.font.Font.size(pygame.font.SysFont("arial", 12), "Error while making login.")
        self.screen.blit(text_surface, (self.screen_size[0]/2-size[0]/2,300))
        self.count += 1
        return "login"

    # Method that refresh all the variable
    def refreshInputsAndAtributes(self):
        self.active = ''
        for key in self.inputBoxs.keys():
            self.inputBoxs[key][0] = ""
            self.inputBoxs[key][1] = False
    
    # Method that connect and send the message to the server
    def sendToServer(self):
        name = self.inputBoxs["Poll name."][0]
        passCode = self.inputBoxs["Password / Access code."][0]
        try:
            self.client.connectingToServer(f'managers/post name={name},passCode={passCode}') 
            self.connectionSent = True
        except:
            self.connectionSent =  False
        