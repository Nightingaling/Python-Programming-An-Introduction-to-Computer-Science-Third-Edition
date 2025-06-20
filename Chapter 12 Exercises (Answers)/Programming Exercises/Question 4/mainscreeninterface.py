from graphics import *
from button import Button

class MainScreenInterface:

    def __init__(self):
        self.win = GraphWin("ATM", 500, 500)
        self.logo = Text(Point(38,20), "OCBC")
        self.logo.setFill('red')
        self.logo.setStyle('bold')
        self.logo.setSize(10)
        self.logo.draw(self.win)
        self.msg = Text(Point(40,60),'Hello!').draw(self.win)
        self.msg = Text(Point(134,80),'What would you like to do today?').draw(self.win)
        self.msg = Text(Point(55,200),'Get Cash')
        self.msg.setStyle('bold')
        self.msg.draw(self.win)
        self.msg = Text(Point(325,200),'Non Cash Services')
        self.msg.setStyle('bold')
        self.msg.draw(self.win)
        self.hundred = Button(self.win, Point(70,260), 100, 50, "$100")
        self.twohundred = Button(self.win, Point(180,260), 100, 50, "$200")
        self.fivehundred = Button(self.win, Point(70,320), 100, 50, "$500")
        self.thousand = Button(self.win, Point(180,320), 100, 50, "$1000")
        self.others = Button(self.win, Point(125,380), 210, 50, "Other Cash Amounts")
        self.enquiry = Button(self.win, Point(305,290), 110, 110, "Balance\nEnquiry")
        self.transfer = Button(self.win, Point(425,290), 110, 110, "Fund\nTransfer")
        self.exit = Button(self.win, Point(480,20), 30, 30, "Exit")
        self.hundred.activate()
        self.twohundred.activate()
        self.fivehundred.activate()
        self.thousand.activate()
        self.others.activate()
        self.enquiry.activate()
        self.transfer.activate()
        self.exit.activate()

    def servicesPressed(self):
        p = self.win.getMouse()
        if self.hundred.clicked(p):
            amt = 100
            return 'withdraw', amt
        elif self.twohundred.clicked(p):
            amt = 200
            return 'withdraw', amt
        elif self.fivehundred.clicked(p):
            amt = 500
            return 'withdraw', amt
        elif self.thousand.clicked(p):
            amt = 1000
            return 'withdraw', amt
        elif self.others.clicked(p):
            return self.otherAmt()
        elif self.enquiry.clicked(p):
            return 'enquiry', None
        elif self.transfer.clicked(p):
            return self.Transfer()
        elif self.exit.clicked(p):
            return self.quit()
        else:
            return '', None

    def Transfer(self):
        win = GraphWin('Transfer', 400, 250)
        self.msg = Text(Point(200,20), "Transfer Confirmation")
        self.msg.setStyle('bold')
        self.msg.setSize(16)
        self.msg.draw(win)
        Rectangle(Point(50,40), Point(350,160)).draw(win)
        Rectangle(Point(50,170), Point(350,200)).draw(win)
        Line(Point(200,40), Point(200,160)).draw(win)
        Text(Point(150,185), "Amount: $").draw(win)
        amtEntry = Entry(Point(235,185), 10).draw(win)
        left = Button(win, Point(125,100), 100, 100, "Checking\n↓\nSavings")
        right = Button(win, Point(275,100), 100, 100, "Savings\n↓\nChecking")
        cont = Button(win, Point(200,220), 70, 20, "Confirm")
        left.activate()
        right.activate()
        while True:
            p = win.getMouse()
            if left.clicked(p):
                left.rect.setFill('green')
                right.rect.setFill('lightgray')
                cont.activate()
                choice = 'transfer,checking'
            elif right.clicked(p):
                right.rect.setFill('green')
                left.rect.setFill('lightgray')
                cont.activate()
                choice = 'transfer,savings'
            elif cont.clicked(p):
                break
        amt = amtEntry.getText()
        if amt == '':
            amt = 0
        win.close()
        return choice, float(amt)
        
    def Enquiry(self, checking, savings):
        win = GraphWin('Accounts', 500, 250)
        self.logo = Text(Point(30,10), "OCBC")
        self.logo.setFill('red')
        self.logo.setStyle('bold')
        self.logo.setSize(10)
        self.logo.draw(win)
        self.rect = Rectangle(Point(0,30), Point(500,50))
        self.rect.setFill('red')
        self.rect.draw(win)
        self.text = Text(Point(60,40), 'Balance Inquiry')
        self.text.setFill('white')
        self.text.draw(win)
        self.text = Text(Point(250,80), 'Review your balance information, then\nselect Continue when you are done.')
        self.text.draw(win)
        Text(Point(150,150), "Account: Checking").draw(win)
        Text(Point(350,150), "Account: Savings").draw(win)
        Text(Point(150,180), "Avaliable Balance: ${0}".format(checking)).draw(win)
        Text(Point(350,180), "Avaliable Balance: ${0}".format(savings)).draw(win)
        cont = Button(win, Point(250,220), 70, 20, "Continue")
        cont.activate()
        p = win.getMouse()
        while not cont.clicked(p):
            p = win.getMouse()
        win.close()
        
    def otherAmt(self):
        win = GraphWin('Other Cash Amount', 400, 100)
        amtEntry = Entry(Point(200,30), 15).draw(win)
        Text(Point(200,10), "Enter amount:").draw(win)
        confirm = Button(win, Point(200,70), 80, 40, 'Confirm')
        confirm.activate()
        p = win.getMouse()
        while not confirm.clicked(p):
            p = win.getMouse()
        amt = amtEntry.getText()
        if amt == '':
            amt = 0
        win.close()
        return 'withdraw', float(amt)

    def successfulTransaction(self, amt):
        win = GraphWin('Successful Transaction', 400, 100)
        Text(Point(200,30), '${0} has been successfully withdrawn!'.format(amt)).draw(win)
        confirm = Button(win, Point(200,70), 80, 40, 'Confirm')
        confirm.activate()
        p = win.getMouse()
        while not confirm.clicked(p):
            p = win.getMouse()
        win.close()

    def insufficentAmount(self):
        win = GraphWin('Failed Transaction', 400, 100)
        Text(Point(200,30), 'Failed Transaction. Insufficent amount.').draw(win)
        confirm = Button(win, Point(200,70), 80, 40, 'Confirm')
        confirm.activate()
        p = win.getMouse()
        while not confirm.clicked(p):
            p = win.getMouse()
        win.close()

    def lessthan10Amount(self):
        win = GraphWin('Failed Transaction', 400, 100)
        Text(Point(200,30), 'Failed Transaction. Please withdraw more than $10.').draw(win)
        confirm = Button(win, Point(200,70), 80, 40, 'Confirm')
        confirm.activate()
        p = win.getMouse()
        while not confirm.clicked(p):
            p = win.getMouse()
        win.close()
        
    def quit(self):
        self.win.close()
        return 'quit', None
