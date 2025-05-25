# **Question 1**
**Modified Code**:
```python
#rball.py
from random import random

def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB = simNGames(n, probA, probB)
    printSummary(winsA, winsB)

def printIntro():
    print("This program simulates a game of racquetball between two") 
    print('players called "A" and "B". The ability of each player is') 
    print("indicated by a probability (a number between 0 and 1) that") 
    print("the player wins the point when serving. Player A always") 
    print("has the first serve.")

def getInputs():
    # Returns the three simulation parameters 
    a = float(input("What is the prob. player A wins a serve? ")) 
    b = float(input("What is the prob. player B wins a serve? ")) 
    n = int(input("How many games to simulate? ")) 
    return a, b, n

def simNGames(n, probA, probB):
    # Simulates n games of racquetball between players whose
    #    abilities are represented by the probability of winning a serve. 
    # Returns number of wins for A and B 
    winsA = winsB = 0
    serving = "A"
    for i in range(n):
        if (i + 1) % 2 == 0: #Even game
            serving = "B"
        else: #Odd game
            serving = "A"
        scoreA, scoreB = simOneGame(probA, probB, serving) 
        if scoreA > scoreB: 
            winsA = winsA + 1 
        else: 
            winsB = winsB + 1
        if winsA > int(n/2):
            break
        elif winsB > int(n/2):
            break
    return winsA, winsB

def simOneGame(probA, probB, serving):
    # Simulates a single game or racquetball between players whose 
    #    abilities are represented by the probability of winning a serve. 
    # Returns final scores for A and B 
    scoreA = 0 
    scoreB = 0 
    while not gameOver(scoreA, scoreB): 
        if serving == "A":
            if random() < probA: 
                scoreA = scoreA + 1
            else: 
                serving = "B" 
        else: 
            if random() < probB: 
                scoreB = scoreB + 1 
            else: 
                serving = "A" 
    return scoreA, scoreB

def gameOver(a, b):
    # a and b represent scores for a racquetball game 
    # Returns True if the game is over, False otherwise. 
    return a==15 or b==15

def printSummary(winsA, winsB):
    # Prints a summary of wins for each player. 
    n = winsA + winsB 
    print("\nGames simulated:", n) 
    print("Wins for A: {0} ({1:0.1%})".format(winsA, winsA/n)) 
    print("Wins for B: {0} ({1:0.1%})".format(winsB, winsB/n))

if __name__ == '__main__': main()
```

---

# **Question 2**
**Modified Code**:
```python
#rball.py
from random import random

def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB, shutoutA, shutoutB = simNGames(n, probA, probB)
    printSummary(winsA, winsB, shutoutA, shutoutB)

def printIntro():
    print("This program simulates a game of racquetball between two") 
    print('players called "A" and "B". The ability of each player is') 
    print("indicated by a probability (a number between 0 and 1) that") 
    print("the player wins the point when serving. Player A always") 
    print("has the first serve.")

def getInputs():
    # Returns the three simulation parameters 
    a = float(input("What is the prob. player A wins a serve? ")) 
    b = float(input("What is the prob. player B wins a serve? ")) 
    n = int(input("How many games to simulate? ")) 
    return a, b, n

def simNGames(n, probA, probB):
    # Simulates n games of racquetball between players whose
    #    abilities are represented by the probability of winning a serve. 
    # Returns number of wins for A and B 
    winsA = winsB = shutoutA = shutoutB = 0 
    for i in range(n): 
        scoreA, scoreB = simOneGame(probA, probB) 
        if scoreA > scoreB: 
            winsA = winsA + 1 
        else: 
            winsB = winsB + 1
        if scoreA == 15 and scoreB == 0:
            shutoutA = shutoutA + 1
        elif scoreB == 15 and scoreA == 0:
            shutoutB = shutoutB + 1
    return winsA, winsB, shutoutA, shutoutB

def simOneGame(probA, probB):
    # Simulates a single game or racquetball between players whose 
    #    abilities are represented by the probability of winning a serve. 
    # Returns final scores for A and B 
    serving = "A" 
    scoreA = 0 
    scoreB = 0 
    while not gameOver(scoreA, scoreB): 
        if serving == "A":
            if random() < probA: 
                scoreA = scoreA + 1
            else: 
                serving = "B" 
        else: 
            if random() < probB: 
                scoreB = scoreB + 1 
            else: 
                serving = "A"
    return scoreA, scoreB

def gameOver(a, b):
    # a and b represent scores for a racquetball game 
    # Returns True if the game is over, False otherwise. 
    return a==15 or b==15

def printSummary(winsA, winsB, shutoutA, shutoutB):
    # Prints a summary of wins for each player. 
    n = winsA + winsB
    print("\nGames simulated:", n) 
    print("Wins for A: {0} ({1:0.1%})".format(winsA, winsA/n))
    print("Wins for B: {0} ({1:0.1%})".format(winsB, winsB/n))
    if winsA == 0:
        print("Shutouts for A: 0 (0%)")
    else:
        print("Shutouts for A: {0} ({1:0.1%})".format(shutoutA, shutoutA/winsA))
    if winsB == 0:
        print("Shutouts for B: 0 (0%)")
    else:
        print("Shutouts for B: {0} ({1:0.1%})".format(shutoutB, shutoutB/winsB))

if __name__ == '__main__': main()
```

