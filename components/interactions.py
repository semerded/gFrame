from importer import pygame
from elements.enums import mouseButton
from components.draw import Draw
from components.rect import Rect

import vars

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
    
    def isMouseInArea(topCord: int, bottomCord: int) -> bool:
        rect = Rect(topCord, bottomCord)
        return Interactions.isMouseOver(rect)
    
    def isMouseInPolygon(polygon: list | tuple [vars.coordinate]) -> bool:
        return Draw.pointInPolygon(pygame.mouse.get_pos(), polygon)
    
    def isMouseInCircle(center: vars.coordinate, radius: int) -> bool:
        return Draw.distanceBetweenPoints(center, pygame.mouse.get_pos()) < radius

    # click detection
    def isMouseClicked(mouseButton: mouseButton) -> bool:
        return Interactions._posFlank(mouseButton)
    
    def isMouseClickedInRect(mouseButton: mouseButton, rect: Rect) -> bool:
        return Interactions.isMouseOver(rect) and Interactions.isMouseClicked(mouseButton)
    
    def isMouseClickedInPolygon(mouseButton: mouseButton, polygon: list | tuple [list | tuple]) -> bool:
        return Interactions.isMouseInPolygon(polygon) and Interactions.isMouseClicked(mouseButton)
    
    def isMouseClickedInCircle(mouseButton: mouseButton, center: vars.coordinate, radius: int) -> bool:
        return Interactions.isMouseInCircle(center, radius) and Interactions.isMouseClicked(mouseButton)

    # release detection
    def isMouseReleased(mouseButton: mouseButton) -> bool:
        return Interactions._negFlank(mouseButton)
    
    def isMouseReleasedInRect(mouseButton: mouseButton, rect: Rect) -> bool:
        return Interactions.isMouseOver(rect) and Interactions.isMouseReleasedeased(mouseButton)
    
    def isMouseReleasedInPolygon(mouseButton: mouseButton, polygon: list | tuple [list | tuple]) -> bool:
        return Interactions.isMouseInPolygon(polygon) and Interactions.isMouseReleased(mouseButton)
    
    def isMouseReleasedInCircle(mouseButton: mouseButton, center: vars.coordinate, radius: int) -> bool: 
        return Interactions.isMouseInCircle(center, radius) and Interactions.isMouseReleased(mouseButton)

    
    # hold detection
    def isMousePressing(mouseButton: mouseButton):
        return Interactions._pressed(mouseButton)
    
    def isMousePressingInRect(mouseButton: mouseButton, rect: Rect):
        return Interactions.isMouseOver(rect) and Interactions._pressed(mouseButton)
    
    def isMousePressingInPolygon(mouseButton: mouseButton, polygon: list | tuple [list | tuple]):
        return Interactions.isMouseInPolygon(polygon) and Interactions.isMousePressing(mouseButton)
    
    def isMousePressingInCircle(mouseButton: mouseButton, center: vars.coordinate, radius: int) -> bool:
        return Interactions.isMouseInCircle(center, radius) and Interactions.isMousePressing(mouseButton)
        
        
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
    
    