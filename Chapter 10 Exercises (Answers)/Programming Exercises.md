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
**Code**:
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
class Student:
    def __init__(self, name, hours, qpoints):
        self.name = name
        self.hours = float(hours)
        self.qpoints = float(qpoints)
    
    def getName(self): 
        return self.name
    
    def getHours(self): 
        return self.hours
    
    def getQPoints(self): 
        return self.qpoints
    
    def gpa(self):
        if self.hours == 0:
            return 0.0
        return self.qpoints / self.hours

    def addGrade(self, gradePoint, credits):
        self.qpoints = self.qpoints + (gradePoint * credits)
        self.hours = self.hours + credits

def main():
    # Create student with initial 0 credits and quality points
    student = Student("", 0, 0)
    
    n = int(input('Number of courses taken: '))
    for i in range(n):
        gp = float(input('Grade points for course {0}: '.format(i+1)))
        cr = float(input('Credit hours: '))
        student.addGrade(gp, cr)
    
    print('Final GPA: {0:0.2f}'.format(student.gpa()))

if __name__ == '__main__':
    main()
```

---

# **Question 6**
**Modified Code**:
```python
class Student:
    def __init__(self, name, hours, qpoints):
        self.name = name
        self.hours = float(hours)
        self.qpoints = float(qpoints)
    
    def getName(self): 
        return self.name
    
    def getHours(self): 
        return self.hours
    
    def getQPoints(self): 
        return self.qpoints
    
    def gpa(self):
        if self.hours == 0:
            return 0.0
        return self.qpoints / self.hours

    def addGrade(self, gradePoint, credits):
        self.qpoints = self.qpoints + (gradePoint * credits)
        self.hours = self.hours + credits

    def addLetterGrade(self, letterGrade, credits):
        # Convert to uppercase and remove whitespace
        grade = letterGrade.upper().strip()
        gp = 0.0
        
        # Map letter grades to grade points using if/elif chain
        if grade == "A":
            gp = 4.0
        elif grade == "A-":
            gp = 3.7
        elif grade == "B+":
            gp = 3.3
        elif grade == "B":
            gp = 3.0
        elif grade == "B-":
            gp = 2.7
        elif grade == "C+":
            gp = 2.3
        elif grade == "C":
            gp = 2.0
        elif grade == "C-":
            gp = 1.7
        elif grade == "D+":
            gp = 1.3
        elif grade == "D":
            gp = 1.0
        elif grade == "F":
            gp = 0.0
        else:
            print("Invalid grade '{0}' - course skipped".format(letterGrade))
            return
        
        # Add the valid grade
        self.addGrade(gp, credits)

def main():
    # Create student with initial 0 credits and quality points
    student = Student("", 0, 0)
    
    n = int(input('Number of courses taken: '))
    for i in range(n):
        lg = input('Letter grade for course {0}: '.format(i+1))
        cr = float(input('Credit hours: '))
        student.addLetterGrade(lg, cr)
    
    print('Final GPA: {0:0.2f}'.format(student.gpa()))

if __name__ == '__main__':
    main()
```

---

# **Question 7**
**Modified Code**:
```python
#button.py
from graphics import *
from math import *

class CButton:

    """A button is a labeled rectangle in a window.
    It is activated or deactivated with the activate()
    and deactivate() methods. The clicked(p) method
    returns True if the button is active and p is inside it."""

    def __init__(self, win, center, radius, label):
        """Creates a circular button, eg:
        qb = Button(myWin, centerPoint, radius, 'Quit')"""
        self.cX = center.getX()
        self.cY = center.getY()
        self.radius = radius
        self.circle = Circle(center, radius)
        self.circle.setFill('lightgray')
        self.circle.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.deactivate()

    def clicked(self, p):
        "Returns True if button active and p is inside"
        a = sqrt((self.cX - p.getX())**2 + (self.cY - p.getY())**2)
        return (self.active and a <= self.radius)


    def getLabel(self):
        "Returns the label string of this button."
        return self.label.getText()

    def activate(self):
        "Sets this button to 'active'."
        self.label.setFill('black')
        self.circle.setWidth(2)
        self.active = True

    def deactivate(self):
        "Sets this button to 'inactive'."
        self.label.setFill('darkgrey')
        self.circle.setWidth(1)
        self.active = False
