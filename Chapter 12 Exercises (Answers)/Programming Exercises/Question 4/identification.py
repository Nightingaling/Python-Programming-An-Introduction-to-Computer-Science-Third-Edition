from graphics import *
from button import Button

class Identification:

    def __init__(self):
        self.win = GraphWin("ATM", 300, 300)
        self.win.setBackground("black")
        self.text = Text(Point(150,25),"Welcome to OCBC ATM").draw(self.win)
        self.text.setFill('white')
        self.text.setStyle('bold')
        self.text.setSize(15)
        self.text = Text(Point(75,70),"User ID:").draw(self.win)
        self.text.setFill('white')
        self.ID = Entry(Point(150,70),10).draw(self.win)
        self.text = Text(Point(90,100),"Pin:").draw(self.win)
        self.text.setFill('white')
        self.pin = Entry(Point(150,100),10).draw(self.win)
        self.submit = Button(self.win, Point(150,150), 60, 30, "Submit")
        self.submit.activate()

    def getEntry(self):
        p = self.win.getMouse()
        while not self.submit.clicked(p):
            p = self.win.getMouse()
        return self.ID.getText(), self.pin.getText()

    def fail(self):
        self.text = Text(Point(150,50),'Incorrect ID or Pin. Please try again.')
        self.text.setFill('white')
        self.text.draw(self.win)
        self.ID.setText("")
        self.pin.setText("")

    def close(self):
        self.win.close()
