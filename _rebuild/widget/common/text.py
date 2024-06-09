from ...colors import Color
from ...fonts import Font


class Text:
    def __init__(self, text: str, *args, color = Color.BLACK) -> None:
        pass
    
    
    @classmethod
    def H1(cls, text, color = Color.BLACK):
        return cls(text, Font.H1, color)
    
    @classmethod
    def H2(cls, text, color = Color.BLACK):
        return cls(text, Font.H2, color)