```

---

# **Question 8**
**Modified Code**:
```python
# dieview.py
from graphics import *
class DieView:
    """ DiewView is a widget that displays a graphical representation
    of a standard six-sided die."""

    def __init__(self, win, center, size):
        """Create a view of a die, e.g.: 
            d1 = DieView(myWin, Point(40,50), 20) 
        creates a die centered at (40,50) having sides 
        of length 20."""
        
        # first define some standard values 
        self.win = win           # save this for drawing pips later 
        self.background = "white"# color of die face 
        self.foreground = "black"# color of the pips
        self.psize = 0.1 * size  # radius of each pip
        hsize = size / 2.0       # half the size of the die 
        offset = 0.6 * hsize     # distance from center to outer pips
        
        # create a square for the face 
        cx, cy = center.getX(), center.getY() 
        p1 = Point(cx-hsize, cy-hsize) 
        p2 = Point(cx+hsize, cy+hsize) 
        rect = Rectangle(p1,p2) 
        rect.draw(win) 
        rect.setFill(self.background)
        
        # Create 7 circles for standard pip locations 
        self.pip1 = self.__makePip(cx-offset, cy-offset) 
        self.pip2 = self.__makePip(cx-offset, cy) 
        self.pip3 = self.__makePip(cx-offset, cy+offset) 
        self.pip4 = self.__makePip(cx, cy) 
        self.pip5 = self.__makePip(cx+offset, cy-offset) 
        self.pip6 = self.__makePip(cx+offset, cy) 
        self.pip7 = self.__makePip(cx+offset, cy+offset)
        
        # Draw an initial value 
        self.setValue(1)

    def __makePip(self, x, y): 
        "Internal helper method to draw a pip at (x,y)" 
        pip = Circle(Point(x,y), self.psize) 
        pip.setFill(self.background) 
        pip.setOutline(self.background) 
        pip.draw(self.win) 
        return pip 

    def setValue(self, value): 
        "Set this die to display value." 
        # turn all pips off
        self.value = value
        self.pip1.setFill(self.background) 
        self.pip2.setFill(self.background) 
        self.pip3.setFill(self.background)
        self.pip4.setFill(self.background) 
        self.pip5.setFill(self.background) 
        self.pip6.setFill(self.background)
        self.pip7.setFill(self.background)

        #turn correct pips on
        if value == 1:
            self.pip4.setFill(self.foreground)
        elif value == 2:
            self.pip1.setFill(self.foreground)
            self.pip7.setFill(self.foreground)
        elif value == 3:
            self.pip1.setFill(self.foreground)
            self.pip7.setFill(self.foreground)
            self.pip4.setFill(self.foreground)
        elif value == 4:
            self.pip1.setFill(self.foreground)
            self.pip3.setFill(self.foreground)
            self.pip5.setFill(self.foreground)
            self.pip7.setFill(self.foreground)
        elif value == 5:
            self.pip1.setFill(self.foreground)
            self.pip3.setFill(self.foreground)
            self.pip4.setFill(self.foreground)
            self.pip5.setFill(self.foreground)
            self.pip7.setFill(self.foreground)
        else:
            self.pip1.setFill(self.foreground)
            self.pip2.setFill(self.foreground)
            self.pip3.setFill(self.foreground)
            self.pip5.setFill(self.foreground)
            self.pip6.setFill(self.foreground)
            self.pip7.setFill(self.foreground)

    def setColor(self, color):
        self.foreground = color
        self.setValue(self.value)
```

---

# **Question 9**
**Code**:
```python
from math import *

class Sphere:

    def __init__(self, radius):
        self.radius = radius

    def getRadius(self):
        return self.radius

    def surfaceArea(self):
        return (4 * pi * (self.radius ** 2))
        
    def volume(self):
        return (4/3 * pi * (self.radius ** 3))

def main():
    r = float(input('Enter the radius of a sphere: '))
    sphere = Sphere(r)
    print('The volume of the sphere is:', sphere.volume())
    print('The surface area of the sphere is:', sphere.surfaceArea())

