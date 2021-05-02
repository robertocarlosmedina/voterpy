from enum import Enum

# class Enum that store all the color's that are used in this project
class Color(Enum):
    blue=(0, 0, 255)
    blue3=(15, 159, 191)
    blue1 = (3, 120, 166)
    white=(255, 255, 255)
    white1=(155, 155, 155)
    white3=(185, 185, 185)
    white2 = (242, 242, 242)
    yellow = (255, 255, 0)
    green=(0, 255, 0)
    green1 = (70, 115, 2)
    green2=(116, 166, 10)
    green3=(136, 191, 17)
    black=(0,0,0)
    black1=(25, 25, 25)
    black2=(0, 1, 13)
    grey=(105, 105, 105)
    grey1=(87, 88, 89)
    grey2 = (217, 217, 217)
    grey3 = (35, 35, 35)
    grey4=(57, 58, 59)
    red=(255, 0, 0)
    red1= (242, 15, 15)
    red2= (255, 25, 25)

# this is to return the RGB value of the color
def rgbColor(co):
    return [color_e.value for color_name, color_e in Color.__members__.items() if co == color_name][0]
