from importer import pygame
from elements.enums import mouseButton
from components.display import Display
import vars

class Interactions:
    # mouse button        
    def resetPreviousMouseButtonStatus():
        vars.previousMouseButtonStatus = []
        for _ in range(len(mouseButton)):
            vars.previousMouseButtonStatus.append(False)

    def _isMouseButtonPressed(mouseButton: mouseButton):
        mouseButton = Interactions._checkIfInt(mouseButton)
        if vars.mouseButtonsStatus[mouseButton]:
            return True
        return False

    def _mouseButtonPositiveFlank(mouseButton: mouseButton):
        mouseButton = Interactions._checkIfInt(mouseButton)
        if vars.mouseButtonsStatus[mouseButton] and not vars.previousMouseButtonStatus[mouseButton]:
            vars.previousMouseButtonStatus[mouseButton] = True
            return True
        return False

    def _mouseButtonNegativeFlank(mouseButton: mouseButton):
        mouseButton = Interactions._checkIfInt(mouseButton)
        if not vars.mouseButtonsStatus[mouseButton] and vars.previousMouseButtonStatus[mouseButton]:
            vars.previousMouseButtonStatus[mouseButton] = True
            return True
        return False
    
    def _checkIfInt(mouseButton: int | mouseButton):
        if type(mouseButton) == int:
            return mouseButton
        return mouseButton.value

    def onMouseOver(rect: pygame.Rect):
        return rect.collidepoint(pygame.mouse.get_pos())
    
    def isMouseInArea(topCord: int, bottomCord: int):
        rect = pygame.Rect(topCord, bottomCord)
        return Interactions.onMouseOver(rect)
    
    def isMouseInPolygon(polygon: list | tuple [list | tuple]) -> bool:
        return Display.pointInPolygon(pygame.mouse.get_pos(), polygon)

    def onMouseClick(mouseButton: mouseButton) -> bool:
        return Interactions._mouseButtonPositiveFlank(mouseButton)
    
    def onMouseClickInRect(rect: pygame.Rect, mouseButton: mouseButton):
        return Interactions.onMouseOver(rect) and Interactions.onMouseClick(mouseButton)
    
    def onMouseClickInPolygon(polygon: list | tuple [list | tuple], mouseButton: mouseButton) -> bool:
        return Interactions.isMouseInPolygon(polygon) and Interactions.onMouseClick(mouseButton)

    def isReleased(mouseButton: mouseButton):
        return Interactions._mouseButtonNegativeFlank(mouseButton)
    
    def isReleasedInRect(rect: pygame.Rect, mouseButton: mouseButton):
        return Interactions.onMouseOver(rect) and Interactions.isReleased(mouseButton)
    
    def onMouseHold(mouseButton: mouseButton):
        return Interactions._isMouseButtonPressed(mouseButton)
    
    def onMouseHoldInRect(rect: pygame.Rect, mouseButton: mouseButton):
        return Interactions.onMouseOver(rect) and Interactions._isMouseButtonPressed(mouseButton)
    
    # scrolling
    def isScrolledUp():
        return Interactions._isMouseButtonPressed(mouseButton.scrollUp)
    
    def isScrolledDown():
        return Interactions._isMouseButtonPressed(mouseButton.scrollDown)
    
    def isScrolled():
        return Interactions._isMouseButtonPressed(mouseButton.scrollUp) or Interactions._isMouseButtonPressed(mouseButton.scrollDown)
    
    # keyboard
    
    
    # other
    def rectInRect(masterRect: pygame.Rect, childRect: pygame.Rect):
        return masterRect.colliderect(childRect)
    