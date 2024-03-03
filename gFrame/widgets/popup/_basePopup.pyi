from typing import overload
import vars

class _BasePopup:
    def __init__(self, size: tuple[vars.validScreenUnit], backgroundColor: vars.RGBvalue, borderWidth: vars.validScreenUnit, borderColor: vars.RGBvalue, discardWhenClickedOutsidePopup: bool = True) -> None: ...
    
    def place(self) -> None: ...
    
    