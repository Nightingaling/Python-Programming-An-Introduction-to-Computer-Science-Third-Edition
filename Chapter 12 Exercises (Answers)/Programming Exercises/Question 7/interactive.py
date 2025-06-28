class Interactive:

    def __init__(self):
        print('Welcome to Single Deck Blackjack Table 1')

    def displayBankroll(self, total):
        print('Your bankroll: ${0}'.format(total))

    def tie(self):
        print('\nIt is a push (tie)\n')

    def playerWin(self, blackjack):
        if blackjack:
            print('\nPlayer Blackjack! Player win!\n')
        else:
            print('\nPlayer Win!\n')

    def dealerWin(self, blackjack):
        if blackjack:
            print('\nDealer Blackjack! Dealer win!\n')
        else:
            print('\nDealer Win!\n')

    def bust(self, player):
        if player:
            print('\nPlayer bust. Dealer win!\n')
        else:
            print('\nDealer bust. Player win!\n')

    def displayHands(self, playerhand, dealerhand):
        print('\nBlackjack Table:\n')
        rank = self.FaceCardDisplay(dealerhand[0])
        print('Dealer Hand:')
        print('Card 1: {0} of {1}\nCard 2: Hole Card'.format(rank, dealerhand[0][1]))
        self.displayPlayerHand(playerhand)

    def FaceCardDisplay(self, card):
        for i in card:
            if i == 1:
                return 'Ace'
            elif i == 11:
                return 'Jack'
            elif i == 12:
                return 'Queen'
            elif i == 13:
                return 'King'
            else:
                return i

    def playerOptions(self, options):
        print('\nPlayer Options:')
        for i in options:
            print('{0}. {1}'.format(i, options[i]))

    def displayDealerHand(self, hand):
        print('\nDealer Hand:')
        for i in range(len(hand)):
            rank = self.FaceCardDisplay(hand[i])
            print('Card {0}: {1} of {2}'.format((i+1), rank, hand[i][1]))

    def displayPlayerHand(self, hand):
        print('\nPlayer Hand:')
        for i in range(len(hand)):
            rank = self.FaceCardDisplay(hand[i])
            print('Card {0}: {1} of {2}'.format((i+1), rank, hand[i][1]))

    def displayRank(self, dealer, player):
        print('\nDealer total:', dealer)
        print('Player total:', player)

    def drawCard(self):
        print('\nDrawing card...')

    def surrender(self):
        print('Player surrenders. Dealer win!')
