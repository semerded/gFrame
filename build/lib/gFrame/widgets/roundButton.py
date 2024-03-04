from ..baseImporter import pygame, vars
from ..components.draw import Draw
from ..components.interactions import Interactions
from ..components.screenUnits import ScreenUnit
from ..widgets._baseImage import _BaseImage
from ..elements.fonts import Font
from ..elements.colors import Color
from ..elements.enums import mouseButton, overFlow
from ..widgets._coloredWidget import _ColoredWidget
from ..widgets.text import Text

# TODO change sizing borderradius to actually drawing a circle
class RoundButton(_ColoredWidget):
    def __init__(self, size: tuple[vars.validScreenUnit], color: vars.RGBvalue) -> None:
        super().__init__(size, color, 10000000)
        self.buttonText = None
        self.buttonIcon = None
        self.textSurface = pygame.Surface((0, 0))
        self.disableColor = Color.GREY
    
    def text(self, text: str, textFont: pygame.font = Font.H4, color: vars.RGBvalue = Color.BLACK, overFlow = overFlow.ellipsis):
        self.buttonText = Text.textOverflow(text, textFont, self.widgetSize[0], overFlow)
        self.buttonTextFont = textFont
        self.buttonTextColor = color
        
    def icon(self, iconPath: str):
        self.buttonIcon = _BaseImage(iconPath)
        self._resizeIcon()
                
    def _resizeIcon(self):
        self.buttonIcon.resizeImage(self.widgetSize[0], self.widgetSize[1])
    
    def _placeText(self):
        if self.buttonText != None:
            self.textSurface = self.buttonTextFont.render(self.buttonText, True, self.buttonTextColor)
            textPosX, textPosY = Text.centerTextInRect(self.textSurface, self.widgetRect)
            vars.mainDisplay.blit(self.textSurface, (textPosX, textPosY))
            
    
    
    def place(self, left, top):
        left, top = ScreenUnit.convertMultipleUnits(left, top)
            
        self._colordWidgetPlace(left, top, True)
        self._placeText()
        
        if self.buttonIcon != None:
            self.buttonIcon._baseImagePlace(left, top)
        self._baseWidgetPlace(left, top)
            
        
    