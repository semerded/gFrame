try:
    import pygame
except ImportError:
    raise ImportError("install pygame with 'pip install pygame'")
try:
    import pygame_textinput
except ImportError:
    pygame__textinputImported = False
else:
    pygame__textinputImported = True

version = '1.1.0'
def getVersion():
    print(version)
    

import sys, os
from typing_extensions import TypeAlias, Literal




pygame.init()
pygame.mixer.init()

screenUnit: TypeAlias = int | str
modifiableFunctions: TypeAlias = Literal[
    "quit"
]

RGBvalue: TypeAlias = tuple[int, int, int]
font : TypeAlias = pygame.font


# pygameLogger = logging.basicConfig() # TODO add logger



displayInfo = pygame.display.Info()
userScreenWidth = displayInfo.current_w
userScreenHeight = displayInfo.current_h
appScreenWidth = 0
appScreenHeight = 0
mainDisplay = None
screenUpdate = False

# LMB, MMB, RMB, SCRLup, SCRLdown, SMBbottom, SMBtop
mouseButtonsStatus = [False, False, False, False, False, False, False]
previousMouseButtonStatus = []

scrollValue = 0




    





        
    

            



        