if __name__ == "__main__":
    main()
```

---

# **Question 10**
**Modified Code**:
```python
class Cube:

    def __init__(self, length):
        self.length = length

    def getLength(self):
        return self.length

    def surfaceArea(self):
        return ((self.length ** 2) * 6)
        
    def volume(self):
        return (self.length ** 3)

def main():
    l = float(input('Enter the length of a cube: '))
    cube = Cube(l)
    print('The volume of the cube is:', cube.volume())
    print('The surface area of the cube is:', cube.surfaceArea())

if __name__ == "__main__":
    main()
```

---

# **Question 11**
**Code**:
```python
from random import randrange

class Card:

    def __init__(self, rank, suit):
        if suit == "d":
            self.suit = 'Diamonds'
        elif suit == "c":
            self.suit = 'Clubs'
        elif suit == 'h':
            self.suit = 'Hearts'
        else:
            self.suit = 'Spades'

        # Store rank as integer for value calculation
        self.rank = rank

        # Set display rank
        if rank == 1:
            self.display_rank = 'Ace'
        elif rank == 11:
            self.display_rank = 'Jack'
        elif rank == 12:
            self.display_rank = 'Queen'
        elif rank == 13:
            self.display_rank = 'King'
        else:
            self.display_rank = str(rank)
        

    def getRank(self):
        return self.rank # Return numeric rank

    def getSuit(self):
        return self.suit

    def value(self):
        # Calculate Blackjack value
        if self.rank in [11, 12, 13]: # Face cards
            return 10
        else:
            return self.rank # Ace = 1, others = their value

    def __str__(self):
        return ('{0} of {1}'.format(self.display_rank, self.suit))

def main():
    suits = ['d','c','h','s']
    total = 0
    n = int(input('Number of cards to generate: '))
    for i in range(n):
        card_num = randrange(1, 14)
        suit = suits[randrange(0,4)]
        c = Card(card_num, suit)
        total = total + c.value()
        print(c)
    print('The associated Blackjack value of {0} numbers of cards is: {1}'.format(n, total))

if __name__ == "__main__":
    main()
```

---

# **Question 12**
**Modified Code**:
```python
from random import randrange
from graphics import *

class Card:

    def __init__(self, rank, suit):
        if suit == "d":
            self.suit = 'Diamonds'
        elif suit == "c":
            self.suit = 'Clubs'
        elif suit == 'h':
            self.suit = 'Hearts'
        else:
            self.suit = 'Spades'

        # Store rank as integer for value calculation
        self.rank = rank

        # Set display rank
        if rank == 1:
            self.display_rank = 'Ace'
        elif rank == 11:
            self.display_rank = 'Jack'
        elif rank == 12:
            self.display_rank = 'Queen'
        elif rank == 13:
            self.display_rank = 'King'
        else:
            self.display_rank = str(rank)
        

    def getRank(self):
        return self.rank # Return numeric rank

    def getSuit(self):
        return self.suit

    def value(self):
        # Calculate Blackjack value
        if self.rank in [11, 12, 13]: # Face cards
            return 10
        else:
            return self.rank # Ace = 1, others = their value

    def __str__(self):
        return ('{0} of {1}'.format(self.display_rank, self.suit))

    def draw(self, win, center):
        filename = "{0}_of_{1}.png".format(self.display_rank, self.suit)
        Image(center, filename.lower()).draw(win)

def main():
    win = GraphWin("Cards", 700, 700)
    suits = ['d','c','h','s']
    total = x = 0
    for i in range(5):
        card_num = randrange(1, 14)
        suit = suits[randrange(0,4)]
        c = Card(card_num, suit)
        total = total + c.value()
        x = x + 100
        c.draw(win, Point(x,350))
        print(c)
    print('The associated Blackjack value of 5 numbers of cards is: {0}'.format(total))

    # close win
    win.getMouse()
    win.close()

if __name__ == "__main__":
    main()
```
> In order for the graphics window to accommodate five card images, the card image must be small.

---

# **Question 13**
**Modified Code**:
```python
# face.py
from graphics import *

