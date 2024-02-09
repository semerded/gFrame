from importer import pygame
from components.screenUnits import ScreenUnit
from elements.enums import axis
import vars
try:
    import PIL.Image
except ImportError:
    PILimported = False
else:
    PILimported = True

class Display:
    if PILimported:
        def getPixelColorFromBackground(left: int, top: int) -> vars.RGBvalue:
            displayString = pygame.image.tostring(vars.mainDisplay, 'RGB')
            displayByte = PIL.Image.frombytes('RGB', (vars.appWidth, vars.appHeight), displayString)
            return displayByte.getpixel((left, top))
        
    def fill(color: vars.RGBvalue):
        vars.mainDisplay.fill(color)
        
    def set(width, height, *flags):
        vars.appWidth = width
        vars.appHeight = height
        vars.appFlags = flags
        vars.mainDisplay = pygame.display.set_mode((width, height), *flags)
        
    def setMinimumScreenDimension(minimumScreenWidth: vars.validScreenUnit = None, minimumScreenHeight: vars.validScreenUnit = None):
        vars.minimumScreenWidth = minimumScreenWidth if minimumScreenWidth != None else None
        vars.minimumScreenHeight = minimumScreenHeight if minimumScreenHeight != None else None
        
    def checkForMinimumScreenSizeBreaches():
        width, height = Display.getAppScreenDimensions
        updateScreen = False
        if width < vars.minimumScreenWidth:
            width = vars.minimumScreenWidth
            updateScreen = True
        if height < vars.minimumScreenHeight:
            height = vars.minimumScreenHeight
            updateScreen = True
        if updateScreen:
            Display.set(width, height, *vars.appFlags)
    
    def setAspectRatio(aspectRatio: str | float, width: int = None, height: int = None):
        vars.aspectRatioObject.setAspectRatio(aspectRatio, width, height)
    
    def disableAspectRatio():
        vars.aspectRatioObject.disableAspectRatio()
        
    @property
    def getAppScreenDimensions():
        displayInfo = pygame.display.Info()
        return displayInfo.current_w, displayInfo.current_h