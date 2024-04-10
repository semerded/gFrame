from ..baseImporter import pygame
from ..elements.enums import mouseButton
from ..components.draw import Draw
from ..components.rect import Rect

from ..baseImporter import vars

class Interactions:
    #* mouse button 
    #private       
    def _posFlank(mouseButton: mouseButton):
        mouseButton = Interactions._checkIfInt(mouseButton)
        return vars.mouseFlank[mouseButton] and vars.mouseButtonsStatus[mouseButton]
    
    def _negFlank(mouseButton: mouseButton):
        mouseButton = Interactions._checkIfInt(mouseButton)
        return vars.mouseFlank[mouseButton] and not vars.mouseButtonsStatus[mouseButton]
    
    def _pressed(mouseButton: mouseButton):
        mouseButton = Interactions._checkIfInt(mouseButton)
        return vars.mouseButtonsStatus[mouseButton]
    
    def _checkIfInt(mouseButton: int | mouseButton):
        if type(mouseButton) == int:
            return mouseButton
        return mouseButton.value


    # area detection
    def isMouseOver(rect: Rect) -> bool:
        return rect.collidepoint(pygame.mouse.get_pos())
    
    def isMouseInArea(topCord: vars.coordinate, bottomCord: vars.coordinate) -> bool:
        size = (abs(bottomCord[0] - topCord[0]), abs(bottomCord[1] - topCord[1]))
        rect = Rect(topCord, size)
        return Interactions.isMouseOver(rect)
    
    def isMouseInPolygon(polygon: list | tuple [vars.coordinate]) -> bool:
        return Draw.pointInPolygon(pygame.mouse.get_pos(), polygon)
    
    def isMouseInCircle(center: vars.coordinate, radius: int) -> bool:
        return Draw.distanceBetweenPoints(center, pygame.mouse.get_pos()) < radius

    # click detection
    def isMouseClicked(mouseButton: mouseButton = mouseButton.leftMouseButton) -> bool:
        return Interactions._posFlank(mouseButton)
    
    def isMouseClickedInRect(rect: Rect, mouseButton: mouseButton = mouseButton.leftMouseButton) -> bool:
        return Interactions.isMouseOver(rect) and Interactions.isMouseClicked(mouseButton)
    
    def isMouseClickedInPolygon(polygon: list | tuple [list | tuple], mouseButton: mouseButton = mouseButton.leftMouseButton) -> bool:
        return Interactions.isMouseInPolygon(polygon) and Interactions.isMouseClicked(mouseButton)
    
    def isMouseClickedInCircle(center: vars.coordinate, radius: int, mouseButton: mouseButton = mouseButton.leftMouseButton) -> bool:
        return Interactions.isMouseInCircle(center, radius) and Interactions.isMouseClicked(mouseButton)
    
    #? not variations
    def isMouseClickedNotInRect(rect: Rect, mouseButton: mouseButton = mouseButton.leftMouseButton) -> bool:
        return not Interactions.isMouseOver(rect) and Interactions.isMouseClicked(mouseButton)
    
    def isMouseClickedNotInPolygon(polygon: list | tuple [list | tuple], mouseButton: mouseButton = mouseButton.leftMouseButton) -> bool:
        return not Interactions.isMouseInPolygon(polygon) and Interactions.isMouseClicked(mouseButton)
    
    def isMouseClickedNotInCircle(center: vars.coordinate, radius: int, mouseButton: mouseButton = mouseButton.leftMouseButton) -> bool:
        return not Interactions.isMouseInCircle(center, radius) and Interactions.isMouseClicked(mouseButton)

    # release detection
    def isMouseReleased(mouseButton: mouseButton = mouseButton.leftMouseButton) -> bool:
        return Interactions._negFlank(mouseButton)
    
    def isMouseReleasedInRect(rect: Rect, mouseButton: mouseButton = mouseButton.leftMouseButton) -> bool:
        return Interactions.isMouseOver(rect) and Interactions.isMouseReleased(mouseButton)
    
    def isMouseReleasedInPolygon(polygon: list | tuple [list | tuple], mouseButton: mouseButton = mouseButton.leftMouseButton) -> bool:
        return Interactions.isMouseInPolygon(polygon) and Interactions.isMouseReleased(mouseButton)
    
    def isMouseReleasedInCircle(center: vars.coordinate, radius: int, mouseButton: mouseButton = mouseButton.leftMouseButton) -> bool: 
        return Interactions.isMouseInCircle(center, radius) and Interactions.isMouseReleased(mouseButton)
    
    #? not variations
    def isMouseReleasedNotInRect(rect: Rect, mouseButton: mouseButton = mouseButton.leftMouseButton) -> bool:
        return not Interactions.isMouseOver(rect) and Interactions.isMouseReleased(mouseButton)
    
    def isMouseReleasedNotInPolygon(polygon: list | tuple [list | tuple], mouseButton: mouseButton = mouseButton.leftMouseButton) -> bool:
        return not Interactions.isMouseInPolygon(polygon) and Interactions.isMouseReleased(mouseButton)
    
    def isMouseReleasedNotInCircle(center: vars.coordinate, radius: int, mouseButton: mouseButton = mouseButton.leftMouseButton) -> bool: 
        return not Interactions.isMouseInCircle(center, radius) and Interactions.isMouseReleased(mouseButton)

    
    # hold detection
    def isMousePressing(mouseButton: mouseButton = mouseButton.leftMouseButton):
        return Interactions._pressed(mouseButton)
    
    def isMousePressingInRect(rect: Rect, mouseButton: mouseButton = mouseButton.leftMouseButton):
        return Interactions.isMouseOver(rect) and Interactions.isMousePressing(mouseButton)
    
    def isMousePressingInPolygon(polygon: list | tuple [list | tuple], mouseButton: mouseButton = mouseButton.leftMouseButton):
        return Interactions.isMouseInPolygon(polygon) and Interactions.isMousePressing(mouseButton)
    
    def isMousePressingInCircle(center: vars.coordinate, radius: int, mouseButton: mouseButton = mouseButton.leftMouseButton) -> bool:
        return Interactions.isMouseInCircle(center, radius) and Interactions.isMousePressing(mouseButton)
    
    #? not variations
    def isMousePressingNotInRect(rect: Rect, mouseButton: mouseButton = mouseButton.leftMouseButton):
        return not Interactions.isMouseOver(rect) and Interactions._pressed(mouseButton)
    
    def isMousePressingNotInPolygon(polygon: list | tuple [list | tuple], mouseButton: mouseButton = mouseButton.leftMouseButton):
        return not Interactions.isMouseInPolygon(polygon) and Interactions.isMousePressing(mouseButton)
    
    def isMousePressingNotInCircle(center: vars.coordinate, radius: int, mouseButton: mouseButton = mouseButton.leftMouseButton) -> bool:
        return not Interactions.isMouseInCircle(center, radius) and Interactions.isMousePressing(mouseButton)
        
        
    # scrolling detection
    def isScrolledUp():
        return Interactions._pressed(mouseButton.scrollUp)
    
    def isScrolledDown():
        return Interactions._pressed(mouseButton.scrollDown)
    
    def isScrolled():
        return Interactions._pressed(mouseButton.scrollUp) or Interactions._pressed(mouseButton.scrollDown)
    
    
    # keyboard
    def isKeyClicked(key: int):
        return key in vars.clickedKeys
    
    def isKeyReleased(key: int):
        return key in vars.releasedKeys
    
    def isKeyPressing(key: int):
        return key in vars.activeKeys
    
    # other
    def rectInRect(masterRect: Rect, childRect: Rect):
        return masterRect.colliderect(childRect)
    
    