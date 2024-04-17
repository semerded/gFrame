from ..baseImporter import pygame
import sys, traceback

def debugging(func):
    print("\033[93mDebugging is enabled")
    while True:
        try:
            func()
        except KeyboardInterrupt:
            print("program exited with CRTL-C")
            pygame.quit()
            sys.exit()
            
        except Exception as error:
            ex_type, ex, tb = sys.exc_info()
            print(f"\033[1;91man error occured: {ex_type.__name__} -> {ex}") # add loop count or logger
            print("\033[0;94m\n### traceback ###")
            traceback.print_tb(tb)
            print("\033[97;40m")
            
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