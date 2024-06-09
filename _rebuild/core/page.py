from .. import data

class Page:
    def addPage(pageName: str, pageObject: 'PageConstructor'):
            data.pages[pageName] = pageObject
            
    def switchPage(pageName: str):
        pass
    
    
class PageConstructor:
    def __init__(self, pageName, pageDrawer, *drawerArgs) -> None:
        self.pageName = pageName
        self.pageDrawer = pageDrawer
        self.drawerArgs = drawerArgs
        
    def draw(self):
        self.pageDrawer(*self.drawerArgs)