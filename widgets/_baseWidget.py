from importer import pygame

import vars
from components.interactions import Interactions
from components.draw import Draw
from elements.enums import mouseButton
from elements.colors import Color

class _baseWidget:
    def __init__(self, size: tuple[vars.validScreenUnit, vars.validScreenUnit], color: vars.RGBvalue, borderRadius: int = -1) -> None:
        self.widgetSize = size
        self.widgetRect: pygame.Rect = pygame.Rect(0, 0, 0, 0)
        self.widgetBorderRadius = borderRadius
        
        self.widgetBorderWidth = 0
        self.widgetBorderColor = Color.BLACK
        
    def border(self, borderWidth: int, borderColor: vars.RGBvalue):
        self.widgetBorderWidth = borderWidth
        self.widgetBorderColor : borderColor    
        
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
        if self.isMouseOver():
            self.border(borderWidth, borderColor)
        else:
            self.border(self.widgetBorderWidth, self.widgetBorderColor)
            
    def addBorderOnClick(self, borderWidth: int, borderColor: vars.RGBvalue):
        if self.isClicked():
            self.border(borderWidth, borderColor)
        else:
            self.border(self.widgetBorderWidth, self.widgetBorderColor)

    def widgetPlace(self, left, top):
        self.widgetRect = pygame.Rect(left, top, self.widgetSize[0], self.widgetSize[1])
        if self.widgetBorderWidth > 0:
            Draw.border(self.widgetBorderWidth, self.widgetRect, self.widgetBorderColor, self.widgetBorderRadius)

            
    def resize(self, width, height):
        self.widgetSize = [width, height]
        
    @property
    def getRect(self):
        return self.widgetRect
           