class Face:
    
    def __init__(self, window, center, size):
        # Display face
        eyeSize = 0.15 * size 
        eyeOff = size / 3.0
        mouthSize = 0.8 * size
        mouthOff = size / 2.0
        self.head = Circle(center,size)
        self.head.draw(window) 
        self.leftEye = Circle(center, eyeSize) 
        self.leftEye.move(-eyeOff, -eyeOff) 
        self.rightEye = Circle(center, eyeSize) 
        self.rightEye.move(eyeOff, -eyeOff) 
        self.leftEye.draw(window) 
        self.rightEye.draw(window) 
        p1 = center.clone() 
        p1.move(-mouthSize/2, mouthOff) 
        p2 = center.clone() 
        p2.move(mouthSize/2, mouthOff)
        self.mouth = Line(p1,p2)
        self.mouth.draw(window)

        # Display text of facial expressions
        buttonsY = textY = center.getY() + size + 50
        j = 0
        for i in range(-100, 101, 100):
            textX = center.getX() + i
            self.label = Text(Point(textX, textY), ['Smile', 'Wink', 'Frown'][j])
            self.label.draw(window)
            j = j + 1

        # Display Smile button
        self.smilebutton_p1 = Point(center.getX() - 125, buttonsY - 10)
        self.smilebutton_p2 = Point(center.getX() - 75, buttonsY + 10)
        Rectangle(self.smilebutton_p1, self.smilebutton_p2).draw(window)

        # Display Wink button
        self.winkbutton_p1 = Point(center.getX() - 25, buttonsY - 10)
        self.winkbutton_p2 = Point(center.getX() + 25, buttonsY + 10)
        Rectangle(self.winkbutton_p1, self.winkbutton_p2).draw(window)

        # Display Frown button
        self.frownbutton_p1 = Point(center.getX() + 75, buttonsY - 10)
        self.frownbutton_p2 = Point(center.getX() + 125, buttonsY + 10)
        Rectangle(self.frownbutton_p1, self.frownbutton_p2).draw(window)

    def smile(self, win):
        p1 = self.mouth.getP1()
        p2 = self.mouth.getP2()
        p3 = Point(p1.getX() - 10, p1.getY() - 10)
        p4 = Point(p2.getX() + 10, p2.getY() - 10)
        Line(p3,p1).draw(win)
        Line(p2,p4).draw(win)

    def wink(self, win):
        self.leftEye.undraw()
        lefteyeX = self.leftEye.getCenter().getX()
        lefteyeY = self.leftEye.getCenter().getY()
        p1 = Point(lefteyeX, lefteyeY - 10)
        p2 = Point(lefteyeX + 10, lefteyeY)
        p3 = Point(lefteyeX, lefteyeY + 10)
        Line(p1,p2).draw(win)
        Line(p2,p3).draw(win)

    def frown(self, win):
        p1 = self.mouth.getP1()
        p2 = self.mouth.getP2()
        p3 = Point(p1.getX() - 10, p1.getY() + 10)
        p4 = Point(p2.getX() + 10, p2.getY() + 10)
        Line(p3,p1).draw(win)
        Line(p2,p4).draw(win)
        
    def buttonclicked(self, p):
        if (self.smilebutton_p1.getX() <= p.getX() <= self.smilebutton_p2.getX()) and (self.smilebutton_p1.getY() <= p.getY() <= self.smilebutton_p2.getY()):
            return "smile"
        elif (self.winkbutton_p1.getX() <= p.getX() <= self.winkbutton_p2.getX()) and (self.winkbutton_p1.getY() <= p.getY() <= self.winkbutton_p2.getY()):
            return "wink"
        elif (self.frownbutton_p1.getX() <= p.getX() <= self.frownbutton_p2.getX()) and (self.frownbutton_p1.getY() <= p.getY() <= self.frownbutton_p2.getY()):
            return "frown"


def main():
    win = GraphWin("Face", 300, 300)
    face = Face(win, Point(150,150), 50)
    mode = face.buttonclicked(win.getMouse())
    if mode == "smile":
        face.smile(win)
    elif mode == "wink":
        face.wink(win)
    elif mode == "frown":
        face.frown(win)

    # close window
    win.getMouse()
    win.close()


