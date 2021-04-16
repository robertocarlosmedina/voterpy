import pygame
from support.client import Client
from support.inputBoxs import drawInputBoxs, verifyInput
from support.buttons import verticalButtonsDisplay
from support.color import Color


# Class data will facilitade the iteration whit the program and the server's data'bases
class ObjectRepresentation:
    client = Client()

    def __init__(self, screen, screen_size):
        self.screen, self.screen_size = screen, screen_size

        # Atributes to the method newCandidateRegistration
        self.inputBoxs = {"First Name":["", False],"Lat Name":["",False],"Age":["",False],"Color":["",False]}
        self.registerButton = ["Register"]
        self.active = ''
        
        self.connectionSent = False
        self.error = self.success = False

        # Method relative to the class
        self.events = None
        self.mouse_pos = None
        self.response = None
        self.count = 0

    def newCandidateRegistration(self,events, mouse_pos):
        self.events, self.mouse_pos = events, mouse_pos
        # Draw all the input box's 
        self.inputBoxs = drawInputBoxs(self.screen, self.inputBoxs,36, self.events,self.mouse_pos,150,40,(380,40),60)
        # Called Method that draw the button on the screen
        self.active = verticalButtonsDisplay(self.screen, self.registerButton,410,(80, 423),(300, 50), self.mouse_pos,self.active,\
             pygame.font.SysFont("arial", 25))
        
        if self.active == "Register":
            if verifyInput(self.inputBoxs):
                self.connectionSent = self.sendToServer(f"candidates/post firstName={self.inputBoxs['First Name'][0]},lastName={self.inputBoxs['Lat Name'][0]},\
age={self.inputBoxs['Age'][0]},color={self.inputBoxs['Color'][0]},voterCounts=0")
                self.connectionMessage()
                self.refreshInputsAndAtributes()
            self.active = ''          
        
        self.supportToBlitErrorAndSuccessMessage()
        if self.success:
            self.success = False
            return "Candidates"
        else:
            return "Register"

     # Method that support while controling the reponse success
    def supportToBlitErrorAndSuccessMessage(self):
        # if error sending message
        if self.error:
            if self.count < 350:
                self.connectionMessage()
                self.count += 1
            else:
                self.error = False
                self.count = 0
        # if success while sendig message
        if self.success:
            if self.count < 350:
                self.connectionMessage()
                self.count += 1
            else:
                self.success = False
                self.count = 0

    # Method that will display the reponse status
    def connectionMessage(self):
        if not self.connectionSent:
            self.error = True
            text_surface = pygame.font.SysFont("arial", 15).render("Error while making registe.", True, Color.red2.value)
            size = pygame.font.Font.size(pygame.font.SysFont("arial", 12), "Error while making reguste.")
            self.screen.blit(text_surface, (self.screen_size[0]/2-size[0]/2-130,385))

        else:
            self.success = True
            text_surface = pygame.font.SysFont("arial", 15).render("Registe donne perfectly.", True, Color.green.value)
            size = pygame.font.Font.size(pygame.font.SysFont("arial", 12), "Registe donne perfectly.")
            self.screen.blit(text_surface, (self.screen_size[0]/2-size[0]/2-130,385))

    # Method that will refresh all the atributes
    def refreshInputsAndAtributes(self):
        self.active = ""
        self.response = None
        for key in self.inputBoxs.keys():
            self.inputBoxs[key][0] = ""
            self.inputBoxs[key][1] = False

    def viewCandidatesOnRegister(self,events, mouse_pos):
        self.events, self.mouse_pos = events, mouse_pos
        # to get connect whit server just one time 
        if type(self.response) != list or len(self.response)==0 or self.response == None:
            self.connectionSent = self.sendToServer("candidates/get")
        y, x =145,70
        count = 0
        if self.connectionSent:
            for element in self.response: # this will display the candidates on the screen according to the list
                y1,x1=y,x
                pygame.draw.rect(self.screen, Color.green.value, pygame.Rect(x1, y1, 100, 100))
                pygame.draw.rect(self.screen, Color.white.value, pygame.Rect(x1, y1, 100, 100),2)
                # pygame.draw.rect(self.screen, Color.white.value, pygame.Rect(x1+2, y1+2, 98, 98),2)
                for key, value in element.items():
                    if key != "id" and key != "color" and key != "voterCounts":
                        text_surface = pygame.font.SysFont("arial", 12).render(str(value), True, Color.grey1.value)
                        size = pygame.font.Font.size(pygame.font.SysFont("arial", 12), str(value))
                        self.screen.blit(text_surface, (x1+100/2-size[0]/2,y1+10))
                        y1 +=20
                count +=1
                if count == 3: # check if is time to jump to new line and draw more candidates painel
                    y += 110
                    x = 70
                    count = 0
                else:
                    x += 110
        return "Candidates"

    def viewVotersOnRegister(self,events, mouse_pos):
        return "Voters"

    def countVotes(self,events, mouse_pos):
        return "Count Votes"

    def pollInfo(self,events, mouse_pos):
        return "Poll Info"

    # Method that will send the message to the server
    def sendToServer(self, message):
        try:
            self.response = self.client.connectingToServer(message)
            return True
        except:
            return False
        # if self.response!="None":
        #     self.connectionSent = bool(self.response)
        #     print(type(self.response))
