from ..baseImporter import pygame

class Audio:
    def __init__(self, filePath: str) -> None:
        self.soundObject = pygame.mixer.Sound(filePath)
        
    def play(self):
        self.soundObject.play(-1)
        
    def stop(self):
        self.soundObject.stop()