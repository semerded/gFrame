from importer import pygame
import vars
from elements.colors import Color

class Draw:
    def rectangle(left: float, top: float, width: float, height: float, color: vars.RGBvalue = Color.LIGHT_GRAY, cornerRadius: int = -1):
        return pygame.draw.rect(vars.mainDisplay, color, pygame.Rect(left, top, width, height), border_radius=cornerRadius)
    
    def rectangleFromRect(rect: pygame.Rect, color: vars.RGBvalue = Color.LIGHT_GRAY, cornerRadius: int = -1):
        return Draw.rectangle(rect.x, rect.y, rect.width, rect.height, color, cornerRadius)
    
    def transparantRectangle(left: float, top: float, width: float, height: float, transparancy: int, color: vars.RGBvalue = Color.LIGHT_GRAY):
        rectangle = pygame.Surface((width, height))
        rectangle.set_alpha(transparancy)
        rectangle.fill(color)
        return vars.mainDisplay.blit(rectangle, (left, top))
        
    def transparantRectangleFromRect(rect: pygame.Rect, transparancy: int, color: vars.RGBvalue = Color.LIGHT_GRAY):
        return Draw.transparantRectangle(rect.x, rect.y, rect.width, rect.height, transparancy, color)
        
    def border(left: float, top: float, width: float, height: float, borderWidth: int, color: vars.RGBvalue = Color.BLACK, cornerRadius: int = -1) -> pygame.Rect:
        return pygame.draw.rect(vars.mainDisplay, color, pygame.Rect(left - borderWidth / 2, width - borderWidth - borderWidth / 2, width, height - borderWidth), width=borderWidth, border_radius=cornerRadius)
    
    def borderFromRect(rect: pygame.Rect, borderWidth: int, color: vars.RGBvalue = Color.BLACK, cornerRadius: int = -1):
        return Draw.border(rect.x, rect.y, rect.width, rect.height, borderWidth, color, cornerRadius)
    
    def pixel(left: vars.validScreenUnit, top: vars.validScreenUnit, color: vars.RGBvalue):
        return Draw.rectangle(left, top, 1, 1, color)
    
    def calculateInnerBorderRadius(outerBorderRadius, borderWidth):
        innerBorderRadius = (outerBorderRadius - borderWidth)
        return innerBorderRadius if innerBorderRadius > 0 else 0
    
    def pointInPolygon(point: list | tuple, polygon: list | tuple[list | tuple]) -> bool:
        num_vertices = len(polygon)
        x, y = point[0], point[1]

        inside = False
        p1 = polygon[0]

        for i in range(1, num_vertices + 1):
            p2 = polygon[i % num_vertices]
            if y > min(p1[1], p2[1]):
                if y <= max(p1[1], p2[1]):
                    if x <= max(p1[0], p2[0]):
                        x_intersection = (y - p1[1]) * (p2[0] - p1[0]) / (p2[1] - p1[1]) + p1[0]
                        if p1[0] == p2[0] or x <= x_intersection:
                            inside = not inside
            p1 = p2
        return inside
    