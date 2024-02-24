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
        self.widgetRect: pygame.Rect = pygame.Rect(0, 0, 0, 0)
        self.borderRect: pygame.Rect = pygame.Rect(0, 0, 0, 0)
        self.widgetBorderRadius = ScreenUnit.checkIfValidScreenUnit(borderRadius)
        
        self.deActivated = False
        
        self.widgetBorderWidth = 0
        self.widgetBorderColor = Color.BLACK
        
    def border(self, borderWidth: int, borderColor: vars.RGBvalue):
        self.widgetBorderWidth = int(ScreenUnit.checkIfValidScreenUnit(borderWidth))
        self.widgetBorderColor = borderColor    
        
    def isMouseOver(self, overWriteWidgetPressRegistration: bool = False):
        if not self.deActivated or not vars.widgetAlreadyPressed:
            return Interactions.isMouseOver(self.widgetRect)
        return False
    
    def isClicked(self, mouseButton: mouseButton = mouseButton.leftMouseButton, overWriteWidgetPressRegistration: bool = False):
        if not overWriteWidgetPressRegistration and (self.deActivated or vars.widgetAlreadyPressed):
            return False
        vars.widgetAlreadyPressed = True
        return Interactions.isMouseClickedInRect(mouseButton, self.widgetRect)
    
    def isReleased(self, mouseButton: mouseButton = mouseButton.leftMouseButton, overWriteWidgetPressRegistration: bool = False):
        if not overWriteWidgetPressRegistration and (self.deActivated or vars.widgetAlreadyPressed):
            return False
        return Interactions.isMouseReleasedInRect(mouseButton, self.widgetRect)
    
    def isPressing(self, mouseButton: mouseButton = mouseButton.leftMouseButton, overWriteWidgetPressRegistration: bool = False):
        if not overWriteWidgetPressRegistration and (self.deActivated or vars.widgetAlreadyPressed):
            return False        
        vars.widgetAlreadyPressed = True
        return Interactions.isMousePressingInRect(mouseButton, self.widgetRect)
    
    def inRect(self, rect: pygame.Rect):
        return Interactions.rectInRect(rect, self.widgetRect)
    
    def addBorderOnHover(self, borderWidth: int, borderColor: vars.RGBvalue):
        self._addBorderOnEvent(self.isMouseOver, ScreenUnit.checkIfValidScreenUnit(borderWidth), borderColor)
            
    def addBorderOnClick(self, borderWidth: int, borderColor: vars.RGBvalue):
        self._addBorderOnEvent(self.isClicked, borderWidth, borderColor)
        
    def addBorderOnPressing(self, borderWidth: int, borderColor: vars.RGBvalue):
        self._addBorderOnEvent(self.isPressing, borderWidth, borderColor)
    
    def _addBorderOnEvent(self, event, borderWidth: int, borderColor: vars.RGBvalue):
        if not self.deActivated:
            if event():
                Draw.borderFromRect(self.borderRect, ScreenUnit.checkIfValidScreenUnit(borderWidth), borderColor, self.widgetBorderRadius)
      
    def changeBorderOnHover(self, borderColor: vars.RGBvalue):
        self._changeBorderOnEvent(self.isMouseOver, borderColor)
    
    def changeBorderOnClick(self, borderColor: vars.RGBvalue):
        self._changeBorderOnEvent(self.isClicked, borderColor)
        
    def changeBorderOnPressing(self, borderWidth: int, borderColor: vars.RGBvalue):
        self._changeBorderOnEvent(self.isPressing, borderWidth, borderColor)
    
    def _changeBorderOnEvent(self, event, borderColor: vars.RGBvalue):
        if not self.deActivated:
            if event():
                self.border(self.widgetBorderWidth, borderColor)
            else:
                self.border(self.widgetBorderWidth, self.widgetBorderColor)

    def _baseWidgetPlace(self, left, top):
        left, top = ScreenUnit.convertMultipleUnits(left, top)
        self.widgetRect = pygame.Rect(left, top, self.widgetSize[0], self.widgetSize[1])
        self.borderRect = pygame.Rect(left - self.widgetBorderWidth / 2, top - self.widgetBorderWidth / 2, self.widgetSize[0] + self.widgetBorderWidth, self.widgetSize[1] + self.widgetBorderWidth)
        
        if self.widgetBorderWidth > 0:
            Draw.borderFromRect(self.widgetRect, self.widgetBorderWidth, self.widgetBorderColor, self.widgetBorderRadius)

            
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
           