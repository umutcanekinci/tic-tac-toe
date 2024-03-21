import os
import sys
os.environ['SDL_AUDIODRIVER'] = 'dsp'
import pygame
from PyGUI.PyButton import Button
from PyGUI.PyImage import Image
from PyGUI.PyLabel import Label

class Window:
    def __init__(self, Title, Size, Color="white", ImagePath=None):
        
        pygame.init()
        #pygame.mixer.init()
        
        self.Tab, self.Tabs = "Main", {}
        self.CreateTab("Main", Title, Size, Color)
        self.Window = pygame.display.set_mode(self.Tabs[self.Tab][1])
        pygame.display.set_caption(self.Tabs[self.Tab][0])
        
        self.Run = True
        self.Clock = pygame.time.Clock()
        self.FPS = 60
        self.Show()

    def Show(self):
        self.Title = self.Tabs[self.Tab][0]
        self.Size = self.Width, self.Height = self.Tabs[self.Tab][1]
        self.Objects = self.Tabs[self.Tab][2]

        self.Events = pygame.event.get()
        self.MousePosition = pygame.mouse.get_pos()
        self.Keys = pygame.key.get_pressed()
        self.HandleEvents()
        self.Draw()

    def CreateTab(self, Tab, Title, Size, Color="white"):
        self.Tabs[Tab] = [Title, Size, pygame.Color(Color), {"Images" : {}, "Labels" : {}, "Buttons" : {}}]
    def CreateImage(self, Tab, Name, Rect, Path, Alpha=True, Show=True):
        self.Tabs[Tab][3]["Images"][Name] = Image(Rect, Path, Alpha, Show)
    def CreateLabel(self, Tab, Text, Color, Size, FontPath, Bold=False, Italic=False, Underline=False, Show=True):
        self.Tabs[Tab][3]["Labels"][Text] = Label(Text, Color, Size, FontPath, Bold, Italic, Underline, Show)
    def CreateButton(self, Tab, Text, Rect, IconPath=None, **kwargs):
        self.Tabs[Tab][3]["Buttons"][Text] = Button(Text, Rect, IconPath, **kwargs)

    def ChangeTab(self, Tab="Main"):
        if self.Tab != Tab and Tab in self.Tabs:
            self.Tab = Tab
            self.Window = pygame.display.set_mode(self.Tabs[self.Tab][1])
            pygame.display.set_caption(self.Tabs[self.Tab][0])
            pygame.display.update()

    def UpdateTab(self, Tab=None, **kwargs):
        if Tab is None:
            if "Title" in kwargs: self.Tabs[self.Tab][0] = kwargs["Title"]
            if "Size" in kwargs: self.Tabs[self.Tab][0] = kwargs["Size"]
            if "Color" in kwargs: self.Tabs[self.Tab][0] = pygame.Color(kwargs["Color"])
            if "Objects" in kwargs: self.Tabs[self.Tab][0] = kwargs["Objects"]
        else:
            if "Title" in kwargs: self.Tabs[Tab][0] = kwargs["Title"]
            if "Size" in kwargs: self.Tabs[Tab][0] = kwargs["Size"]
            if "Color" in kwargs: self.Tabs[Tab][0] = pygame.Color(kwargs["Color"])
            if "Objects" in kwargs: self.Tabs[Tab][0] = kwargs["Objects"]        

    def PlayMusic(self, Path):
        pygame.mixer.music.load(Path)
        pygame.mixer.music.play()

    def Draw(self):
        #self.Window.fill(pygame.Color(self.Tabs[self.Tab][2]))
        for self.Image in self.Tabs[self.Tab][3]["Images"].values():
            if self.Image.Show == True: self.Image.Draw(self.Window)
        for self.Label in self.Tabs[self.Tab][3]["Labels"].values():
            if self.Label.Show == True: self.Label.Draw(self.Window)
        for self.Button in self.Tabs[self.Tab][3]["Buttons"].values():
            if self.Button.Show == True: self.Button.Draw(self.Window, self.MousePosition)
        pygame.display.update()
    
    def HandleEvents(self):
        for self.Event in self.Events:   
            if self.Event.type == pygame.QUIT:
                self.Close()
            if self.Event.type == pygame.KEYDOWN:
                if self.Event.key == pygame.K_ESCAPE:
                    self.Close()
            #if self.Event.type == pygame.MOUSEMOTION:
            self.MouseOverObjects = []                
            if self.Event.type == pygame.MOUSEBUTTONDOWN:
                for Object in list(self.Tabs[self.Tab][3]["Images"].values()) + list(self.Tabs[self.Tab][3]["Buttons"].values()):
                    try:
                        if Object.Rect.collidepoint(pygame.mouse.get_pos()):
                            Object.ClickEvent()
                    except AttributeError:
                       pass

    def Close(self):
        self.Run = False
        pygame.quit()
        sys.exit()
