from typing_extensions import TypeAlias
from components.aspectRatio import _AspectRatio
from importer import pygame

# type declaration
RGBvalue: TypeAlias = tuple[int, int, int]
validScreenUnit: TypeAlias = int | float
pygameFont: TypeAlias = pygame.font.Font

# screen info
displayInfo = pygame.display.Info()
displayWidth = displayInfo.current_w
displayHeight = displayInfo.current_h
appWidth: int
appHeight: int
minimumScreenWidth: int = None
minimumScreenHeight: int = None
appFlags: tuple
mainDisplay: pygame.Surface = None
screenUpdate = False
windowResized = False

aspectRatioObject: _AspectRatio = _AspectRatio()

# global interactions
#? LMB, MMB, RMB, SCRLup, SCRLdown, SMBbottom, SMBtop
mouseButtonsStatus = [False, False, False, False, False, False, False]
mouseFlank = [False, False, False, False, False, False, False]

#? keyboard
activeKeys = []
releasedKeys = []
clickedKeys = []


scrollValue = 0
