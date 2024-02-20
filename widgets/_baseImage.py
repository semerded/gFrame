from importer import pygame
from components.screenUnits import ScreenUnit
import vars

class _BaseImage:
    def __init__(self, fileName: str, nameHint: str = "") -> None:
        self.image = pygame.image.load(fileName, nameHint)
        self.imageSize = self.getImageSize
        
    def resizeImageAndKeepProportions(self, width: float, height: float):
        aspectRatio = self.getAspectRatio
        imageWidth, imageHeight = self.getImageSize
        if aspectRatio < 1:
            width = int(imageWidth * aspectRatio)
        else:
            height = int(imageHeight / aspectRatio)
        self.resizeImage(width, height)
        
    def resizeImage(self, width, height):
        self.image = pygame.transform.scale(self.image, (width, height))
        self.imageSize = self.getImageSize
        
    def _baseImagePlace(self, left, top):
        left, top = ScreenUnit.convertMultipleUnits(left, top)
        self.imagePosition = (left, top)
        vars.mainDisplay.blit(self.image, self.imagePosition)
        
    @property
    def getImageSize(self):
        return self.image.get_size()
    
    @property
    def getImage(self):
        return self.image
    
    @property
    def getAspectRatio(self):
        imageWidth, imageHeight = self.getImageSize
        return imageWidth / imageHeight