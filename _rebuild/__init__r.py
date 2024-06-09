import pygame
pygame.init()

try:
    pygame.mixer.init()
except:
    _mixer_imported = False
else:
    _mixer_imported = True
    
#base
from .colors import Color as Color
from .fonts import Font as Font
from .typedef import RGBvalue, screenUnit


#core
if _mixer_imported:
    from .core.audio import AudioQueue, AudioObject
del _mixer_imported
from .core.draw import Draw
from .core.rect import Rect
from .core.renderQueue import RenderQueue
from .core.appConstructor import AppConstructor
from .core.properties.get import get
from .core.properties.set import set
from .core.display import Display
from .core.interactions import Interactions
from .core.eventHandler import eventHandler
from .core.exit import exit
from .core.runmode import main

#std
from .std.screenunit import vw, vh, dw, dh, percent, getVwFromPx, getVhFromPx
from .std.windowContstructor import windowConstructor
from .core.tickClock import TickClock
