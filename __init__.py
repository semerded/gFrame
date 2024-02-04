from importer import pygame
version = '1.1.3'
def getVersion():
    print(version)

pygame.init()
pygame.mixer.init()

from components.animate import Animate
from components.audio import Audio
from components.appConstructor import AppConstructor
from components.button import Button
from components.display import Display
from components.draw import Draw
from components.image import Image
from components.interactions import Interactions
from components.logger import Logger
from components.screenUnits import ScreenUnit
from components.scroll import Scroll
from components.slider import Slider
from components.text import Text
from components.textBox import Textbox
from components.updating import Updating
from elements.colors import *
from elements.enums import *
from elements.fonts import *