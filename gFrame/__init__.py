import pygame

from pygame import FULLSCREEN, NOFRAME

pygame.init()
try:
    pygame.mixer.init()
except:
    _mixer = False
else:
    _mixer = True
    
pygame.display.set_caption("gFrame (powered by pygame)")

from .vars import RGBvalue, validScreenUnit, getVersion

from .colors import Color
from .enums import aspectRatios, axis, hoverSpeed, interactionType, mouseButton, overFlow, scrollSpeed, xTextPositioning, yTextPositioning
from .fonts import Font

from .core.rect import Rect
from .core.display import Display
from .core.appConstructor import AppConstructor
from .core.animate import Animate
if _mixer:
    from .core.audio import Audio
del _mixer
from .core.draw import Draw
from .core.interactions import Interactions
from .core.logger import Logger
from .core.screenUnits import ScreenUnit
from .core.scroll import Scroll
from .core.updating import Updating
from .core.debugger import Debugger, RunTimer
from .core.runmodes import debugging, logging, production

from .widgets.button import Button
from .widgets.text import Text
# from widgets.slider import Slider
from .widgets.image import Image
from .widgets.roundButton import RoundButton
# from widgets.textBox import Textbox

