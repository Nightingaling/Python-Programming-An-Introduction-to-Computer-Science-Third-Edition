# **Question 1**
**Modified Code**:
```python
from graphics import *

def main():
    win = GraphWin("Squares", 500, 500)
    
    # (a) & (b) Draw new red square at each click position
    for i in range(10):
        click_point = win.getMouse()
        pt_x = click_point.getX()
        pt_y = click_point.getY()
        # Create square centered at click with 40x40 size
        square = Rectangle(Point(pt_x - 20, pt_y - 20), Point(pt_x + 20, pt_y + 20))
        square.draw(win)
    
    # (c) Final message and exit click
    message = Text(Point(250, 470), "Click again to quit")
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

# **Question 4**  
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

# **Question 5**  
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

# **Question 6**
**Code**:
```python
# futval_graph.py 
from graphics import * 
def main() : 
    # Introduction 
    print("This program plots the growth of a 10-year investment.")
    
    # Get principal and interest rate
    win = GraphWin("Investment Growth Chart", 320, 240)
    win.setBackground("white")

    display_principal = Text(Point(125,100),'Principal').draw(win)
    display_apr = Text(Point(125,150),'Interest rate').draw(win)
    display_close = Text(Point(160,200),'Click anywhere to start plotting').draw(win)

    principal_text = Entry(Point(200,100), 4)
    principal_text.setText("0.0")
    principal_text.draw(win)

    apr_text = Entry(Point(200,150), 4)
    apr_text.setText("0.00")
    apr_text.draw(win)
    
    #wait for a mouse click
    win.getMouse()

    #get input
    principal = float(principal_text.getText())
    apr = float(apr_text.getText())

    #Remove entries and text using undraw()
    principal_text.undraw()
    apr_text.undraw()
    display_principal.undraw()
    display_apr.undraw()
    display_close.undraw()
    
    # Create a graphics window with labels on left edge  
    Text(Point(20, 230) , ' O.OK') .draw(win) 
    Text(Point(20, 180) , ' 2.5K') .draw(win) 
    Text(Point(20, 130) , ' 5.0K') .draw(win) 
    Text(Point(20, 80) , ' 7.5K') .draw(win) 
    Text(Point(20, 30) , '10.0K') .draw(win)
    
    # Draw bar for initial principal 
    height = principal * 0.02 
    bar = Rectangle(Point(40, 230) , Point(65, 230-height)) 
    bar.setFill("green") 
    bar. setWidth(2) 
    bar.draw(win)
    
    # Draw bars for successive years 
    for year in range(1,11) : 
        # calculate value for the next year 
        principal = principal * (1 + apr) 
        # draw bar for this value 
        xll = year * 25 + 40 
        height = principal * 0.02 
        bar = Rectangle(Point(xll, 230) , Point(xll+25, 230-height)) 
        bar. setFill ("green") 
        bar.setWidth(2) 
        bar.draw(win)
        
    win.getMouse() 
    win.close()

main()
```

---

# **Question 7**
**Code**:
```python
from graphics import *
from math import *

# Input (floats for decimal values)
radius = float(input('What is the radius of the circle: '))
y_intercept = float(input('What is the y-intercept of the line: '))

# Create window with coordinate system
win = GraphWin("Circle Intersection", 500, 500)
win.setCoords(-10, -10, 10, 10)

# Draw circle centered at (0,0)
circle = Circle(Point(0, 0), radius)
circle.draw(win)

# Draw horizontal line
line = Line(Point(-10, y_intercept), Point(10, y_intercept))
line.draw(win)

# Calculate intersection points
x = sqrt(radius**2 - y_intercept**2)

# Print x-values (formatted to 2 decimal places)
print("Intersection points at x =", round(x,2), "and x =", -round(x,2))

# Draw red intersection points
point1 = Point(x, y_intercept)
point1.setFill("red")
point1.draw(win)

point2 = Point(-x, y_intercept)
point2.setFill("red")
point2.draw(win)

# Keep window open until click
win.getMouse()
win.close()
```

---

# **Question 8**
**Code**:
```python
from graphics import *
from math import *

win = GraphWin()

