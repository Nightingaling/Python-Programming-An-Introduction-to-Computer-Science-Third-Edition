# **Question 1**
**Code**:
```python
def farm_line():
    print('Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!')

def animal_line(animal):
    print('And on that farm he had a {0}, Ee-igh, Ee-igh, Oh!'.format(animal))

def animal_sound_line(sound):
    print('With a {0}, {0} here and a {0}, {0} there.'.format(sound))
    print('Here a {0}, there a {0}, everywhere a {0}, {0}.'.format(sound))

animal = ['cow', 'chicken', 'pig', 'duck', 'dog']
animal_sound = ['moo', 'cluck', 'oink', 'quack', 'woof']
for i in range(5):
    farm_line()
    animal_line(animal[i])
    animal_sound_line(animal_sound[i])
    farm_line()
    print('\n')
```

---

# **Question 2**
**Code**:
```python
def marching_line(num):
    print('The ants go marching {0} by {0}, hurrah! hurrah!'.format(num))
    print('The ants go marching {0} by {0}, hurrah! hurrah!'.format(num))
    print('The ants go marching {0} by {0},'.format(num))

def little_one_line(do):
    print('The little one stops to {0},'.format(do))

def rest_of_the_lyrics():
    print('And they all go marching down ...') 
    print('In the ground ...')
    print('To get out ....')
    print('Of the rain.')
    print('Boom! Boom! Boom!')


number = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
action = ['suck his thumb', 'tie his shoe', 'read his book', 'eat his food',
          'carry his weight', 'kill his enemy', 'defend his land', 'fix his hair',
          'sing his song', 'carry his weapon']
for i in range(0, 10):
    marching_line(number[i])
    little_one_line(action[i])
    rest_of_the_lyrics()
    print('\n')
```

---

# **Question 3**
**Modified Code**:
```python
import math

def sphereArea(radius):
     return 4 * math.pi * radius**2

def sphereVolume(radius):
     return (4/3) * math.pi * radius**3

radius = float(input("Enter the radius of the sphere: "))
print("Volume:", sphereVolume(radius))
print("Surface Area:", sphereArea(radius))
```

---

# **Question 4**
**Code**:
```python
def sumN(n):
    total = 0
    for i in range(0, n + 1):
        total = total + i
    return total

def sumNCubes(n):
    total = 0
    for i in range(0, n + 1):
        total = total + (i ** 3)
    return total

n = int(input('Value of n: '))
print('Sum of the first n natural numbers is: ', sumN(n))
print('Sum of the cubes of the first n natural numbers is: ', sumNCubes(n))
```

---

# **Question 5**
**Modified Code**:
```python
import math

def area(diameter):
    radius = diameter / 2
    return (math.pi * radius**2)

def cost(price, area):
    return price / area

diameter = float(input("Enter the diameter of the pizza (inches): "))
price = float(input("Enter the price of the pizza ($): "))
print("Cost per square inch:", cost(price, area(diameter)))
```

---

# **Question 6**
**Modified Code**:
```python
# Program: triangle2.py 
import math 
from graphics import *

def square(x): 
    return x ** 2

def distance(p1, p2): 
    dist = math.sqrt(square(p2.getX() - p1.getX()) + square(p2.getY() - p1.getY())) 
    return dist

def area(a, b, c):
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

def main(): 
    win = GraphWin("Draw a Triangle") 
    win.setCoords(0.0, 0.0, 10.0, 10.0) 
    message = Text(Point(5, 0.5), "Click on three points") 
    message.draw(win) 

    # Get and draw three vertices of triangle 
    p1 = win.getMouse() 
    p1.draw(win) 
    p2 = win.getMouse() 
    p2.draw(win) 
    p3 = win.getMouse() 
    p3. draw(win) 

    # Use Polygon object to draw the triangle 
    triangle = Polygon(p1,p2,p3) 
    triangle.setFill("peachpuff") 
    triangle.setOutline("cyan") 
    triangle.draw(win) 

    # Calculate the perimeter and area of the triangle 
    perim = distance(p1,p2) + distance(p2,p3) + distance(p3,p1)
    total_area = area(distance(p1,p2), distance(p2,p3), distance(p3,p1))
    message.setText("The perimeter is: {0:0.2f}".format(perim))
    Text(Point(5, 1.5), "The area is: {0:0.2f}".format(total_area)).draw(win)
    

    # Wait for another click to exit 
    win.getMouse() 
    win. close()
    
main()
```