---

# **Question 3**
**Modified Code**:
```python
#volleyball.py
from random import random

def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB = simNGames(n, probA, probB)
    printSummary(winsA, winsB)

def printIntro():
    print("This program simulates a game of volleyball between two") 
    print('teams called "A" and "B". The ability of each team is') 
    print("indicated by a probability (a number between 0 and 1) that") 
    print("the team wins the point when serving. team A always") 
    print("has the first serve.")

def getInputs():
    # Returns the three simulation parameters 
    a = float(input("What is the prob. team A wins a serve? ")) 
    b = float(input("What is the prob. team B wins a serve? ")) 
    n = int(input("How many games to simulate? ")) 
    return a, b, n

def simNGames(n, probA, probB):
    # Simulates n games of volleyball between teams whose
    #    abilities are represented by the probability of winning a serve. 
    # Returns number of wins for A and B 
    winsA = winsB = 0 
    for i in range(n): 
        scoreA, scoreB = simOneGame(probA, probB) 
        if scoreA > scoreB: 
            winsA = winsA + 1 
        else: 
            winsB = winsB + 1 
    return winsA, winsB

def simOneGame(probA, probB):
    # Simulates a single game or volleyball between teams whose 
    #    abilities are represented by the probability of winning a serve. 
    # Returns final scores for A and B 
    serving = "A" 
    scoreA = 0 
    scoreB = 0 
    while not gameOver(scoreA, scoreB): 
        if serving == "A":
            if random() < probA: 
                scoreA = scoreA + 1
            else: 
                serving = "B" 
        else: 
            if random() < probB: 
                scoreB = scoreB + 1 
            else: 
                serving = "A" 
    return scoreA, scoreB

def gameOver(a, b):
    # a and b represent scores for a volleyball game 
    # Returns True if the game is over, False otherwise.
    if a >= 15 and (a - b) >= 2:
        return True
    elif b >= 15 and (b - a) >= 2:
        return True
    else:
        return False

def printSummary(winsA, winsB):
    # Prints a summary of wins for each team. 
    n = winsA + winsB 
    print("\nGames simulated:", n) 
    print("Wins for A: {0} ({1:0.1%})".format(winsA, winsA/n)) 
    print("Wins for B: {0} ({1:0.1%})".format(winsB, winsB/n))

if __name__ == '__main__': main()
```

---

