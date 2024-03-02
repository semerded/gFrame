from importer import pygame
from typing import overload
import vars

class Rect(pygame.Rect):
    @overload
    def __init__(self, left: vars.validScreenUnit, top: vars.validScreenUnit, width: vars.validScreenUnit, height: vars.validScreenUnit) -> None: ...
    @overload
    def __init__(self, positionCord: vars.coordinate, size: list[vars.validScreenUnit]) -> None: ...
    
    def unpack(self) -> tuple[int]: ...