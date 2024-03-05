from ..baseImporter import pygame
from ..components.screenUnits import ScreenUnit
from ..components.display import Display
from ..components.updating import Updating
from ..components.aspectRatio import _AspectRatio

from typing_extensions import TypeAlias, Literal
from .. import vars
import sys, os

modifiableFunctions: TypeAlias = Literal[
    "quit",
    "test"
]

constructorUnit: TypeAlias = int | float | Literal[
    "dw",
    "dh",
    "px"
]

class AppConstructor:
    """
    the appConstructor initializes the game display\n
    it main purpose is to do every action within the `eventhandler` function
    """
    def __init__(self, appWidth: constructorUnit, appHeight: constructorUnit, *flags, manualUpdating: bool = False) -> None:
        vars.aspectRatioObject = _AspectRatio()
        vars.appWidth, vars.appHeight = ScreenUnit.convertMultipleUnits(appWidth, appHeight)
        vars.appFlags = flags
        self.manualUpdating = manualUpdating
        self.clock = pygame.time.Clock()
        
        self.appEvents: pygame.event
        self.modifiableFunctions = {"quit": None}

        self.updatePending = False
        self.appFrameCounter = 0
        self.pageCounter = 0
        
        Display.set(appWidth, appHeight, *flags)
        
        self.minimumScreenWidth = None
        self.minimumScreenHeight = None
        
    def eventHandler(self, fps: float = 60):
        self.fps = fps
        self.clock.tick(fps)
        
        if self.isFirstFrame(): # reset when first page frame
            vars.mouseButtonsStatus = [False, False, False, False, False, False, False]
            vars.activeKeys = []
            vars.releasedKeys = []
            vars.clickedKeys = []
        
        # reset
        vars.windowResized = False
        
        vars.mouseFlank = [False, False, False, False, False, False, False]
        vars.clickedKeys = []
        vars.releasedKeys = []
        
        vars.widgetAlreadyPressed = False
        
        # * get all events
        self.appEvents = pygame.event.get()
        if not self.isFirstFrame():
            for event in self.appEvents:                
                if event.type == pygame.MOUSEBUTTONDOWN:  
                    vars.mouseFlank[event.button] = True
                    vars.mouseButtonsStatus[event.button] = True
                
                elif event.type == pygame.MOUSEBUTTONUP:
                    vars.mouseFlank[event.button] = True
                    vars.mouseButtonsStatus[event.button] = False
                
                elif event.type == pygame.KEYDOWN:
                    vars.activeKeys.append(event.key)
                    vars.clickedKeys.append(event.key)
                
                elif event.type == pygame.KEYUP:
                    index = vars.activeKeys.index(event.key)
                    vars.releasedKeys.append(vars.activeKeys.pop(index))
                    
                elif event.type == pygame.WINDOWRESIZED:
                    vars.windowResized = True
                    if vars.minimumScreenWidth != None or vars.minimumScreenHeight != None:
                        Display.checkForMinimumScreenSizeBreaches()
                    if vars.aspectRatioObject.aspectRatioActive:
                        vars.aspectRatioObject.updateAspectRatio()
                        
                elif event.type == pygame.QUIT:
                    if self.modifiableFunctions["quit"] == None:
                        pygame.quit()
                        sys.exit()
                    else:
                        self.modifiableFunctions["quit"]()
                                
                if event.type == pygame.MOUSEWHEEL:
                    vars.scrollValue = event.y
                else:
                    vars.scrollValue = 0
                    
        if not self.manualUpdating or self.updatePending or self.isFirstFrame() or vars.windowResized:
            Updating.updateDisplay()
            
        self.appFrameCounter += 1
        self.pageCounter += 1
        
    def isFirstFrame(self):
        return self.pageCounter < 2
            
    def setModifiableFunction(self, type: modifiableFunctions, function): 
        self.modifiableFunctions[type] = function
    
    def resetModifiableFunction(self, type: modifiableFunctions):
        self.modifiableFunctions[type] = None
        
    def everySecond(self):
        if self.appFrameCounter % self.fps == 0:
            return True
        return False
    
    def everyAmountOfTicks(self, everyAmountOfFrames: int):
        if self.appFrameCounter % everyAmountOfFrames == 0:
            return True
        return False
    
    def switchPage(self):
        self.pageCounter = 0
    
    def centerApp(self):
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        
    def isScreenResized(self):
        return vars.windowResized
    
    def fill(self, color: vars.RGBvalue):
        "does the same thing as `game.Display.fill()`"
        Display.fill(color)
        
    @property
    def getEvents(self):
        return self.appEvents
    
    @property
    def getFrameCounter(self):
        return self.appFrameCounter
    