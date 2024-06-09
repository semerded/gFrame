import pygame
from . import typedef
from .core.tickClock import TickClock
from .core.renderQueue import RenderObject
running: bool = True

renderQueue: dict[int, dict[typedef.g_id, RenderObject]] = {}

#? screen
#* dimensions
appWidth = 0
appHeight = 0
appFlags = None

screenInfo = pygame.display.Info()
displayWidth = screenInfo.current_w
displayHeight = screenInfo.current_h
selectedDisplay = 0

backgroundColor = (0, 0, 0)

#* properties
mainDisplay: pygame.Surface = None
canvas: pygame.Surface = None
frameRate: float = 60
windowResized: bool = False

#* screen updating
reloadScreen: bool = True
autoUpdate: bool = False
fullScreenUpdatePending: bool = False


#? eventhandler
#* mouse
mouseButtonsStatus = [False, False, False, False, False, False, False]
mouseFlank = [False, False, False, False, False, False, False]

scrollValue = (0, 0)

#* keyboard
activeKeys = []
releasedKeys = []
clickedKeys = []

#* properties
appEvents: list[pygame.event.Event] = None
frameCounter: int = 0
pageCounter: int = 0

from .core.page import PageConstructor

pages: dict[str, PageConstructor] = {}

globalFontPath: typedef.path | typedef.fonts = "arial"
globalFont: pygame.font.Font = pygame.font.SysFont(globalFontPath, 14)

#? widgets
widgetAlreadyPressed = False
widgetConstantUpdates = {}

#? tick clock
defaultTickSpeed = 10
defaultTickClock = TickClock()