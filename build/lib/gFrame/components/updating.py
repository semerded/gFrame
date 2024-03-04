from ..baseImporter import pygame

class Updating:
    def updateDisplay():
        pygame.display.update()
        
    def __init__(self, **kwargs) -> None:
        self.objectList = kwargs
        self.emptyObjectList = kwargs
        
    def resetObjectList(self):
        self.objectList = self.emptyObjectList
