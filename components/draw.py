from importer import pygame
import vars
from elements.colors import Color

class Draw:
    def rectangle(xPosition: float, yPosition: float, width: float, height: float, color: vars.RGBvalue = Color.LIGHT_GRAY, cornerRadius: int = -1):
        return pygame.draw.rect(vars.mainDisplay, color, pygame.Rect(xPosition, yPosition, width, height), border_radius=cornerRadius)
    
    def rectangleFromRect(rect: pygame.Rect, color: vars.RGBvalue = Color.LIGHT_GRAY, cornerRadius: int = -1):
        return pygame.draw.rect(vars.mainDisplay, color, rect, border_radius=cornerRadius)
    
    def transparantRectangle(xPosition: float, yPosition: float, width: float, height: float, transparancy: int, color: vars.RGBvalue = Color.LIGHT_GRAY):
        rectangle = pygame.Surface((width, height))
        rectangle.set_alpha(transparancy)
        rectangle.fill(color)
        vars.mainDisplay.blit(rectangle, (xPosition, yPosition))
        
    def transparantRectangleFromRect(rect: pygame.Rect, transparancy: int, color: vars.RGBvalue = Color.LIGHT_GRAY):
        rectangle = pygame.Surface((rect.width, rect.height))
        rectangle.set_alpha(transparancy)
        rectangle.fill(color)
        vars.mainDisplay.blit(rectangle, (rect.x, rect.y))
        
    def border(borderWidth: int, rectValue: pygame.Rect | tuple[float, float, float, float], color: vars.RGBvalue = Color.BLACK, cornerRadius: int = -1) -> pygame.Rect:
        if isinstance(rectValue, pygame.Rect):
            xPosition = rectValue.x - borderWidth / 2
            yPosition = rectValue.y - borderWidth / 2
            width = rectValue.width + borderWidth
            height = rectValue.height + borderWidth
        else:
            xPosition = rectValue[0] - borderWidth / 2
            yPosition = rectValue[1] - borderWidth / 2
            width = rectValue[2] - borderWidth
            height = rectValue[3] - borderWidth
        return pygame.draw.rect(vars.mainDisplay, color, pygame.Rect(xPosition, yPosition, width, height), width=borderWidth, border_radius=cornerRadius)
    
    def calculateInnerBorderRadius(outerBorderRadius, borderWidth):
        innerBorderRadius = (outerBorderRadius - borderWidth)
        return innerBorderRadius if innerBorderRadius > 0 else 0
    