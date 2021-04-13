import pygame
from support.color import Color
from support.buttons import verticalButtonsDisplay

# class that draw the home screen
class HomePage:
    def __init__(self, screen, screen_size):
        self.screen, self.screen_size = screen, screen_size
        self.font = pygame.font.SysFont("arial", 35)
        self.font1 = pygame.font.SysFont("arial", 11)
        self.font2 = pygame.font.SysFont("arial", 25)
        self.surface = pygame.Surface((200,350))
        self.surface.fill(Color.grey3.value)
        self.buttons = {"Register":1,"Candidates":2,"Voters":3,"Count Votes":1,\
                        "Poll Info":20,}
        self.active = 'Register'
        self.mouse_pos = None

    # Method the control this class
    def run(self, events):
        self.mouse_pos = pygame.mouse.get_pos()

        # Bliting on the screen title name
        size = pygame.font.Font.size(self.font, 'Voterpy')
        line = self.font.render('Voterpy', True, Color.white3.value)
        self.screen.blit(line, (self.screen_size[0]/2+225-size[0]/2, 30))
        # Bliting on the screen app name
        size = pygame.font.Font.size(self.font1, 'Manager-App')
        line = self.font1.render('Manager-App', True, Color.white.value)
        self.screen.blit(line, (self.screen_size[0]/2+225-size[0]/2, 70))
        # Bliting the surface
        self.screen.blit(self.surface,(self.screen_size[0]/2+280-150,110))

        # Calling method that draw the screen content according to the buttons
        self.drawbuttonContent()

        # Drwing buttons on the screen
        self.active = verticalButtonsDisplay(self.screen, self.buttons.keys(),170,(481, 177),(198, 40), self.mouse_pos,self.active,\
             pygame.font.SysFont("arial", 20))
        return "homePage"
    
    def drawbuttonContent(self):
        for key,value in self.buttons.items():
            if key == self.active:
                size = pygame.font.Font.size(self.font2, key)
                line = self.font2.render(key, True, Color.white.value)
                self.screen.blit(line, (self.screen_size[0]/2-240-size[0]/2, 80))
                pygame.draw.line(self.screen, Color.grey1.value, (40, 110),(420, 110), 2)