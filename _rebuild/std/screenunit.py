from ..typedef import screenUnit
from .. import data

def percent(parentSize, percent):
    return parentSize / 100 * percent

def dw(screenUnit: float) -> float:
    """
    display width
    """
    return data.displayWidth / 100 * screenUnit

def dh(screenUnit: float) -> float:
    """
    display height
    """
    return data.displayHeight / 100 * screenUnit

def vw(screenUnit: float) -> float:
    """
    view width 
    """
    return data.appWidth / 100 * screenUnit

def vh(screenUnit: float) -> float:
    """
    view height
    """
    return data.appHeight / 100 * screenUnit

def getVwFromPx(xPixel: int) -> (int | float):
    return xPixel / (data.appWidth / 100)
    
def getVhFromPx(yPixel: int) -> (int | float):
    return yPixel / (data.appHeight / 100)

def getRelativePositionFromCord(coordinate: tuple[int]) -> tuple[(int | float)]:
        vw = getVwFromPx(coordinate[0])
        vh = getVhFromPx(coordinate[1])
        return vw, vh
    
def centerOfScreen():
    return data.appWidth / 2, data.appHeight / 2

# def centerRectInScreen(*args): # make pyi file
#         if len(args) == 2:
#             width, heigth = ScreenUnit.convertMultipleUnits(args[0], args[1])
#         else:
#             width, heigth = args[0].width, args[0].height
            
#         screenCenterW, screenCenterH = ScreenUnit.centerOfScreen()
#         return screenCenterW - (width / 2), screenCenterH - (heigth / 2) 
