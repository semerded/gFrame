from ..typedef import *
from .. import data
from ..core.rect import Rect

class RenderQueue:
    def add(renderObject, z_index, g_id):
        """
        
        """
        if not (z_index >= 0 and z_index < 256):
            z_index = 0
        if z_index not in data.renderQueue:
            data.renderQueue[z_index]
        data.renderQueue[z_index][g_id] = renderObject
        
    def requestFullScreenUpdate():
        data.fullScreenUpdatePending = True
        
    def removeFromID(z_index, g_id):
        try: 
            data.renderQueue[z_index].pop(g_id)
        except: pass

    def clear():
        data.renderQueue = {}

    def renderAllFromQueue():
        for renderLevel in data.renderQueue.values():
            for renderObject in renderLevel:
                renderObject.render()

    @staticmethod
    def renderLayer(layer):
        for renderObject in data.renderQueue[layer]:
            renderObject.render()

    @staticmethod
    def renderFromLayer(layer):
        for _layer in range(layer, 256):
            for renderObject in data.renderQueue[_layer]:
                renderObject.render()

    def getRenderRect(rect: Rect):
        #! deprecated
        rect.expandWidth(1)
        rect.expandHeight(1)
        return rect


class RenderObject:
    def __init__(self, renderFunction, *renderArgs) -> None:
        self.renderFunction = renderFunction
        self.renderArgs = renderArgs

    def render(self):
        self.renderFunction(*self.renderArgs)
