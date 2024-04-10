from .baseImporter import pygame

pygame.init()
try:
    pygame.mixer.init()
except:
    _mixer = False
else:
    _mixer = True
    
pygame.display.set_caption("gFrame (powered by pygame)")

from .vars import RGBvalue, validScreenUnit, getVersion

from .elements.colors import Color
from .elements.enums import aspectRatios, axis, hoverSpeed, interactionType, mouseButton, overFlow, scrollSpeed, xTextPositioning, yTextPositioning
from .elements.fonts import Font

from .components.rect import Rect
from .components.display import Display
from .components.appConstructor import AppConstructor
from .components.animate import Animate
if _mixer:
    from .components.audio import Audio
del _mixer
from .components.draw import Draw
from .components.interactions import Interactions
from .components.logger import Logger
from .components.screenUnits import ScreenUnit
from .components.scroll import Scroll
from .components.updating import Updating
from .components.debugger import Debugger, RunTimer
from .components.runmodes import debugger, logging, production

from .widgets.button import Button
from .widgets.text import Text
# from widgets.slider import Slider
from .widgets.image import Image
from .widgets.roundButton import RoundButton
# from widgets.textBox import Textbox
