from importer import pygame
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
        vars.mainDisplay = pygame.display.set_mode((width, height), *flags)