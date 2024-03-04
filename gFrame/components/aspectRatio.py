from ..elements.enums import axis, aspectRatios
from ..components.screenUnits import ScreenUnit
from ..components.display import Display
from .. import vars

class _AspectRatio:
    def __init__(self) -> None:
        self.aspectRatioActive = False
        self.aspectRatio: float
        self.aspectRatioAxis: axis
        
    def setAspectRatio(self, aspectRatio: str | float | aspectRatios, width: vars.validScreenUnit = None, height: vars.validScreenUnit = None):
        if isinstance(aspectRatio, aspectRatios):
            aspectRatio = aspectRatio.value
        width, height = ScreenUnit.convertMultipleUnits(width, height)
        
        self.aspectRatioActive = True
        self._getAspectRatio(aspectRatio)
        width = self._getAxis(width, height)
        width, height = self._calculateAspectRatioDimensions(width, height)
        Display.set(width, height, *vars.appFlags)
    
    def disableAspectRatio(self):
        self.aspectRatioActive = False
        
    def updateAspectRatio(self):
        if self.aspectRatioAxis == axis.x:
            width = vars.appWidth
            height = 0
        else:
            width = 0
            height = vars.appHeight
        width, height, self._calculateAspectRatioDimensions(width, height)
        Display.set(width, height, *vars.appFlags)


    # private    
    def _getAspectRatio(self, aspectRatio):
        if isinstance(aspectRatio, str):
            self.aspectRatio = ScreenUnit.aspectRatioFromString(aspectRatio)
        else:
            self.aspectRatio = aspectRatio
            
    def _getAxis(self, width, height):
        if width == None and height == None:
            width = vars.appHeight
            self.aspectRatioAxis = axis.x
        elif width != None:
            self.aspectRatioAxis = axis.x
        else:
            self.aspectRatioAxis = axis.y
        return width
    
    def _calculateAspectRatioDimensions(self, width, height):
        if self.aspectRatioAxis == axis.x:
            height = width / self.aspectRatio
        else:
            width = height * self.aspectRatio
        return width, height    
    
    