import pygame

class Voted():
    def __init__(self, screen, screen_size):
        self.screen, self.screen_size = screen, screen_size
        self.events = None
        self.mouse_pos = None

    def run(self, events):
        self.events = events
        self.mouse_pos = pygame.mouse.get_pos()
        return "voted"