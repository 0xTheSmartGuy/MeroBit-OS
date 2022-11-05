import pygame, shelve
import pygame_widgets
from pygame_widgets.widget import WidgetBase
from pygame_widgets.mouse import Mouse, MouseState

class OpixxWidget(WidgetBase): # With help of code @AustL GitHub
    REPEAT_DELAY = 4
    REPEAT_INTERVAL = 7
    CURSOR_INTERVAL = 4
    def __init__(self, file, win, x, y, width, height, isSubWidget=False, **kwargs):
        super().__init__(win, x, y, width, height, isSubWidget)
        self.selected=False
        self.showCursor=False
        self.cursorTime=0
        self.cursorPosition=0
        self.repeatTime=0
        self.repeatKey=None
        self.firstRepeat=True
        self.keyDown=False
        self.file=file
        self.escape=False
        self.maxLengthReached=False
        self.borderThickness=kwargs.get('borderThickness', 3)
        self.borderColour=kwargs.get('borderColour', (0, 0, 0))
        self.radius=kwargs.get('radius', 0)
        self.cursorOffsetTop=self._height // 6
    def opixx_open(self, scrn, x, y):
       a=shelve.open(self.file, writeback=False)
       w=pygame.PixelArray(scrn)
       w[a[0], a[1]]=(255, 255, 0)
       
