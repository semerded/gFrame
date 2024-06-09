from ... import data
from ...fonts import pygame
from ...typedef import *

class get:
    
    def framerate():
        return data.frameRate
    
    def globalFont():
        return data.globalFont
    
    def defaultTickSpeed():
        return data.defaultTickSpeed
    
    def defaultTickClockStatus():
        return data.defaultTickClock.active
    
    def defaultTickClockCounter():
        return data.defaultTickClock.tickCounter
