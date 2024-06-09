from .. import data
from ..core.clock import Clock
from ..core.renderQueue import RenderQueue
import pygame, sys

clock = Clock(data.frameRate)

default = None

def eventHandler(backgroundColor = default, fps = default):
    if data.autoUpdate or data.fullScreenUpdatePending:
        RenderQueue.renderAllFromQueue()
        data.mainDisplay.blit(data.canvas, (0, 0))
        pygame.display.flip()
        
        #* make a blank canvas
        
        data.canvas.fill(data.backgroundColor if backgroundColor == None else backgroundColor)
    
    # new frame
    clock.sleep(data.frameRate if fps == None else fps)
    
    if data.reloadScreen:
        data.mouseButtonsStatus = [False, False, False, False, False, False, False]
        data.activeKeys = []
        data.releasedKeys = []
        data.clickedKeys = []
        
    data.mouseFlank = [False, False, False, False, False, False, False]
    data.fullScreenUpdatePending = False
    
    #* get all events
    _pygameEventHandler()
    
    #* update WCU
    _constantUpdateHandler()
    
    
def drawables():
    return True
    
def _constantUpdateHandler():
    for constantUpdatables in data.widgetConstantUpdates.values():
        for constantUpdatable in constantUpdatables:
            constantUpdatable()
    
def _pygameEventHandler():
    data.appEvents = pygame.event.get()
    if not data.reloadScreen:
        for event in data.appEvents:
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                data.mouseFlank[event.button] = True
                data.mouseButtonsStatus[event.button] = True
            
            elif event.type == pygame.MOUSEBUTTONUP:
                data.mouseFlank[event.button] = True
                data.mouseButtonsStatus[event.button] = False
                
            elif event.type == pygame.KEYDOWN:
                data.activeKeys.append(event.key)
                data.clickedKeys.append(event.key)
                
            elif event.type == pygame.KEYUP:
                try:
                    index = data.activeKeys.index(event.key)
                    data.releasedKeys.append(data.activeKeys.pop(index))
                except KeyError:
                    pass
                
            elif event.type == pygame.WINDOWRESIZED:
                pass
            
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.MOUSEWHEEL:
                data.scrollValue = (event.x, event.y)
            else:
                data.scrollValue = (0, 0)