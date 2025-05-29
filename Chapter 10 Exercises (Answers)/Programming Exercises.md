# **Question 1**
**Modified Code**:
```python
# cball4.py
from projectile import Projectile

def getInputs():
    a = float(input("Enter the launch angle (in degrees): "))
    v = float(input("Enter the initial velocity (in meters/sec): ")) 
    h = float(input("Enter the initial height (in meters): ")) 
    t = float(input("Enter the time interval between position calculations: "))
    return a, v, h, t

def main():
    angle, vel, h0, time = getInputs()
    cball = Projectile(angle, vel, h0)
    max_y = h0  # Initialize with starting height
    while cball.getY() >= 0:
        cball.update(time)
        current_y = cball.getY()
        if current_y > max_y:
            max_y = current_y
    
    print("\nDistance traveled: {0:0.1f} meters.".format(cball.getX()))
    print("Maximum height achieved: {0:0.1f} meters.".format(max_y))

if __name__ == "__main__":
    main()
```

---

# **Question 2**
**Modified Code**:
```python
from random import randrange
from button import Button
from graphics import *

def diceroll():
    return randrange(1, 7) + randrange(1, 7)

win = GraphWin()
button = Button(win, Point(100,100), 100, 20, 'Roll the dice')
button.activate()
while button.clicked(win.getMouse()) == True:
    roll = diceroll()
    if roll == 7 or roll == 11:
        print('You win!')
    elif roll != 2 and roll != 3 and roll != 12:
        while True:
            reroll = diceroll()
            if reroll == 7:
                print('You lose...')
                break
            elif reroll == roll:
                print('You win!')
                break
```
> Modified from Chapter 9 Question 7

---

# **Question 3**
**Modified Code**:
```python
from graphics import *
from button import Button
from random import randrange

def main():
    win = GraphWin('Three Button Monte', 300, 300)
    
    # Create buttons
    button1 = Button(win, Point(75, 150), 60, 30, "Door 1")
    button2 = Button(win, Point(150, 150), 60, 30, "Door 2")
    button3 = Button(win, Point(225, 150), 60, 30, "Door 3")
    button1.activate()
    button2.activate()
    button3.activate()
    
    # Create message area
    msg = Text(Point(150, 50), "Click a door to choose!")
    msg.draw(win)
    
    # Random winning door (1-3)
    winbutton = randrange(1, 4)
    
    # Get player choice
    chosen = None
    while chosen == None:
        pt = win.getMouse()
        if button1.clicked(pt):
            chosen = 1
        elif button2.clicked(pt):
            chosen = 2
        elif button3.clicked(pt):
            chosen = 3
    
    # Determine and display result
    if chosen == winbutton:
        result = "You Win!!!"
        # Highlight winning door in green
        if winbutton == 1:
            button1.rect.setFill('green')
        elif winbutton == 2:
            button2.rect.setFill('green')
        else:
            button3.rect.setFill('green')
    else:
        result = "You Lose... Correct door was {0}".format(winbutton)
        # Highlight player's choice in red
        if chosen == 1:
            button1.rect.setFill('red')
        elif chosen == 2:
            button2.rect.setFill('red')
        else:
            button3.rect.setFill('red')
        # Highlight correct door in green
        if winbutton == 1:
            button1.rect.setFill('green')
        elif winbutton == 2:
            button2.rect.setFill('green')
        else:
            button3.rect.setFill('green')
    
    msg.setText(result)
    exit_msg = Text(Point(150, 250), "Click anywhere to exit")
    exit_msg.draw(win)
    
    # Wait for exit click
    win.getMouse()
    win.close()

if __name__ == "__main__":
    main()
```

---

# **Question 4**
**Modified Code**:
```python
from graphics import *
from button import Button
from random import randrange

def main():
    win = GraphWin('Three Button Monte', 300, 300)
    
    # Create buttons
    button1 = Button(win, Point(75, 150), 60, 30, "Door 1")
    button2 = Button(win, Point(150, 150), 60, 30, "Door 2")
    button3 = Button(win, Point(225, 150), 60, 30, "Door 3")
    quitbutton = Button(win, Point(150, 250), 40, 25, "Quit")
    button1.activate()
    button2.activate()
    button3.activate()
    quitbutton.activate()

    # Create message area
    msg = Text(Point(150,25), "Click a door to choose!")
    msg.draw(win)

    win_text = Text(Point(150, 75), "Wins: 0")
    win_text.draw(win)
    loss_text = Text(Point(150, 95), "Losses: 0")
    loss_text.draw(win)

    #Initialize counters
    wins = 0
    losses = 0

    while True:
        # Random winning door (1-3)
        winbutton = randrange(1, 4)

        #Get player choice
        chosen = None
        while chosen == None:
            pt = win.getMouse()
            if button1.clicked(pt):
                chosen = 1
            elif button2.clicked(pt):
                chosen = 2
            elif button3.clicked(pt):
                chosen = 3
            elif quitbutton.clicked(pt):
                chosen = "quit"

        # Check for quit first
        if chosen == "quit":
            break

        #Determine and display result
        if chosen == winbutton:
            result = "You Win!!!"
            wins = wins + 1
            # Highlight winning door in green
            if winbutton == 1:
                button1.rect.setFill('green')
            elif winbutton == 2:
                button2.rect.setFill('green')
            else:
                button3.rect.setFill('green')
        else:
            result = "You Lose... Correct door was {0}".format(winbutton)
            losses = losses + 1
            # Highlight player's choice in red
            if chosen == 1:
                button1.rect.setFill('red')
            elif chosen == 2:
                button2.rect.setFill('red')
            else:
                button3.rect.setFill('red')
            # Highlight correct door in green
            if winbutton == 1:
                button1.rect.setFill('green')
            elif winbutton == 2:
                button2.rect.setFill('green')
            else:
                button3.rect.setFill('green')
                
        # Update UI
        msg.setText(result + "\nClick anywhere to continue or Quit to exit")
        win_text.setText("Wins: {0}".format(wins))
        loss_text.setText("Losses: {0}".format(losses))

        # Prepare for next round with quit option
        next_click = win.getMouse()
        if quitbutton.clicked(next_click):
            break
        else:
            # Update button UI
            button1.rect.setFill('lightgray')
            button2.rect.setFill('lightgray')
            button3.rect.setFill('lightgray')
            msg.setText("Click a door to choose!")

    # Quit button pressed
    win.close()
        
if __name__ == "__main__":
    main()
```

---

# **Question 5**
**Modified Code**:
```python
<code>
```
