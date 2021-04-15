from typing import Deque
import pygame
import os
import hashlib
from pygame import *

from support.color import Color
from support.client import Client
from src.login import Login
from src.start import Start
from src.homepage import HomePage

# declaration of screen info
screen_size = (700, 500)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Manager App")

# links of the project that are store in a dict, where the keys are the page name
# and the value is an instance of the class that represent that it
links = {"start": Start(screen, screen_size), "login": Login(screen, screen_size),\
        "homePage":HomePage(screen, screen_size)\
    }

current_layout = "homePage"
events = None

# clock = pygame.time.Clock()
m2 = None
def checkingchanges(m2):
    m = hashlib.md5()
    for root, dirs, files in os.walk(os.getcwd()):
        for file_read in files:
            full_path = os.path.join(root, file_read)
            for line in open(full_path, encoding="utf8", errors='ignore').readlines():
                m.update(line.encode().strip())

    if m2 != m.digest():
        print("Changes")
        if m2 == None:
            m2 = m.digest()
            return False,m2
        return True,m2
    return False,m2
    
while True:
    events = pygame.event.get()
    for event in events:
        if event.type == QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if pygame.key.get_pressed()[K_KP_ENTER]:
                exit()
            # print (event.unicode)
    change, m2 = checkingchanges(m2)
    if change:
        break
    screen.fill(Color.grey4.value)
    current_layout = links[current_layout].run(events)
    # clock.tick(60)
    pygame.display.update()
