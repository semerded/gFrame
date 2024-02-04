import __init__ as game

GAME = game.AppConstructor(500, 500)

slider = game.Slider((50, 30), 50, 300, game.Color.RED, borderRadius=50)

while True:
    GAME.eventHandler(game.pygame.event.get())
    GAME.maindisplay.fill(game.Color.WHITE)
    
    print(slider.place(100, 100))
    GAME.updateDisplay()