from ..colors import Color
from ..core.rect import Rect
from ..widget._widgetrect import _WidgetRect
from ..widget._draw import Draw
from ..widget.base.border import Border
from .. import data
from ..core.renderQueue import RenderQueue, RenderObject

class _BaseWidget(_WidgetRect):
    active = True
    isClickedInWidget = False
    position = (0, 0)
    z_index = None
    
    def __init__(self, size, color, cornerRadius = -1) -> None:
        super().__init__(size)
        self.color = color
        self.cornerRadius = cornerRadius
        self.__border = Border(size)
        self.__innerBorder = Border(size, innerBorder=True)

    def innerBorder(self, width, color):
        self.__innerBorder.setWidth(width)
        self.__innerBorder.setColor(color)
        self.__innerBorder.setRadius(0) # TODO
        
    def border(self, width, color):
        self.__border.setWidth(width)
        self.__border.setColor(color)
        self.__border.setRadius(0) # TODO
        
    def addToRenderQueue(self):
        RenderQueue.add(RenderObject(self.place, *self.position, self.z_index), self.z_index, self.id)
    
    def place(self, left, top, z_index = 0):
        self.position = (left, top)
        
        if z_index != self.z_index:
            if z_index == None:
                self.z_index = z_index
                RenderQueue.add(RenderObject(self.place, *self.position, self.z_index), self.z_index, self.id)
            else:
                RenderQueue.removeFromID(self.z_index, self.id)
                self.z_index = z_index
                RenderQueue.add(RenderObject(self.place, *self.position, self.z_index), self.z_index, self.id)
        
        Draw.rectangle(left, top, self.size[0], self.size[1], self.color, z_index, 0) # TODO
        self.__innerBorder.place(left, top, z_index)
        self.__border.place(left, top, z_index)
        

    