from time import perf_counter, sleep

class Clock:
    
    def __init__(self, fps):
        self.start = perf_counter()
        self.fps = fps
        self.frame_length = 1/fps
    @property
    def tick(self):
        return int((perf_counter() - self.start)/self.frame_length)

    def sleep(self, fps = ...):
        if fps != ... and fps != self.fps:
            self.fps = fps
            self.frame_length = 1/fps
            
        r = self.tick + 1
        while self.tick < r:
            sleep(1/1000)
            
    