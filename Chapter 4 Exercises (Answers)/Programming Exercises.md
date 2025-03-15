# **Question 1**
**Modified Code**:
```python
from graphics import *

def main():
    win = GraphWin("Squares", 500, 500)  # Larger window for visibility
    
    # (a) & (b) Draw new red square at each click position
    for i in range(10):
        click_point = win.getMouse()
        # Create square centered at click with 40x40 size
        square = Rectangle(
            Point(click_point.getX() - 20, click_point.getY() - 20),
            Point(click_point.getX() + 20, click_point.getY() + 20)
        )
        square.setOutline("red")
        square.setFill("red")
        square.draw(win)
    
    # (c) Final message and exit click
    message = Text(Point(win.getWidth()/2, win.getHeight() - 30), "Click again to quit")
    message.setSize(15)
    message.draw(win)
    win.getMouse()
    win.close()

main()
```

---

# **Question 2**
**Code**:
```python
from graphics import *

def main():
    win = GraphWin("Archery Target", 500, 500)
    center = Point(250, 250)
    radius = 40  # Yellow circle radius
    n = 5 
    
    # Define rings color from largest (outermost) to smallest (innermost)
    rings_color = ['white', 'black', 'blue', 'red', 'yellow']
    
    for color in rings_color:
        r = radius * n
        circle = Circle(center, r)
        circle.setFill(color)
        circle.draw(win)
        n = n - 1
    
    win.getMouse()
    win.close()

main()
```

---

# **Question 3**  
**Code**:
```python
from graphics import *

def main():
    win = GraphWin("Smiley Face", 500, 500)
    win.setBackground("lightgray")

    # Head
    head = Circle(Point(250, 250), 120)
    head.setFill("yellow")
    head.draw(win)

    # Eyes
    left_eye = Circle(Point(200, 200), 20)
    left_eye.setFill("black")
    left_eye.draw(win)

    right_eye = Circle(Point(300, 200), 20)
    right_eye.setFill("black")
    right_eye.draw(win)

    # Smiling mouth (arc)
    mouth = Polygon(
        Point(200, 320), Point(250, 370), Point(300, 320),
        Point(250, 340), Point(200, 320)
    )
    mouth.setFill("red")
    mouth.draw(win)

    # Nose (triangle)
    nose = Polygon(Point(250, 250), Point(240, 280), Point(260, 280))
    nose.setFill("orange")
    nose.draw(win)

    win.getMouse()
    win.close()

main()
``` 

---

# **Question 4 **  
**Code**:
```python
from graphics import *

def main():
    win = GraphWin("Winter", 500, 500)

    christmas_tree = Polygon(
        #Half Left
        Point(150,150),
        Point(130,170), Point(145,170),
        Point(110,210), Point(145,210),
        Point(90,270), Point(145,270),
        Point(145,290), Point(150,290),
        #Half Right
        Point(155,290), Point(155,270),
        Point(210,270), Point(155,210),
        Point(190,210), Point(155,170),
        Point(170,170)
        )
    christmas_tree.draw(win)

    #Snowman
    #body
    body = Circle(Point(280,250), 40)
    body.setFill('white')
    body.draw(win)

    #head
    head = Circle(Point(280,210), 25)
    head.setFill('white')
    head.draw(win)

    #eyes
    left_eye = Circle(Point(270,200), 5)
    left_eye.setFill('black')
    right_eye = Circle(Point(290,200), 5)
    right_eye.setFill('black')
    left_eye.draw(win)
    right_eye.draw(win)

    #hands
    Line(Point(320,250), Point(340,225)).draw(win) #right hand
    Line(Point(240,250), Point(220,225)).draw(win) #left hand

    #buttons
    top_button = Circle(Point(280,250), 2)
    top_button.setFill('black')
    middle_button = Circle(Point(280,260), 2)
    middle_button.setFill('black')
    bottom_button = Circle(Point(280,270), 2)
    bottom_button.setFill('black')
    top_button.draw(win)
    middle_button.draw(win)
    bottom_button.draw(win)

    win.getMouse()
    win.close()

main()
```

---

# **Question 5 **  
**Code**:
```python
from graphics import *

def main():
    win = GraphWin("Dice")

    #1
    dice = Rectangle(Point(50,50), Point(70,70))
    dice.draw(win)
    dot = Circle(Point(60,60), 2)
    dot.setFill('black')
    dot.draw(win)
    

    #2
    dice = Rectangle(Point(80,50), Point(100,70))
    dice.draw(win)
    dot = Circle(Point(85,55), 2)
    dot.setFill('black')
    dot.draw(win)
    dot = Circle(Point(95,65), 2)
    dot.setFill('black')
    dot.draw(win)

    #3
    dice = Rectangle(Point(110,50), Point(130,70))
    dice.draw(win)
    dot = Circle(Point(125,55), 2) 
    dot.setFill('black')
    dot.draw(win)
    dot = Circle(Point(120,60), 2)
    dot.setFill('black')
    dot.draw(win)
    dot = Circle(Point(115,65), 2)
    dot.setFill('black')
    dot.draw(win)

    #4
    dice = Rectangle(Point(140,50), Point(160,70))
    dice.draw(win)
    dot = Circle(Point(155,55), 2)
    dot.setFill('black')
    dot.draw(win)
    dot = Circle(Point(145,55), 2)
    dot.setFill('black')
    dot.draw(win)
    dot = Circle(Point(145,65), 2)
    dot.setFill('black')
    dot.draw(win)
    dot = Circle(Point(155,65), 2)
    dot.setFill('black')
    dot.draw(win)

    #5
    dice = Rectangle(Point(170,50), Point(190,70))
    dice.draw(win)    
    dot = Circle(Point(185,55), 2)
    dot.setFill('black')
    dot.draw(win)
    dot = Circle(Point(175,55), 2)
    dot.setFill('black')
    dot.draw(win)
    dot = Circle(Point(175,65), 2)
    dot.setFill('black')
    dot.draw(win)
    dot = Circle(Point(185,65), 2)
    dot.setFill('black')
    dot.draw(win)
    dot = Circle(Point(180,60), 2)
    dot.setFill('black')
    dot.draw(win)

    win.getMouse()
    win.close()
    
main()
```

---

# **Question 5 **
**Code**:
