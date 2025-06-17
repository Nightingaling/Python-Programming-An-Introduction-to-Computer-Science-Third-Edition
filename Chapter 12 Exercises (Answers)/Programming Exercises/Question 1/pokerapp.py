from random import randrange

class Dice:

    def __init__(self):
        self.dice = [0]*5
        self.rollAll()

    def roll(self, which):
        for pos in which:
            self.dice[pos] = randrange(1,7)

    def rollAll(self):
        self.roll(range(5))

    def values(self):
        return self.dice[:]

    def score(self):
        # Create the counts list
        counts = [0] * 7
        for value in self.dice:
            counts[value] = counts[value] + 1

        # score the hand
        if 5 in counts:
            return "Five of a Kind", 30
        elif 4 in counts:
            return "Four of a Kind", 15
        elif (3 in counts) and (2 in counts):
            return "Full House", 12
        elif 3 in counts:
            return "Three of a Kind",  8
        elif counts[:] == [0,1,1,1,1,1,0] or counts[:-1] == [1,1,1,1,1,0] or counts[1:] == [0,1,1,1,1,1]:
            return "Straight", 20
        elif counts.count(2) == 2:
            return "Two Pairs", 5
        else:
            return "Garbage", 0

class PokerApp:
    def __init__(self, interface):
        self.dice = Dice()
        self.money = 100
        
        # c)
        self.score = 0
        self.scores = []
        self.names = []
        infile = open("highscore.txt", "r")
        for i in infile.read().rstrip().split("\t"):
            self.scores.append(int(i.split(",")[1]))
            self.names.append(i.split(",")[2])
        infile.close()

        self.interface = interface

    def run(self):
        while self.money >= 10 and self.interface.wantToPlay():
            self.playRound()

        # c)
        if self.score != 0 and self.InHighScore():
            self.appendHighScore(self.interface.EntryWindow())

        self.interface.close()
        
    def playRound(self):
        self.money = self.money - 10
        self.interface.setMoney(self.money)
        self.doRolls()
        result, score = self.dice.score()
        self.interface.showResult(result, score)
        self.money = self.money + score
        self.score = self.score + score #c)
        self.interface.setMoney(self.money)

    def doRolls(self):
        self.dice.rollAll()
        roll = 1
        self.interface.setDice(self.dice.values())
        toRoll = self.interface.chooseDice()
        while roll < 3 and toRoll != []:
            self.dice.roll(toRoll)
            roll = roll + 1
            self.interface.setDice(self.dice.values())
            if roll < 3:
                toRoll = self.interface.chooseDice()

    # c)
    def InHighScore(self):
        for i in self.scores:
            if self.score >= i:
                return True
        return False

    def appendHighScore(self, name):
        for i in range(len(self.scores)):
            if self.score >= self.scores[i]:
                self.scores.insert(i,self.score)
                self.names.insert(i,name)
                break
        del self.scores[-1]
        del self.names[-1]
        outfile = open("highscore.txt", "w")
        rank = ["1st","2nd","3rd","4th","5th","6th","7th","8th","9th","10th"]
        for i in range(len(self.scores)):
            print("{0},{1},{2}".format(rank[i], self.scores[i], self.names[i]),
                  file=outfile, end="\t")
        outfile.close()
        
