from ..baseImporter import pygame, vars
from ..widgets._coloredWidget import _ColoredWidget
from ..core.screenUnits import ScreenUnit
from ..core.draw import Draw
from ..colors import Color
from ..core.updating import Updating
from ..core.interactions import Interactions

class Slider(_ColoredWidget):
    _slidingActive = False
    
    def __init__(self, size: tuple[vars.validScreenUnit], sliderMin: int | float, sliderMax: int | float, color: vars.RGBvalue, startValue: int | float = None, borderRadius: vars.validScreenUnit = -1) -> None:
        super().__init__(size, color, borderRadius)
        self.sliderMin = sliderMin
        self.sliderMax = sliderMax
        
        if startValue != None and startValue >= sliderMin and startValue <= sliderMax:
            self.startValue = startValue
        else:
            self.startValue = sliderMin
            
        self.sliderPosition = self.startValue
            
    def _placeSlider(self, left, top):
        Draw.rectangle(left + self.sliderPosition, top, self.widgetSize[1], self.widgetSize[1], Color.GREEN)
    
    def _getSliderPosition(self, left):
        if super().isSuperClicked():
            self._slidingActive = True
        if Interactions.isMouseReleased():
            self._slidingActive = False
            
        if self._slidingActive:
            mouseXpos = pygame.mouse.get_pos()[0]
            if mouseXpos - left < 0:
                self.sliderPosition = 0
            elif mouseXpos - left > self.widgetSize[0]:
                self.sliderPosition = self.widgetSize[0]
            else:
                self.sliderPosition = mouseXpos - left
            Updating.requestRectUpdate(self.borderRect)
        
    def place(self, left, top):
        left, top = ScreenUnit.convertMultipleUnits(left, top)
        
        self._getSliderPosition(left)
        self._colordWidgetPlace(left, top, 255, True)
        self._placeSlider(left, top)
        
        
        