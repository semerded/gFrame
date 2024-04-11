from typing import overload
from ..widgets._baseWidget import _BaseWidget
from ..colors import Color
from ..baseImporter import vars

class _ColoredWidget(_BaseWidget):
    @overload
    def __init__(self, size: tuple[vars.validScreenUnit], color: vars.RGBvalue, borderRadius: vars.validScreenUnit = -1) -> None: ...
    
    def updateColor(self, newColor: vars.RGBvalue) -> None: ...
    
    def changeColorOnHover(self, hoverColor: vars.RGBvalue) -> None: ...
    def changeColorOnClick(self, clickColor: vars.RGBvalue) -> None: ...
    def changeColorOnPressing(self, clickColor: vars.RGBvalue) -> None: ...
    
    def disable(self, disableColor: vars.RGBvalue = Color.GRAY) -> None: ...
    def enable(self) -> None: ...
    