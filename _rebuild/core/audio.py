import pygame

class AudioObject:
    def __init__(self, filePath, volume = 100, loops = 0, maxtime_ms = 0, fade_ms = 0) -> None:
        self.soundObject = pygame.mixer.Sound(filePath)
        self.soundObject.set_volume(volume / 100)
        self.loops = loops
        self.maxtime_ms = maxtime_ms
        self.fade_ms = fade_ms
        
    def play(self):
        self.soundObject.play(self.loops, self.maxtime_ms, self.fade_ms)
        
    def stop(self):
        self.soundObject.stop()
        
    def setVolume(self, volume):
        self.soundObject.set_volume(volume / 100)
    
        
class AudioQueue:
    def add(self, filePath, volume = 100, loops = 0, maxtime_ms = 0, fade_ms = 0):
        pass