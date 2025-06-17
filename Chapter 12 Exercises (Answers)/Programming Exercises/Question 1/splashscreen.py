# a)
from graphics import *
from button import Button

class SplashScreen:

    def __init__(self):
        self.win = GraphWin("Splash Screen", 600, 700)
        self.win.setBackground("black")
        banner = Text(Point(300,20), "Dice Poker")
        banner.setSize(24)
        banner.setFill("yellow2")
        banner.setStyle("bold")
        banner.draw(self.win)
        self.msg = Text(Point(300,60), "Poker, not cards, but with random dice throws")
        self.msg.setSize(18)
        self.msg.setFill("white")
        self.msg.draw(self.win)
        self.play = Button(self.win, Point(300,620), 150, 40, "Let's Play")
        self.exit = Button(self.win, Point(300,670), 150, 40, "Exit")
        self.play.activate()
        self.exit.activate()

        # c)
        self.msg = Text(Point(300,150), "HALL OF FAME")
        self.msg.setSize(24)
        self.msg.setFill("gold3")
        self.msg.setStyle("bold")
        self.msg.draw(self.win)
        x = 100
        for i in ["RANK", "SCORE", "NAME"]:
            self.msg = Text(Point(x,200), i)
            self.msg.setSize(24)
            self.msg.setFill("purple")
            self.msg.setStyle("bold")
            self.msg.draw(self.win)
            x = x + 200
        y, j = 240, 0
        infile = open('highscore.txt', 'r')
        color = ["grey", "red", "orange", "pink", "yellow4", "yellow", "lightgreen", "lightblue", "blue", "green"]
        for i in infile.read().rstrip().split("\t"):
            rank, score, name = i.split(",")
            x = 100
            self.msg = Text(Point(x,y), rank)
            self.msg.setSize(20)
            self.msg.setFill(color[j])
            self.msg.setStyle("bold")
            self.msg.draw(self.win)
            x = x + 200
            self.msg = Text(Point(x,y), score)
            self.msg.setSize(20)
            self.msg.setFill(color[j])
            self.msg.setStyle("bold")
            self.msg.draw(self.win)
            x = x + 200
            self.msg = Text(Point(x,y), name)
            self.msg.setSize(20)
            self.msg.setFill(color[j])
            self.msg.setStyle("bold")
            self.msg.draw(self.win)
            y = y + 35
            j = j + 1
        infile.close()

    def enter(self):
        p = self.win.getMouse()
        while True:
            if self.play.clicked(p):
                self.win.close()
                return True
            elif self.exit.clicked(p):
                self.win.close()
                return False
            else:
                p = self.win.getMouse()
