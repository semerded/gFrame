import vars
from components.interactions import Interactions
from components.screenUnits import ScreenUnit
from components.draw import Draw
from components.rect import Rect
from elements.enums import mouseButton
from elements.colors import Color

class _BaseWidget:
    deActivated = False
    isClickedInWidget = False
    widgetBorderWidth = 0
    widgetBorderColor = Color.BLACK
    
    def __init__(self, *args, borderRadius: int = -1) -> None:
        if len(args) == 1:
            args = args[0]
            
        self.widgetSize: list[int | float] = ScreenUnit.convertMultipleUnits(*args) # size
        self.widgetRect: Rect = Rect(0, 0, 0, 0)
        self.borderRect: Rect = Rect(0, 0, 0, 0)
        self.widgetBorderRadius = ScreenUnit.checkIfValidScreenUnit(borderRadius)
        
    def setBorder(self, borderWidth, borderColor: vars.RGBvalue):
        self.widgetBorderWidth = int(ScreenUnit.checkIfValidScreenUnit(borderWidth))
        self.widgetBorderColor = borderColor    
        
    def isMouseOver(self) -> bool:
        if not self.deActivated:
            return Interactions.isMouseOver(self.widgetRect)
        return False
    
    def isClicked(self, mouseButton: mouseButton = mouseButton.leftMouseButton) -> bool:
        if self.deActivated or vars.widgetAlreadyPressed:
            return False
        return self._setWidgetAlreadyPressed(mouseButton, Interactions.isMouseClickedInRect)
    
    def isReleased(self, mouseButton: mouseButton = mouseButton.leftMouseButton) -> bool:
        if self.deActivated or vars.widgetAlreadyPressed:
            return False
        if self._setWidgetAlreadyPressed(mouseButton, Interactions.isMouseReleasedInRect) and self.isClickedInWidget:
            self.isClickedInWidget = False
            return True
        return False
    
    def isPressing(self, mouseButton: mouseButton = mouseButton.leftMouseButton) -> bool:
        if self.deActivated or vars.widgetAlreadyPressed:
            return False
        return self._setWidgetAlreadyPressed(mouseButton, Interactions.isMousePressingInRect)
        
    
    def _setWidgetAlreadyPressed(self, mouseButton: mouseButton, func):
        if (result := func(mouseButton, self.widgetRect)):
            vars.widgetAlreadyPressed = True
        return result
    
    def isSuperClicked(self, mouseButton: mouseButton = mouseButton.leftMouseButton):
        if not self.deActivated:
            return Interactions.isMouseClickedInRect(mouseButton, self.widgetRect)
        return False
    
    def isSuperPressing(self, mouseButton: mouseButton = mouseButton.leftMouseButton):
        if not self.deActivated:
            return Interactions.isMousePressingInRect(mouseButton, self.widgetRect)
        return False
    
    def isSuperReleased(self, mouseButton: mouseButton = mouseButton.leftMouseButton):
        if not self.deActivated:
            return Interactions.isMouseReleasedInRect(mouseButton, self.widgetRect)
        return False
    
    def _checkIfWidgetIsClicked(self):
        if Interactions.isMouseClickedInRect(mouseButton.leftMouseButton, self.widgetRect):
            self.isClickedInWidget = True
    
    def inRect(self, rect: Rect):
        return Interactions.rectInRect(rect, self.widgetRect)
    
    def addBorderOnHover(self, borderWidth: int, borderColor: vars.RGBvalue):
        self._addBorderOnEvent(self.isMouseOver, borderWidth, borderColor)
            
    def addBorderOnClick(self, borderWidth: int, borderColor: vars.RGBvalue):
        self._addBorderOnEvent(self.isSuperClicked, borderWidth, borderColor)
        
    def addBorderOnPressing(self, borderWidth: int, borderColor: vars.RGBvalue):
        self._addBorderOnEvent(self.isSuperPressing, borderWidth, borderColor)
    
    def _addBorderOnEvent(self, event, borderWidth: int, borderColor: vars.RGBvalue):
        if not self.deActivated:
            if event():
                borderWidth = int(ScreenUnit.checkIfValidScreenUnit(borderWidth))
                Draw.borderFromRect(self.borderRect, borderWidth, borderColor, Draw.calculateOuterBorderRadius(self.widgetBorderRadius, borderWidth))

    def changeBorderOnHover(self, borderColor: vars.RGBvalue):
        self._changeBorderOnEvent(self.isMouseOver, borderColor)
    
    def changeBorderOnClick(self, borderColor: vars.RGBvalue):
        self._changeBorderOnEvent(self.isSuperClicked, borderColor)
        
    def changeBorderOnPressing(self, borderColor: vars.RGBvalue):
        self._changeBorderOnEvent(self.isSuperPressing, borderColor)
    
    def _changeBorderOnEvent(self, event, borderColor: vars.RGBvalue):
        if not self.deActivated:
            if event():
                self.border(self.widgetBorderWidth, borderColor)
            else:
                self.border(self.widgetBorderWidth, self.widgetBorderColor)

    def _baseWidgetPlace(self, left, top):
        left, top = ScreenUnit.convertMultipleUnits(left, top)
        self.widgetRect = Rect(left, top, self.widgetSize[0], self.widgetSize[1])
        self.borderRect = Rect(left - self.widgetBorderWidth / 2, top - self.widgetBorderWidth / 2, self.widgetSize[0] + self.widgetBorderWidth, self.widgetSize[1] + self.widgetBorderWidth)
        
        if self.widgetBorderWidth > 0:
            Draw.borderFromRect(self.widgetRect, self.widgetBorderWidth, self.widgetBorderColor, Draw.calculateOuterBorderRadius(self.widgetBorderRadius, self.widgetBorderWidth))
        self._checkIfWidgetIsClicked()
        
    def resize(self, width, height):
        width, height = ScreenUnit.convertMultipleUnits(width, height)
        self.widgetSize = [width, height]
        return self.widgetSize
        
    def enable(self):
        self.deActivated = False
        
    def disable(self):
        self.deActivated = True
        
    @property
    def getRect(self):
        return self.widgetRect
    
    @property
    def getBorderRect(self):
        return self.borderRect
    
    @property
    def getWidgetStatus(self):
        return not self.deActivated
