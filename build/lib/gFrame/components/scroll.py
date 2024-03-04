from ..elements.enums import scrollSpeed
from ..baseImporter import vars

class Scroll():
    def __init__(self, maxScrollPixel: int, speed: scrollSpeed) -> None:
        self.maxScroll = maxScrollPixel
        self.scrollPosition = 0
        self.scrollSpeed = speed
        self._makeMaxScrollNegative()
        
    def _makeMaxScrollNegative(self):
        if self.maxScroll > 0:
            self.maxScroll * -1

    def setMaxScroll(self, maxScrollPixel: int):
        self.maxScroll = maxScrollPixel
        self._makeMaxScrollNegative()
        
    def setSpeed(self, speed: scrollSpeed):
        self.scrollSpeed = speed
        
    def scrollController(self) -> int:
        self.scrollPosition += vars.scrollValue * self.scrollSpeed
        if self.scrollPosition > 0:
            self.scrollPosition = 0
        if self.scrollPosition < self.maxScroll:
            self.scrollPosition = self.maxScroll        
        return self.scrollPosition
