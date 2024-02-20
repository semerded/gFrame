from importer import pygame

import vars
from components.interactions import Interactions
from components.screenUnits import ScreenUnit
from components.draw import Draw
from elements.enums import mouseButton
from elements.colors import Color

class _baseWidget:
    def __init__(self, size: tuple[vars.validScreenUnit, vars.validScreenUnit], borderRadius: int = -1) -> None:
        self.widgetSize = ScreenUnit.convertMultipleUnits(*size) # size
        self.widgetRect: pygame.Rect = pygame.Rect(0, 0, 0, 0)
        self.borderRect: pygame.Rect = pygame.Rect(0, 0, 0, 0)
        self.widgetBorderRadius = ScreenUnit.checkIfValidScreenUnit(borderRadius)
        
        self.widgetBorderWidth = 0
        self.widgetBorderColor = Color.BLACK
        
    def border(self, borderWidth: int, borderColor: vars.RGBvalue):
        self.widgetBorderWidth = int(ScreenUnit.checkIfValidScreenUnit(borderWidth))
        self.widgetBorderColor = borderColor    
        
    def isMouseOver(self):
        return Interactions.isMouseOver(self.widgetRect)
    
    def isClicked(self, mouseButton: mouseButton = mouseButton.leftMouseButton):
        return Interactions.isMouseClickedInRect(mouseButton, self.widgetRect)
    
    def isReleased(self, mouseButton: mouseButton = mouseButton.leftMouseButton):
        return Interactions.isMouseReleasedInRect(mouseButton, self.widgetRect)
    
    def isPressing(self, mouseButton: mouseButton = mouseButton.leftMouseButton):
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
        if event():
            Draw.borderFromRect(self.borderRect, ScreenUnit.checkIfValidScreenUnit(borderWidth), borderColor, self.widgetBorderRadius)
      
    def changeBorderOnHover(self, borderColor: vars.RGBvalue):
        self._changeBorderOnEvent(self.isMouseOver, borderColor)
    
    def changeBorderOnClick(self, borderColor: vars.RGBvalue):
        self._changeBorderOnEvent(self.isClicked, borderColor)
        
    def changeBorderOnPressing(self, borderWidth: int, borderColor: vars.RGBvalue):
        self._changeBorderOnEvent(self.isPressing, borderWidth, borderColor)
    
    def _changeBorderOnEvent(self, event, borderColor: vars.RGBvalue):
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
        
    @property
    def getRect(self):
        return self.widgetRect
    
    @property
    def getBorderRect(self):
        return self.borderRect
           