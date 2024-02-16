from importer import pygame
import vars
from components.draw import Draw
from components.interactions import Interactions
from components.screenUnits import ScreenUnit
from widgets.image import Image
from elements.fonts import Font
from elements.colors import Color
from elements.enums import mouseButton, overFlow
from widgets._coloredWidget import _ColoredWidget
from widgets.text import Text

class Button(_ColoredWidget):
    def __init__(self, size: tuple[vars.validScreenUnit], color: vars.RGBvalue) -> None:
        super().__init__(size, color)
        self.buttonText = None
        self.buttonIcon = None
        self.textSurface = pygame.Surface((0, 0))
        
    # static
    def simpleButton(size,
                     position, 
                     backgroundColor: vars.RGBvalue = Color.LIGHT_GRAY, 
                     text: str = "", 
                     font: vars.pygameFont = Font.H3,
                     textColor: vars.RGBvalue = Color.BLACK, 
                     cornerRadius: int = -1, 
                     borderWidth: int = 0,
                     borderColor: vars.RGBvalue = Color.BLACK,
                     ) -> bool:
        
        size = ScreenUnit.convertMultipleUnits(*size)
        position = ScreenUnit.convertMultipleUnits(*position)
        borderWidth = ScreenUnit.checkIfValidScreenUnit(borderWidth)
        cornerRadius = ScreenUnit.checkIfValidScreenUnit(cornerRadius)
        
        buttonRect = Draw.rectangle(position[0], position[1], size[0], size[1], backgroundColor, cornerRadius)
        if borderWidth > 0:
            buttonRect = Draw.border(borderWidth, buttonRect, borderColor, cornerRadius)
        if text != "":
            buttonText = font.render(text, True, textColor)
            vars.mainDisplay.blit(buttonText, (position[0] + size[0] / 2 - buttonText.get_width() / 2, position[1] + size[1] / 2 - buttonText.get_height() / 2))
        return Interactions.isMouseClickedInRect(buttonRect, mouseButton.leftMouseButton.value)
    
    def text(self, text: str, textFont: pygame.font = Font.H4, color: vars.RGBvalue = Color.BLACK, overFlow = overFlow.ellipsis):
        self.buttonText = Text.textOverflow(text, textFont, self.widgetSize[0], overFlow)
        self.buttonTextFont = textFont
        self.buttonTextColor = color
        
    def icon(self, iconPath: str):
        self.buttonIcon = Image(iconPath)
        self._resizeIcon()
                
    def _resizeIcon(self):
        self.buttonIcon.resize(self.widgetSize[0], self.widgetSize[1])
    
    def _placeText(self):
        if self.buttonText != None:
            self.textSurface = self.buttonTextFont.render(self.buttonText, True, self.buttonTextColor)
            textPosX, textPosY = Text.centerTextInRect(self.textSurface, self.widgetRect)
            vars.mainDisplay.blit(self.textSurface, (textPosX, textPosY))
    
    def place(self, left, top):
        left, top = ScreenUnit.convertMultipleUnits(left, top)
        Draw.rectangleFromRect(self.widgetRect, self.widgetColor, Draw.calculateInnerBorderRadius(self.widgetBorderRadius, self.widgetBorderWidth))
        self._placeText()
        
        if self.buttonIcon != None:
            self.buttonIcon.place(left, top)
        self.widgetPlace(left, top)
            
        
    