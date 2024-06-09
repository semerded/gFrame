import pygame
from .. import data
from ..core.rect import Rect
from ..colors import Color
from math import dist

class Draw:
    @staticmethod
    def rectangle(left: float, top: float, width: float, height: float, color = Color.LIGHT_GRAY, cornerRadius: int = -1):
        return pygame.draw.rect(data.canvas, color, Rect(left, top, width, height), border_radius=int(cornerRadius))
    
    @staticmethod
    def rectangleFromRect(rect: Rect, color = Color.LIGHT_GRAY, cornerRadius: int = -1):
        return Draw.rectangle(rect.x, rect.y, rect.width, rect.height, color, cornerRadius)
    
    @staticmethod
    def transparantRectangle(left: float, top: float, width: float, height: float, transparancy: int, color = Color.LIGHT_GRAY):
        rectangle = pygame.Surface((width, height))
        rectangle.set_alpha(transparancy)
        rectangle.fill(color)
        return data.canvas.blit(rectangle, (left, top))
    
    @staticmethod    
    def transparantRectangleFromRect(rect: Rect, transparancy: int, color = Color.LIGHT_GRAY):
        return Draw.transparantRectangle(rect.x, rect.y, rect.width, rect.height, transparancy, color)
    
    @staticmethod   
    def border(left: float, top: float, width: float, height: float, borderWidth: int, color = Color.BLACK, cornerRadius: int = -1) -> Rect:
        return pygame.draw.rect(data.canvas, color, Rect(left - borderWidth / 2, top - borderWidth / 2, width + borderWidth, height + borderWidth), width=int(borderWidth), border_radius=int(cornerRadius))
    
    @staticmethod
    def borderFromRect(rect: Rect, borderWidth: int, color = Color.BLACK, cornerRadius: int = -1):
        return Draw.border(*rect.unpack(), borderWidth=borderWidth, color=color, cornerRadius=cornerRadius)
    
    @staticmethod
    def innerBorder(left: float, top: float, width: float, height: float, borderWidth: int, color = Color.BLACK, cornerRadius: int = -1) -> Rect:
        return pygame.draw.rect(data.canvas, color, Rect(left, top, width, height), width=int(borderWidth), border_radius=int(cornerRadius))
    
    @staticmethod
    def innerBorderFromRect(rect: Rect, borderWidth: int, color = Color.BLACK, cornerRadius: int = -1):
        return Draw.innerBorder(*rect.unpack(), borderWidth=borderWidth, color=color, cornerRadius=cornerRadius)
    
    @staticmethod
    def pixel(left, top, color):
        return Draw.rectangle(left, top, 1, 1, color)
    
    @staticmethod
    def polygon(color, points, width = 0):
        return pygame.draw.polygon(data.canvas, color, points, width)
    
    @staticmethod
    def circle(center, radius, color, width = 0):
        return Draw.partialCirle(center, radius, color, width)
    
    @staticmethod
    def partialCirle(center, radius, color, width = 0, drawTopLeft: bool = False, drawTopRight: bool = False, drawBottemLeft: bool = False, drawBottemRight: bool = False):
        return pygame.draw.circle(data.canvas, color, center, radius, width, drawTopRight, drawTopLeft, drawBottemLeft, drawBottemRight)
    
    @staticmethod
    def calculateOuterBorderRadius(innerBorderRadius, borderWidth):
        outerBorderRadius = innerBorderRadius + borderWidth
        return outerBorderRadius if innerBorderRadius > 0 else 0
    
    @staticmethod
    def pointInPolygon(point: list | tuple, polygon: list | tuple[list | tuple]) -> bool:
        num_vertices = len(polygon)
        x, y = point

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

    @staticmethod
    def distanceBetweenPoints(point1: tuple[int], point2: tuple[int]):
        return dist(point1, point2)
