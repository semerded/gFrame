import pygame
from . import data
pygame.font.init()

class Font:
    H1 = pygame.font.SysFont(data.globalFontPath, 34)
    H2 = pygame.font.SysFont(data.globalFontPath, 30)
    H3 = pygame.font.SysFont(data.globalFontPath, 24)
    H4 = pygame.font.SysFont(data.globalFontPath, 20)
    H5 = pygame.font.SysFont(data.globalFontPath, 18)
    H6 = pygame.font.SysFont(data.globalFontPath, 16)
    XXSMALL = pygame.font.SysFont(data.globalFontPath, 8)
    XSMALL = pygame.font.SysFont(data.globalFontPath, 12)
    SMALL = pygame.font.SysFont(data.globalFontPath, 14)
    MEDIUM = pygame.font.SysFont(data.globalFontPath, 28)
    LARGE = pygame.font.SysFont(data.globalFontPath, 38)
    XLARGE = pygame.font.SysFont(data.globalFontPath, 46)
    XXLARGE = pygame.font.SysFont(data.globalFontPath, 60)
    XXXLARGE = pygame.font.SysFont(data.globalFontPath, 72)
    FONT50 = pygame.font.SysFont(data.globalFontPath, 50)
    FONT100 = pygame.font.SysFont(data.globalFontPath, 100)
    FONT150 = pygame.font.SysFont(data.globalFontPath, 150)

    def createFont(size, font = None):
        if font == None:
            return pygame.font.SysFont(data.globalFontPath, size)
        try:
            return pygame.font.SysFont(font, size)
        except:
            return pygame.font.Font(font, size)
    