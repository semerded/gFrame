import pygame, os
from ..typedef import *
from .. import data

@staticmethod
class Display:
    def set(width: screenUnit, height: screenUnit, *flags):
        data.appWidth, data.appHeight = width, height
        data.appFlags = flags
        data.mainDisplay = pygame.display.set_mode((width, height), *flags)
        
    def fill(color: RGBvalue):
        data.mainDisplay.fill(color)
        
    def center():
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        
    def switchPage():
        data.pageCounter = 0