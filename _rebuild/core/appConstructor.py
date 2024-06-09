import pygame
from .. import data
from ..colors import Color

try:
    import win32api
    import win32gui
    import win32con
    compatibleTransparentBackground = True
except ImportError:
    compatibleTransparentBackground = False
    

class AppConstructor:
    def __init__(self, width, height, backgroundColor = Color.BLACK, selectedDisplay = 0, fullscreen = False, resizable = False, noFrame = False, scaled = False, openHidden = False, vsync = False, autoUpdate=True) -> None:
        
        data.appWidth, data.appHeight = width, height
        data.autoUpdate = autoUpdate
        data.appFlags = AppConstructor._updateFlags(resizable, noFrame, scaled)
        
        data.backgroundColor = backgroundColor
        
        data.selectedDisplay = selectedDisplay if pygame.display.get_num_displays() >= selectedDisplay else 0
        
        data.mainDisplay = pygame.display.set_mode((width, height), *data.appFlags, display=selectedDisplay, vsync= 1 if vsync else 0).convert()
        data.canvas = pygame.Surface((width, height)).convert()
    
    @staticmethod  
    def _updateFlags(resizable, noFrame, scaled):
        flags = []
        if resizable:
            flags.append(pygame.RESIZABLE)
        if noFrame:
            flags.append(pygame.NOFRAME)
        if scaled:
            flags.append(pygame.SCALED)
        return tuple(flags)
    
    if compatibleTransparentBackground: 
        @staticmethod
        def transparentWindow():
            data.backgroundColor = (1, 1, 1)
            hwnd = pygame.display.get_wm_info()["window"]
            win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                        win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
            win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*(1, 1, 1)), 0, win32con.LWA_COLORKEY)