import gFrame.__init__ as game

GAME = game.AppConstructor("50dw", "50dh", manualUpdating=True)
game.Display.setAspectRatio(game.aspectRatios.ratio16to9, "50dw")

# slider = game.Slider((50, 30), 50, 300, game.Color.RED, borderRadius=50)
button = game.Button(("20vw", "30vh"), game.Color.GREEN, borderRadius=50)
button.setBorder("1vw", game.Color.AQUAMARINE)
button.text("hello", game.Font.H3, game.Color.BLACK)
# button.icon("test.jpg")



roundo = game.RoundButton(("20vw", "20vw"), game.Color.TEA_GREEN)

secondButton = game.Button(("10vw", "5vh"), game.Color.RED, borderRadius=1)
secondButton.text("disable", "ariel", "2vw", game.Color.BLACK, italic=True)

image = game.Image("test.jpg")
image.resize(50, 50)

text = game.Text("hello world!", "comic sans", "10vw", game.Color.BLACK)
# text.setHover(100)
text.setBackground(game.Color.AQUAMARINE)
text.setBorder(5, game.Color.BITTERSWEET, 5)

slider = game.Slider((200, 50), 0, 100, game.Color.BITTERSWEET)
slider.setKnob(25, game.Color.BLUE)

@game.debugging
def main():
    GAME.eventHandler()
    GAME.fill(game.Color.WHITE)
    
    button.addBorderOnPressing("2vw", game.Color.ORANGE)    
    button.changeColorOnHover(game.Color.RED)
    button.place("30vw", "30vh")
    
    secondButton.addBorderOnHover("1vw", game.Color.BLUE)
    secondButton.place("60vw", "30vh")

    
    # if button.isReleased():
    #     print("clicked the button")
        
    # if button.isHeldFor(2000):
    #     print("held done")
        
    if button.isDoubleClicked():
        bleh = ... * 5
        
    if secondButton.isClicked():
        if button.getWidgetStatus:
            button.disable()
        else:
            button.enable()
    image.place(50, 50)
    
    slider.place(500, 10)
    print(slider.getValue())
    
    # roundo.place(10, 10)
    
    text.placeInRect(game.Rect(("80vw", "20vh"), (200, 200)), game.xTextPositioning.right, game.yTextPositioning.bottom)
    


# main()