import pygame
from pygame import *
import os
import sys


from support.color import Color
from support.client import Client
from src.login import Login
from src.start import Start
from src.createUser import CreateUser
from src.homepage import HomePage


screen_size = (700, 500)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Manager App")

# links of the project
links = {"start": Start(screen, screen_size), "login": Login(screen, screen_size),\
     "createUser":CreateUser(screen, screen_size),"homePage":HomePage(screen, screen_size)\
    }
current_layout = "start"

# clock = pygame.Clock()


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

        elif event.type == pygame.KEYDOWN:
            if pygame.key.get_pressed()[K_KP_ENTER]:
                exit()

    screen.fill(Color.grey4.value)
    current_layout = links[current_layout].run()
    pygame.display.update()