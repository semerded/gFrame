from importer import pygame
import vars
try:
    import PIL.Image
except ImportError:
    PILimported = False
else:
    PILimported = True

class Display:
    if PILimported:
        def getPixelColorFromBackground(left: int, top: int) -> vars.RGBvalue:
            displayString = pygame.image.tostring(vars.mainDisplay, 'RGB')
            displayByte = PIL.Image.frombytes('RGB', (vars.appScreenWidth, vars.appScreenHeight), displayString)
            return displayByte.getpixel((left, top))
        
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