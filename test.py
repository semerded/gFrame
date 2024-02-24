import __init__ as game

GAME = game.AppConstructor("50dw", "50dh")

# slider = game.Slider((50, 30), 50, 300, game.Color.RED, borderRadius=50)
button = game.Button(("20vw", "30vh"), game.Color.GREEN, 50)
button.border("1vw", game.Color.AQUAMARINE)
button.text("hello")
# button.icon("test.jpg")

secondButton = game.Button(("10vw", "5vh"), game.Color.RED, 3)
secondButton.text("disable")

image = game.Image("test.jpg")

while True:
    GAME.eventHandler()
    GAME.fill(game.Color.WHITE)
    
    button.addBorderOnPressing("2vw", game.Color.ORANGE)    
    button.changeColorOnHover(game.Color.RED)
    button.place("30vw", "30vh")
    
    secondButton.addBorderOnHover("1vw", game.Color.BLUE)
    secondButton.place("60vw", "30vh")
    
    if secondButton.isClicked():
        if button.getWidgetStatus:
            button.disable()
        else:
            button.enable()
        
    
    if button.isClicked():
        print(True)


