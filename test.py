import __init__ as game

GAME = game.AppConstructor("50dw", "50dh")

# slider = game.Slider((50, 30), 50, 300, game.Color.RED, borderRadius=50)
button = game.Button(("20vw", "30vh"), game.Color.GREEN)

while True:
    GAME.eventHandler()
    game.Display.fill(game.Color.WHITE)
    
    button.place("30vw", "30vh")
    
    print(button.isClicked())
    
    
    game.Updating.updateDisplay()


