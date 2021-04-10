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
    
    # Method to control all the key pressed
    # def keysControl(self, key):
    #     text = ''
    #     keysDict = {key[K_q]:'q', key[K_w]: 'w',key[K_e]: 'e',key[K_r]:'r',key[K_t]:'t',key[K_y]:'y',
    #     key[K_u]: 'u',key[K_i]:'i',key[K_o]:'o',key[K_p]:'p',key[K_a]:'a',key[K_s]:'s',key[K_d]:'d',
    #     key[K_f]:'f',key[K_g]:'g',key[K_j]:'j',key[K_k]:'k',key[K_l]:'l',key[K_z]:'z',key[K_x]: 'x',
    #     key[K_c]:'c',key[K_v]:'v',key[K_b]:'b',key[K_n]:'n',key[K_m]:'m', key[K_SPACE:]:' ',
    #     key[K_1]:'1', key[K_2]: '2',key[K_3]: '3',key[K_4]:'4',key[K_5]:'6',key[K_6]:'6',
    #     key[K_7]:'7', key[K_8]: '8',key[K_9]: '9',key[K_0]:'0'}

    #     text = [value for keys, value in keysDict.items() if keys]
    #     if len(text):
    #         return text[0]
    #     else:
    #         return ''