from importer import pygame
from elements.fonts import *
from elements.enums import overFlow, mouseButton
from elements.colors import Color
import vars
from components.interactions import Interactions
from components.screenUnits import ScreenUnit

class Text:
    def __init__(self, font: pygame.font, color: vars.RGBvalue) -> None:
        self.font = font
        self.textColor = color
        self.hoveringUp = True
        self.hoverDistance = 0
        self.position = [0, 0]
        self._antiAllias = True

    
    # static
    def textOverflow(text: str, font: pygame.font, maxWidth: int | float, overFlowType: overFlow = overFlow.ellipsis) -> str:
        if font.size(text)[0] < maxWidth:
            return text
        
        if overFlowType == overFlow.show:
            return text
        elif overFlowType == overFlow.ellipsis:
            ellipsisWidth = font.size("...")[0]
            maxWidth -= ellipsisWidth - ellipsisWidth / 3
            overFlowTrailing = "..."
        else:
            overFlowTrailing = ""
            
        newText = ""
        textWidth = 0
        for letter in text:
            textWidth += font.size(letter)[0]
            if textWidth < maxWidth - 10:
                newText += letter
            else:
                return newText.strip() + overFlowTrailing
        return text

    def simpleText( position: tuple[int,int], text: str, font: pygame.font = Font.H3, color: vars.RGBvalue = Color.BLACK, antiAllias: bool = True):
        textsurface = font.render(f"{text}", antiAllias, color)       
        vars.mainDisplay.blit(textsurface, (position[0], position[1]))
        return textsurface

    def centerTextInRect(textSurface: pygame.Surface, rect: pygame.Rect) -> tuple[float, float]:
        xPos = rect.x + (rect.width / 2) - (textSurface.get_width() / 2)
        yPos = rect.y + (rect.height / 2) - (textSurface.get_height() / 2)
        return xPos, yPos
        
    # instance
    def renderText(self, text):
        self.textSurface = self.font.render(text, self._antiAllias, self.textColor)
        
    def antiAllias(self, antiAllias: bool):
        self._antiAllias = antiAllias

        
    def color(self, textColor: vars.RGBvalue = None, backgroundColor: vars.RGBvalue = None, borderColor: vars.RGBvalue = None):
        if textColor != None:
            self.textColor = textColor
        if backgroundColor != None:
            self.backgroundColor = backgroundColor
        if borderColor != None:
            self.borderColor = borderColor
        
    def place(self, text: str, position):
        self.renderText(text)
        self.position = position
        vars.mainDisplay.blit(self.textSurface, (position[0], position[1]))
        
    def centerTextInScreen(self, text):
        self.renderText(text)
        vars.mainDisplay.blit(self.textSurface, (ScreenUnit.vw(50) - self.textSurface.get_width() / 2, ScreenUnit.vh(50) - self.textSurface.get_height() / 2))
    
    def placeInRect(self, text: str, rect: pygame.Rect | tuple[float, float, float, float]):
        self.renderText(text)
        xCord = rect.centerx - (self.textSurface.get_width() / 2)
        yCord = rect.centery - (self.textSurface.get_height() / 2)
        self.position = [xCord, yCord]
        vars.mainDisplay.blit(self.textSurface, (xCord, yCord))
        
    def onMouseClick(self, mouseButton: mouseButton = mouseButton.leftMouseButton):
        if Interactions.onMouseClickInRect(self.getRect, mouseButton):
            return True
        return False

    
    def hover(self, text, rect: pygame.Rect, hoverDistance: int):
        if self.hoveringUp:
            self.hoverDistance += 1
        else:
            self.hoverDistance -= 1
        if self.hoverDistance > hoverDistance / 2:
            self.hoveringUp = False
        if self.hoverDistance < -hoverDistance / 2:
            self.hoveringUp = True
        rect = pygame.Rect(rect.left, rect.top, rect.width, rect.height + self.hoverDistance)
        self.placeInRect(text, rect)
        
    @property
    def getRect(self):
        textRect = self.textSurface.get_rect()
        return pygame.Rect(self.position[0], self.position[1], textRect[2], textRect[3])
