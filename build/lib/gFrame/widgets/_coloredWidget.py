from ..widgets._baseWidget import _BaseWidget
from ..components.updating import Updating
from ..components.draw import Draw
from ..elements.colors import Color
from ..baseImporter import vars

class _ColoredWidget(_BaseWidget):
    def __init__(self, size, color, borderRadius: vars.validScreenUnit = -1) -> None:
        super().__init__(size, borderRadius=borderRadius)
        self.widgetColor = color
        self.defaultColor = color
        
        self.disableColor = Color.GREY

    
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
        if self.getWidgetStatus:
            if event():
                Updating.requestRectUpdate(self.getBorderRect)
                self.widgetColor = clickColor
            else:
                self.widgetColor = self.defaultColor 
                
    def disable(self, disableColor: vars.RGBvalue = Color.GRAY):
        super().disable()
        self.disableColor = disableColor
    
    def enable(self):
        super().enable()
            
    def _colordWidgetPlace(self, left, top, opacity: int = 255, placeBaseWidget: bool = True):
        if not self.getWidgetStatus:
            self.widgetColor = self.disableColor

        if opacity >= 1:
            Draw.rectangleFromRect(self.getRect, self.widgetColor, self.widgetBorderRadius)
        else: 
            Draw.transparantRectangleFromRect(self.getRect, opacity, self.widgetColor)   
        
        if placeBaseWidget:
            self._baseWidgetPlace(left, top)
            