from ..baseImporter import pygame, vars
from ..elements.enums import overFlow, xTextPositioning, yTextPositioning, hoverSpeed
from ..elements.colors import Color
from ..elements.fonts import Font
from ..components.draw import Draw
from ..components.display import Display
from ..components.screenUnits import ScreenUnit
from ..components.rect import Rect


class Text:
    borderColor: vars.RGBvalue = None
    borderWidth: vars.validScreenUnit = None
    borderRadius: int = -1
    backgroundColor = None
    
    hoverDistance: vars.validScreenUnit = 0
    _hoverSpeed: int = 0
    _hoverDifference: int = 0
    _hoverUp: bool = True
    
    antiAllias: bool = True

    textRect: Rect = Rect(0, 0, 0, 0)
    
    def __init__(self, *args, bold = False, italic = False):
        if len(args) == 4:
            fontSize = int(ScreenUnit.checkIfValidScreenUnit(args[2]))
            try:
                self.font = pygame.font.SysFont(args[1], fontSize)
            except:
                self.font = pygame.font.Font(args[1], fontSize)

            self.color = args[3]      
        else:
            self.font: pygame.font.Font = args[1]
            self.color = args[2]      
            
        self.text = args[0]
        self._renderText(self.text)

        self.font.bold = bold
        self.font.italic = italic 
    
    
    def setAntiAllias(self, active):
        self.antiAllias = active
        
    def setBackground(self, backgroundColor):
        self.backgroundColor = backgroundColor
        
    def setTextColor(self, color):
        self.color = color
        
    def setBorder(self, borderWidth, borderColor, borderRadius = -1):
        borderWidth, borderRadius = ScreenUnit.convertMultipleUnits(borderWidth, borderRadius)
        self.borderWidth = borderWidth
        self.borderColor = borderColor
        self.borderRadius = borderRadius
        
    def setHover(self, hoverDistance, speed = hoverSpeed.normal):
        self.hoverDistance = ScreenUnit.checkIfValidScreenUnit(hoverDistance)
        if isinstance(speed, hoverSpeed):
            self._hoverSpeed = speed.value
        else:
            self._hoverSpeed = speed

    def setText(self, text, bold = False, italic = False):
        self.text = text
        self.font.bold = bold
        self.font.italic = italic
        self._renderText(text)
    
    def _textHover(self, top):
        if self.hoverDistance > 0:
            if self._hoverUp:
                self._hoverDifference += 0.02 * self._hoverSpeed
            else: 
                self._hoverDifference -= 0.02 * self._hoverSpeed
            
            if self._hoverDifference > self.hoverDistance / 2:
                self._hoverUp = False
            if self._hoverDifference < -self.hoverDistance / 2:
                self._hoverUp = True  
            return top + self._hoverDifference
        
        return top
    
    def _renderText(self, text):
        self.textSurface = self.font.render(text, self.antiAllias, self.color)
        self.textHeight = self.textSurface.get_height()
        self.textWidth = self.textSurface.get_width()
        
    def _drawBase(self):
        if self.backgroundColor != None:
            Draw.rectangleFromRect(self.textRect, self.backgroundColor, self.borderRadius)
        if self.borderColor != None and self.borderWidth > 0:
            Draw.borderFromRect(self.textRect, self.borderWidth, self.borderColor, Draw.calculateOuterBorderRadius(self.borderRadius, self.borderWidth))
            
        
    def place(self, *args):
        if len(args) == 3:
            self.text = args[2]
        left, top = ScreenUnit.convertMultipleUnits(args[0], args[1])
        top = self._textHover(top)
        self.textRect = Rect(left, top, self.textWidth + 6, self.textHeight + 6)
        self._drawBase()
        vars.mainDisplay.blit(self.textSurface, (left + 3, top + 3))
        
    def placeCenterX(self, top: vars.validScreenUnit):
        pass
    
    def placeCenterY(self, left: vars.validScreenUnit):
        pass
    
    def placeCenterScreen(self):
        pass
    
    def placeInRect(self, *args):
        if len(args) == 4:
            self.setText(args[3])
        # top = self._textHover(top) # TODO add hover
        _rect: Rect = args[0]
        self.textRect = Rect(_rect.x, _rect.y, _rect.width + 6, _rect.height + 6)
        x, y = self._calculateTextPositioning(self.textRect, args[1], args[2])
        self._drawBase()
        vars.mainDisplay.blit(self.textSurface, (x + 3, y + 3))
        
    def _calculateTextPositioning(self, rect: Rect, xPositioning, yPositioning):
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
    
    
    # static functions
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
            
    def simpleText(text: str, left: vars.validScreenUnit, top: vars.validScreenUnit, font: pygame.font.Font = Font.H3, color: vars.RGBvalue = Color.BLACK, bold: bool = False, italic: bool = False):
        font.bold = bold
        font.italic = italic

        return vars.mainDisplay.blit(font.render(f"{text}", True, color), (left, top))
    
    def centerTextInRect(textSurface: pygame.Surface, rect: Rect):
        xPos = rect.x + (rect.width / 2) - (textSurface.get_width() / 2)
        yPos = rect.y + (rect.height / 2) - (textSurface.get_height() / 2)
        return xPos, yPos
    
    def textColorFromBackground(textRect: pygame.Rect):
        """
        calculates the textcolor based on the center pixel of the rect\n
        a dark color will return white and a light color will return black
        """
        pixelColor = Display.getPixelColorFromBackground(*textRect.center)
        lightColor = False
        for value in pixelColor:
            if value >= 125:
                lightColor = True
        return Color.BLACK if lightColor else Color.WHITE

    def textColorFromColor(color: vars.RGBvalue):
        lightColor = False
        for value in color:
            if value >= 125:
                lightColor = True
        return Color.BLACK if lightColor else Color.WHITE
            