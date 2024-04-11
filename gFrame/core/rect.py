from ..baseImporter import pygame
from ..core.screenUnits import ScreenUnit

class Rect(pygame.Rect):
    def __init__(self, *args):
        if len(args) == 4:
            left, top, width, height = ScreenUnit.convertMultipleUnits(args[0], args[1], args[2], args[3])
            super().__init__(left, top, width, height)
        else:
            positionCord = ScreenUnit.convertMultipleUnits(*args[0])
            size = ScreenUnit.convertMultipleUnits(*args[1])
            super().__init__(positionCord, size)

    def unpack(self):
        return self.left, self.top, self.width, self.height
    
    @staticmethod
    def placeHolder():
        return pygame.Rect(0, 0, 0, 0)