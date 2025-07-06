from deck import Deck

class Bridge:

    def __init__(self):
        deck = Deck()
        deck.shuffle()
        self.players = []
        for i in range(4):
            hand = []
            for j in range(13):
                hand.append(deck.dealCard())
            player = Player(hand, i)
            self.players.append(player)

    def run(self, interactive):
        for player in self.players:
            HCP = player.calculate_HCP()
            bid = player.suggest_opening(HCP)
            interactive.displayBid(player.playerType(), HCP, bid)
            interactive.displayHand(player.playerType(), player.getHand())


class Player:

    def __init__ (self, hand, playerNo):
        self.hand = hand
        self.sortHand()
        if playerNo == 0:
            self.player = 'South'
        elif playerNo == 1:
            self.player = 'West'
        elif playerNo == 2:
            self.player = 'North'
        elif playerNo == 3:
            self.player = 'East'

    def getHand(self):
        return self.hand

    def sortHand(self):
        self.hand.sort()
        self.hand.sort(key=self.bySuits, reverse = True)

    def bySuits(self, pair):
        return pair[1]

    def playerType(self):
        return self.player

    def calculate_HCP(self):
        HCP = 0
        self.suit_counts = {"Spades":0, "Hearts":0, "Diamonds":0, "Clubs":0}
        for rank, suit in self.hand:
            if rank == 1: # Ace
                HCP = HCP + 4
            elif rank == 13: # King
                HCP = HCP + 3
            elif rank == 12: # Queen
                HCP = HCP + 2
            elif rank == 11: # Jack
                HCP = HCP + 1
            self.suit_counts[suit] = self.suit_counts[suit] + 1
        return HCP

    def suggest_opening(self, HCP):
        mostSuit, num = 'Spades', self.suit_counts['Spades']
        for suit in self.suit_counts:
            if self.suit_counts[suit] > num:
                mostSuit = suit
                num = self.suit_counts[suit]
        if 6 <= HCP <= 10 and num >= 6:
            if mostSuit in ('Hearts', 'Spades'):
                return '2 {0}'.format(mostSuit)
            else:
                return 'pass'
        elif HCP >= 22:
            return '2 Clubs'
        elif 20 <= HCP <= 21 and self.is_balanced():
            return '2NT'
        elif 15 <= HCP <= 17 and self.is_balanced():
            return '1NT'
        elif 15 <= HCP <= 17 and not self.is_balanced():
            return '1 {0}'.format(mostSuit)
        elif 12 <= HCP <= 21 and num >= 5:
            return '1 {0}'.format(mostSuit)
        else:
            return 'pass'

    def is_balanced(self):
        counts = []
        for suit in self.suit_counts:
            counts.append(self.suit_counts[suit])
        counts.sort()
        return counts in [[3, 3, 3, 4], [2, 3, 4, 4], [2, 3, 3, 5]]


class Interactive:

    def displayHand(self, player, hand):
        print(player, 'Hand:')
        for card in hand:
            if card[0] == 1:
                rank = 'Ace'
            elif card[0] == 11:
                rank = 'Jack'
            elif card[0] == 12:
                rank = 'Queen'
            elif card[0] == 13:
                rank = 'King'
            else:
                rank = card[0]
            print('{0} of {1}'.format(rank, card[1]))
        print('\n')

    def displayBid(self, player, HCP, bid):
        print('{0}: {1} points | Recommended Opening Bid: {2}'.format(player, HCP, bid))


Bridge().run(Interactive())
