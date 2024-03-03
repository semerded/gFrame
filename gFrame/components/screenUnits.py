import vars
from elements.enums import aspectRatios

class ScreenUnit:
    def precent(parentSize, percent):
        return parentSize / 100 * percent

    def dw(screenUnit: float) -> float:
        """
        display width
        """
        return vars.displayWidth / 100 * screenUnit

    def dh(screenUnit: float) -> float:
        """
        display height
        """
        return vars.displayHeight / 100 * screenUnit
    
    def vw(screenUnit: float) -> float:
        """
        view width 
        """
        return vars.appWidth / 100 * screenUnit
    
    def vh(screenUnit: float) -> float:
        """
        view height
        """
        return vars.appHeight / 100 * screenUnit
    
    def px(screenUnit: float) -> float:
        return screenUnit
    
    def getVwFromPx(xPixel: int) -> (int | float):
        return xPixel / (vars.appWidth / 100)
    
    def getVhFromPx(yPixel: int) -> (int | float):
        return yPixel / (vars.appHeight / 100)

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
    
    def checkIfValidScreenUnit(screenUnit: vars.validScreenUnit):
        if isinstance(screenUnit, str):
            return _StrScreenUnitConverter.getUnitType(screenUnit)
        return screenUnit
    
    def convertMultipleUnits(*screenUnit: vars.validScreenUnit):
        results = []
        for unit in screenUnit:
            results.append(ScreenUnit.checkIfValidScreenUnit(unit))
        return results
    
    def centerOfScreen():
        return vars.appWidth / 2, vars.appHeight / 2
    
    def centerRectInScreen(*args): # make pyi file
        if len(args) == 2:
            width, heigth = ScreenUnit.convertMultipleUnits(args[0], args[1])
        else:
            width, heigth = args[0].width, args[0].height
            
        screenCenterW, screenCenterH = ScreenUnit.centerOfScreen()
        return screenCenterW - (width / 2), screenCenterH - (heigth / 2) 

class _StrScreenUnitConverter:
    def getUnitType(screenUnit):
        splitUnit = _StrScreenUnitConverter.splitUnit(screenUnit)
        try: 
            return _screenUnitMapping[splitUnit[1]](splitUnit[0])
        except KeyError:
            print("an error occured") # TODO add error to log file
            return 0
        
    def splitUnit(screenUnit):
        number = string = ""
        for char in screenUnit:
            try:
                int(char)
                number += char
            except ValueError:
                string += char
        return int(number), string
    
    def emUnit(screenUnit):
        pass

_screenUnitMapping = {
    "vw": ScreenUnit.vw,
    "vh": ScreenUnit.vh,
    "dw": ScreenUnit.dw,
    "dh": ScreenUnit.dh,
    "px": ScreenUnit.px
} 

