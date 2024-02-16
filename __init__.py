from importer import pygame
version = '1.2.2'
def getVersion():
    print(version)

pygame.init()
pygame.mixer.init()

from elements.colors import *
from elements.enums import *
from elements.fonts import *

from components.display import Display
from components.appConstructor import AppConstructor
from components.animate import Animate
from components.audio import Audio
from components.draw import Draw
from components.interactions import Interactions
from components.logger import Logger
from components.screenUnits import ScreenUnit
from components.scroll import Scroll
from widgets.buttontemp import Button
# from widgets.text import Text
# from widgets.slider import Slider
# from widgets.image import Image
# from widgets.textBox import Textbox
from components.updating import Updating
