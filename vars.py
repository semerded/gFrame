from typing_extensions import TypeAlias, Literal
from importer import pygame

RGBvalue: TypeAlias = tuple[int, int, int]
validScreenUnit: TypeAlias = int | float
pygameFont: TypeAlias = pygame.font.Font

displayInfo = pygame.display.Info()
userScreenWidth = displayInfo.current_w
userScreenHeight = displayInfo.current_h
appScreenWidth = 0
appScreenHeight = 0
mainDisplay: pygame.Surface = None
screenUpdate = False

# LMB, MMB, RMB, SCRLup, SCRLdown, SMBbottom, SMBtop
mouseButtonsStatus = [False, False, False, False, False, False, False]
previousMouseButtonStatus = [False, False, False, False, False, False, False]

scrollValue = 0
