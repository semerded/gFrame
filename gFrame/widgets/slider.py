from ..baseImporter import pygame, vars
from ._coloredWidget import _ColoredWidget
from ..core.screenUnits import ScreenUnit
from ..core.draw import Draw
from ..colors import Color
from ..core.updating import Updating
from ..core.interactions import Interactions

rounded = -2

class Slider(_ColoredWidget):
    _slidingActive = False
    _drawKnob = False
    knobRadius = -2
    knobColor = Color.BLACK
    
    def __init__(self, size: tuple[vars.validScreenUnit], sliderMin: int | float, sliderMax: int | float, sliderColor: vars.RGBvalue, backgroundColor: vars.RGBvalue, startValue: int | float = None, borderRadius: vars.validScreenUnit = rounded, reverse: bool = False) -> None:
        if borderRadius == -2:
            borderRadius = size[1] / 2
        self.sliderRadius = borderRadius
        super().__init__(size, backgroundColor, borderRadius)
        self.sliderMin = sliderMin
        self.sliderMax = sliderMax
        self.sliderColor = sliderColor
        self.position = (0, 0)
        
        if startValue != None and startValue >= sliderMin and startValue <= sliderMax:
            self.startValue = startValue
        else:
            self.startValue = sliderMin
        self.sliderValue = self.startValue
        
        if reverse:
            self.sliderMin = sliderMax
            self.sliderMax = sliderMin
        
        difference = self.sliderMax - self.sliderMin
        
        self.sliderPosition = (self.startValue - self.sliderMin) * (self.widgetSize[0] / difference) 
    
    def setKnob(self, radius: vars.validScreenUnit, color: vars.RGBvalue):
        self._drawKnob = True
        self.knobRadius = radius
        self.knobColor = color       
            
    def _placeSlider(self, left, top):
        Draw.rectangle(left, top, self.sliderPosition, self.widgetSize[1], self.sliderColor, self.sliderRadius)
    
    def _getSliderPosition(self, left, top):
        if super().isSuperClicked() or (self._drawKnob and Interactions.isMouseClickedInCircle((left + self.sliderPosition , top + self.widgetSize[1] / 2), self.knobRadius)):
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
            # Updating.requestUpdate()
        difference = self.sliderMax - self.sliderMin
        self.sliderValue = self.sliderPosition / (self.widgetSize[0] / difference) + self.sliderMin
        return self._slidingActive
    
    def handler(self):
        """
        use this to handle the click events when you are using manual updating
        """
        return self._getSliderPosition(*self.position)
        
        
        
    def place(self, left, top):
        left, top = ScreenUnit.convertMultipleUnits(left, top)
        self.position = (left, top)
        
        self._getSliderPosition(left, top)
        self._colordWidgetPlace(left, top, 255, True)
        self._placeSlider(left, top)
        if self._drawKnob:
            Draw.circle((left + self.sliderPosition , top + self.widgetSize[1] / 2), self.knobRadius, self.knobColor)
        
    def getValue(self):
        return self.sliderValue
        
        
        
        