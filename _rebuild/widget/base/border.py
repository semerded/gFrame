from ...widget._draw import Draw
from ...colors import Color
from ...core.rect import Rect

unchanged = None
class Border:
    def __init__(self, size, width=0, color=Color.BLACK, radius=-1, innerBorder=False) -> None:
        self.size = size
        self.width = width
        self.color = color
        self.radius = radius
        self.innerBorder = innerBorder
        self.drawable = False

    def resize(self, width, height):
        self.size = width, height

    def setColor(self, color):
        self.color = color
        
    def setRadius(self, radius):
        self.radius = radius
        
    def setWidth(self, width):
        self.width = width
        if self.width > 0:
            self.drawable = True
        else:
            self.drawable = False
        
    def setInnerBorder(self, status):
        self.innerBorder = status

    def place(self, left, top, z_index=0):
        if self.drawable:
            if not self.innerBorder:
                return Draw.border(left, top, *self.size, self.width, self.color,
                            z_index, cornerRadius=self.radius)
            return Draw.innerBorder(left, top, *self.size, self.width, self.color, z_index, cornerRadius=self.radius)
        return Rect(left, top, *self.size)
