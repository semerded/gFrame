from importer import pygame
from elements.enums import overFlow, xTextPositioning, yTextPositioning, hoverSpeed
from elements.colors import Color
from elements.fonts import Font
from components.draw import Draw
from components.screenUnits import ScreenUnit
import vars


class Text:
    def __init__(self, text: str, fontName_or_path: str, fontSize: int, color: vars.RGBvalue, bold: bool = False, italic: bool = False) -> None:
        if isinstance(fontName_or_path, str): # check if classmethod is used
            try:
                self.font = pygame.font.SysFont(fontName_or_path, fontSize, bold, italic)
            except:
                self.font = pygame.font.Font(fontName_or_path, fontSize)
                self.font.bold = bold
                self.font.italic = italic
        else:
            self.font: pygame.font.Font = fontName_or_path
            self.font.bold = bold
            self.font.italic = italic

        self.color = color
        self.backgroundColor = None
        
        self.borderColor = None
        self.borderWidth = None
        self.borderRadius = -1
        
        self.hoverDistance = 0
        self.hoverSpeed = 0
        self._hoverDifference = 0
        self._hoverUp = True
        
        self.antiAllias = True
        
        self.text = text
        self._renderText(text)
        
        
        self.textRect = pygame.Rect(0, 0, 0, 0)

    @classmethod 
    def fromFont(cls, text: str, font: pygame.font, color: vars.RGBvalue, bold: bool = False, italic: bool = False):
        return cls(text, font, 0, color, bold, italic)
    
    @staticmethod
    def textOverflow(text: str, font: pygame.font, maxWidth: int | float, overFlowType: overFlow = overFlow.ellipsis) -> str:
        if font.size(text)[0] < maxWidth:
            return text
        
        if overFlowType == overFlow.show:
            return text
        elif overFlowType == overFlow.ellipsis:
            ellipsisWidth = font.size("...")[0]
            maxWidth -= ellipsisWidth - ellipsisWidth / 3
            overFlowTrailing = "..."
        else:
            overFlowTrailing = ""
            
        newText = ""
        textWidth = 0
        for letter in text:
            textWidth += font.size(letter)[0]
            if textWidth < maxWidth - 10:
                newText += letter
            else:
                return newText.strip() + overFlowTrailing
            
    @staticmethod
    def simpleText(text: str, left: vars.validScreenUnit, top: vars.validScreenUnit, font: pygame.font.Font = Font.H3, color: vars.RGBvalue = Color.BLACK, bold: bool = False, italic: bool = False):
        font.bold = bold
        font.italic = italic
  
        return vars.mainDisplay.blit(font.render(f"{text}", True, color), (left, top))
            
    def setAntiAllias(self, active: bool):
        self.antiAllias = active
        
    def setBackground(self, backgroundColor: vars.RGBvalue):
        self.backgroundColor = backgroundColor
        
    def setTextColor(self, color: vars.RGBvalue):
        self.color = color
        
    def setBorder(self, borderWidth: vars.validScreenUnit, borderColor: vars.RGBvalue, borderRadius: vars.validScreenUnit = -1):
        borderWidth, borderRadius = ScreenUnit.convertMultipleUnits(borderWidth, borderRadius)
        self.borderWidth = borderWidth
        self.borderColor = borderColor
        self.borderRadius = borderRadius
        
    def setHover(self, hoverDistance: vars.validScreenUnit, speed: int | hoverSpeed = hoverSpeed.normal):
        self.hoverDistance = ScreenUnit.checkIfValidScreenUnit(hoverDistance)
        if isinstance(speed, hoverSpeed):
            self.hoverSpeed = speed.value
        else:
            self.hoverSpeed = speed

    def setText(self, text: str, bold: bool = False, italic: bool = False):
        self.text = text
        self.font.bold = bold
        self.font.italic = italic
        self._renderText(text)
    
    def _textHover(self, top):
        if self.hoverDistance > 0:
            if self._hoverUp:
                self._hoverDifference += 0.02 * self.hoverSpeed
            else: 
                self._hoverDifference -= 0.02 * self.hoverSpeed
            
            if self._hoverDifference > self.hoverDistance / 2:
                self._hoverUp = False
            if self._hoverDifference < -self.hoverDistance / 2:
                self._hoverUp = True  
            return top + self._hoverDifference
        
        return top
    
    def _renderText(self, text: str):
        self.textSurface = self.font.render(text, self.antiAllias, self.color)
        self.textHeight = self.textSurface.get_height()
        self.textWidth = self.textSurface.get_width()
        
    def _drawBase(self):
        if self.backgroundColor != None:
            Draw.rectangleFromRect(self.textRect, self.backgroundColor, self.borderRadius)
        if self.borderColor != None and self.borderWidth > 0:
            Draw.borderFromRect(self.textRect, self.borderWidth, self.borderColor, Draw.calculateOuterBorderRadius(self.borderRadius, self.borderWidth))
            
        
    def place(self, left: vars.validScreenUnit, top: vars.validScreenUnit):
        left, top = ScreenUnit.convertMultipleUnits(left, top)
        top = self._textHover(top)
        self.textRect = pygame.Rect(left, top, self.textWidth + 6, self.textHeight + 6)
        self._drawBase()
        vars.mainDisplay.blit(self.textSurface, (left + 3, top + 3))
        
    
    def placeInRect(self, rect: pygame.Rect, xPositioning: xTextPositioning, yPositioning: yTextPositioning):
        # top = self._textHover(top) # TODO add hover
        self.textRect = pygame.Rect(rect.x, rect.y, rect.width + 6, rect.height + 6)
        x, y = self._calculateTextPositioning(rect, xPositioning, yPositioning)
        self._drawBase()
        vars.mainDisplay.blit(self.textSurface, (x + 3, y + 3))
        
    def _calculateTextPositioning(self, rect: pygame.Rect, xPositioning: xTextPositioning, yPositioning: yTextPositioning):
        if xPositioning == xTextPositioning.center:
            x = rect.x + (rect.width / 2) - (self.textWidth / 2)
        elif xPositioning == xTextPositioning.right:
            x = (rect.x + rect.width) - self.textWidth
        else:
            x = rect.x
            
        if yPositioning == yTextPositioning.center:
            y = rect.y + (rect.height / 2) - (self.textHeight / 2)
        elif yPositioning == yTextPositioning.bottom:
            y = (rect.y + rect.height) - self.textHeight
        else:
            y = rect.y
        return x, y
    
    @property
    def getRect(self):
        return self.textRect