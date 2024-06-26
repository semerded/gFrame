from typing_extensions import TypeAlias, Literal
from .baseImporter import pygame

print("\n\033[97mgFrame! (powered by pygame)")
print("read documentations here: \n")

_GFRAME_VERSION = '1.0.0'
gFrameVersion: TypeAlias = str
def getVersion() -> gFrameVersion:
    print(_GFRAME_VERSION)
    return _GFRAME_VERSION

# type declaration
RGBvalue: TypeAlias = tuple[int, int, int]
validScreenUnit: TypeAlias = int | float | Literal[
                                                    "vw",
                                                    "vh",
                                                    "dw",
                                                    "dh",
                                                    "px",
                                                    "em"
                                                    ]

pygameFont: TypeAlias = pygame.font.Font
coordinate: TypeAlias = list[int] | tuple[int]
path: TypeAlias = str
functionAdress: TypeAlias = ... # a function without the brackets

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

updatePending = False
windowResized = False
updateableRectsPending = []

aspectRatioObject = None

# global interactions
#? LMB, MMB, RMB, SCRLup, SCRLdown, SMBbottom, SMBtop
mouseButtonsStatus = [False, False, False, False, False, False, False]
mouseFlank = [False, False, False, False, False, False, False]

#? keyboard
activeKeys = []
releasedKeys = []
clickedKeys = []


scrollValue = 0


#? widgets
widgetAlreadyPressed = False


#? debugger
debugTimePoints = []
