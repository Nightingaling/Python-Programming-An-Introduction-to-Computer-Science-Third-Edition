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
from random import randrange

n = int(input('How many games of blackjack to simulate: '))
bust = 0
for i in range(n):
    hand = 0
    hasAce = False
    while True:
        drawcard = randrange(1, 11)
        hand = hand + drawcard
        if drawcard == 1 and hasAce == False:
            hand = hand + 10
            hasAce = True

        #bust or win
        if hand > 21:
            if hasAce == True:
                hand = hand - 10
                if hand >= 17 and hand <= 21:
                    break
            else:
                bust = bust + 1
                break
        elif hand >= 17 and hand <= 21:
            break
        
print("Probability of dealer bust: {0:0.3}".format(bust/n))
```

---

# **Question 9**
**Modified Code**:
```python
from random import randrange

n = int(input('How many games of blackjack to simulate for each starting value: '))
for i in range(1, 11): #from ace to 10
    bust = 0
    for j in range(n): #reinteration of n games for each starting card
        hasAce = False
        if i == 1:
            hand = 11
            hasAce = True
        else:
            hand = i
        while True:
            drawcard = randrange(1, 11)
            hand = hand + drawcard
            if drawcard == 1 and hasAce == False:
                hand = hand + 10
                hasAce = True

            #bust or win
            if hand > 21:
                if hasAce == True:
                    hand = hand - 10
                    if hand >= 17 and hand <= 21:
                        break
                else:
                    bust = bust + 1
                    break
            elif hand >= 17 and hand <= 21:
                break
    if i == 1:
        print("Probability of dealer bust for Ace: {0:0.3}".format(bust/n))
    else:
        print("Probability of dealer bust for {0}: {1:0.3}".format(i,bust/n))
```

---

# **Question 10**
**Code**:
```python
from random import random

n = int(input('How many darts to throw: '))
h = 0
for i in range(n):
    x = 2 * random() - 1
    y = 2 * random() - 1
    if (x ** 2) + (y ** 2) <= 1:
        h = h + 1
print(4 * (h/n))
```

---

# **Question 11**
**Code**:
```python
from random import randrange

n = int(input('How many rolls to get 5 of a kind: '))
five_of_a_kind = 0
for i in range(n):
    dice1 = randrange(1,7)
    dice2 = randrange(1,7)
    dice3 = randrange(1,7)
    dice4 = randrange(1,7)
    dice5 = randrange(1,7)
    if dice1 == dice2 == dice3 == dice4 == dice5:
        five_of_a_kind = five_of_a_kind + 1
print("Probability of 5 of a kind: {0:0.3}".format(five_of_a_kind/n))
```

---

# **Question 12**
**Code**:
```python
from random import randrange

n = int(input("Number of coin flips: "))
trials = int(input("Number of trials: "))
total_distance = 0

for j in range(trials):
    position = 0
    for i in range(n):
        if randrange(0, 2) == 1:
            position = position + 1
        else:
            position = position - 1
    total_distance = total_distance + abs(position)

average_distance = total_distance / trials
print("Average distance after {0} steps: {1:0.2}".format(n, average_distance))
```

---

# **Question 13**
**Modified Code**:
```python
from random import randrange
import math

trials = int(input("Number of trials: "))
steps = int(input("Number of steps per trial: "))
total_distance = 0

for i in range(trials):
    x, y = 0, 0  # Start at origin
    for j in range(steps):
        direction = randrange(0, 4)
        if direction == 0:
            y = y + 1
        elif direction == 1:
            y = y - 1
        elif direction == 2:
            x = x + 1
        else:
            x = x - 1
    distance = math.sqrt(x**2 + y**2)  # Euclidean distance
    total_distance = total_distance + distance

average_distance = total_distance / trials
print("Expected distance after {0} steps: {1:0.2}".format(steps, average_distance))
```

---

# **Question 14**
**Modified Code**:
```python
from graphics import *
from math import *
from random import random

win = GraphWin("Simulation",500,500)
win.setCoords(-50,-50,50,50)

n = int(input('Number of steps: '))
x, y = 0, 0 #start at origin
for i in range(n):
    current_step = Point(x, y)
    angle = random() * 2 * pi
    x = x + cos(angle)
    y = y + sin(angle)
    Line(Point(current_step.getX(), current_step.getY()), Point(x, y)).draw(win)

# Wait for user click before closing
win.getMouse()
win.close()
```

---

# **Question 15**
**Code**:
```python
from random import random

def simulate_vision_fraction(num_samples):
    hits = 0
    # Observer is at x=0.5, Wall is at x=1.0. 
    # Distance to wall is 0.5.
    dist_to_wall = 0.5

    for _ in range(num_samples):
        # --- 1. Rejection Sampling (Get a random 3D direction) ---
        while True:
            # random() returns [0.0, 1.0)
            # We convert this to [-1.0, 1.0) for x, y, and z
            vx = (2 * random()) - 1
            vy = (2 * random()) - 1
            vz = (2 * random()) - 1
            
            # Check if this point lies inside the unit sphere
            # (This ensures the direction is uniformly random)
            if 0 < (vx*vx + vy*vy + vz*vz) <= 1:
                break
        
        # --- 2. Check Intersection ---
        
        # Filter A: Is the ray moving towards the wall (positive x)?
        if vx <= 0:
            continue
            
        # Filter B: Where does the ray hit the plane x=1?
        # The ray equation is: Position = Origin + t * Vector
        # We need: 0.5 + t * vx = 1.0
        t = dist_to_wall / vx
        
        # Calculate the Y and Z coordinates at that impact point
        hit_y = 0 + t * vy
        hit_z = 0 + t * vz
        
        # Filter C: Does it hit within the square wall boundaries?
        # The wall goes from -1 to 1 in both Y and Z
        if -1 <= hit_y <= 1 and -1 <= hit_z <= 1:
            hits += 1

    return hits / num_samples

# --- Run the Simulation ---
n = 1000000
result = simulate_vision_fraction(n)

print("Simulation with {0} rays.".format(n))
print("Fraction: {0:.5f}".format(result))
print("Percentage: {0:.2f}%".format(result * 100))
```
