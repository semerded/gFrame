from .. import data

class RenderList:
    @staticmethod
    def add(renderObject, z_index, g_id=None):
        g_id = generateID() if g_id == None else g_id
        if not (z_index >= 0 and z_index < 256):
            z_index = 0
        if z_index not in data.renderQueue:
            data.renderQueue[z_index]
        data.renderQueue[z_index][g_id] = renderObject