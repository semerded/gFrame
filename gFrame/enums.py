from enum import Enum
class mouseButton(Enum):
    leftMouseButton = 1
    middleMouseButton = 2
    rightMouseButton = 3
    scrollUp = 4
    scrollDown = 5
    bottomSideMouseButton = 6
    topSideMouseButton = 7
    
class interactionType(Enum):
    mouseOver = 1
    mouseClick = 2
    mouseRelease = 3
    mouseHold = 4
    
class overFlow(Enum):
    ellipsis = 1
    hide = 2
    show = 3

class aspectRatios(Enum):
    ratio1to1 = "1/1"
    ratio16to9 = "16/9"
    ratio9to16 = "9/16"
    ratio4to3 = "4/3"
    ratio3to4 = "3/4"
    
class axis(Enum):
    x = 0
    y = 1
    z = 2
    
class scrollSpeed(Enum):
    slow = 20
    medium = 40
    fast = 60
    
class hoverSpeed(Enum):
    extraSlow = 5
    slow = 15
    normal = 25
    fast = 40
    veryFast = 60
    extreme = 80
    lightSpeed = 100
    
class xTextPositioning(Enum):
    left = 1
    center = 2
    right = 3
    
class yTextPositioning(Enum):
    top = 1
    center = 2
    bottom = 3