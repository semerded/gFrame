import pygame
from .. import gID, data
from ..colors import Color
from ._widgetrect import _WidgetRect
from ..core.rect import Rect

globalFont = ...

class _BaseText(_WidgetRect):
    antiAllias = True
    textSurface = None
    textWidth = 0
    textHeight = 0
    
    def __init__(self, text: str, font = globalFont, fontsize = globalFont, color = Color.BLACK, bold = False, italic = False) -> None:
        
        if font == globalFont and fontsize == globalFont:
            self.font = data.globalFont
        else:
            try:
                self.font = pygame.font.SysFont(font, fontsize)
            except:
                self.font = pygame.font.Font(font, fontsize)
            
        self.font.bold = bold
        self.font.italic = italic
        self.text = str(text)
        self.color = color
        self._renderText(text) 
        
        super().__init__((self.textWidth, self.textHeight))
        
    def setAntiAllias(self, status):
        self.antiAllias = status
        self._renderText(self.text)
        
    def setText(self, text, bold = False, italic = False):
        self.text = text
        self.font.bold = bold
        self.font.italic = italic
        self._renderText(text)
    
    def _renderText(self, text):
        self.textSurface = self.font.render(text, self.antiAllias, self.color)
        self.textHeight = self.textSurface.get_height()
        self.textWidth = self.textSurface.get_width()
        
    def placeText(self, left, top):
        super().updateRect(left, top)
        data.mainDisplay.blit(self.textSurface, (left + 3, top + 3))
    
    def placeTextInRect(self, rect: Rect, rw = 50, rh = 50):
        super().updateRect(rect.x, rect.y)
        widthRange = rect.width - self.textWidth
        heightRange = rect.height - self.textHeight
        data.mainDisplay.blit(self.textSurface, ((widthRange / 100 * rw) / 2, (heightRange / 100 * rh / 2)))
        
        