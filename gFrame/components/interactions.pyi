from ..elements.enums import mouseButton
from ..components.rect import Rect
from ..baseImporter import vars

class Interactions:
    def isMouseOver(rect: Rect) -> bool: ...
    def isMouseInArea(topCord: vars.coordinate, bottomCord: vars.coordinate) -> bool: ...
    
    def isMouseInPolygon(polygon: list | tuple [vars.coordinate]) -> bool: ...
    def isMouseInCircle(center: vars.coordinate, radius: int) -> bool: ...
    
    def isMouseClicked(mouseButton: mouseButton = mouseButton.leftMouseButton) -> bool: ... 
    def isMouseClickedInRect(rect: Rect, mouseButton: mouseButton = mouseButton.leftMouseButton) -> bool: ...
    def isMouseClickedInPolygon(polygon: list | tuple [vars.coordinate], mouseButton: mouseButton = mouseButton.leftMouseButton) -> bool: ...
    def isMouseClickedInCircle(center: vars.coordinate, radius: int, mouseButton: mouseButton = mouseButton.leftMouseButton) -> bool: ...
    
    def isMouseClickedNotInRect(rect: Rect, mouseButton: mouseButton = mouseButton.leftMouseButton) -> bool: ...
    def isMouseClickedNotInPolygon(polygon: list | tuple [vars.coordinate], mouseButton: mouseButton = mouseButton.leftMouseButton) -> bool: ...
    def isMouseClickedNotInCircle(center: vars.coordinate, radius: int, mouseButton: mouseButton = mouseButton.leftMouseButton) -> bool: ...
    
    def isMouseReleased(mouseButton: mouseButton = mouseButton.leftMouseButton) -> bool: ...
    def isMouseReleasedInRect(rect: Rect, mouseButton: mouseButton = mouseButton.leftMouseButton) -> bool: ...
    def isMouseReleasedInPolygon(polygon: list | tuple [vars.coordinate], mouseButton: mouseButton = mouseButton.leftMouseButton) -> bool: ...
    def isMouseReleasedInCircle(center: vars.coordinate, radius: int, mouseButton: mouseButton = mouseButton.leftMouseButton) -> bool: ... 
    
    def isMouseReleasedNotInRect(rect: Rect, mouseButton: mouseButton = mouseButton.leftMouseButton) -> bool: ...
    def isMouseReleasedNotInPolygon(polygon: list | tuple [vars.coordinate], mouseButton: mouseButton = mouseButton.leftMouseButton) -> bool: ...
    def isMouseReleasedNotInCircle(center: vars.coordinate, radius: int, mouseButton: mouseButton = mouseButton.leftMouseButton) -> bool: ... 
    
    def isMousePressing(mouseButton: mouseButton = mouseButton.leftMouseButton) -> bool: ...
    def isMousePressingInRect(rect: Rect, mouseButton: mouseButton = mouseButton.leftMouseButton) -> bool: ...
    def isMousePressingInPolygon(polygon: list | tuple [vars.coordinate], mouseButton: mouseButton = mouseButton.leftMouseButton) -> bool: ...
    def isMousePressingInCircle(center: vars.coordinate, radius: int, mouseButton: mouseButton = mouseButton.leftMouseButton) -> bool: ...
    
    def isMousePressingNotInRect(rect: Rect, mouseButton: mouseButton = mouseButton.leftMouseButton) -> bool: ...
    def isMousePressingNotInPolygon(polygon: list | tuple [vars.coordinate], mouseButton: mouseButton = mouseButton.leftMouseButton) -> bool: ...
    def isMousePressingNotInCircle(center: vars.coordinate, radius: int, mouseButton: mouseButton = mouseButton.leftMouseButton) -> bool: ...
    
    def isScrolledUp() -> bool: ...
    def isScrolledDown() -> bool: ...
    def isScrolled() -> bool: ...
    
    def isKeyClicked(key: int) -> bool: ...
    def isKeyReleased(key: int) -> bool: ...
    def isKeyPressing(key: int) -> bool: ...
    
    def rectInRect(masterRect: Rect, childRect: Rect) -> bool: ...
    