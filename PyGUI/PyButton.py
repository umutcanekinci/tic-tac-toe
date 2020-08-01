import os
os.environ['SDL_AUDIODRIVER'] = 'dsp'
import pygame
from PyGUI.PyImage import Image


class Button:
    def __init__(self, Text, Rect, IconPath=None, FontPath=None, Bold=False, TextSize=15, IconSize=[32, 32], Border=-1, CornerRadius=1, Color=["white", "white"], TextColor=["black", "black"], BorderColor=["black", "black"], TextSide="Center", IconSide="CenterLeft", Show=True):
        self.Show = Show
        self.Rect, self.Font, self.Border = pygame.Rect(Rect), pygame.font.Font(FontPath, TextSize), Border
        self.Color, self.TextColor, self.BorderColor = [pygame.Color(Color[0]), pygame.Color(Color[1])],\
                                                  [pygame.Color(TextColor[0]), pygame.Color(TextColor[1])],\
                                                  [pygame.Color(BorderColor[0]), pygame.Color(BorderColor[1])]
        self.Font.set_bold(Bold)
        self.Text = [self.Font.render(Text, True, self.TextColor[0]), self.Font.render(Text, True, self.TextColor[1])]

		# Surfaces
        self.Surface = pygame.Surface(self.Rect.size, pygame.SRCALPHA)
        self.MouseOverSurface = self.Surface.copy()

        # Colors
        pygame.draw.rect(self.Surface, self.Color[0], [[0,0], self.Rect.size], 0, CornerRadius)
        pygame.draw.rect(self.MouseOverSurface, self.Color[1], [[0, 0], self.Rect.size], 0, CornerRadius)

        # Borders
        if self.Border > 0:
            pygame.draw.rect(self.Surface, self.BorderColor[0], [[0, 0], self.Rect.size], self.Border, CornerRadius)
            pygame.draw.rect(self.MouseOverSurface, self.BorderColor[1], [[0, 0], self.Rect.size], self.Border, CornerRadius)

        # Icons
        if type(IconPath) is str:
            if type(Text) is str and Text.replace(" ", "") != "":
                self.IconRect = pygame.Rect([(self.Rect.width - IconSize[0] - 10 - self.Text[0].get_width())//2, (self.Rect.height - IconSize[1])//2], IconSize)
            else:
                self.IconRect = pygame.Rect([(self.Rect.width - IconSize[0])//2, (self.Rect.height - IconSize[1])//2], IconSize)
            
            self.Icon = Image(IconRect, IconPath)
            self.Icon.Draw(self.Surface, self.MouseOverSurface)

            # Texts
            self.Surface.blit(self.Text[0], [self.IconRect.x + self.IconRect.width + 10, (self.Rect.height - self.Text[0].get_height())//2])
            self.MouseOverSurface.blit(self.Text[1], [self.IconRect.x + self.IconRect.width + 10, (self.Rect.height - self.Text[0].get_height())//2])
        else:
            # Texts
            self.Surface.blit(self.Text[0], [(self.Rect.width - self.Text[0].get_width())//2, (self.Rect.height - self.Text[0].get_height())//2])
            self.MouseOverSurface.blit(self.Text[1], [(self.Rect.width - self.Text[0].get_width())//2, (self.Rect.height - self.Text[0].get_height())//2])

    def MouseOver(self, MousePosition):
        return self.Rect.collidepoint(MousePosition)
    
    def ClickEvent(self):
        pass

    def Draw(self, Surface, MousePosition):
        if self.MouseOver(MousePosition): Surface.blit(self.MouseOverSurface, self.Rect)
        else: Surface.blit(self.Surface, self.Rect)
