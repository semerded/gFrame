from typing import overload
from importer import pygame
from elements.enums import overFlow, hoverSpeed, xTextPositioning, yTextPositioning
from elements.fonts import Font
from elements.colors import Color
from components.rect import Rect
import vars

class Text:
    font: pygame.font.Font
    @overload
    def __init__(self, text: str, fontName: str, fontSize: vars.validScreenUnit, color: vars.RGBvalue, bold: bool = False, italic: bool = False) -> None: ...
    @overload
    def __init__(self, text: str, fontPath: vars.path, fontSize: vars.validScreenUnit, color: vars.RGBvalue, bold: bool = False, italic: bool = False) -> None: ...
    @overload
    def __init__(self, text: str, font: pygame.font.Font, color: vars.RGBvalue, bold: bool = False, italic: bool = False) -> None: ...
    
    @staticmethod
    def textOverflow(text: str, font: pygame.font.Font, maxWidth: int | float, overFlowType: overFlow = overFlow.ellipsis) -> str: ...
    
    @staticmethod
    def simpleText(text: str, left: vars.validScreenUnit, top: vars.validScreenUnit, font: pygame.font.Font = Font.H3, color: vars.RGBvalue = Color.BLACK, bold: bool = False, italic: bool = False): ...
    
    @staticmethod
    def centerTextInRect(textSurface: pygame.Surface, rect: Rect):
        xPos = rect.x + (rect.width / 2) - (textSurface.get_width() / 2)
        yPos = rect.y + (rect.height / 2) - (textSurface.get_height() / 2)
        return xPos, yPos
    
    def setAntiAllias(self, active: bool): ...
    
    def setBackground(self, backgroundColor: vars.RGBvalue): ...

    def setTextColor(self, color: vars.RGBvalue): ...
    
    def setBorder(self, borderWidth: vars.validScreenUnit, borderColor: vars.RGBvalue, borderRadius: vars.validScreenUnit = -1): ...
    
    def setHover(self, hoverDistance: vars.validScreenUnit, speed: int | hoverSpeed = hoverSpeed.normal): ...
    
    def setText(self, text: str, bold: bool = False, italic: bool = False): ...
    
    @overload
    def place(self, left: vars.validScreenUnit, top: vars.validScreenUnit): ...
    @overload
    def place(self, left: vars.validScreenUnit, top: vars.validScreenUnit, text: str): ...

    @overload
    def placeInRect(self, rect: Rect, xPositioning: xTextPositioning, yPositioning: yTextPositioning): ...
    @overload
    def placeInRect(self, rect: Rect, xPositioning: xTextPositioning, yPositioning: yTextPositioning, text: str): ...
    
    
    @property
    def getRect(self): ...