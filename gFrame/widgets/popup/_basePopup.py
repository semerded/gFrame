from ...enums import mouseButton
from ...core.rect import Rect
from ...core.screenUnits import ScreenUnit
from ...core.interactions import Interactions
from ...core.draw import Draw

class _BasePopup:
    popupRect = Rect(0, 0, 0, 0)
    
    def __init__(self, size: tuple[vars.validScreenUnit], backgroundColor: vars.RGBvalue, borderWidth: vars.validScreenUnit, borderColor: vars.RGBvalue, cornerRadius: vars.validScreenUnit = -1, discardWhenClickedOutsidePopup: bool = True) -> None:
        self.size = ScreenUnit.convertMultipleUnits(*size)
        self.borderWidth = ScreenUnit.checkIfValidScreenUnit(borderWidth)
        self.cornerRadius = ScreenUnit.checkIfValidScreenUnit(cornerRadius)
        self.backgroundColor = backgroundColor
        self.borderColor = borderColor
        self.discardWhenClickedOutsidePopup = discardWhenClickedOutsidePopup
        
    def place(self):
        pos = ScreenUnit.centerRectInScreen(self.size[0], self.size[1])
        self.popupRect = Rect(pos, self.size)
        
        Draw.rectangleFromRect(self.popupRect, self.backgroundColor, self.cornerRadius)
        Draw.borderFromRect(self.popupRect, self.borderWidth, self.borderColor, Draw.calculateOuterBorderRadius(self.cornerRadius, self.borderWidth))
        
        if self.discardWhenClickedOutsidePopup and Interactions.isMouseClickedNotInRect(mouseButton.leftMouseButton, self.popupRect):
            return "discard"
    
    