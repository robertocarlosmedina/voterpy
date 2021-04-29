import pygame
from support.color import Color
from src.homeComponnents import ObjectRepresentation
from support.buttons import verticalButtonsDisplay


# class that draw the home screen
class HomePage:

    def __init__(self, screen, screen_size):
        self.screen, self.screen_size = screen, screen_size
        self.objt = ObjectRepresentation(screen, screen_size)
        self.font = pygame.font.SysFont("arial", 35)
        self.font1 = pygame.font.SysFont("arial", 11)
        self.font2 = pygame.font.SysFont("arial", 25)
        self.surface = pygame.Surface((230,350))
        self.surface.fill(Color.grey3.value)
        self.buttons = {"Register":self.objt.newCandidateRegistration,"Candidates":self.objt.viewCandidatesOnRegister,\
                        "Voters":self.objt.viewVotersOnRegister,"Count Votes":self.objt.countVotes,"Poll Info":self.objt.pollInfo}
        self.active = ''
        self.mouse_pos = None
        self.events = None
        self.controlActive =""

    # Method the control this class
    def run(self, events):
        self.events = events
        self.mouse_pos = pygame.mouse.get_pos()

        # Bliting on the screen title name
        size = pygame.font.Font.size(self.font, 'Voterpy')
        line = self.font.render('Voterpy', True, Color.white3.value)
        self.screen.blit(line, (self.screen_size[0]/2+225-size[0]/2, 30))
        # Bliting on the screen app name
        size = pygame.font.Font.size(self.font1, 'Manager-App')
        line = self.font1.render('Manager-App', True, Color.white.value)
        self.screen.blit(line, (self.screen_size[0]/2+225-size[0]/2, 70))
        # Bliting the surface and the line
        self.screen.blit(self.surface,(self.screen_size[0]/2+280-165,110))
        pygame.draw.rect(self.screen, Color.white.value, pygame.Rect(self.screen_size[0]/2+280-165,110,230, 350), 2)
        pygame.draw.line(self.screen, Color.white3.value, (40, 110),(420, 110), 2)

        # Calling method that draw the screen content according to the buttons
        self.drawbuttonContent()

        # Drwing buttons on the screen
        self.active = verticalButtonsDisplay(self.screen, self.buttons.keys(),170,(481, 180),(198, 40), self.mouse_pos,self.active,\
             pygame.font.SysFont("arial", 20))
        
        return "homePage"
    
    def drawbuttonContent(self):
        # If there is no active function the display on the top function will be manager app
        if self.active == "":
            size = pygame.font.Font.size(self.font2, "Manager App")
            line = self.font2.render("Manager App", True, Color.white.value)
            self.screen.blit(line, (self.screen_size[0]/2-230-size[0]/2, 80))

        # checking the key on the dict that is active and run the method tha is related to it 
        for key,value in self.buttons.items():
            if key == self.active:
                size = pygame.font.Font.size(self.font2, key)
                line = self.font2.render(key, True, Color.white.value)
                self.screen.blit(line, (self.screen_size[0]/2-230-size[0]/2, 80))
                if key == self.controlActive:
                    self.active=value(self.events, self.mouse_pos, False)
                else:
                    self.active=value(self.events, self.mouse_pos, True)
                    self.controlActive = key
                  