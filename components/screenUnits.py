import vars
from elements.enums import aspectRatios

class ScreenUnit:
    def convert():
        ...

    def precent(parentSize, percent):
        return parentSize / 100 * percent

    def dw(screenUnit: float) -> float:
        """
        display width
        """
        return vars.userScreenWidth / 100 * screenUnit

    def dh(screenUnit: float) -> float:
        """
        display height
        """
        return vars.userScreenHeight / 100 * screenUnit
    
    def vw(screenUnit: float) -> float:
        """
        view width 
        """
        return vars.appScreenWidth / 100 * screenUnit
    
    def vh(screenUnit: float) -> float:
        """
        view height
        """
        return vars.appScreenHeight / 100 * screenUnit
    
    def getVwFromPx(xPixel: int) -> (int | float):
        return xPixel / (vars.appScreenWidth / 100)
    
    def getVhFromPx(yPixel: int) -> (int | float):
        return yPixel / (vars.appScreenHeight / 100)

    def getRelativePosition(position: tuple[int]) -> tuple[(int | float)]:
        vw = ScreenUnit.getVwFromPx(position[0])
        vh = ScreenUnit.getVhFromPx(position[1])
        return vw, vh
    
    def aspectRatioFromInt(xRatio: int, yRatio: int):
        return xRatio / yRatio
    
    def aspectRatioFromString(aspectRatio: str | aspectRatios):
        if isinstance(aspectRatio, aspectRatios):
            aspectRatioValues = aspectRatio.value.split("/")
        else:
            aspectRatioValues = aspectRatio.split("/")
        return int(aspectRatioValues[0]) / int(aspectRatioValues[1])
