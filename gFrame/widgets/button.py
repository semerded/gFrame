from ..baseImporter import pygame, vars
from ..core.draw import Draw
from ..core.interactions import Interactions
from ..core.screenUnits import ScreenUnit
from ..core.rect import Rect
from ..widgets._baseImage import _BaseImage
from ..fonts import Font
from ..colors import Color
from ..enums import mouseButton, overFlow
from ..widgets._coloredWidget import _ColoredWidget
from ..widgets.text import Text
from time import time # type: ignore

class Button(_ColoredWidget):
    pressingTime = 0
    doubleClickTimeDifference = 0
    DOUBLE_CLICK_MAX_INTERVAL = 0.5 # seconds (default on windows)
    
    def __init__(self, size, color, borderRadius: vars.validScreenUnit = -1) -> None:
        super().__init__(size, color, borderRadius=borderRadius)
        self.buttonText = None
        self.buttonIcon = None
        self.textSurface = pygame.Surface((0, 0))
        self.disableColor = Color.GREY
        
    # static
    @staticmethod
    def simpleButton(rect: Rect, backgroundColor= Color.LIGHT_GRAY, text = "", font = Font.H3,textColor = Color.BLACK, cornerRadius = -1, borderWidth = 0, borderColor = Color.BLACK) -> bool:
        left, top, width, height = rect.unpack()  
        
        borderWidth = ScreenUnit.checkIfValidScreenUnit(borderWidth)
        cornerRadius = ScreenUnit.checkIfValidScreenUnit(cornerRadius)
        
        buttonRect = Draw.rectangle(left, top, width, height, backgroundColor, cornerRadius)
        if borderWidth > 0:
            buttonRect = Draw.border(borderWidth, buttonRect, borderColor, cornerRadius)
        if text != "":
            buttonText = font.render(text, True, textColor)
            vars.mainDisplay.blit(buttonText, (left + width / 2 - buttonText.get_width() / 2, top + height / 2 - buttonText.get_height() / 2))
        return Interactions.isMouseClickedInRect(mouseButton.leftMouseButton, buttonRect)
    
    def text(self, *args, bold = False, italic = False, overFlow = overFlow.ellipsis):
        if len(args) == 4:
            fontSize = int(ScreenUnit.checkIfValidScreenUnit(args[2]))
            try:
                self.buttonTextFont = pygame.font.SysFont(args[1], fontSize)
            except:
                self.buttonTextFont = pygame.font.Font(args[1], fontSize) 
            self.buttonTextColor = args[3]

        else:
            self.buttonTextFont: pygame.font.Font = args[1]
            self.buttonTextColor = args[2]
        self.buttonTextFont.bold = bold
        self.buttonTextFont.italic = italic
        self.buttonText = Text.textOverflow(args[0], self.buttonTextFont, self.widgetSize[0], overFlow)
        
    def icon(self, iconPath: str):
        self.buttonIcon = _BaseImage(iconPath)
        self._resizeIcon()
                
    def _resizeIcon(self):
        self.buttonIcon.resize(self.widgetSize[0], self.widgetSize[1])
    
    def _placeText(self):
        if self.buttonText != None:
            self.textSurface = self.buttonTextFont.render(self.buttonText, True, self.buttonTextColor)
            textPosX, textPosY = Text.centerTextInRect(self.textSurface, self.widgetRect)
            vars.mainDisplay.blit(self.textSurface, (textPosX, textPosY))
            
    def isHeldFor(self, milliseconds: int):
        if self.isSuperClicked():
            self.pressingTime = time()
        
        if self.isSuperPressing() and self.isClickedInWidget and (time() - self.pressingTime > milliseconds / 1000):
            return True
        return False
    
    def isDoubleClicked(self, mousebutton: mouseButton = mouseButton.leftMouseButton):
        if self.isSuperClicked(mousebutton):
            if time() - self.doubleClickTimeDifference < self.DOUBLE_CLICK_MAX_INTERVAL:
                self.doubleClickTimeDifference = 0
                return True
            self.doubleClickTimeDifference = time()
        if Interactions.isMouseClickedNotInRect(self.getRect, mousebutton):
            self.doubleClickTimeDifference = 0
        return False 

    def place(self, left, top, opacity: int = 255):
        left, top = ScreenUnit.convertMultipleUnits(left, top)
            
        self._colordWidgetPlace(left, top, opacity, False)
        self._placeText()
        
        if self.buttonIcon != None:
            self.buttonIcon._baseImagePlace(left, top)
        self._baseWidgetPlace(left, top)

    @property       
    def getPressingTime(self):
        self.pressingTime
        
    def setDoubleClickMaxInterval(self, maxInterval_inMilliseconds: int):
        self.DOUBLE_CLICK_MAX_INTERVAL = maxInterval_inMilliseconds / 1000
    