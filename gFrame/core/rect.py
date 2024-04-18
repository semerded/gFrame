from ..baseImporter import pygame, vars
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
    
    def expandWidth(self, expansion: vars.validScreenUnit):
        expansion = ScreenUnit.checkIfValidScreenUnit(expansion)
        self.width += expansion
        self.left -= int(expansion / 2)
        
    def shrinkWidth(self, shrinkage: vars.validScreenUnit):
        shrinkage = ScreenUnit.checkIfValidScreenUnit(shrinkage)
        self.expandWidth(-shrinkage)
        
    def expandHeight(self, expansions: vars.validScreenUnit):
        expansion = ScreenUnit.checkIfValidScreenUnit(expansion)
        self.height += expansions
        self.top -= int(expansion / 2)
        
    def shrinkHeight(self, shrinkage: vars.validScreenUnit):
        shrinkage = ScreenUnit.checkIfValidScreenUnit(shrinkage)
        self.expandHeight(-shrinkage)
        
    def rw(self, screenUnit: float):
        return self.width / 100 * screenUnit
    
    def rh(self, screenUnit: float):
        return self.height / 100 * screenUnit
    
    def pw(self, screenUnit: float):
        return (self.width / 100 * screenUnit) + self.x
    
    def ph(self, screenUnit: float):
        return (self.height / 100 * screenUnit) + self.y
    
    @staticmethod
    def placeHolder():
        return pygame.Rect(0, 0, 0, 0)