import pygame 
from pygame.locals import *

# class for all the game input by the keyboard
class Textinput:
    def __init__(self):
        pygame.init()
        self.base_font = pygame.font.SysFont("arial", 20)
        self.text = ''
        self.color_passive = pygame.Color(128,128,128)
        self.color_active = pygame.Color(255, 255, 255)
        self.color = self.color_passive
        self.active = True
        self.limit = 12
        # self.count = 0
    
    # Method to receive the input text from the keyboard
    def getInputText(self,all_event, screen, dim_x,pos_y, screen_size):
        self.input_rect = pygame.Rect(screen_size[0]/2-dim_x/2, pos_y,dim_x , 40)
        # Pega todos os eventos de escrita do teclado
        for event in all_event:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key ==pygame.K_KP_ENTER:
                    text = self.text
                    self.text = ''
                    return text
                elif event.key==pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                elif((len(self.text)<=self.limit)):
                    self.text += event.unicode

        if self.active:
            self.color = self.color_active
        else:
            self.color = self.color_passive

        pygame.draw.rect(screen, self.color, self.input_rect, 2)
        text_surface = self.base_font.render(self.text, True, (255, 255, 255))
        size = pygame.font.Font.size(self.base_font, str(self.text))
        screen.blit(text_surface, (screen_size[0]/2-size[0]/2, int(self.input_rect.y+5)))
        self.input_rect.w = max(340, text_surface.get_width() + 10)
        return self.text
    