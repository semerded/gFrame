from typing import overload
from ..elements.enums import mouseButton
from ..components.rect import Rect
from ..baseImporter import vars

class _BaseWidget:
    @overload
    def __init__(self, size: tuple[vars.validScreenUnit], borderRadius: vars.validScreenUnit = -1) -> None: ...
    
    def setBorder(self, borderWidth: vars.validScreenUnit, borderColor: vars.RGBvalue) -> None: ...
    
    # interactions
    def isMouseOver(self) -> bool: ...
    def isClicked(self, mouseButton: mouseButton = mouseButton.leftMouseButton) -> bool: ...
    def isReleased(self, mouseButton: mouseButton = mouseButton.leftMouseButton) -> bool: ...
    def isPressing(self, mouseButton: mouseButton = mouseButton.leftMouseButton) -> bool: ...
    
    def isSuperClicked(self, mouseButton: mouseButton = mouseButton.leftMouseButton) -> bool: ...
    def isSuperPressing(self, mouseButton: mouseButton = mouseButton.leftMouseButton) -> bool: ...
    def isSuperReleased(self, mouseButton: mouseButton = mouseButton.leftMouseButton) -> bool: ...
    
    def inRect(self, rect: Rect): ...
    
    def addBorderOnHover(self, borderWidth: vars.validScreenUnit, borderColor: vars.RGBvalue) -> None: ...
    def addBorderOnClick(self, borderWidth: vars.validScreenUnit, borderColor: vars.RGBvalue) -> None: ...
    def addBorderOnPressing(self, borderWidth: vars.validScreenUnit, borderColor: vars.RGBvalue) -> None: ...
    
    def changeBorderOnHover(self, borderColor: vars.RGBvalue) -> None: ...
    def changeBorderOnClick(self, borderColor: vars.RGBvalue) -> None: ...
    def changeBorderOnPressing(self, borderColor: vars.RGBvalue) -> None: ...
    
    def resize(self, width: vars.validScreenUnit, height: vars.validScreenUnit) -> tuple[int | float]: ...
    
    def enable(self) -> None: ...
    def disable(self) -> None: ...
    
    @property
    def getRect(self) -> Rect: ...
    
    @property
    def getBorderRect(self) -> Rect: ...
    
    @property
    def getWidgetStatus(self) -> bool: ...