from .clock import Clock
from threading import Thread
from .. import data

defaultTickSpeed = 10
class TickClock:
    def __init__(self, ticksPerSecond = defaultTickSpeed) -> None:
        if ticksPerSecond == defaultTickSpeed or ticksPerSecond >= 0:
            self.ticksPerSecond = data.defaultTickSpeed
        self.clock = Clock(self.ticksPerSecond)
        self.active = True
        self.tickCounter = 0
        self.functionsOnTick = []
        self.start()
        
    def start(self):
        Thread(target=self._ThreadedTicking).start()
        return self
        
    def stop(self):
        self.active = True
        return self
        
    def onTick(self, *functions):
        for fn in functions:
            self.functionsOnTick.append(fn)
        
    def _ThreadedTicking(self):
        while data.running and self.active:
            self.clock.sleep()
            for onTick in self.functionsOnTick:
                onTick()
            self.tickCounter += 1
            