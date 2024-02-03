from pygameaddons import *

APP = AppConstructor(500, 500, pygame.RESIZABLE)
clock = pygame.time.Clock()

APP.setMinimumScreenDimensions(300, 300)
APP.centerScreen()

testButton = Button((50, 50), Color.GREEN, 20)
testButton.text("hello world!", Font.H2)
testButton.border(5, Color.BLUE)


while True:
    APP.eventHandler(pygame.event.get())
    clock.tick(60)
    APP.maindisplay.fill((255, 0, 0))
    
    testButton.place(200, 200)
    
    if testButton.onMouseOver():
        print("1")
        
    testButton.changeColorOnMouseClick(Color.WHITE)
    
    
    
    
    

