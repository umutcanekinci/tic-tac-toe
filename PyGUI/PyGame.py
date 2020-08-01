import os
import sys
os.environ['SDL_AUDIODRIVER'] = 'dsp'
import pygame
from PyGUI.PyWindow import Window

class Game():

    def __init__(self, Title="Game", Size=[500, 500], Color="white", ImagePath=None, Objects={"Buttons" : {}, "Images" : {}}):

        pygame.init()
        self.MainWindow = Window(Title, Size, Color, ImagePath, Objects)

    def Start(self):
        while True:
            self.MousePosition = pygame.mouse.get_pos()
            self.Keys = pygame.key.get_pressed()

            for self.Event in pygame.event.get():
                if self.Event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if self.Event.type == pygame.KEYDOWN:
                    if self.Event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

            self.MainWindow.Draw(self.MousePosition)
