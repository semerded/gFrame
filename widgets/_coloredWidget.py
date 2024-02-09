from vars import RGBvalue
from widgets._baseWidget import _baseWidget
import vars

class _ColoredWidget(_baseWidget):
    def __init__(self, size: tuple[int | float, int | float], color: vars.RGBvalue) -> None:
        super().__init__(size)
        
        self.widgetColor = color
        self.defaultColor = color
    
    def updateColor(self, newColor: vars.RGBvalue):
        self.widgetColor = newColor
        self.defaultColor = newColor
        
    def changeColorOnClick(self, clickColor: vars.RGBvalue):
        if self.isClicked():
            self.widgetColor = clickColor
        else:
            self.widgetColor = self.defaultColor
            
    def changeColorOnPressing(self, clickColor: vars.RGBvalue):
        if self.isPressing():
            self.widgetColor = clickColor
        else:
            self.widgetColor = self.defaultColor
            