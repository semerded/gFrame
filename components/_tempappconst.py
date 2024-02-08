from importer import pygame
from components.interactions import Interactions
from components.updating import Updating
from components.display import Display
from elements.enums import axis
import vars, sys, os

class AppConstructor:
    def __init__(self, appWidth: vars.validScreenUnit, appHeight: vars.validScreenUnit, *flags, manualUpdating: bool = False) -> None:
        vars.appWidth = appWidth
        vars.appHeight = appHeight
        vars.appFlags = flags
        self.manualUpdating = manualUpdating
        self.clock = pygame.time.Clock()
        
        self.appEvents: pygame.event
                
        self.updatePending = False
        self.appFrameCounter = 0
        self.pageCounter = 0
        
        Display.set(appWidth, appHeight, *flags)
        
        self.minimumScreenWidth = None
        self.minimumScreenHeight = None
        
    def eventHandler(self, fps: float = 60):
        self.clock.tick(fps)
        
        if not self.manualUpdating or self.updatePending or self.pageCounter < 2:
            Updating.updateDisplay()
            
        for event in self.appEvents:
            if event.type == pygame.QUIT:
                pass
            
            elif event.type == pygame.WINDOWRESIZED:
                pass
            
            elif event.type == pygame.KEYDOWN:
                pass
            
            elif event.type == pygame.KEYUP:
                pass
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pass
            
            elif event.type == pygame.MOUSEBUTTONUP:
                pass
            
            if event.type == pygame.MOUSEWHEEL:
                vars.scrollValue = event.y
            else:
                vars.scrollValue = 0
                
        self.appFrameCounter += 1
        self.pageCounter += 1
            
            
            
    def everySecond(self):
        pass
    
    def everyAmountOfTicks(self):
        pass
    

        
    