#Get mouse clicks
user_press = win.getMouse()
p1 = Point(user_press.getX(), user_press.getY())
user_press = win.getMouse()
p2 = Point(user_press.getX(), user_press.getY())

#Draw the line
Line(p1,p2).draw(win)

#Draw midpoint of line segment in cyan
dx = p2.getX() - p1.getX()
dy = p2.getY() - p1.getY()
mid_x = dx / 2 + p1.getX()
mid_y = dy / 2 + p1.getY()
mid_point = Point(mid_x, mid_y)
mid_point.setFill(color_rgb(0,255,255))
mid_point.draw(win)

#Print lenth and slope of line
slope = dy / dx
length = sqrt(dx ** 2 + dy ** 2)
print('The slope of the line is: ', round(slope,2))
print('The length of the line is: ', round(length,2))

#Wait for click before close window
win.getMouse()
win.close()
```

---

# **Question 9**
**Code**:
```python
from graphics import *

win = GraphWin()

#Get mouse clicks
user_press = win.getMouse()
p1 = Point(user_press.getX(), user_press.getY())
user_press = win.getMouse()
p2 = Point(user_press.getX(), user_press.getY())

#Draw the rectangle
Rectangle(p1,p2).draw(win)

#Print perimeter and area of rectangle
length = abs(p2.getX() - p1.getX())
width = abs(p2.getY() - p1.getY())
area = length * width
perimeter = 2 * (length + width)
print('The area of the rectangle is: ', round(area,2))
print('The perimeter of the rectangle is: ', round(perimeter,2))

#Wait for click before close window
win.getMouse()
win.close()
```

---

# **Question 10**
**Code**:
```python
from graphics import *
from math import *

win = GraphWin()

#Get mouse clicks
user_press = win.getMouse()
p1 = Point(user_press.getX(), user_press.getY())
user_press = win.getMouse()
p2 = Point(user_press.getX(), user_press.getY())
user_press = win.getMouse()
p3 = Point(user_press.getX(), user_press.getY())

#Draw the triangle
Polygon(p1,p2,p3).draw(win)

#Find perimeter of triangle
# length = sqrt(dx ** 2 + dy ** 2)
a = sqrt((p2.getX() - p1.getX()) ** 2 + (p2.getY() - p1.getY()) ** 2)
b = sqrt((p3.getX() - p2.getX()) ** 2 + (p3.getY() - p2.getY()) ** 2)
c = sqrt((p1.getX() - p3.getX()) ** 2 + (p1.getY() - p3.getY()) ** 2)
perimeter = a + b + c

#Find area of triangle
s = (a + b + c) / 2
area = sqrt(s * (s - a) * (s - b) * (s - c))

#Print perimeter and area of triangle
print('The area of the triangle is: ', round(area,2))
print('The perimeter of the triangle is: ', round(perimeter,2))

#Wait for click before close window
win.getMouse()
win.close()
```

---

# **Question 11**
**Code**:
```python
from graphics import *

win = GraphWin()

#First two clicks
user_press = win.getMouse()
bottom_left = Point(user_press.getX(), user_press.getY())
user_press = win.getMouse()
top_right = Point(user_press.getX(), user_press.getY())
Rectangle(bottom_left, top_right).draw(win)

#Third click
user_press = win.getMouse()
house_width = top_right.getX() - bottom_left.getX()
door_width = (house_width) / 5
door_top_left = Point(user_press.getX() - door_width / 2, user_press.getY())
door_bottom_right = Point(user_press.getX() + door_width / 2, bottom_left.getY())
Rectangle(door_top_left, door_bottom_right).draw(win)

#Forth click
window_width = door_width / 2
user_press = win.getMouse()
window_top_left = Point(user_press.getX() - window_width / 2, user_press.getY() - window_width / 2)
window_bottom_right = Point(user_press.getX() + window_width / 2, user_press.getY() + window_width / 2)
Rectangle(window_top_left, window_bottom_right).draw(win)

#Fifth click
top_roof = win.getMouse()
top_left = Point(bottom_left.getX(), top_right.getY())
Polygon(top_roof, top_left, top_right).draw(win)

#Wait for click before close window
win.getMouse()
win.close()
```
