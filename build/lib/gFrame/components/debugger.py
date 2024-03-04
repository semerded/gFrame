import time, vars
from ..components.appConstructor import AppConstructor
from ..widgets.text import Text
from ..elements.colors import Color

class Debugger:
    def showFPS(appObject: AppConstructor):
        fps = appObject.clock.get_fps()
        Text.simpleText((5, 5), fps, color= Color.GREEN)
        
class RunTimer:
    def setTimePoint():
        vars.debugTimePoints.append(time.process_time())
        
    def getResults():
        for index, _time in enumerate(vars.debugTimePoints):
            print(f"{index}. {_time}")
        vars.debugTimePoints = []