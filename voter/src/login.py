import pygame
from support.color import Color
from support.client import Client
from support.inputBoxs import drawInputBoxs, verifyInput
from support.buttons import verticalButtonsDisplay


class Login:
    pygame.init()
    client = Client()
    def __init__(self, screen, screen_size):
        self.screen, self.screen_size = screen, screen_size
        self.font = pygame.font.SysFont("arial", 40)
        self.font1 = pygame.font.SysFont("arial", 12)
        self.surface = pygame.Surface((330,390))
        self.surface.fill(Color.grey3.value)
        self.inputBoxs = {"First name.":["", False],"Last name.":["", False],"Poll code.":["",False],"Your code/Id.":["",False]}
        self.components = ["Registe"]
        self.active = ''
        self.error = False
        self.connectionSent = False
        self.count = 0
        self.mouse_pos = None
        self.events = None
        self.id = None # the id of the person that is making login
    
    def run(self, events, id):
        self.id = id
        self.events = events
        self.mouse_pos = pygame.mouse.get_pos()
        # draw the tittle
        size = pygame.font.Font.size(self.font, 'Voterpy')
        line = self.font.render('Voterpy', True, Color.white3.value)
        self.screen.blit(line, (self.screen_size[0]/2-size[0]/2, 10))

        size = pygame.font.Font.size(self.font1, 'Voter App')
        line = self.font1.render('Voter App', True, Color.white.value)
        self.screen.blit(line, (self.screen_size[0]/2-size[0]/2, 50))

        # Draw the imput box's background
        self.screen.blit(self.surface,(self.screen_size[0]/2-165,90))
        # draw the input box 
        self.inputBoxs = drawInputBoxs(self.screen,self.inputBoxs,20,self.events,self.mouse_pos,130,\
                                        int(self.screen_size[0]/2-125),(250,40),70)
        # Called Method that draw the button on the screen
        self.active = verticalButtonsDisplay(self.screen, self.components,410,(225, 417),(250, 40), self.mouse_pos,self.active,\
                                                pygame.font.SysFont("arial", 25))
        # verify the input when submited
        if self.active == "Registe":
            if verifyInput(self.inputBoxs):
                if not self.checkIfUserAlreadyExist():
                    self.sendToServer()
                self.refreshInputsAndAtributes()
            self.active = ''
            if self.connectionSent:
                # request = "jsonFileName/get"
                request = self.client.connectingToServer("voters/get")
                self.id = request[len(request)-1]["id"]
                self.refreshInputsAndAtributes()
                self.connectionSent = False
                return "homePage", self.id
            else:
                self.messageNotSentError()

        # show to error message in a period of time
        if self.error:
            if self.count < 550:
                return self.messageNotSentError()
            else:
                self.error = False
                self.count = 0

        return "login", self.id

    # checkif the user already exist
    def checkIfUserAlreadyExist(self):
        isThis = False
        try:
            dados = self.client.connectingToServer("voters/get")
            for dado in dados:
                for key, value in dado.items():
                    # verify if this codeId is already user by an user
                    if(key == 'codeId' and int((self.inputBoxs["Your code/Id."][0])) == value):
                        return True
            return False                
        except:
            return False

    # Method that will check if the user loged in is already voted
    # def checkIfUserIsAlreadyVoted(self):
    #     isThis = False
    #     try:
    #         dados = self.client.connectingToServer("voters/get")
    #         for dado in dados:
    #             for key, value in dado.items():
    #                 # verify if this is user
    #                 if(key == 'codeId'and int((self.inputBoxs["Your code/Id."][0])) == value):
    #                     isThis = True
    #                 # verify if the user is voted
    #                 if(key == "voted" and isThis and value):
    #                     return True
    #         return False                
    #     except:
    #         return False

    # Method to show error
    def messageNotSentError(self):
        self.error = True
        text_surface = pygame.font.SysFont("arial", 12).render("Error while making login or code/Id already exist.", True, Color.red1.value)
        size = pygame.font.Font.size(pygame.font.SysFont("arial", 12), "Error while making login or code/Id already exist.")
        self.screen.blit(text_surface, (self.screen_size[0]/2-size[0]/2,390))
        self.count += 1
        return "login", self.id
    
    # Method that refresh all the variable
    def refreshInputsAndAtributes(self):
        self.active = ''
        for key in self.inputBoxs.keys():
            self.inputBoxs[key][0] = ""
            self.inputBoxs[key][1] = False
        

    # Method that connect and send the message to the server
    def sendToServer(self):
        try:
            self.client.connectingToServer(f'voters/post firstName={self.inputBoxs["First name."][0]},\
lastName={self.inputBoxs["Last name."][0]},pollCode={self.inputBoxs["Poll code."][0]},codeId={self.inputBoxs["Your code/Id."][0]},\
voted=False')
            self.connectionSent = True
        except:
            self.connectionSent =  False        
        