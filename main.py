import sys
import os
from threading import Thread
import pygame
from pygame.locals import *
from support.color import Color as cs
from support.buttons import verticalButtonsDisplay  


# Thread apps that will allow multiple apps to be executed
class Threads(Thread):
    def __init__(self, app):
        Thread.__init__(self)
        self.app = app
    
    def run(self):
         # Starting the thread according to the app name sent
        if self.app != "server":
            os.system(f"python3 {self.app}/main.py &")
        else:
            os.system(f"python3 {self.app}/main.py")


# class that will display an front interface that will allow the user to choice what app he 
# wanna use
class FrontApp:
    def __init__(self):
        self.keep_going = True
        self.screen_size = (400, 300)
        self.screen = pygame.display.set_mode(self.screen_size)
        self.font = pygame.font.SysFont("arial", 50)
        self.font1 = pygame.font.SysFont("arial", 12)
        self.button = [ "Server","Voter App","Manager App"]# this are the buttons related to the apps
        self.appsOpen = []
        self.active = ""
        self.delay = 0
        self.events = self.mouse_pos = None

        pygame.display.set_caption("Voterpy")

    # Methof that will start the app chosen
    def startApp(self, app):
        if app not in self.appsOpen:
            os.system(f"python3 {app}/main.py &")
            self.appsOpen.append(app)

    def run(self):
        # The cicle of the fronty application
        while self.keep_going:
            self.mouse_pos = pygame.mouse.get_pos()
            self.events = pygame.event.get()
            for event in self.events:
                if event.type == pygame.QUIT:
                    exit()

                elif event.type == pygame.KEYDOWN:
                    if pygame.key.get_pressed()[pygame.K_KP_ENTER]:
                        exit()
            self.screen.fill(cs.grey3.value)
            self.draw()
            pygame.display.update()

    # Method that will draw the button and the tittles on the screen
    def draw(self):
        # drawing tittle
        size = pygame.font.Font.size(self.font, 'Voterpy')
        line = self.font.render('Voterpy', True, cs.white3.value)
        self.screen.blit(line, (int(self.screen_size[0]/2-size[0]/2), 10))
        # drawing sub tittle
        size = pygame.font.Font.size(self.font1, 'Front App')
        line = self.font1.render('Front App', True, cs.white.value)
        self.screen.blit(line, (int(self.screen_size[0]/2-size[0]/2), 55))
        # Called Method that draw the button start on the screen
        self.active = verticalButtonsDisplay(self.screen, self.button,100,(int(self.screen_size[0]/2)-100, 110),(200, 40), self.mouse_pos,self.active,\
                                            pygame.font.SysFont("arial", 20))
        if self.active != '': # to check if the user chose one app to start
            self.startApp(self.active.split(" ")[0].lower())
            self.active = ''
            self.delay = 0
        
        if self.delay > 250: # to refresh the apps open
            self.display = 0
            self.appsOpen = []
        self.delay += 1
        
        # drawinghelp message
        size = pygame.font.Font.size(pygame.font.SysFont("arial", 15), 'Chose the app you wanna start and click on it.')
        line = pygame.font.SysFont("arial", 15).render('Chose the app you wanna start and click on it.', True, cs.white.value)
        self.screen.blit(line, (int(self.screen_size[0]/2-size[0]/2), 255))


# __________________________ Start Mode control ____________________________
# Note: the start mode is according to the atributes specifyed on the program execution 

# Checking if the sys.argv array have a value/values to start the app specify in the value/values
if len(sys.argv)>1:
    # Starting all the app that the user wants by threads
    for i in range(1, len(sys.argv)):
        # send the files name written in the terminal when executing the code
        th = Threads(sys.argv[i]) 
        th.start()

# If not the program will open a windows that will allow you two chose the app that will be started
else:
    # Interface of the front-app manager
    pygame.init()
    app = FrontApp()
    app.run()