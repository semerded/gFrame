from importer import pygame

import vars
from components.interactions import Interactions
from components.screenUnits import ScreenUnit
from components.draw import Draw
from elements.enums import mouseButton
from elements.colors import Color

class _BaseWidget:
    def __init__(self, size: tuple[vars.validScreenUnit, vars.validScreenUnit], borderRadius: int = -1) -> None:
        self.widgetSize = ScreenUnit.convertMultipleUnits(*size) # size
        self.widgetRect: Rect = Rect(0, 0, 0, 0)
        self.borderRect: Rect = Rect(0, 0, 0, 0)
        self.widgetBorderRadius = ScreenUnit.checkIfValidScreenUnit(borderRadius)
        
        self.deActivated = False
        
        self.widgetBorderWidth = 0
        self.widgetBorderColor = Color.BLACK
        
    def border(self, borderWidth: int, borderColor: vars.RGBvalue):
        self.widgetBorderWidth = int(ScreenUnit.checkIfValidScreenUnit(borderWidth))
        self.widgetBorderColor = borderColor    
        
    def isMouseOver(self) -> bool:
        if not self.deActivated:
            return Interactions.isMouseOver(self.widgetRect)
        return False
    
    def isClicked(self, mouseButton: mouseButton = mouseButton.leftMouseButton, overWriteWidgetPressRegistration: bool = False) -> bool:
        if self.deActivated or not overWriteWidgetPressRegistration and vars.widgetAlreadyPressed:
            return False
        return self._setWidgetAlreadyPressed(mouseButton, Interactions.isMouseClickedInRect)
    
    def isReleased(self, mouseButton: mouseButton = mouseButton.leftMouseButton, overWriteWidgetPressRegistration: bool = False) -> bool:
        if self.deActivated or not overWriteWidgetPressRegistration and vars.widgetAlreadyPressed:
            return False
        return self._setWidgetAlreadyPressed(mouseButton, Interactions.isMouseReleasedInRect)
    
    def isPressing(self, mouseButton: mouseButton = mouseButton.leftMouseButton, overWriteWidgetPressRegistration: bool = False) -> bool:
        if self.deActivated or not overWriteWidgetPressRegistration and vars.widgetAlreadyPressed:
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
                Draw.borderFromRect(self.borderRect, ScreenUnit.checkIfValidScreenUnit(borderWidth), borderColor, Draw.calculateOuterBorderRadius(self.widgetBorderRadius, borderWidth))
      
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
     
    def resize(self, width, height):
        width, height = ScreenUnit.convertMultipleUnits(width, height)
        self.widgetSize = [width, height]
        
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
           