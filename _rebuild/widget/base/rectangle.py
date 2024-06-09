from ...widget._basewidget import _BaseWidget
class Rectangle(_BaseWidget):
    def __init__(self, size, color, cornerRadius=-1) -> None:
        super().__init__(size, color, cornerRadius)
        
    def place(self, left, top):
        self.addToRenderQueue()
