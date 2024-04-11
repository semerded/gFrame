from ..baseImporter import pygame, vars
from ..core.interactions import Interactions
from ..core.draw import Draw
from ..colors import Color
from ..enums import mouseButton
from ..core.rect import Rect

minSliderValue = None

class Slider:
    def __init__(self, size: list[int, int], sliderMin: int | float, sliderMax: int | float, color: vars.RGBvalue, startValue: int | float = minSliderValue, borderRadius: int = -1) -> None:
        self.sliderMin = sliderMin
        self.sliderMax = sliderMax
        self.sliderSize = size
        self.sliderColor = color
        self.sliderBorderRadius = borderRadius
        self.sliderRect = Rect(0, 0, 0, 0)
        self.sliderPosition = sliderMin if minSliderValue == None else startValue
        self.borderWidth = 0
        self.clickedInRect = False
        
    def border(self, borderWidth: int, borderColor: vars.RGBvalue):
        self.borderWidth = borderWidth
        self.borderColor = borderColor
        
    def setPosition(self, sliderPostition):
        if sliderPostition <= self.sliderMax and sliderPostition >= self.sliderMin:
            self.sliderPosition = sliderPostition
            
    def onMouseClick(self):
        Interactions.onMouseClickInRect(self.sliderRect, mouseButton.leftMouseButton)
    
    def place(self, left, top):
        self.sliderRect = Rect(left, top, self.sliderSize[0], self.sliderSize[1])
        self.fullRect = Rect(left - self.borderWidth / 2, top - self.borderWidth / 2, self.sliderSize[0] + self.borderWidth, self.sliderSize[1] + self.borderWidth)
        
        self._getSliderPosition(left)
        self._placeSliderShell(left, top)
        self._placeSlider(left, top)
        self._placeBorder()
        return self._calculateSliderPosition()
    
    def _getSliderPosition(self, left):
        if Interactions.onMouseClickInRect(self.sliderRect, mouseButton.leftMouseButton):
            self.clickedInRect = True
        
        if Interactions.isReleased(mouseButton.leftMouseButton):
            self.clickedInRect = False
        if self.clickedInRect:
            mouseXpos = pygame.mouse.get_pos()[0]
            if mouseXpos - left < 0:
                self.sliderPosition = 0
            elif mouseXpos - left > self.sliderSize[0]:
                self.sliderPosition = self.sliderSize[0]
            else:
                self.sliderPosition = mouseXpos - left

    def _placeSliderShell(self, left, top):
        Draw.rectangle(left, top, self.sliderSize[0], self.sliderSize[1], self.sliderColor, Draw.calculateInnerBorderRadius(self.sliderBorderRadius, self.borderWidth))
        
    def _placeSlider(self, left, top):
        Draw.rectangle(left, top, self.sliderPosition, self.sliderSize[1], Color.GREEN, Draw.calculateInnerBorderRadius(self.sliderBorderRadius, self.borderWidth))
        
    def _calculateSliderPosition(self):
        difference = self.sliderMax - self.sliderMin
        return self.sliderPosition / (self.sliderSize[0] / difference) + self.sliderMin
 
        
    def _placeBorder(self):
        if self.borderWidth > 0:
            Draw.border(self.borderWidth, self.sliderRect, self.borderColor, self.sliderBorderRadius)
        