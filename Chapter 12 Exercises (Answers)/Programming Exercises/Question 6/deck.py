from random import randrange

class Deck:

    def __init__(self):
        self.deck = []
        for i in ['Diamonds', 'Clubs', 'Hearts', 'Spades']:
            for j in range(1, 14):
                self.deck.append((j, i))

    def shuffle(self):
        for i in range(len(self.deck) - 1, -1, -1):
            j = randrange(0, i + 1)
            self.deck[i], self.deck[j] = self.deck[j], self.deck[i]

    def dealCard(self):
        return self.deck.pop(0)

    def cardsLeft(self):
        return len(self.deck)

    def remove(self, card):
        self.deck.remove(card)
