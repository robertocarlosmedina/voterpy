import pygame
from support.color import Color
from support.client import Client
from support.buttons import verticalButtonsDisplay

class HomePage:
    client  = Client()
    def __init__(self,screen, screen_size):
        self.screen, self.screen_size = screen, screen_size
        self.font = pygame.font.SysFont("arial", 40)
        self.font1 = pygame.font.SysFont("arial", 12)
        self.surface = pygame.Surface((500,280))
        self.surface.fill(Color.grey1.value)
        self.components = ["Vote"]
        self.active = ''
        self.events = None
        self.response = None
        self.mouse_pos = None
        
    def run(self,events):
        self.events = events
        self.mouse_pos = pygame.mouse.get_pos()
        # draw the tittle
        size = pygame.font.Font.size(self.font, 'Voterpy')
        line = self.font.render('Voterpy', True, Color.white3.value)
        self.screen.blit(line, (self.screen_size[0]/2-size[0]/2, 20))
        # draw the sub tittle
        size = pygame.font.Font.size(self.font1, 'Voter App')
        line = self.font1.render('Voter App', True, Color.white.value)
        self.screen.blit(line, (self.screen_size[0]/2-size[0]/2, 60))

        # Draw all the candidates on the screen
        self.viewCandidatesOnRegister()

        # Called Method that draw the button on the screen
        self.active = verticalButtonsDisplay(self.screen, self.components,400,(225, 417),(250, 60), self.mouse_pos,self.active,\
                                                pygame.font.SysFont("arial", 25))
        # Drawing the surface on the screen
        self.screen.blit(self.surface,(self.screen_size[0]/2-250, self.screen_size[1]/2-140))
        return "homePage"
    
    # Method that show all the candidates
    def viewCandidatesOnRegister(self):
        # to get connect whit server just one time 
        if type(self.response) != list or len(self.response)==0 or self.response == None:
            self.connectionSent = self.sendToServer("candidates/get")
        y, x =145,70
        count = 0
        if self.connectionSent:
            for element in self.response: # this will display the candidates on the screen according to the list
                y1,x1=y,x
                pygame.draw.rect(self.surface, Color.green.value, pygame.Rect(x1, y1, 100, 100))
                pygame.draw.rect(self.surface, Color.grey1.value, pygame.Rect(x1, y1, 100, 100),2)
                # pygame.draw.rect(self.screen, Color.white.value, pygame.Rect(x1+2, y1+2, 98, 98),2)
                for key, value in element.items():
                    if key != "id" and key != "color" and key != "voterCounts"and key != "age":
                        if key == "age":
                            text_surface = pygame.font.SysFont("arial", 13).render(str(value)+" years old", True, Color.black1.value)
                            size = pygame.font.Font.size(pygame.font.SysFont("arial", 13), str(value)+" years old")
                        else:
                            text_surface = pygame.font.SysFont("arial", 13).render(str(value), True, Color.black1.value)
                            size = pygame.font.Font.size(pygame.font.SysFont("arial", 13), str(value))
                        self.surface.blit(text_surface, (x1+100/2-size[0]/2,y1+25))
                        y1 +=20
                # count +=1
                # if count == 3: # check if is time to jump to new line and draw more candidates painel
                #     y += 110
                #     x = 70
                #     count = 0
                # else:
                x += 110

    def sendToServer(self, message):
        try:
            self.response = self.client.connectingToServer(message)
            return True
        except:
            return False