from ... import data
from ...fonts import pygame
from ...typedef import *


class set:
    def framerate(framerate: float):
        data.frameRate = framerate
        
    def setAutoUpdating(status):
        data.autoUpdate = status
        
    def aspectRatio(aspectRatio):
        pass
    
    def globalFont(*args):
        try:
                data.globalFont = pygame.font.SysFont(args[0], args[1], bold=args[2], italic=[3])
        except:
            try:
                data.globalFont = pygame.font.Font(args[0], args[1])
                data.globalFont.bold = args[2]
                data.globalFont.italic = args[3]
            except:
                data.globalFont = pygame.font.SysFont("arial", 14, bold=False, italic=False)
    
    def autoUpdate(status: bool):
        data.autoUpdate = status
        
    def caption(caption: str):
        pygame.display.set_caption(caption)
        
    def icon(icon: path):
        icon = pygame.image.load(icon)
        pygame.display.set_icon(icon)
        
    def modifiableFunctions(modifiableFunctionName, newFunction):
        pass
    
                        
        