from importer import pygame
from components.display import Display
from components.updating import Updating
from components.aspectRatio import _AspectRatio
from elements.enums import axis
from typing_extensions import TypeAlias, Literal
import vars, sys, os

modifiableFunctions: TypeAlias = Literal[
    "quit",
    "test"
]

class AppConstructor:
    """
    the appConstructor initializes the game display\n
    it main purpose is to do every action within the `eventhandler` function
    """
    def __init__(self, appWidth: vars.validScreenUnit, appHeight: vars.validScreenUnit, *flags, manualUpdating: bool = False) -> None:
        vars.aspectRatioObject = _AspectRatio()
        vars.appWidth = appWidth
        vars.appHeight = appHeight
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
        
        # reset
        vars.windowResized = False
        
        vars.mouseFlank = [False, False, False, False, False, False, False]
        vars.clickedKeys = []
        vars.releasedKeys = []
        
        # * get all events
        self.appEvents = pygame.event.get()
        for event in self.appEvents:
            if event.type == pygame.QUIT:
                if self.modifiableFunctions["quit"] == None:
                    pygame.quit()
                    sys.exit()
                else:
                    self.modifiableFunctions["quit"]()
            
            elif event.type == pygame.WINDOWRESIZED:
                vars.windowResized = True
                if vars.minimumScreenWidth != None or vars.minimumScreenHeight != None:
                    Display.checkForMinimumScreenSizeBreaches()
                if vars.aspectRatioObject.aspectRatioActive:
                    vars.aspectRatioObject.updateAspectRatio()
            
            elif event.type == pygame.KEYDOWN:  
                vars.mouseFlank[event.button] = True
                vars.mouseButtonsStatus[event.button] = True
            
            elif event.type == pygame.KEYUP:
                vars.mouseFlank[event.button] = True
                vars.mouseButtonsStatus[event.button] = False
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                vars.activeKeys.append(event.key)
                vars.clickedKeys.append(event.key)
            
            elif event.type == pygame.MOUSEBUTTONUP:
                index = vars.activeKeys.index(event.button)
                vars.releasedKeys.append(vars.activeKeys.pop(index))
                            
            if event.type == pygame.MOUSEWHEEL:
                vars.scrollValue = event.y
            else:
                vars.scrollValue = 0
                
        if not self.manualUpdating or self.updatePending or self.pageCounter < 2 or vars.windowResized:
            Updating.updateDisplay()
            
        self.appFrameCounter += 1
        self.pageCounter += 1
            
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
        
    @property
    def getEvents(self):
        return self.appEvents
    
    @property
    def getFrameCounter(self):
        return self.appFrameCounter
    