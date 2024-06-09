from ..core.rect import Rect
from ..core.interactions import Interactions
from ..enums import mouseButton
from .. import data
from .. import gID
from ..core.renderQueue import RenderQueue


class _WidgetRect:
    active = True

    def __init__(self, size) -> None:
        self.id = gID.generateID()
        self.size = size
        self.rect = Rect.placeHolder()

        data.widgetConstantUpdates[self.id] = [self._checkIfWidgetIsClicked]

    def _checkIfWidgetIsClicked(self):
        if Interactions.isMouseClickedInRect(self.rect, mouseButton.leftMouseButton):
            self.isClickedInWidget = True

    def isMouseOver(self):
        return Interactions.isMouseOver(self.rect) if self.active else False

    def isClicked(self, mouseButton: mouseButton = mouseButton.leftMouseButton) -> bool:
        if not self.active or data.widgetAlreadyPressed:
            return False
        return self._setWidgetAlreadyPressed(mouseButton, Interactions.isMouseClickedInRect)

    def isReleased(self, mouseButton: mouseButton = mouseButton.leftMouseButton) -> bool:
        if not self.active or data.widgetAlreadyPressed:
            return False
        if self._setWidgetAlreadyPressed(mouseButton, Interactions.isMouseReleasedInRect) and self.isClickedInWidget:
            self.isClickedInWidget = False
            return True
        return False

    def isPressing(self, mouseButton: mouseButton = mouseButton.leftMouseButton) -> bool:
        if not self.active or data.widgetAlreadyPressed:
            return False
        return self._setWidgetAlreadyPressed(mouseButton, Interactions.isMousePressingInRect)

    def _setWidgetAlreadyPressed(self, mouseButton: mouseButton, func):
        if (result := func(self.rect, mouseButton)):
            data.widgetAlreadyPressed = True
            RenderQueue.requestFullScreenUpdate()
        return result

    def isSuperClicked(self, mouseButton: mouseButton = mouseButton.leftMouseButton):
        if self.active:
            if (status := Interactions.isMouseClickedInRect(self.rect, mouseButton)):
                RenderQueue.requestFullScreenUpdate()
            return status
        return False

    def isSuperPressing(self, mouseButton: mouseButton = mouseButton.leftMouseButton):
        if self.active:
            if (status := Interactions.isMousePressingInRect(self.rect, mouseButton)):
                RenderQueue.requestFullScreenUpdate()
            return status
        return False

    def isSuperReleased(self, mouseButton: mouseButton = mouseButton.leftMouseButton):
        if self.active:
            if (status := Interactions.isMouseReleasedInRect(self.rect, mouseButton)):
                RenderQueue.requestFullScreenUpdate()
            return status
        return False

    def inRect(self, rect: Rect):
        return Interactions.rectInRect(rect, self.rect)

    def updateRect(self, left, top):
        self.rect = Rect(left, top, self.size[0], self.size[1])

    def delete(self):
        gID.removeIDfromWCU(self.id)
