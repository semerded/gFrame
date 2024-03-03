from importer import pygame
import vars
from components.draw import Draw
from components.rect import Rect
from components.interactions import Interactions
from components.screenUnits import ScreenUnit
from vars import RGBvalue
from widgets._baseImage import _BaseImage
from elements.fonts import Font
from elements.colors import Color
from elements.enums import mouseButton, overFlow
from widgets._coloredWidget import _ColoredWidget
from widgets.text import Text
from typing import overload

class Button(_ColoredWidget):
    @overload
    def __init__(self, size: tuple[vars.validScreenUnit], color: vars.RGBvalue, borderRadius: vars.validScreenUnit = -1) -> None: ...
    @overload
    def __init__(self, width: vars.validScreenUnit, height: vars.validScreenUnit, color: vars.RGBvalue, borderRadius: vars.validScreenUnit = -1) -> None: ...
    
    @overload
    @staticmethod
    def simpleButton(size: tuple[vars.validScreenUnit], position: vars.coordinate, backgroundColor: vars.RGBvalue = Color.LIGHT_GRAY, borderColor: vars.RGBvalue = Color.BLACK, borderWidth: vars.validScreenUnit = 5) -> bool: ...
    @overload
    @staticmethod
    def simpleButton(width: vars.validScreenUnit, height: vars.validScreenUnit, left: vars.validScreenUnit, top: vars.validScreenUnit, backgroundColor: vars.RGBvalue = Color.LIGHT_GRAY, borderColor: vars.RGBvalue = Color.BLACK, borderWidth: vars.validScreenUnit = 5) -> bool: ...
    @overload
    @staticmethod
    def simpleButton(rect: Rect, backgroundColor: vars.RGBvalue = Color.LIGHT_GRAY, borderColor: vars.RGBvalue = Color.BLACK, borderWidth: vars.validScreenUnit = 5) -> bool: ...
    
    @overload
    def text(self, text: str, textFont: pygame.font.Font, color: vars.RGBvalue, bold: bool = False, italic: bool = False, overFlow: overFlow = overFlow.ellipsis) -> None: ...
    @overload
    def text(self, text: str, fontName: str, fontSize: vars.validScreenUnit, color: vars.RGBvalue, bold: bool = False, italic: bool = False, overFlow: overFlow = overFlow.ellipsis) -> None: ...
    @overload
    def text(self, text: str, fontPath: vars.path, fontSize: vars.validScreenUnit, color: vars.RGBvalue, bold: bool = False, italic: bool = False, overFlow: overFlow = overFlow.ellipsis) -> None: ...
    
    def icon(self, iconPath: str) -> None: ...
    
    def isHeldFor(self, milliseconds: int) -> bool: ...
    
    def isDoubleClicked(self, mousebutton: mouseButton = mouseButton.leftMouseButton) -> bool: ...
    
    def place(self, left: vars.validScreenUnit, top: vars.validScreenUnit, opacity: int = 255) -> None: ...
    
    @property
    def getPressedTime(self) -> float: ...
    
    def setDoubleClickMaxInterval(self, maxInterval_inMilliseconds: int) -> None: ...
    