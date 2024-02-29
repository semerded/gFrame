from importer import pygame
import vars
from elements.colors import Color
from components.screenUnits import ScreenUnit
from math import sqrt

class Draw:
    def rectangle(left: float, top: float, width: float, height: float, color: vars.RGBvalue = Color.LIGHT_GRAY, cornerRadius: int = -1):
        left, top, width, height, cornerRadius = ScreenUnit.convertMultipleUnits(left, top, width, height, cornerRadius)
        return pygame.draw.rect(vars.mainDisplay, color, pygame.Rect(left, top, width, height), border_radius=int(cornerRadius))
    
    def rectangleFromRect(rect: pygame.Rect, color: vars.RGBvalue = Color.LIGHT_GRAY, cornerRadius: int = -1):
        return Draw.rectangle(rect.x, rect.y, rect.width, rect.height, color, cornerRadius)
    
    def transparantRectangle(left: float, top: float, width: float, height: float, transparancy: int, color: vars.RGBvalue = Color.LIGHT_GRAY):
        left, top, width, height = ScreenUnit.convertMultipleUnits(left, top, width, height)
        rectangle = pygame.Surface((width, height))
        rectangle.set_alpha(transparancy)
        rectangle.fill(color)
        return vars.mainDisplay.blit(rectangle, (left, top))
        
    def transparantRectangleFromRect(rect: pygame.Rect, transparancy: int, color: vars.RGBvalue = Color.LIGHT_GRAY):
        return Draw.transparantRectangle(rect.x, rect.y, rect.width, rect.height, transparancy, color)
        
    def border(left: float, top: float, width: float, height: float, borderWidth: int, color: vars.RGBvalue = Color.BLACK, cornerRadius: int = -1) -> pygame.Rect:
        left, top, width, height, cornerRadius = ScreenUnit.convertMultipleUnits(left, top, width, height, cornerRadius)
        return pygame.draw.rect(vars.mainDisplay, color, pygame.Rect(left - borderWidth / 2, top - borderWidth / 2, width + borderWidth, height + borderWidth), width=int(borderWidth), border_radius=int(cornerRadius))
    
    def borderFromRect(rect: pygame.Rect, borderWidth: int, color: vars.RGBvalue = Color.BLACK, cornerRadius: int = -1):
        return Draw.border(rect.x, rect.y, rect.width, rect.height, borderWidth, color, cornerRadius)
    
    def pixel(left: vars.validScreenUnit, top: vars.validScreenUnit, color: vars.RGBvalue):
        left, top = ScreenUnit.convertMultipleUnits(left, top)
        return Draw.rectangle(left, top, 1, 1, color)
    
    def calculateOuterBorderRadius(outerBorderRadius, borderWidth):
        outerBorderRadius, borderWidth = ScreenUnit.convertMultipleUnits(outerBorderRadius, borderWidth)
        return outerBorderRadius + borderWidth
    
    def pointInPolygon(point: list | tuple, polygon: list | tuple[list | tuple]) -> bool:
        num_vertices = len(polygon)
        x, y = ScreenUnit.convertMultipleUnits(*point)

        inside = False
        p1 = ScreenUnit.checkIfValidScreenUnit(polygon[0])

        for i in range(1, num_vertices + 1):
            p2 = ScreenUnit.checkIfValidScreenUnit(polygon[i % num_vertices])
            if y > min(p1[1], p2[1]):
                if y <= max(p1[1], p2[1]):
                    if x <= max(p1[0], p2[0]):
                        x_intersection = (y - p1[1]) * (p2[0] - p1[0]) / (p2[1] - p1[1]) + p1[0]
                        if p1[0] == p2[0] or x <= x_intersection:
                            inside = not inside
            p1 = p2
        return inside
    
    def distanceBetweenPoints(point1: tuple[int], point2: tuple[int]):
        return sqrt((point1[1] - point1[0]) ** 2 + (point2[1] - point2[0]) ** 2)
