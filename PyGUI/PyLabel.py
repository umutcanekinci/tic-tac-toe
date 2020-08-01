import os
os.environ['SDL_AUDIODRIVER'] = 'dsp'
import pygame

class Label(pygame.Surface):
    def __init__(self, Text, Color, Size, Pos, FontPath, Bold=False, Italic=False, Underline=False, Show=True):
        self.Pos = Pos
        self.Show = Show
        self.Font = pygame.font.Font(FontPath, Size)
        self.Font.set_bold(Bold)
        self.Font.set_italic(Italic)
        self.Font.set_underline(Underline)
        self.Text = self.Font.render(Text, True, pygame.Color(Color))
        super(Label, self).__init__((self.Text.get_width(), self.Text.get_height()), pygame.SRCALPHA)
        self.blit(self.Text, (0, 0))
    
    def Draw(self, *Surfaces):
        for Surface in Surfaces:
            if self.Pos[0] == "Center": self.Pos[0] = (Surface.get_width() - self.Text.get_width())//2
            if self.Pos[1] == "Center": self.Pos[1] = (Surface.get_height() - self.Text.get_height())//2
            Surface.blit(self, self.Pos)
