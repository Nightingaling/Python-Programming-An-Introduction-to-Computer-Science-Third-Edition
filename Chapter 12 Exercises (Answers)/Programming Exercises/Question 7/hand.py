class PlayerHand:

    def __init__(self, hand):
        self.hasAce = False
        self.playerHand = hand
        self.checkforAce()

    def getCardsInHand(self):
        return len(self.playerHand)

    def getHand(self): #change to getHand
        return self.playerHand

    def checkforAce(self):
        for i in self.playerHand:
            if i[0] == 1:
                self.hasAce = True

    def blackJack(self):
        for i in self.playerHand:
            if i[0] in (10,11,12,13) and self.hasAce:
                return True
        return False

    def checkRank(self):
        total = 0
        ace_count = 0
        for i in self.playerHand:
            if i[0] in (11,12,13):
                total = total + 10
            elif i[0] == 1:
                ace_count = ace_count + 1
                total = total + 11
            else:
                total = total + i[0]
        for i in range(ace_count):
            if total > 21:
                total = total - 10
        return total

    def add(self, card):
        self.playerHand.append(card)


class DealerHand:

    def __init__(self, hand):
        self.hasAce = False
        self.dealerHand = hand
        self.checkforAce()

    def getHand(self):
        return self.dealerHand

    def checkforAce(self):
        for i in self.dealerHand:
            if i[0] == 1:
                self.hasAce = True

    def blackJack(self):
        for i in self.dealerHand:
            if i[0] in (10,11,12,13) and self.hasAce:
                return True
        return False

    def checkRank(self):
        total = 0
        self.ace_count = 0
        for i in self.dealerHand:
            if i[0] in (11,12,13):
                total = total + 10
            elif i[0] == 1:
                self.ace_count = self.ace_count + 1
                total = total + 11
            else:
                total = total + i[0]
        for i in range(self.ace_count):
            if total > 21:
                total = total - 10
                self.ace_count = self.ace_count - 1
        return total

    def add(self, card):
        self.dealerHand.append(card)

    def isSoft(self):
        if self.checkRank() == 17:
            if self.ace_count:
                ''' use ace as 11'''
                return True
            else:
                return False
