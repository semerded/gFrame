from vars import RGBvalue
from widgets._baseWidget import _BaseWidget
from components.draw import Draw
import vars

class _ColoredWidget(_BaseWidget):
    def __init__(self, size: tuple[int | float, int | float], color: vars.RGBvalue, borderRadius) -> None:
        super().__init__(size, borderRadius)
        
        self.widgetColor = color
        self.defaultColor = color
    
    def updateColor(self, newColor: vars.RGBvalue):
        self.widgetColor = newColor
        self.defaultColor = newColor
        
    def changeColorOnHover(self, hoverColor: vars.RGBvalue):
        self._changeColorOnEvent(self.isMouseOver, hoverColor)
        
    def changeColorOnClick(self, clickColor: vars.RGBvalue):
        self._changeColorOnEvent(self.isClicked(), clickColor)

    def changeColorOnPressing(self, clickColor: vars.RGBvalue):
        self._changeColorOnEvent(self.isPressing(), clickColor)
            
    def _changeColorOnEvent(self, event, clickColor: vars.RGBvalue):
        if event():
            self.widgetColor = clickColor
        else:
            self.widgetColor = self.defaultColor 
            
    def _colordWidgetPlace(self, left, top, placeBaseWidget: bool = True):
        Draw.rectangleFromRect(self.getRect, self.widgetColor, Draw.calculateInnerBorderRadius(self.widgetBorderRadius, self.widgetBorderWidth))
        if placeBaseWidget:
            self._BaseWidgetPlace(left, top)
            