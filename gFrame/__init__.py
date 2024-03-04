from .baseImporter import pygame
_GFRAME_VERSION = '1.0.0'
def getVersion():
    print(_GFRAME_VERSION)


# from . import vars

from .elements.colors import Color
from .elements.enums import aspectRatios, axis, hoverSpeed, interactionType, mouseButton, overFlow, scrollSpeed, xTextPositioning, yTextPositioning
from .elements.fonts import Font

from .components.rect import Rect
from .components.display import Display
from .components.appConstructor import AppConstructor
from .components.animate import Animate
from .components.audio import Audio
from .components.draw import Draw
from .components.interactions import Interactions
from .components.logger import Logger
from .components.screenUnits import ScreenUnit
from .components.scroll import Scroll
from .widgets.button import Button
from .widgets.text import Text
# from widgets.slider import Slider
from .widgets.image import Image
from .widgets.roundButton import RoundButton
# from widgets.textBox import Textbox
from .components.updating import Updating