---

# **Question 7**
**Modified Code**:
```python
def Fibonacci(n):
    prev_prev, prev, current = 0, 1, 1
    for i in range(1, n):
        current = prev_prev + prev
        prev_prev = prev
        prev = current
    return current

n = int(input("Enter n (n >= 1): "))
print("The Fibonacci number is:", Fibonacci(n))
```

---

# **Question 8**
**Modified Code**:
```python
import math

def nextGuess(guess, x):
    return (guess + x / guess) / 2

x = eval(input("Enter the value to find the square root of: "))
iterations = int(input("Enter the number of iterations: "))

guess = x /2
for i in range(iterations):
    guess = nextGuess(guess, x)

difference = math.sqrt(x) - guess
print("Estimated square root:", guess)
print("Difference from math.sqrt(x):", difference)
```

---

# **Question 9**
**Modified Code**:
```python
def grade(score):
    grades = ['F', 'F', 'F', 'F', 'F', 'F', 'D', 'C', 'B', 'A', 'A']
    return grades[score // 10]

score = int(input('What is your exam score: '))
print("Grade:", grade(score))
```

---

# **Question 10**
**Modified Code**:
```python
def acronym(phrase):
    words = phrase.split()
    acronym = ''
    for word in words:
        acronym = acronym + word[0].upper()
    return acronym

phrase = input('Phrase: ')
print(acronym(phrase))
```

---

# **Question 11**
**Code**:
```python
def squareEach(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2
```

---

# **Question 12**
**Code**:
```python
def sumList(nums):
    total = 0
    for i in nums:
        total = total + i
    return total
```

---

# **Question 13**
**Code**:
```python
def toNumbers(strList):
    for i in range(len(strList)):
        strList[i] = float(strList[i])
```

---

# **Question 14**
**Code**:
```python
def toNumbers(strList):
    for i in range(len(strList)):
        strList[i] = float(strList[i].rstrip())
    return strList

def sumList(nums):
    total = 0
    for i in nums:
        total = total + i
    return total

def squareEach(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2

#Open and read file
num_file = input('File: ')
numbers = open(num_file, 'r')
strList = numbers.readlines()
numbers.close()

#Compute sum of squares of numbers
nums = toNumbers(strList)
squareEach(nums)
print('The sum of the squares of the values is:', sumList(nums))
```

---

# **Question 15**
**Code**:
```python
from graphics import *

def drawFace(center, size, win):

    #Head
    head = Circle(center, size)
    head.setFill('yellow')
    head.draw(win)

    coordX = center.getX() - size / 2
    coordY = center.getY() - size / 2

    # Eyes
    left_eye = Circle(Point(coordX, coordY), size * 0.15)
    left_eye.setFill("black")
    left_eye.draw(win)

    right_eye = Circle(Point(coordX + size, coordY), size * 0.15)
    right_eye.setFill("black")
    right_eye.draw(win)

    # Smiling mouth (arc)
    mouth = Polygon(Point(coordX, center.getY() + size * 0.6),
                    Point(center.getX(), center.getY() + size),
                    Point(coordX + size, center.getY() + size * 0.6),
                    Point(center.getX(), center.getY() + size * 0.75)
                    )
    mouth.setFill("red")
    mouth.draw(win)

    # Nose (triangle)
    nose = Polygon(center,
                   Point(center.getX() - size * 0.1, center.getY() + size * 0.25),
                   Point(center.getX() + size * 0.1, center.getY() + size * 0.25))
    nose.setFill("orange")
    nose.draw(win) 
        

#Example usage:
win = GraphWin('Smiley Face', 500, 500)
win.setBackground('lightgray')
drawFace(Point(100, 100), 30, win)
drawFace(Point(300, 200), 50, win)
win.getMouse()
win.close()
```

---

# **Question 16**
**Code**:
```python
<code>
```

---

# **Question 17**
**Code**:
```python
from graphics import *

def moveTo(shape, newCenter):
    c = shape.getCenter()
    dx = newCenter.getX() - c.getX()
    dy = newCenter.getY() - c.getY()
    shape.move(dx,dy)

def main():
    win = GraphWin('Circles') 
    shape = Circle(Point(50,50) , 20)  
    shape.draw(win)
    for i in range(10):
        p = win.getMouse()
        moveTo(shape, p)
    win.close()
main()
```
