from ..baseImporter import pygame
import sys

def debugging(func):
    while True:
        try:
            func()
        except Exception as error:
            print(error) # add loop count or logger
            
def production(func):
    while True:
        try:
            func()
        except KeyboardInterrupt:
            print("program exited with CRTL-C")
            pygame.quit()
            sys.exit()
            
def logging(func):
    pass