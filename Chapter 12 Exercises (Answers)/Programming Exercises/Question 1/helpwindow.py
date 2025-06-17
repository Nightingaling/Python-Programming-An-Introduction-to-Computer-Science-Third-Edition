# b)
from graphics import *

class HelpWindow:

    def __init__(self):
        self.win = GraphWin("Help", 350, 150)
        self.win.setBackground("green3")
        Text(Point(20,10), "Hand").draw(self.win)
        Text(Point(330,10), "Pay").draw(self.win)
        Line(Point(0,20), Point(400,20)).draw(self.win)
        Text(Point(35,30), "Two Pairs").draw(self.win)
        Text(Point(330,30), "$ 5").draw(self.win)
        Text(Point(53,50), "Three of a Kind").draw(self.win)
        Text(Point(330,50), "$ 8").draw(self.win)
        Text(Point(143,70), "Full House (A Pair and a Three of a Kind)").draw(self.win)
        Text(Point(325,70), "$ 12").draw(self.win)
        Text(Point(50,90), "Four of a Kind").draw(self.win)
        Text(Point(325,90), "$ 15").draw(self.win)
        Text(Point(65,110), "Straight(1-5 or 2-6)").draw(self.win)
        Text(Point(325,110), "$ 20").draw(self.win)
        Text(Point(49,130), "Five of a Kind").draw(self.win)
        Text(Point(325,130), "$ 30").draw(self.win)
