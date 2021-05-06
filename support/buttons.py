import pygame
from support.color import Color

def verticalButtonsDisplay(screen, buttons, y, position, box_dim, mouse_pos, active, font):
    # y for the boxes,
    click = pygame.mouse.get_pressed(3)
    x1, y1, = position[0], position[1]  # for the boxes texts
    for button in buttons:
        size = pygame.font.Font.size(font, button)
        button_box = pygame.Rect(x1, y, box_dim[0], box_dim[1])
        # checking if the algorithms choice
        
        if mouse_pos[0]in range(x1, x1+box_dim[0]) and mouse_pos[1] in range(y1, y1+box_dim[1])\
                and click[0] == 1:
            active = button
        # hover button effect
        if mouse_pos[0]in range(x1, x1+box_dim[0]) and mouse_pos[1] in range(y1, y1+box_dim[1]):
            pygame.draw.rect(screen, Color.grey.value, button_box)
            line = font.render(button, True, Color.white.value)
        else:
            pygame.draw.rect(screen, Color.white.value, button_box, 2)
            line = font.render(button, True, Color.white.value)
        
        if active == button:
            pygame.draw.rect(screen, Color.green.value, button_box)
            line = font.render(button, True, Color.black1.value)
        screen.blit(line, (x1-(size[0]/2)+(box_dim[0]/2), y1))
        y += 45
        y1 += 45 
    return active