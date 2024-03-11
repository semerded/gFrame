from ..baseImporter import pygame
from ..elements.enums import aspectRatios
from ..components.screenUnits import ScreenUnit
from ..baseImporter import vars
try:
    import PIL.Image
except ImportError:
    PILimported = False
else:
    PILimported = True

class Display:
    if PILimported:
        def getPixelColorFromBackground(left: int, top: int) -> vars.RGBvalue:
            left, top = ScreenUnit.convertMultipleUnits(left, top)
            displayString = pygame.image.tostring(vars.mainDisplay, 'RGB')
            displayByte = PIL.Image.frombytes('RGB', (vars.appWidth, vars.appHeight), displayString)
            return displayByte.getpixel((left, top))
        
    def fill(color: vars.RGBvalue):
        vars.mainDisplay.fill(color)
        
    def set(width, height, *flags):
        vars.appWidth, vars.appHeight = ScreenUnit.convertMultipleUnits(width, height)
        vars.appFlags = flags
        vars.mainDisplay = pygame.display.set_mode((vars.appWidth, vars.appHeight), *flags)
        
    def setMinimumScreenDimension(minimumScreenWidth: vars.validScreenUnit = None, minimumScreenHeight: vars.validScreenUnit = None):
        minimumScreenWidth, minimumScreenHeight = ScreenUnit.convertMultipleUnits(minimumScreenWidth, minimumScreenHeight)
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
    
    def setAspectRatio(aspectRatio: str | float | aspectRatios, width: int = None, height: int = None):
        """
        calculates the aspect ratio from the width or height and resizes the screen to that size\n
        when no size is givin, the size will be calculated from the current width of the screen\n
        when 2 sizes are givin, the size from the givin width will be used\n
        """
        vars.aspectRatioObject.setAspectRatio(aspectRatio, width, height)
    
    def disableAspectRatio():
        vars.aspectRatioObject.disableAspectRatio()
        
    def getWindowSize():
        displayInfo = pygame.display.Info()
        return displayInfo.current_w, displayInfo.current_h
    
    def getDisplaySize():
        return vars.displayWidth, vars.displayHeight