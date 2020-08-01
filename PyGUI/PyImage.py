import os
os.environ['SDL_AUDIODRIVER'] = 'dsp'
import pygame

class Image(pygame.Surface):
    def __init__(self, Rect, Path=None, Alpha=True, Show=True):
        self.Rect, self.Path, self.Alpha = pygame.Rect(Rect), Path, Alpha
        self.Show = Show
        if self.Alpha: super(Image, self).__init__(self.Rect.size, pygame.SRCALPHA)
        else: super(Image, self).__init__(self.Rect.size, pygame.SRCALPHA)
        
        if type(self.Path) is str and type(self.Rect.size) is tuple and type(self.Alpha) is bool and \
           self.Rect.width > 0 and self.Rect.height > 0:
            self.blit(pygame.transform.scale(pygame.image.load(self.Path), self.Rect.size), (0,0))
    
    def ClickEvent(self):
        pass
    
    def Draw(self, *Surfaces):
        for Surface in Surfaces: Surface.blit(self, self.Rect)
