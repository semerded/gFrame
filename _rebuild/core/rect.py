import pygame

class Rect(pygame.Rect):
    def __init__(self, *args):
        if len(args) == 4:
            super().__init__(*args)
        else:
            super().__init__(args[0], args[1])

    def unpack(self):
        return self.left, self.top, self.width, self.height
    
    def expandWidth(self, expansion):
        self.width += expansion
        self.left -= int(expansion / 2)
        
    def shrinkWidth(self, shrinkage):
        self.expandWidth(-shrinkage)
        
    def expandHeight(self, expansion):
        self.height += expansion
        self.top -= int(expansion / 2)
        
    def shrinkHeight(self, shrinkage):
        self.expandHeight(-shrinkage)
        
    def rw(self, screenUnit: float):
        "rect width (0 - 100)"
        return self.width / 100 * screenUnit
    
    def rh(self, screenUnit: float):
        "rect height (0 - 100)"
        
        return self.height / 100 * screenUnit
    
    def pw(self, screenUnit: float):
        "rect place width (0 - 100)"
        return self.rw(screenUnit) + self.x
    
    def ph(self, screenUnit: float):
        "rect place height (0 - 100)"
        return self.rh(screenUnit) + self.y
    
    @staticmethod
    def placeHolder():
        return Rect(0, 0, 0, 0)
    
    @staticmethod
    def fromPolygon(points):
        pass
    
    @staticmethod
    def fromCircle(center, radius):
        return Rect(center[0] - radius, center[1] - radius, radius * 2, radius * 2)