# **Question 4**
**Modified Code**:
```python
#volleyball.py
from random import random

def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB = simNGames(n, probA, probB)
    printSummary(winsA, winsB)

def printIntro():
    print("This program simulates a game of volleyball between two") 
    print('teams called "A" and "B". The ability of each team is') 
    print("indicated by a probability (a number between 0 and 1) that") 
    print("the team wins the point when serving. team A always") 
    print("has the first serve.")

def getInputs():
    # Returns the three simulation parameters 
    a = float(input("What is the prob. team A wins a serve? ")) 
    b = float(input("What is the prob. team B wins a serve? ")) 
    n = int(input("How many games to simulate? ")) 
    return a, b, n

def simNGames(n, probA, probB):
    # Simulates n games of volleyball between teams whose
    #    abilities are represented by the probability of winning a serve. 
    # Returns number of wins for A and B 
    winsA = winsB = 0 
    for i in range(n): 
        scoreA, scoreB = simOneGame(probA, probB) 
        if scoreA > scoreB: 
            winsA = winsA + 1 
        else: 
            winsB = winsB + 1 
    return winsA, winsB

def simOneGame(probA, probB):
    # Simulates a single game or volleyball between teams whose 
    #    abilities are represented by the probability of winning a serve. 
    # Returns final scores for A and B 
    serving = "A" 
    scoreA = 0 
    scoreB = 0 
    while not gameOver(scoreA, scoreB): 
        if serving == "A":
            if random() < probA: 
                scoreA = scoreA + 1
            else:
                scoreB = scoreB + 1
                serving = "B" 
        else: 
            if random() < probB: 
                scoreB = scoreB + 1 
            else:
                scoreA = scoreA + 1
                serving = "A" 
    return scoreA, scoreB

def gameOver(a, b):
    # a and b represent scores for a volleyball game 
    # Returns True if the game is over, False otherwise.
    if a >= 25 and (a - b) >= 2:
        return True
    elif b >= 25 and (b - a) >= 2:
        return True
    else:
        return False

def printSummary(winsA, winsB):
    # Prints a summary of wins for each team. 
    n = winsA + winsB 
    print("\nGames simulated:", n) 
    print("Wins for A: {0} ({1:0.1%})".format(winsA, winsA/n)) 
    print("Wins for B: {0} ({1:0.1%})".format(winsB, winsB/n))

if __name__ == '__main__': main()
```

---

# **Question 5**
**Modified Code**:
```python
#volleyball.py
from random import random

def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB, winsA_N, winsB_N = simNGames(n, probA, probB)
    printSummary(winsA, winsB, winsA_N, winsB_N)

def printIntro():
    print("This program simulates a game of volleyball between two") 
    print('teams called "A" and "B". The ability of each team is') 
    print("indicated by a probability (a number between 0 and 1) that") 
    print("the team wins the point when serving. team A always") 
    print("has the first serve.")

def getInputs():
    # Returns the three simulation parameters 
    a = float(input("What is the prob. team A wins a serve? ")) 
    b = float(input("What is the prob. team B wins a serve? ")) 
    n = int(input("How many games to simulate? ")) 
    return a, b, n

def simNGames(n, probA, probB):
    # Simulates n games of volleyball between teams whose
    #    abilities are represented by the probability of winning a serve. 
    # Returns number of wins for A and B 
    winsA = winsB = winsA_N = winsB_N = 0 
    for i in range(n): 
        scoreA, scoreB = simOneGame(probA, probB)
        scoreA_N, scoreB_N = simOneNormalGame(probA, probB)
        if scoreA > scoreB: 
            winsA = winsA + 1 
        else: 
            winsB = winsB + 1
        if scoreA_N > scoreB_N: 
            winsA_N = winsA_N + 1 
        else: 
            winsB_N = winsB_N + 1
    return winsA, winsB, winsA_N, winsB_N

def simOneNormalGame(probA, probB):
    # Simulates a single game or volleyball between teams whose 
    #    abilities are represented by the probability of winning a serve. 
    # Returns final scores for A and B 
    serving = "A" 
    scoreA = 0 
    scoreB = 0 
    while not gameOverNormal(scoreA, scoreB): 
        if serving == "A":
            if random() < probA: 
                scoreA = scoreA + 1
            else: 
                serving = "B" 
        else: 
            if random() < probB: 
                scoreB = scoreB + 1 
            else: 
                serving = "A" 
    return scoreA, scoreB    

def simOneGame(probA, probB):
    # Simulates a single game or volleyball between teams whose 
    #    abilities are represented by the probability of winning a serve. 
    # Returns final scores for A and B 
    serving = "A" 
    scoreA = 0 
    scoreB = 0 
    while not gameOver(scoreA, scoreB): 
        if serving == "A":
            if random() < probA: 
                scoreA = scoreA + 1
            else:
                scoreB = scoreB + 1
                serving = "B" 
        else: 
            if random() < probB: 
                scoreB = scoreB + 1 
            else:
                scoreA = scoreA + 1
                serving = "A" 
    return scoreA, scoreB

def gameOverNormal(a, b):
    # a and b represent scores for a volleyball game 
    # Returns True if the game is over, False otherwise.
    if a >= 15 and (a - b) >= 2:
        return True
    elif b >= 15 and (b - a) >= 2:
        return True
    else:
        return False    

def gameOver(a, b):
    # a and b represent scores for a volleyball game 
    # Returns True if the game is over, False otherwise.
    if a >= 25 and (a - b) >= 2:
        return True
    elif b >= 25 and (b - a) >= 2:
        return True
    else:
        return False

def printSummary(winsA, winsB, winsA_N, winsB_N):
    # Prints a summary of wins for each team. 
    n = winsA + winsB
    print("\nGames simulated:", n)
    print('For rally scoring')
    print("Wins for A: {0} ({1:0.1%})".format(winsA, winsA/n)) 
    print("Wins for B: {0} ({1:0.1%})".format(winsB, winsB/n))
    print('\nFor normal scoring')
    print("Wins for A: {0} ({1:0.1%})".format(winsA_N, winsA_N/n)) 
    print("Wins for B: {0} ({1:0.1%})".format(winsB_N, winsB_N/n))

if __name__ == '__main__': main()
```

