import time
from ..baseImporter import vars
from ..components.appConstructor import AppConstructor
from ..widgets.text import Text
from ..elements.colors import Color

class Debugger:
    def showFPS(appObject: AppConstructor):
        fps = appObject.clock.get_fps()
        Text.simpleText((5, 5), fps, color= Color.GREEN)
        
    def loop(appObject: AppConstructor, main: vars.functionAdress, fps: float = 60):
        while True:
            try:
                appObject.eventHandler(fps)
                main()
                Debugger.showFPS()
            except Exception as error:
                print(error)


        
class RunTimer:
    def setTimePoint():
        vars.debugTimePoints.append(time.perf_counter())
        
    def getResults():
        for index, _time in enumerate(vars.debugTimePoints):
            print(f"{index}. {_time}")
        vars.debugTimePoints = []