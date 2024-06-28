import os
os.environ['SDL_AUDIODRIVER'] = 'dsp'
import pygame
from PyGUI.PyWindow import Window


class Game(Window):

    def __init__(self):
        super(Game, self).__init__("TicTacToe", [300, 500], "gray")

        
        FontPath = "fonts/comic.ttf"
        ButtonProperties = {"Color" : ["gray", "pink"],
                            "TextSize" : 20,
                            "TextColor" : ["red", "red"],
                            "FontPath" : FontPath}

        
        self.CreateImage("Main", "Background", [[0, 0], self.Size], "images/background.jpg")
        self.CreateImage("Main", "Logo", [(self.Width - 300)//2, 20, 300, 75], "images/logo.png")
        self.CreateImage("Main", "Music", [240, 440, 48, 48], "images/music.png")
        self.CreateImage("Main", "NoMusic", [240, 440, 48, 48], "images/nomusic.png", Show=False)
        self.CreateLabel("Main", "Made by Umutcan Ekinci", "white", 17, ["Center", 470], FontPath)
        self.CreateButton("Main", "Player vs. Computer", [(self.Width - 200)//2, 155, 200, 50], **ButtonProperties)
        self.CreateButton("Main", "Player vs. Player", [(self.Width - 200)//2, 225, 200, 50], **ButtonProperties)
        self.CreateButton("Main", "Exit", [(self.Width - 200)//2, 295, 200, 50], **ButtonProperties)
        self.Tabs["Main"][3]["Buttons"]["Exit"].ClickEvent = self.Close
        self.Tabs["Main"][3]["Images"]["Music"].ClickEvent = self.Music
        self.Tabs["Main"][3]["Buttons"]["Player vs. Player"].ClickEvent = self.PvP
        self.Tabs["Main"][3]["Buttons"]["Player vs. Computer"].ClickEvent = self.PvC
        
        self.CreateTab("Game", "TicTacToe", [300, 500], "gray")
        self.CreateLabel("Game", "TURN", "red", 25, ["Center", 20], FontPath, True, False, False)
        #self.PlayMusic("sounds/music.mp3")

        while self.Run: self.Show()

    def PvP(self):
        self.ChangeTab("Game")
        #pygame.draw.line(self.Window, pygame.Color("black"), (75, 325), (225, 325))
        #pygame.draw.line(self.Window, pygame.Color("black"), (75, 375), (225, 375))
        #pygame.draw.line(self.Window, pygame.Color("black"), (125, 275), (125, 425))
        #pygame.draw.line(self.Window, pygame.Color("black"), (175, 275), (175, 425))

    def PvC(self):
        self.ChangeTab("Game")
        #pygame.draw.line(self.Window, pygame.Color("black"), (75, 325), (225, 325), 5)
        #pygame.draw.line(self.Window, pygame.Color("black"), (75, 375), (225, 375), 5)
        #pygame.draw.line(self.Window, pygame.Color("black"), (125, 275), (125, 425), 5)
        #pygame.draw.line(self.Window, pygame.Color("black"), (175, 275), (175, 425), 5)

    def Music(self):
        
        self.Tabs["Main"][3]["Images"]["NoMusic"].Show = not self.Tabs["Main"][3]["Images"]["NoMusic"].Show

if __name__ == "__main__": Game()
