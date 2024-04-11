from ..baseImporter import pygame
from ..core.rect import Rect
from ..widgets._baseImage import _BaseImage
from ..widgets._baseWidget import _BaseWidget

class Image(_BaseImage, _BaseWidget):
    def __init__(self, fileName: str, nameHint: str = "") -> None:
        _BaseImage.__init__(self, fileName, nameHint)
        _BaseWidget.__init__(self, self.getImageSize)
        
    def place(self, left: float, top: float):
        self.resize(*self.getImageSize)
        self._baseImagePlace(left, top)
        self._baseWidgetPlace(left, top)
        
    def resize(self, width, height):
        return super().resize(width, height)
        
    @property
    def getImageRect(self):
        return Rect(self.imagePosition, self.getImageSize)
    
    
    