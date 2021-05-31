import pygame
from pygame import *
from support.color import Color
from src.login import Login
from src.start import Start
from src.homePage import HomePage
from src.voted import Voted

# declaration of screen info
screen_size = (700, 500)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Voter App")

# links of the project that are store in a dict, where the keys are the page name
# and the value is an instance of the class that represent that it
links = {"start": Start(screen, screen_size), "login": Login(screen, screen_size),\
        "homePage":HomePage(screen, screen_size),"voted":Voted(screen,screen_size)}
# current_layout = "login"
current_layout = "start"
events = None
id = None

# clock = pygame.time.Clock()

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == QUIT:
            exit()

        elif event.type == pygame.KEYDOWN:
            if pygame.key.get_pressed()[K_KP_ENTER]:
                exit()

    screen.fill(Color.grey4.value)
    current_layout, id = links[current_layout].run(events, id)
    # clock.tick(60)
    pygame.display.update()
