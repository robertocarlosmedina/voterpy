import pygame
from support.client import Client
from support.inputBoxs import drawInputBoxs, verifyInput
from support.buttons import verticalButtonsDisplay
from support.color import Color
import math


# Class data will facilitade the iteration whit the program and the server's data'bases
class ObjectRepresentation:
    client = Client()

    def __init__(self, screen, screen_size):
        self.screen, self.screen_size = screen, screen_size
        self.surface = pygame.Surface((400,315))
        self.surface.fill(Color.grey1.value)

        # Atributes to the method newCandidateRegistration
        self.inputBoxs = {"First Name":["", False],"Last Name":["",False],"Age":["",False],"Color":["",False]}
        self.registerButton = ["Register"]
        self.countButton = ["Count votes"]
        self.counted = False
        self.voteCounted = False
        self.active = ''

        self.connectionSent = False
        self.error = self.success = False
        self.votersCountMatrix = [] # the result value of poll
        self.totalVoters = 0
        self.totalCandidates = 0
        self.maximo = 0
        self.pixel = 0

        # Method relative to the class
        self.events = None
        self.mouse_pos = None
        self.response = []
        self.count = 0
        self.page = 0
        self.delay = 0 # to an delay while pressing the button

    # Method that will allow to make a new candidate register
    def newCandidateRegistration(self,events, mouse_pos, refresh):
        self.events, self.mouse_pos = events, mouse_pos
        # Draw all the input box's 
        self.inputBoxs = drawInputBoxs(self.screen, self.inputBoxs,36, self.events,self.mouse_pos,150,40,(380,40),60)
        # Called Method that draw the button on the screen
        self.active = verticalButtonsDisplay(self.screen, self.registerButton,410,(80, 423),(300, 50), self.mouse_pos,self.active,\
             pygame.font.SysFont("arial", 25))
        
        if self.active == "Register":
            if verifyInput(self.inputBoxs):
                self.connectionSent = self.sendToServer(f"candidates/post firstName={self.inputBoxs['First Name'][0]},lastName={self.inputBoxs['Last Name'][0]},\
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

    # Method that will show all the poll candidate on the screen
    def viewCandidatesOnRegister(self,events, mouse_pos, refresh=None):
        self.events, self.mouse_pos = events, mouse_pos
        # to get connect whit server just one time 
        if refresh:
            self.connectionSent = self.sendToServer("candidates/get")
            self.active = False
        y, x =145,70
        count = 0
        if self.connectionSent:
            for element in self.response: # this will display the candidates on the screen according to the list
                y1,x1=y,x
                pygame.draw.rect(self.screen, Color.green.value, pygame.Rect(x1, y1, 100, 100))
                pygame.draw.rect(self.screen, Color.grey1.value, pygame.Rect(x1, y1, 100, 100),2)
                # pygame.draw.rect(self.screen, Color.white.value, pygame.Rect(x1+2, y1+2, 98, 98),2)
                
                for key, value in element.items():
                    if key != "id" and key != "color" and key != "voterCounts":
                        if key == "age":
                            text_surface = pygame.font.SysFont("arial", 13).render(str(value)+" years old", True, Color.black1.value)
                            size = pygame.font.Font.size(pygame.font.SysFont("arial", 13), str(value)+" years old")
                        else:
                            text_surface = pygame.font.SysFont("arial", 13).render(str(value), True, Color.black1.value)
                            size = pygame.font.Font.size(pygame.font.SysFont("arial", 13), str(value))
                        self.screen.blit(text_surface, (x1+100/2-size[0]/2,y1+25))
                        y1 +=20
                count +=1
                if count == 3: # check if is time to jump to new line and draw more candidates painel
                    y += 110
                    x = 70
                    count = 0
                else:
                    x += 110
        return "Candidates"

    # Method that will display all the voters that participate on the screen
    def viewVotersOnRegister(self,events, mouse_pos, refresh):
        self.events, self.mouse_pos = events, mouse_pos
        # to get connect whit server just one time 
        if refresh:
            self.connectionSent = self.sendToServer("voters/get")
        y, x =25,70
        count = 0
        votersDisplayed = 0
        if self.connectionSent:
            for element in self.response: # this will display the candidates on the screen according to the list
                y1,x1=y,x
                # click = pygame.mouse.get_pressed(3)
                # This is to control the pagination of the data
                pagecontrol = math.floor(count/6)

                if pagecontrol < 0: # to turn the value a positive one
                    pagecontrol = 0

                if pagecontrol==self.page:
                    # drawing the checkbox and the box display of the candidats
                    pygame.draw.rect(self.surface, Color.green.value, pygame.Rect(self.screen_size[0]/2-325, y1, 350, 40))
                    pygame.draw.rect(self.surface, Color.grey2.value, pygame.Rect(self.screen_size[0]/2-325, y1, 350, 40),2)
                    for key, value in element.items(): # Drawing the candidates names on the boxes
                        if key != "id" and key != "pollCode" and key != "codeId":
                            if key == "firstName" or key == "lastName":
                                text_surface = pygame.font.SysFont("arial", 15).render(str(value).capitalize(), True, Color.black1.value)
                                size = pygame.font.Font.size(pygame.font.SysFont("arial", 15), str(value).capitalize())
                                self.surface.blit(text_surface, (x1+150/2-100,y1+size[1]))

                            else:
                                text_surface = pygame.font.SysFont("arial", 15).render("State: "+str(value).capitalize(), True, Color.black1.value)
                                size = pygame.font.Font.size(pygame.font.SysFont("arial", 15), "State: "+str(value).capitalize())
                                self.surface.blit(text_surface, (x+150/2+120,y1+size[1]))
                            x1 +=10+size[0]
                    y += 45     
                    votersDisplayed +=1
                if votersDisplayed > 5:
                    break
                count +=1 
        self.screen.blit(self.surface,(self.screen_size[1]/2-210, 145))
        self.drawArrows() # Method that will draw the arrows
        return "Voters"

    # Method that will draw the arrow button on the screen
    def drawArrows(self):
        # ______ Top and bottom navegate button (arrow) display ___
        slideArrows = [((220, 155), (240, 135), (260, 155)), ((220, 450), (240, 470), (260, 450))]
        count = 0
        for arrow in slideArrows:
            if (self.mouse_pos[0]in range(arrow[0][0], arrow[2][0]) and (self.mouse_pos[1]in range(arrow[0][1], arrow[1][1])or\
                self.mouse_pos[1]in range(arrow[1][1], arrow[0][1]))): # checking if mouse is over them to draw them whit defferent color
                # checking if the mouse is pressed to change the slide page
                if pygame.mouse.get_pressed()[0]:
                    pygame.draw.polygon(self.screen, Color.grey1.value, arrow)
                    pygame.draw.polygon(self.screen, Color.black.value, arrow, 3)
                    if count == 0 and self.page > 0 and self.delay > 30: # check if it is not in the first page to decrement the page
                        self.page -= 1
                        self.delay = 0;
                    # check if it is not in the last page to increment the page
                    elif count == 1 and self.page <= math.floor(len(self.response)-1/6) and self.delay>30:
                        self.page += 1
                        self.delay =0
                    delay = False
                else:
                    pygame.draw.polygon(self.screen, Color.green1.value, arrow)
                    pygame.draw.polygon(self.screen, Color.black.value, arrow, 3)
            else:
                pygame.draw.polygon(self.screen, Color.grey3.value, arrow)
                pygame.draw.polygon(self.screen, Color.white.value, arrow, 3)
            count += 1
        self.delay +=1

    # Method that will draw a graphic
    def drawGraph(self):
        x, y = 50, 150
        x1, y1 = 432, 425

        pygame.draw.line(self.screen, Color.grey.value, (x, y), (x, y1), 3)
        pygame.draw.line(self.screen, Color.grey.value, (x, y1), (x1, y1), 3)

    # Method that will determinate the result of the poll and store them in an array
    def determineVotersMatrixResulte(self):
        self.votersCountMatrix = []
        for candidate in self.response:
            percentage = 100*int(candidate["voterCounts"])/self.totalVoters # Is the percentage of votes that this candidate have
            pixels = 250*percentage/100 # The number of pixel that will be use in the screen
            if pixels > self.maximo:
                self.maximo = pixels
            self.votersCountMatrix.append((candidate["firstName"]+" "+candidate["lastName"],percentage, \
                                            int(candidate["voterCounts"]) ,pixels)) # adding them to the array

    # Method that will show the result of the poll
    def countVotes(self,events, mouse_pos, refresh):
        self.events, self.mouse_pos = events, mouse_pos
        # to get connect whit server just one time and get all the data
        if refresh:
            aux = self.sendToServer("voters/get") # just to count all the vouters
            self.totalVoters = len(self.response)
            del aux # cause we do not need it anymore
            self.connectionSent = self.sendToServer("candidates/get")
            self.totalCandidates = len(self.response)
            self.determineVotersMatrixResulte() # to determinathe the result percentage and the number of pixel that wil be used in the screen
            self.active = ''
            self.pixel = 0

        # Called Method that draw the button on the screen
        if self.counted and self.connectionSent: # Do this just if the button count is press
            y = 370
            if not self.voteCounted: # If the voted were not counted yet
                while True: # this is to make the effect of the voted been counted
                    y = 370
                    for result in self.votersCountMatrix:
                        if self.pixel > result[3]: # to not overpass the real result
                            pygame.draw.rect(self.screen, Color.green.value, pygame.Rect(52, y, result[3], 40))
                        else:
                            pygame.draw.rect(self.screen, Color.green.value, pygame.Rect(52, y, self.pixel, 40))
                        y -= 50
                    if self.delay > 20: # delay to the effect
                        self.pixel +=1
                        self.delay = 0
                    else:
                        self.delay += 1
                    self.drawGraph()# draw the graph lines.
                    if self.pixel > self.maximo:
                        self.voteCounted = not self.voteCounted
                        break

                    pygame.display.update() # to update the screen pixels
            else: # if the votes were already count there is no need to counte them again
                for result in self.votersCountMatrix: 
                    pygame.draw.rect(self.screen, Color.green.value, pygame.Rect(52, y, result[3], 40))
                    text_surface = pygame.font.SysFont("arial", 12).render(result[0]+" - "+str(format(result[1], ' .2f'))+"%", True, Color.white.value)
                    size = pygame.font.Font.size(pygame.font.SysFont("arial", 15), result[0]+" - "+str(format(result[1], ' .2f'))+"%")
                    self.screen.blit(text_surface, (62+result[3],y+size[1]))
                    y -= 50
            self.drawGraph()# draw the graph lines.   
        else:
            self.active = ''
            self.active = verticalButtonsDisplay(self.screen, self.countButton,250,(145, 263),(180, 50), self.mouse_pos,self.active,\
             pygame.font.SysFont("arial", 25)) # the button register on the screen
            if self.active != '':
                self.counted = not self.counted
        
        return "Count Votes"

    # Method that will show the poll info
    def pollInfo(self,events, mouse_pos, refresh):
        x, y = 85, 170
        x1, y1 = 372, 425
        sizeXcolum = []
        texts = ["Select 'Count Votes', to count the votes", "and them select this option to see"," the poll information."]
        # colunas = pygame.draw.line(self.screen, Color.grey.value, (x, y1), (x1, y1), 3)
        hdColunas = ["Candidate","Percentage", "Votes won"]
        if self.counted: # just if votes had been already counted
            # to get connect whit server just one time 
            if refresh:
                self.connectionSent = self.sendToServer("candidates/get")
                self.determineVotersMatrixResulte()
            y1 = 170+(self.totalCandidates+1)*50

            for coluna in hdColunas: # draw all the colums of the table
                pygame.draw.line(self.screen, Color.grey.value, (x, y), (x, y1), 3)
                text_surface = pygame.font.SysFont("arial", 18).render(coluna, True, Color.white.value)
                size = pygame.font.Font.size(pygame.font.SysFont("arial", 18), coluna)
                self.screen.blit(text_surface, (x+5,y+size[1]))
                sizeXcolum.append(x + 5)
                x += size[0]+10
            pygame.draw.line(self.screen, Color.grey.value, (x, y), (x, y1), 3)
            x = 85
            pygame.draw.line(self.screen, Color.grey.value, (x, y), (x1, y), 3)
            for linha in self.votersCountMatrix:# draw all the lines of the table
                y+=50
                i = 0
                for elm in linha:
                    if i <= 2:
                        if type(elm) == float:
                            pygame.draw.line(self.screen, Color.grey.value, (x, y), (x1, y), 3)
                            text_surface = pygame.font.SysFont("arial", 12).render(str(format(elm, ' .2f')), True, Color.white.value)
                            size = pygame.font.Font.size(pygame.font.SysFont("arial", 12), str(format(elm, ' .2f')))

                        else:
                            pygame.draw.line(self.screen, Color.grey.value, (x, y), (x1, y), 3)
                            text_surface = pygame.font.SysFont("arial", 13).render(str(elm), True, Color.white.value)
                            size = pygame.font.Font.size(pygame.font.SysFont("arial", 13), str(elm))
                        self.screen.blit(text_surface, (sizeXcolum[i],y+size[1]+5))
                        # x += size[0]+10
                    i+=1
                x = 85
                pygame.draw.line(self.screen, Color.grey.value, (x, y1), (x1, y1), 3)
            x, y = 85, 170
            pygame.draw.line(self.screen, Color.grey.value, (x, y), (x1, y), 3)
        else:
            y = 250
            for text in texts:
                text_surface = pygame.font.SysFont("arial", 18).render(text, True, Color.red2.value)
                size = pygame.font.Font.size(pygame.font.SysFont("arial", 18), text)
                self.screen.blit(text_surface, (self.screen_size[0]/2-size[0]/2-110,y))
                y += 30

        return "Poll Info"

    # Method that will send the message to the server
    def sendToServer(self, message):
        try:
            self.response = self.client.connectingToServer(message)
            return True
        except:
            return False
