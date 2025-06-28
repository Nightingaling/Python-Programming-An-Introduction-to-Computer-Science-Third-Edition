from deck import Deck
from hand import PlayerHand, DealerHand

class BlackJack:

    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.total = 3500
        self.cont = 'y'

    def getBet(self):
        while True:
            try:
                bet = float(input('Bet to place: $'))
                if bet > self.total:
                    print('Your bet is more than your bankroll. Please input a valid bet.')
                elif bet < 0:
                    print('There is nothing on the bet. Please input a valid bet.')
                else:
                    self.total = self.total - bet
                    return bet
            except:
                print('Please input a valid bet (Numbers only)')

    def getChoice(self):
        while True:
            try:
                choice = int(input('Player next move: '))
                if choice in self.options:
                    return choice
                else:
                    print('Invalid input. Please only enter the corresponding numbers to play your next move.')
            except:
                print('Invalid input. Please only enter the corresponding numbers to play your next move.')

    def getHand(self):
        return [self.deck.dealCard(), self.deck.dealCard()]

    def dealerPlay(self):
        while self.dealerhand.checkRank() < 17 or self.dealerhand.isSoft():
            self.interactive.drawCard()
            self.dealerhand.add(self.deck.dealCard())
            self.interactive.displayDealerHand(self.dealerhand.getHand())

    def conti(self):
        self.cont = input('Do you wish to continue (y/n): ')
        while self.cont != 'y' and self.cont != 'n':
            print('Invalid input. Yes or No only. Please only input (y or n)')
            self.cont = input('Do you wish to continue (y/n): ')

    def playerBust(self):
        return (self.playerhand.checkRank() > 21)

    def outOfCards(self):
        self.deck = Deck()
        self.deck.shuffle()
        for i in self.playerhand.getHand():
            self.deck.remove(i)
        for i in self.dealerhand.getHand():
            self.deck.remove(i)

    def showdown(self, bet):
        self.interactive.displayDealerHand(self.dealerhand.getHand())
        self.dealerPlay()
        self.dealerRank = self.dealerhand.checkRank()
        self.playerRank = self.playerhand.checkRank()
        if self.dealerRank > self.playerRank and self.dealerRank <= 21:
            self.interactive.dealerWin(False)
        elif self.dealerRank < self.playerRank and self.playerRank <= 21:
            self.total = self.total + bet * 2
            self.interactive.playerWin(False)
        elif self.dealerRank > 21:
            self.total =  self.total + bet * 2
            self.interactive.bust(False)
        elif self.playerRank > 21:
            self.interactive.bust(True)
        else:
            self.total = self.total + bet
            self.interactive.tie()

    def run(self, interactive):
        self.interactive = interactive
        while self.total > 0 and self.deck.cardsLeft() > 0 and self.cont == 'y':   
            self.interactive.displayBankroll(self.total)
            bet = self.getBet()
            self.playerhand = PlayerHand(self.getHand())
            self.dealerhand = DealerHand(self.getHand())
            self.interactive.displayHands(self.playerhand.getHand(), self.dealerhand.getHand())
            if self.playerhand.blackJack():
                if self.dealerhand.blackJack():
                    self.interactive.displayDealerHand(self.dealerhand.getHand())
                    self.total = self.total + bet
                    self.interactive.tie()
                    self.conti()
                else:
                    self.total = self.total + (bet * 6/5 + bet)
                    self.interactive.playerWin(True)
                    self.conti()
            elif self.dealerhand.blackJack():
                self.interactive.displayDealerHand(self.dealerhand.getHand())
                self.interactive.dealerWin(True)
                self.conti()
            else:
                self.options = {1:'Hit', 2:'Stand', 3:'Surrender', 4:'Double Down'}
                if bet * 2 > self.total:
                    del self.options[4]
                while True:
                    if self.deck.cardsLeft() == 0:
                        self.outOfCards()
                    if self.playerBust():
                        self.dealerRank = self.dealerhand.checkRank()
                        self.playerRank = self.playerhand.checkRank()
                        self.interactive.displayRank(self.dealerRank, self.playerRank)
                        self.interactive.bust(True)
                        break
                    if (self.playerhand.getCardsInHand() > 2 and (4 in self.options)):
                        del self.options[4]
                    self.interactive.playerOptions(self.options)
                    choice = self.getChoice()
                    if choice == 1:
                        self.playerhand.add(self.deck.dealCard())
                        self.interactive.displayPlayerHand(self.playerhand.getHand())
                    elif choice == 2:
                        self.showdown(bet)
                        break
                    elif choice == 3:
                        self.interactive.surrender()
                        self.total = self.total + bet/2
                        break
                    elif choice == 4:
                        self.playerhand.add(self.deck.dealCard())
                        self.interactive.displayPlayerHand(self.playerhand.getHand())
                        self.total = self.total - bet
                        bet = bet * 2
                        if self.playerBust():
                            self.interactive.bust(True)
                        else:
                            self.showdown(bet)
                        break
                self.conti()
