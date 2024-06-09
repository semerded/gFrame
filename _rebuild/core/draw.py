import pygame
from .. import data
from ..core.rect import Rect
from ..colors import Color
from ..std.screenunit import *
from ..typedef import *
from math import dist
from ..core.renderQueue import RenderQueue, RenderObject

class Draw:
    @staticmethod
    def rectangle(left, top, width, height, color: RGBvalue = Color.LIGHT_GRAY, z_index = 0, cornerRadius: int = -1):
        rect = Rect(left, top, width, height)
        RenderQueue.add(RenderObject(pygame.draw.rect, data.canvas, color, rect, border_radius=int(cornerRadius)), z_index)
        return rect
    
    @staticmethod
    def rectangleFromRect(rect: Rect, color: RGBvalue = Color.LIGHT_GRAY, z_index = 0, cornerRadius: int = -1):
        return Draw.rectangle(rect.x, rect.y, rect.width, rect.height, color, z_index, cornerRadius)
    
    @staticmethod
    def transparantRectangle(left, top, width, height, transparancy: int, color: RGBvalue = Color.LIGHT_GRAY):
        rectangle = pygame.Surface((width, height))
        rectangle.set_alpha(transparancy)
        rectangle.fill(color)
        RenderQueue.add(RenderObject(data.canvas.blit, rectangle, (left, top)))
        return Rect(left, top, width, height)
    
    @staticmethod    
    def transparantRectangleFromRect(rect: Rect, transparancy: int, color: RGBvalue = Color.LIGHT_GRAY):
        return Draw.transparantRectangle(rect.x, rect.y, rect.width, rect.height, transparancy, color)
    
    @staticmethod   
    def border(left, top, width, height, borderWidth: int, color: RGBvalue = Color.BLACK, z_index = 0, cornerRadius: int = -1) -> Rect:
        rect = Rect(left - borderWidth / 2, top - borderWidth / 2, width + borderWidth, height + borderWidth)
        RenderQueue.add(RenderObject(pygame.draw.rect, data.canvas, color, rect, width=int(borderWidth), border_radius=int(cornerRadius)), z_index)
        return rect
    
    @staticmethod
    def borderFromRect(rect: Rect, borderWidth: int, color: RGBvalue = Color.BLACK, z_index = 0, cornerRadius: int = -1):
        return Draw.border(rect.x, rect.y, rect.width, rect.height, borderWidth, color, z_index, cornerRadius)
    
    @staticmethod
    def pixel(left, top, color: RGBvalue):
        return Draw.rectangle(left, top, 1, 1, color)
    
    @staticmethod
    def polygon(color: RGBvalue, points, width = 0, z_index = 0):
        RenderQueue.add(RenderObject(pygame.draw.polygon, data.canvas, color, points, width), z_index)
        return Rect.placeHolder()
    
    @staticmethod
    def circle(center, radius, color: RGBvalue, width = 0, z_index = 0):
        return Draw.partialCirle(center, radius, color, width, z_index = z_index)
    
    @staticmethod
    def partialCirle(center, radius, color: RGBvalue, width = 0, z_index = 0, drawTopLeft: bool = False, drawTopRight: bool = False, drawBottemLeft: bool = False, drawBottemRight: bool = False):
        RenderQueue.add(RenderObject(pygame.draw.circle, data.canvas, color, center, radius, width, drawTopRight, drawTopLeft, drawBottemLeft, drawBottemRight), z_index)
        return Rect.fromCircle(center, radius)
    
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
