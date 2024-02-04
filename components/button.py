from importer import pygame
from elements.colors import Color
from elements.fonts import *
from elements.enums import mouseButton, overFlow
from components.interactions import Interactions
from components.image import Image
from components.text import Text
from components.draw import Draw
import vars


class Button:
    def __init__(self,
                 size: tuple[vars.validScreenUnit, vars.validScreenUnit],
                 color: vars.RGBvalue,
                 borderRadius:int = -1
                 ) -> None:
        self.buttonSize = size
        self.buttonColor = color
        self.defaultButtonColor = color
        self.borderRadius = borderRadius
        self.__text = None
        self.__icon = None
        # self.buttonAtributes = Updating(__text=False, __border=False)
        self.borderWidth = 0
        self.buttonRect = pygame.Rect(0, 0, 0, 0)
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
        
        buttonRect = Draw.rectangle(position[0], position[1], size[0], size[1], backgroundColor, cornerRadius)
        if borderWidth > 0:
            buttonRect = Draw.border(borderWidth, buttonRect, borderColor, cornerRadius)
        if text != "":
            buttonText = font.render(text, True, textColor)
            vars.mainDisplay.blit(buttonText, (position[0] + size[0] / 2 - buttonText.get_width() / 2, position[1] + size[1] / 2 - buttonText.get_height() / 2))
        return Interactions.isClickedInRect(buttonRect, mouseButton.leftMouseButton.value)
        
    # instance
    def text(self, text: str, textFont: pygame.font = Font.H4, textColor: vars.RGBvalue = Color.BLACK, overFlow = overFlow.ellipsis):
        self.__text = Text.textOverflow(text, textFont, self.buttonSize[0], overFlow)
        self.__textFont = textFont
        self.__textColor = textColor
        # self.buttonAtributes["__text"] = True

    def border(self, borderWidth: int, borderColor: vars.RGBvalue):
        self.borderWidth = borderWidth
        self.borderColor = borderColor

    def updateRadius(self, borderRadius):
        self.borderRadius = borderRadius
        
    def icon(self, iconPath: str):
        self.__icon = Image(iconPath)
        self.__resizeIcon()
        
    def updateColor(self, buttonColor: vars.RGBvalue):
        self.buttonColor = buttonColor
        
    def updateText(self, text):
        self.__text = Text.textOverflow(text, self.__textFont, self.buttonSize[0], overFlow)
        
                
    def __resizeIcon(self):
        self.__icon.resize(self.buttonSize[0], self.buttonSize[1])    

    def onMouseOver(self):
        return Interactions.isMouseOver(self.buttonRect)

    def onMouseClick(self, mouseButton: mouseButton = mouseButton.leftMouseButton) -> bool:
        return Interactions.isClickedInRect(self.buttonRect, mouseButton.value)
    
    def onMouseRelease(self, mouseButton: mouseButton = mouseButton.leftMouseButton) -> bool:
        return Interactions.isReleasedInRect(self.buttonRect, mouseButton.value)

    def onMouseHold(self, mouseButton: mouseButton = mouseButton.leftMouseButton) -> bool:
        return Interactions.isHoldingInRect(self.buttonRect, mouseButton.value)
    
    def inRect(self, rect: pygame.Rect):
        return Interactions.rectInRect(rect, self.getRect)

    def changeColorOnHover(self, hoverColor: vars.RGBvalue):
        if self.onMouseOver():
            self.buttonColor = hoverColor
        else:
            self.buttonColor = self.defaultButtonColor 
        
    def changeColorOnMouseClick(self, clickColor: vars.RGBvalue):
        if self.onMouseHold():
            self.buttonColor = clickColor
        else:
            self.buttonColor = self.defaultButtonColor
            
    def addBorderOnHover(self, borderWidth: int, borderColor: vars.RGBvalue):
        if self.onMouseOver():
            self.border(borderWidth, borderColor)
        else:
            self.border(0, borderColor)
            
    def __placeButtonRect(self):
        Draw.rectangleFromRect(self.buttonRect, self.buttonColor, Draw.calculateInnerBorderRadius(self.borderRadius, self.borderWidth))
        
    def __placeIcon(self, left, top):
        if self.__icon != None:
            vars.mainDisplay.blit(self.__icon.getImage, (left, top))
            
        
    def __placeText(self):
        if self.__text != None:
            self.textSurface = self.__textFont.render(self.__text, True, self.__textColor)
            textPosX, textPosY = Text.centerTextInRect(self.textSurface, self.buttonRect)
            vars.mainDisplay.blit(self.textSurface, (textPosX, textPosY))
                
    def __placeBorder(self):
        if self.borderWidth > 0:
            Draw.border(self.borderWidth, self.buttonRect, self.borderColor, self.borderRadius)
        

    def place(self, left, top):
        self.buttonRect = pygame.Rect(left, top, self.buttonSize[0], self.buttonSize[1])
        self.fullRect = pygame.Rect(left - self.borderWidth / 2, top - self.borderWidth / 2, self.buttonSize[0] + self.borderWidth, self.buttonSize[1] + self.borderWidth)
        self.__placeButtonRect()
        if vars.screenUpdate:
            self.__resizeIcon()
        self.__placeIcon(left, top)
        self.__placeText()
        self.__placeBorder()
        
    def resize(self, width, height):
        self.buttonSize = (width, height)
    
    @property
    def getFullSize(self):
        return self.buttonSize[0] + 2 * self.borderWidth, self.buttonSize[1] + 2 * self.borderWidth
    
    @property
    def getRect(self):
        return self.buttonRect
    
    @property
    def getButtonAndBorderRect(self):
        return self.fullRect
    