---

# **Question 6**
**Modified Code**:
```python
#table tennis.py
from random import random

def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB = simNGames(n, probA, probB)
    printSummary(winsA, winsB)

def printIntro():
    print("This program simulates a game of table tennis between two") 
    print('players called "A" and "B". The ability of each player is') 
    print("indicated by a probability (a number between 0 and 1) that") 
    print("the player wins the point when serving. player A always") 
    print("has the first serve.")

def getInputs():
    # Returns the three simulation parameters 
    a = float(input("What is the prob. player A wins a serve? ")) 
    b = float(input("What is the prob. player B wins a serve? ")) 
    n = int(input("How many games to simulate? ")) 
    return a, b, n

def simNGames(n, probA, probB):
    # Simulates n games of table tennis between players whose
    #    abilities are represented by the probability of winning a serve. 
    # Returns number of wins for A and B 
    winsA = winsB = 0 
    for i in range(n): 
        scoreA, scoreB = simOneGame(probA, probB) 
        if scoreA > scoreB: 
            winsA = winsA + 1 
        else: 
            winsB = winsB + 1 
    return winsA, winsB

def simOneGame(probA, probB):
    # Simulates a single game or table tennis between players whose 
    #    abilities are represented by the probability of winning a serve. 
    # Returns final scores for A and B 
    serving = "A" 
    scoreA = 0 
    scoreB = 0
    while not gameOver(scoreA, scoreB):
        if serving == "A":
            if random() < probA: 
                scoreA = scoreA + 1
            else:
                scoreB = scoreB + 1
        else: 
            if random() < probB: 
                scoreB = scoreB + 1 
            else:
                scoreA = scoreA + 1
        if (scoreA + scoreB) % 2 == 0 and serving == "A":
            serving = "B"
        elif (scoreA + scoreB) % 2 == 0 and serving == "B":
            serving = "A"
    return scoreA, scoreB

def gameOver(a, b):
    # a and b represent scores for a table tennis game 
    # Returns True if the game is over, False otherwise.
    if a >= 11 and (a - b) >= 2:
        return True
    elif b >= 11 and (b - a) >= 2:
        return True
    else:
        return False

def printSummary(winsA, winsB):
    # Prints a summary of wins for each player. 
    n = winsA + winsB 
    print("\nGames simulated:", n) 
    print("Wins for A: {0} ({1:0.1%})".format(winsA, winsA/n)) 
    print("Wins for B: {0} ({1:0.1%})".format(winsB, winsB/n))

if __name__ == '__main__': main()
```

---

# **Question 7**
**Code**:
```python
from random import randrange

def diceroll():
    return randrange(1, 7) + randrange(1, 7)

n = int(input('How many games of craps do u wish to play: '))
win = 0
for i in range(n):
    roll = diceroll()
    if roll == 7 or roll == 11:
        win = win + 1
    elif roll != 2 and roll != 3 and roll != 12:
        while True:
            reroll = diceroll()
            if reroll == 7:
                break
            elif reroll == roll:
                win = win + 1
                break

print("Probability of winning craps: {0:0.3}".format(win/n))
```

---

# **Question 8**
**Code**:
```python
<code>
```
