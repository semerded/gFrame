from importer import pygame
from components.interactions import Interactions
from elements.enums import mouseButton
import vars

class Image:
    def __init__(self, fileName: str, nameHint: str = "") -> None:
        self.image = pygame.image.load(fileName, nameHint)
        self.imageSize = self.getSize
        self.imagePosition = (0, 0)

    def resizeAndKeepProportions(self, width: float, height: float):
        aspectRatio = self.getAspectRatio
        imageWidth, imageHeight = self.getSize
        if aspectRatio < 1:
            width = int(imageWidth * aspectRatio)
        else:
            height = int(imageHeight / aspectRatio)
        self.resize(width, height)

    def resize(self, width, height):
        self.image = pygame.transform.scale(self.image, (width, height))
        self.imageSize = self.getSize

    def onMouseOver(self):
        return Interactions.onMouseOver(self.getImageRect)

    def onMouseClick(self, mouseButton: mouseButton):
        return Interactions.onMouseClickInRect(self.getImageRect, mouseButton)

    def isReleased(self, mouseButton: mouseButton):
        return Interactions.isReleasedInRect(self.getImageRect, mouseButton)

    def onMouseHold(self, mouseButton: mouseButton):
        return Interactions.onMouseHoldInRect(self.getImageRect, mouseButton)

    def place(self, xPosition: float, yPosition: float):
        self.imagePosition = (xPosition, yPosition)
        vars.mainDisplay.blit(self.image, self.imagePosition)

    @property
    def getAspectRatio(self):
        imageWidth, imageHeight = self.getSize
        return imageWidth / imageHeight

    @property
    def getSize(self):
        return self.image.get_size()

    @property
    def getPosition(self):
        return self.imagePosition

    @property
    def getImageRect(self):
        return pygame.Rect(*self.getPosition, *self.getSize)

    @property
    def getImage(self):
        return self.image