if __name__ == "__main__":
    main()
```
> The program only processes one button click. To change expressions again, you'd need to restart

---

# **Question 14**
**Modified Code**:
```python
# face.py
from graphics import *

class Face:
    
    def __init__(self, window, center, size):
        self.eyeSize = 0.15 * size 
        eyeOff = size / 3.0
        mouthSize = 0.8 * size
        mouthOff = size / 2.0
        self.head = Circle(center,size)
        self.head.draw(window) 
        self.leftEye = Circle(center, self.eyeSize) 
        self.leftEye.move(-eyeOff, -eyeOff) 
        self.rightEye = Circle(center, self.eyeSize) 
        self.rightEye.move(eyeOff, -eyeOff) 
        self.leftEye.draw(window) 
        self.rightEye.draw(window) 
        p1 = center.clone() 
        p1.move(-mouthSize/2, mouthOff) 
        p2 = center.clone() 
        p2.move(mouthSize/2, mouthOff)
        self.mouth = Line(p1,p2)
        self.mouth.draw(window)
        self.centerP_mouth = self.mouth.getCenter()
        self.centerP_eye = self.leftEye.getCenter()

    def smile(self, win):
        self.mouth.undraw()
        p1 = self.centerP_mouth
        p2 = Point(p1.getX() - 20, p1.getY() - 20)
        p3 = Point(self.centerP_mouth.getX(), self.centerP_mouth.getY() + 10)
        p4 = Point(p1.getX() + 20, p1.getY() - 20)
        self.mouth = Polygon(p1,p2,p3,p4).draw(win)

    def wink(self, win):
        self.leftEye.undraw()
        self.mouth.undraw()
        self.smile(win)
        lefteyeX = self.centerP_eye.getX()
        lefteyeY = self.centerP_eye.getY()
        p1 = Point(lefteyeX, lefteyeY)
        p2 = Point(lefteyeX - 10, lefteyeY - 10) 
        p3 = Point(lefteyeX + 10, lefteyeY)
        p4 = Point(lefteyeX - 10, lefteyeY + 10)
        self.leftEye = Polygon(p1,p2,p3,p4).draw(win)

    def frown(self, win):
        self.mouth.undraw()
        self.leftEye.undraw()
        self.leftEye = Circle(self.centerP_eye, self.eyeSize).draw(win)
        p1 = self.centerP_mouth
        p2 = Point(p1.getX() + 20, p1.getY() + 10)
        p3 = Point(self.centerP_mouth.getX(), self.centerP_mouth.getY() - 10)
        p4 = Point(p1.getX() - 20, p1.getY() + 10)
        self.mouth = Polygon(p1,p2,p3,p4).draw(win)

    def move(self, win, center, size):
        dx = dy = 1
        expressions = [self.smile, self.wink, self.frown]
        expr_index = 0
        while True:
            if win.checkMouse(): break
            current = self.head.getCenter()
            if current.getY() - size <= 0 or current.getY() + size >= 300:
                dy = -dy
                expressions[expr_index](win)
                expr_index = (expr_index + 1) % 3
            if current.getX() - size <= 0 or current.getX() + size >= 300:
                dx = -dx
                expressions[expr_index](win)
                expr_index = (expr_index + 1) % 3
            self.head.move(dx,dy)
            self.leftEye.move(dx,dy)
            self.rightEye.move(dx,dy)
            self.mouth.move(dx,dy)
            self.centerP_mouth.move(dx,dy)
            self.centerP_eye.move(dx,dy)
            update(30)


def main():
    win = GraphWin("Face Animation", 300, 300)
    face = Face(win, Point(75,100), 50)
    face.move(win, Point(75,100), 50)
    win.close()


if __name__ == "__main__":
    main()
```
> The order of change of facial expression is smile, wink then lastly frown. However, if you change the position of the center of the face, where it causes the face to have corner bounces (hitting two walls simultaneously). Then, the order will not be the same, as local variable "expr_index" will + 2 instead of +1. Thus, the order will skip the next one and will execute the subsequent facial expression. e.g. neutral, wink, smile, frown, wink...

---

# **Question 15**
**Modified Code**:
```python
<code>
```
