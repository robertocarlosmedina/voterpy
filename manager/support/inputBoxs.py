import pygame
from support.color import Color

# Method that draw the input's box ont he screen 
def drawInputBoxs(screen,inputBoxs,input_limit,events,mouse_pos,y_start, x_start, boxDim, space_between_box):
    placeHold = "Click and write "
    display = True
    for key,boxInfo in inputBoxs.items():
        # getting the mouse click
        click = pygame.mouse.get_pressed(3)

        # Writing the boxx name on the screen
        if boxInfo[0] != '':
            boxText_surface = pygame.font.SysFont("arial", 12).render(key, True, Color.green.value)

            # bliting the text in the center of the box
            infoText_surface = pygame.font.SysFont("arial", 20).render(inputBoxs[key][0], True, (255, 255, 255))
            sizeInfo = pygame.font.Font.size(pygame.font.SysFont("arial", 20), inputBoxs[key][0])
            screen.blit(infoText_surface, (x_start+boxDim[0]/2-sizeInfo[0]/2,y_start+12))

            # Display the cursor in the box
            if boxInfo[1]:
                pygame.draw.line(screen, Color.grey1.value, (x_start+boxDim[0]/2+sizeInfo[0]/2 , y_start+10),\
                                                         (x_start+boxDim[0]/2+sizeInfo[0]/2, y_start+30), 2)
        else:
            boxText_surface = pygame.font.SysFont("arial", 12).render(key, True, Color.red2.value)
        size = pygame.font.Font.size(pygame.font.SysFont("arial", 12), key)
        screen.blit(boxText_surface, (x_start+boxDim[0]/2-size[0]/2,y_start-15))

        # control if mouse pressed on the box, to active it 
        if mouse_pos[0]in range(x_start, x_start+boxDim[0]) and mouse_pos[1] in range(y_start, y_start+boxDim[1])\
            and click[0] == 1:
            inputBoxs[key][1] = True

            # putting the other box's in state False
            for key1 in inputBoxs.keys():
                if key1 != key:
                    inputBoxs[key1][1] = False

        # drawing the box accordin to his state (True or False)
        pygame.draw.rect(screen, Color.white.value, pygame.Rect(x_start, y_start, boxDim[0], boxDim[1]), 2) if boxInfo[1]\
            else pygame.draw.rect(screen, Color.grey.value, pygame.Rect(x_start, y_start, boxDim[0], boxDim[1]), 2)
        
        # Writing the place holder in the box
        if boxInfo[0] == '' and not boxInfo[1]:
            text_surface = pygame.font.SysFont("arial", 12).render(placeHold+key, True, Color.grey1.value)
            size = pygame.font.Font.size(pygame.font.SysFont("arial", 12), placeHold+key)
            screen.blit(text_surface, (x_start+boxDim[0]/2-size[0]/2,y_start+15))

        # adding some space between the box's
        y_start += space_between_box

        # checking the events and adding the text to the variable
        for event in events:
            if event.type == pygame.KEYDOWN and boxInfo[1]:
                if event.key==pygame.K_BACKSPACE:
                    inputBoxs[key][0] = inputBoxs[key][0][:-1]
                elif event.key==pygame.K_SPACE:
                    pass
                elif((len(inputBoxs[key][0])<=input_limit)):
                    inputBoxs[key][0] += event.unicode
    
    return inputBoxs

# Method that verify all the inputs
def verifyInput(inputBoxs):
    for value in inputBoxs.values():
        if value[0] == "" or value[0] == " " or len(value[0])<2:
            return False
    return True
# Method that Remove the space in the strings
# def 
