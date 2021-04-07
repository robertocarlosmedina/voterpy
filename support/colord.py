from enum import Enum

# class Enum that store all the color's that are used in this project
class color(Enum):
    blue=(0, 0, 255)
    blue3=(15, 159, 191)
    blue1 = (3, 120, 166)
    white=(255, 255, 255)
    white1=(155, 155, 155)
    white2 = (242, 242, 242)
    yellow = (255, 255, 0)
    green=(0, 255, 0)
    green1 = (70, 115, 2)
    green2=(116, 166, 10)
    green3=(136, 191, 17)
    black1=(25, 25, 25)
    black2=(0, 1, 13)
    grey=(105, 105, 105)
    grey1=(87, 88, 89)
    grey3 = (217, 217, 217)
    grey4 = (191, 191, 191)
    red=(255, 0, 0)
    red1= (242, 15, 15)

# this is to return the RGB value of the color
def rgbColor(co):
    return [color_e.value for color_name, color_e in color.__members__.items() if co == color_name][0]
