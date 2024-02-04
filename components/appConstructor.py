from importer import pygame
from components.interactions import Interactions
from components.updating import Updating
from elements.enums import axis
import vars, sys, os

class AppConstructor():
    def __init__(self, screenWidth, screenHeight, *flags, manualUpdating: bool = False) -> None:
        self.screenWidth = vars.displayInfo.current_w
        self.screenHeight = vars.displayInfo.current_h
        self.APPdisplayFlags = flags
        self.manualUpdating = manualUpdating
        self.frameCounter = 0
        self.updatePending = True
        self.clock = pygame.time.Clock()
        
        vars.appScreenWidth = self.screenWidth
        vars.appScreenHeight = self.screenHeight
        
        self.minimumScreenWidth = None
        self.minimumScreenHeight = None
        self.modifiedFunctions = {"quit": None}

        self.APPdisplay = pygame.display.set_mode(
            (screenWidth, screenHeight), *flags)
        vars.mainDisplay = self.APPdisplay
        
        self.resetFlank = False
        self.screenSizeUpdated = False
        self.aspectRatioActive = False
        
    def eventHandler(self, appEvents: pygame.event, fps: float = 60):
        global appScreenWidth, appScreenHeight, scrollValue
        self.fps = fps
        self.clock.tick(fps)
        
        if not self.manualUpdating:
            Updating.updateDisplay()
        elif self.updatePending:
            Updating.updateDisplay()
            self.updatePending = False
        elif self.frameCounter < 2:
            Updating.updateDisplay()
        
        if self.resetFlank:
            Interactions.resetPreviousMouseButtonStatus()
            self.resetFlank = False
            
        self.appEvents = appEvents
        for event in self.appEvents:
            if event.type == pygame.QUIT:
                if self.modifiedFunctions["quit"] == None:
                    pygame.quit()
                    sys.exit()
                else:
                    self.modifiedFunctions["quit"]()

            elif event.type == pygame.WINDOWRESIZED:
                appScreenWidth, appScreenHeight = self.getAppScreenDimensions
                if self.minimumScreenWidth != None and self.minimumScreenHeight != None:
                    self.checkForMinimumScreenSizeBreaches()
                if self.aspectRatioActive and self.getAppScreenDimensions[0] != vars.userScreenWidth:
                    self.updateAspectRatio()
                self.updatePending = True
                

            elif event.type == pygame.MOUSEBUTTONDOWN:
                vars.mouseButtonsStatus[event.button] = True
                Interactions._mouseButtonPositiveFlank(event.button)
                self.resetFlank = True

            elif event.type == pygame.MOUSEBUTTONUP:
                vars.mouseButtonsStatus[event.button] = False
                Interactions._mouseButtonNegativeFlank(event.button)
                self.resetFlank = True
            
            if event.type == pygame.MOUSEWHEEL:
                scrollValue = event.y
            else:
                scrollValue = 0
            
        self.frameCounter += 1
        
    def everySecond(self):
        if self.frameCounter % self.fps == 0:
            return True
        return False
    
    def everyAmountOfTicks(self, everyAmountOfFrames: int):
        if self.frameCounter % everyAmountOfFrames == 0:
            return True
        return False
    
    def resizeAppscreen(self, screenWidth, screenHeight, *flags):
        self.APPdisplayFlags = flags
        self.APPdisplay = pygame.display.set_mode(
            (screenWidth, screenHeight), *flags)
        self.__updateDispalyDimensions()
        
    def keyboardClick(self, *keys: int): # TODO find more optimal method to do this
        for event in self.getEvents:
            if event.type == pygame.KEYDOWN:
                for key in keys:
                    if event.key == key:
                        return True
        return False
        
    def keyboardRelease(self, key: int): # same as above
        for event in self.getEvents:
            if event.type == pygame.KEYUP:
                if event.key == key:
                    return True
        return False

    # def setModifiableFunctions(self, **kwargs: vars.modifiableFunctions):  # TODO finish this function
    #     for modifiedFunction, newFunction in kwargs.items():
    #         self.modifiedFunctions[modifiedFunction] = newFunction

    def setMinimumScreenDimensions(self, minimumScreenWidth: vars.validScreenUnit = None, minimumScreenHeight: vars.validScreenUnit = None):
        if minimumScreenWidth != None:
            self.minimumScreenWidth = minimumScreenWidth
        else:
            self.minimumScreenWidth = None
        if minimumScreenHeight != None:
            self.minimumScreenHeight = minimumScreenHeight
        else:
            self.minimumScreenHeight = None
            
    def setAspectratio(self, aspectRatio: int | float, width: int | None = None, height: int | None = None):
        """
        calculates the aspect ratio from the width or height and resizes the screen to that size\n
        when no size is givin, the size will be calculated from the current width of the screen\n
        when 2 sizes are givin, the size from the givin width will be used\n
        use the function 'ScreenUnit.aspectRatio' to get the aspect ratio
        """
        self.aspectRatioActive = True
        self.aspectRatio = aspectRatio
        self.__checkAspectRatioAxis(width, height)
        
        if width == None and height == None:
            width = self.getAppScreenDimensions[0]
        width, height = self.__calculateAspectRatioAxis(width, height)
        self.resizeAppscreen(width, height, *self.APPdisplayFlags)
        
    def updateAspectRatio(self):
        if self.aspectRatioAxis == axis.x:
            width = self.getAppScreenDimensions[0]
            height = 0
        else:
            height = self.getAppScreenDimensions[1]
            width = 0
        width, height = self.__calculateAspectRatioAxis(width, height)
        self.resizeAppscreen(width, height, *self.APPdisplayFlags)
            
    def __calculateAspectRatioAxis(self, width, height):
        if self.aspectRatioAxis == axis.x:
            height = width / self.aspectRatio
        else:
            width = height * self.aspectRatio
        return width, height            
        
    def updateAspectRatioAxis(self, newAxis: axis):
        self.aspectRatioAxis = newAxis    
        
    def disableAspectRatio(self):
        self.aspectRatioActive = False
        
    def __checkAspectRatioAxis(self, width, height):
        if width == None and height != None:
            self.aspectRatioAxis = axis.y
        else:
            self.aspectRatioAxis = axis.x
    
    def __updateDispalyDimensions(self):
        global mainDisplay, appScreenWidth, appScreenHeight
        mainDisplay = self.APPdisplay
        appScreenWidth, appScreenHeight = self.getAppScreenDimensions
            
    def isScreenResized(self):
        if self.screenSizeUpdated:
            self.screenSizeUpdated = False
            return True
        return False
    
    def switchScreen(self):
        self.frameCounter = 0
        self.requestUpdate
        
    def centerApp(self):
        os.environ['SDL_VIDEO_CENTERED'] = '1'

    def checkForMinimumScreenSizeBreaches(self):
        w, h = self.getAppScreenDimensions
        updateScreen = False
        if w < self.minimumScreenWidth:
            w = self.minimumScreenWidth
            updateScreen = True
        if h < self.minimumScreenHeight:
            h = self.minimumScreenHeight
            updateScreen = True
        if updateScreen:
            self.resizeAppscreen(w, h, *self.APPdisplayFlags)
            
    def updateDisplay(self):
        Updating.updateDisplay()
        
    def firstFrame(self): # TODO get rid of this func and make a general updating func
        if self.getFrameCounter < 2:
            return True
        return False

    @property
    def setRelativeFullscreen(self):
        self.APPdisplay = pygame.display.set_mode(
            (self.screenWidth, self.screenHeight), *self.APPdisplayFlags)
        self.setModifiableFunctions()

    @property
    def getAppScreenDimensions(self):
        displayInfo = pygame.display.Info()
        return displayInfo.current_w, displayInfo.current_h

    @property
    def getdisplayDimensions(self):
        return (self.screenWidth, self.screenHeight)
    
    @property
    def getFrameCounter(self):
        return self.frameCounter

    @property
    def maindisplay(self) -> pygame.surface.Surface:
        """pygame main surface"""
        return self.APPdisplay
    
    @property
    def requestUpdate(self):
        self.updatePending = True
        
    @property
    def updateAvalible(self):
        return self.updatePending
    
    @property
    def getEvents(self):
        return self.appEvents
        