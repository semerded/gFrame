import pygame
import sys
from .. import data


def exit(exitCode: int):
    data.running = False
    pygame.quit()
    print("Code Exited With: %s" % exitCode)
    sys.exit(exitCode)
