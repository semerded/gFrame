from .. import data

@staticmethod
class DefaultTickClock():       
    def setTickSpeed(ticksPerSecond):
        data.defaultTickClock.ticksPerSecond = ticksPerSecond

    def setActive(status):
        data.defaultTickClock.start() if status else data.defaultTickClock.stop()
        
    def onTick(*functions):
        data.defaultTickClock.onTick(*functions)
        
    def stop():
        data.defaultTickClock.stop()
        
    def start():
        data.defaultTickClock.start()
