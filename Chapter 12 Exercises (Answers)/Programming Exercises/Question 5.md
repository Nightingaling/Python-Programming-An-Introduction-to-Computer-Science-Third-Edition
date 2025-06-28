# **Question 5**
**Code**:
```python
from random import randrange

class Craps:

    def __init__(self, interactive):
        self.interactive = interactive
        self.total = 3000
        self.choice = 'play'

    def run(self):
        while self.choice == 'play' and self.total > 0:
            self.interactive.displayBankroll(self.total)
            line = self.interactive.getLine()
            self.amt = self.interactive.getBet(self.total)
            self.total = self.total - self.amt
            self.interactive.displayBet(self.amt)
            if line == 'pass':
                self.PassLine()
            elif line == 'dontpass':
                self.DontPassLine()
            if self.broke(self.total):
                break
            self.choice = self.interactive.choice()

    def PassLine(self):
        roll = self.rollDice(False)
        if roll == 7 or roll == 11:
            self.total = self.win(self.amt, self.total)
        elif roll == 2 or roll == 3 or roll == 12:
            self.interactive.displayLoseBet(self.amt)
        else:
            point = roll
            while True:
                roll = self.rerollRoutine()
                if roll == 7:
                    self.interactive.SevenOut(self.amt)
                    break
                elif roll == point:
                    self.total = self.win(self.amt, self.total)
                    break

    def DontPassLine(self):
        roll = self.rollDice(False)
        if roll == 2 or roll == 3:
            self.total = self.win(self.amt, self.total)
        elif roll == 7 or roll == 11:
            self.interactive.displayLoseBet(self.amt)
        elif roll == 12:
            self.interactive.displayPush()
            self.total = self.total + self.amt
        else:
            point = roll
            while True:
                roll = self.rerollRoutine()
                if roll == point:
                    self.interactive.displayLoseBet(self.amt)
                    break
                elif roll == 7:
                    self.total = self.win(self.amt, self.total)
                    break

    def rollDice(self, reroll):
        dice1, dice2 = randrange(1,7), randrange(1,7)
        roll = dice1 + dice2
        if reroll:
            self.interactive.displayReroll(dice1, dice2, roll)
        else:
            self.interactive.displayInitialRoll(dice1, dice2, roll)
        return roll

    def rerollRoutine(self):
        print('\nContinue rolling')
        return self.rollDice(True)

    def win(self, amt, total):
        self.interactive.displayWinBet(amt)
        total = total + amt*2
        return total

    def broke(self, total):
        if total == 0:
            print('\nNo more money in bankroll. Unable to continue')
            return True
        else:
            return False


class Interactive():

    def displayBankroll(self, total):
        print('Bankroll: ${0}'.format(total))

    def getLine(self):
        line = input("Pass Line or Don't Pass Line? (pass/dontpass): ").lower()
        while line != 'pass' and line != 'dontpass':
            print('Please input a valid answer. (pass/dontpass)')
            line = input("Pass Line or Don't Pass Line? (pass/dontpass): ").lower()
        return line

    def getBet(self, total):
        while True:
            try:
                amt = float(input('How much are u betting: $'))
                if amt > total:
                    print('Invalid Amount. Please enter a valid amount.')
                else:
                    break
            except ValueError:
                print('Please input a valid amount (Numbers only).')
        return amt

    def displayBet(self, amt):
        print('Bet: ${0}'.format(amt))

    def displayInitialRoll(self, dice1, dice2, roll):
        print("\nDice 1: {0}\nDice 2: {1}\nCome-out roll: {2}".format(dice1, dice2, roll))

    def displayWinBet(self, amt):
        print('You win ${0}'.format(amt))

    def displayLoseBet(self, amt):
        print('You lose ${0}'.format(amt))

    def displayReroll(self, dice1, dice2, roll):
        print("\nDice 1: {0}\nDice 2: {1}\nReroll: {2}".format(dice1, dice2, roll))

    def SevenOut(self, amt):
        print('Seven-out. You lose ${0}'.format(amt))

    def displayPush(self):
        print('You Push.')

    def choice(self):
        choice = input('Play another round or Quit? (play/quit): ').lower()
        while choice != 'play' and choice != 'quit':
            print('Please input a valid answer. (play/quit)')
            choice = input('\nPlay another round or Quit? (play/quit): ').lower()
        return choice


def main():
    crap = Craps(Interactive())
    crap.run()


if __name__ == "__main__":
    main()
```
