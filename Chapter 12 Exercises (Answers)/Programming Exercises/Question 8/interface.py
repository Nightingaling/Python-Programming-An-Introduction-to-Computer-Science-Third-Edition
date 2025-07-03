from graphics import *
from button import Button

class Interface:

    def __init__(self):
        # draw connect4 board
        self.win = GraphWin('Connect 4', 500, 550)
        board = Rectangle(Point(25,75), Point(475,525)).draw(self.win)
        x = 65
        y = 115
        for i in range(7):
            for j in range(6):
                Circle(Point(x,y), 20).draw(self.win)
                y = y + 75
            x = x + 60
            y = 115
        # draw buttons
        x = 65
        y = 75
        self.button = []
        n = 1
        b1 = b2 = b3 = b4 = b5 = b6 = b7 = 0
        for i in [b1,b2,b3,b4,b5,b6,b7]:
            i = Button(self.win, Point(x,y), 40, 20, n)
            self.button.append(i)
            i.activate()
            x = x + 60
            n = n + 1
        # draw player Turn message
        self.msg = Text(Point(250,30), 'Player 1 Turn')
        self.msg.setStyle('bold')
        self.msg.setSize(24)
        self.msg.setFill('red')
        self.msg.draw(self.win)

    def drawToken(self, centerPoint, color):
        token = Circle(Point(centerPoint[0], 115), 20)
        token.setFill(color)
        token.draw(self.win)
        while token.getCenter().getY() != centerPoint[1]:
            token.move(0,1)
            update(360)

    def updatePlayerTurn(self, player, color):
        self.msg.setText('{0} Turn'.format(player))
        self.msg.setFill(color)

    def ButtonClicked(self):
        while True:
            p = self.win.getMouse()
            for button in self.button:
                if button.clicked(p):
                    return self.button.index(button)

    def updateResult(self, result):
        if result == 'Tie':
            self.msg.setText('Game {0}!'.format(result))
            self.msg.setFill('black')
        else:
            self.msg.setText('{0} win!'.format(result))
            self.msg.setFill('green')
        self.win.getMouse()
        self.win.close()
