import pygame
pygame.init()

# LibSzk can be integrated to LibGrphc
class Windows:
     def __init__(self, width, height, wintitle, bgcolr):
        self.width = width
        self.height = height
        self.z = [self.width, self.height]
        self.screen_display = pygame.display
        self.screen_display.set_caption(wintitle)
        self.surface = self.screen_display.set_mode(z)
        self.window = True
     def mainloop(self):
        while self.window:
             for event in pygame.event.get():
                 if event.type == pygame.QUIT:
                     self.window = False
             self.surface.blit(bgcolr)
             self.screen_display.update()
        pygame.quit()
