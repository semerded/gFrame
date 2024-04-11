from ..baseImporter import pygame, vars
from ..core.rect import Rect

class Updating:
    def updateDisplay():
        pygame.display.update()
        
        
    def updateRects(*rect: Rect):
        pygame.display.update(*rect)
        
    def requestUpdate():
        vars.updatePending = True
        
    def removeRequestForUpdate():
        vars.updatePending = False
        
    def requestRectUpdate(*rect: Rect):
        Updating.requestUpdate()
        for _rect in rect:
            vars.updateableRectsPending.append(_rect)
            
    def __init__(self, **kwargs) -> None:
        self.objectList = kwargs
        self.emptyObjectList = kwargs
        
    def resetObjectList(self):
        self.objectList = self.emptyObjectList
