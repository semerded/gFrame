from ..baseImporter import pygame, vars
from ..components.rect import Rect
from ..elements.colors import Color
from ..components.screenUnits import ScreenUnit
from math import sqrt

class Draw:
    @staticmethod
    def rectangle(left: float, top: float, width: float, height: float, color: vars.RGBvalue = Color.LIGHT_GRAY, cornerRadius: int = -1):
        left, top, width, height, cornerRadius = ScreenUnit.convertMultipleUnits(left, top, width, height, cornerRadius)
        return pygame.draw.rect(vars.mainDisplay, color, Rect(left, top, width, height), border_radius=int(cornerRadius))
    
    @staticmethod
    def rectangleFromRect(rect: Rect, color: vars.RGBvalue = Color.LIGHT_GRAY, cornerRadius: int = -1):
        return Draw.rectangle(rect.x, rect.y, rect.width, rect.height, color, cornerRadius)
    
    @staticmethod
    def transparantRectangle(left: float, top: float, width: float, height: float, transparancy: int, color: vars.RGBvalue = Color.LIGHT_GRAY):
        left, top, width, height = ScreenUnit.convertMultipleUnits(left, top, width, height)
        rectangle = pygame.Surface((width, height))
        rectangle.set_alpha(transparancy)
        rectangle.fill(color)
        return vars.mainDisplay.blit(rectangle, (left, top))
    
    @staticmethod    
    def transparantRectangleFromRect(rect: Rect, transparancy: int, color: vars.RGBvalue = Color.LIGHT_GRAY):
        return Draw.transparantRectangle(rect.x, rect.y, rect.width, rect.height, transparancy, color)
    
    @staticmethod   
    def border(left: float, top: float, width: float, height: float, borderWidth: int, color: vars.RGBvalue = Color.BLACK, cornerRadius: int = -1) -> Rect:
        left, top, width, height, cornerRadius = ScreenUnit.convertMultipleUnits(left, top, width, height, cornerRadius)
        return pygame.draw.rect(vars.mainDisplay, color, Rect(left - borderWidth / 2, top - borderWidth / 2, width + borderWidth, height + borderWidth), width=int(borderWidth), border_radius=int(cornerRadius))
    
    @staticmethod
    def borderFromRect(rect: Rect, borderWidth: int, color: vars.RGBvalue = Color.BLACK, cornerRadius: int = -1):
        return Draw.border(rect.x, rect.y, rect.width, rect.height, borderWidth, color, cornerRadius)
    
    @staticmethod
    def pixel(left: vars.validScreenUnit, top: vars.validScreenUnit, color: vars.RGBvalue):
        left, top = ScreenUnit.convertMultipleUnits(left, top)
        return Draw.rectangle(left, top, 1, 1, color)
    
    @staticmethod
    def polygon(points: tuple[vars.coordinate], color: vars.RGBvalue, width: vars.validScreenUnit = 0):
        for index, point in enumerate(points):
            points[index] = ScreenUnit.convertMultipleUnits(point)
        width = ScreenUnit.checkIfValidScreenUnit(width)
        return pygame.draw.polygon(vars.mainDisplay, color, points, width)
    
    @staticmethod
    def circle(center: vars.coordinate, radius: vars.validScreenUnit, color: vars.RGBvalue, width: vars.validScreenUnit = 0):
        return Draw.partialCirle(center, radius, color, width)
    
    @staticmethod
    def partialCirle(center: vars.coordinate, radius: vars.validScreenUnit, color: vars.RGBvalue, width: vars.validScreenUnit = 0, drawTopLeft: bool = False, drawTopRight: bool = False, drawBottemLeft: bool = False, drawBottemRight: bool = False):
        center = ScreenUnit.convertMultipleUnits(*center)
        radius, width = ScreenUnit.convertMultipleUnits(radius, width)
        return pygame.draw.circle(vars.mainDisplay, color, center, radius, width, drawTopRight, drawTopLeft, drawBottemLeft, drawBottemRight)
    
    @staticmethod
    def calculateOuterBorderRadius(innerBorderRadius, borderWidth):
        innerBorderRadius, borderWidth = ScreenUnit.convertMultipleUnits(innerBorderRadius, borderWidth)
        outerBorderRadius = innerBorderRadius + borderWidth
        return outerBorderRadius if innerBorderRadius > 0 else 0
    
    @staticmethod
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

    @staticmethod
    def distanceBetweenPoints(point1: tuple[int], point2: tuple[int]):
        return sqrt((point1[1] - point1[0]) ** 2 + (point2[1] - point2[0]) ** 2)
