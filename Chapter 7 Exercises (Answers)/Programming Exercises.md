# **Question 1**
**Code**:
```python
hours = float(input('Number of hours worked this week: '))
hourly_rate = float(input('Hourly rate: '))
if hours > 40:
        amount = (40 * hourly_rate) + ((hours - 40) * hourly_rate * 1.5)
else:
        amount = hours * hourly_rate
print('The total wages for the week is ${0:0.2f}'.format(amount))
```

---

# **Question 2**
**Code**:
```python
score = int(input('What is your quiz score (0 - 5): '))  
if score == 5:  
    print('Your grade is A')  
elif score == 4:  
    print('Your grade is B')  
elif score == 3:  
    print('Your grade is C')  
elif score == 2:  
    print('Your grade is D')  
else:
    print('Your grade is F')
```

---

# **Question 3**
**Code**:
```python
score = int(input('What is your exam score (0 - 100): '))
if score >= 90:
    print('Your grade is A')
elif score >= 80 and score < 90:
    print('Your grade is B')
elif score >= 70 and score < 80:
    print('Your grade is C')
elif score >= 60 and score < 70:
    print('Your grade is D')
else:
    print('Your grade is F')
```

---

# **Question 4**
**Code**:
```python
credit = int(input('Credits earned: '))
if credit < 7:
    print('Freshman')
elif credit >= 7 and credit < 16:
    print('Sophomore')
elif credit >= 16 and credit < 26:
    print('Junior')
else:
    print('Senior')
```

---

# **Question 5**
**Code**:
```python
weight = float(input('What is your weight (in pounds): '))
height = float(input('What is your height (in inches): '))
BMI = (weight * 720) / (height ** 2)
if BMI < 19:
    print('Your BMI is below the healthy range')
elif BMI > 25:
    print('Your BMI is above the healthy range')
else:
    print('Your BMI is within the healthy range')
```

---

# **Question 6**
**Code**:
```python
speed = int(input('What is the clocked speed (in mph): '))
limit = int(input('What is your speed limit (in mph): '))
base_fine = (speed - limit) * 5 + 50
if  speed > limit and speed <= 90:
    print('Fine amount: ${0}'.format(base_fine))
elif speed > 90:
    print('Fine amount: ${0}'.format(base_fine + 200))
else:
    print('Clocked speed was legal')
```

---

# **Question 7**
**Code**:
```python
def time_counter(hours):
    if int(end[1]) > int(start[1]):
        mins = int(end[1]) - int(start[1])

    elif int(end[1]) < int(start[1]):
        mins = 60 + int(end[1]) - int(start[1])
        hours = hours - 1

    else:
        mins = 0

    return hours, mins

start = input('What is the starting time (in 24hr format, e.g. 13:00): ').split(':')
end = input('What is the ending time (in 24hr format, e.g. 21:59): ').split(':')
hours = int(end[0]) - int(start[0])

if int(start[0]) >= 21:
    hours, mins = time_counter(hours)
    bill = (hours * 1.75) + (1.75 / 60 * mins)
    print('Bill: ${0:0.2f}'.format(bill))
    
elif int(end[0]) >= 21:
    hours = 21 - int(start[0])
    OT_hours = int(end[0]) - 21
    OT_mins = int(end[1])
    if int(start[1]) > 0:
        mins = 60 - int(start[1])
        hours = hours - 1
    else:
        mins = 0
    bill = ((hours * 2.5) + (2.5 / 60 * mins)) + ((OT_hours * 1.75) + (1.75 / 60 * OT_mins))
    print('Bill: ${0:0.2f}'.format(bill))

else:
    hours, mins = time_counter(hours)
    bill = (hours * 2.5) + (2.5 / 60 * mins)
    print('Bill: ${0:0.2f}'.format(bill))
```

---

# **Question 8**
**Code**:
```python    
age = int(input('Your age: '))
years = int(input('How long have you been a US citizen: '))
if age >= 30 and years >= 9:
    print('You are eligible for both US Senate and House')
elif age >= 25 and years >= 7:
    print('You are only eligible for US House')
else:
    print('You are not eligible for US Senate or House')
```

---

# **Question 9**
**Code**:
```python
year = int(input('Enter year ranging from (1982 - 2048): '))

if year < 1982:
    print('Invalid year. Program Ending')

elif year > 2048:
    print('Invalid year. Program Ending')

else:
    a = year%19
    b = year%4
    c = year%7
    d = (19*a + 24) % 30
    e = (2*b + 4*c + 6*d + 5) % 7
    date = 22 + d + e
    if date > 31:
        print('The date of Easter in year {0} is {1} April'.format(year, date - 31))
    else:
        print('The date of Easter in year {0} is {1} March'.format(year, date))
```

---

# **Question 10**
**Modified Code**:
```python
year = int(input('Enter year ranging from (1900 - 2099): '))
a = year%19
b = year%4
c = year%7
d = (19*a + 24) % 30
e = (2*b + 4*c + 6*d + 5) % 7
date = 22 + d + e

def Easter(date):
    if date > 31:
        print('The date of Easter in year {0} is {1} April'.format(year, date - 31))
    else:
        print('The date of Easter in year {0} is {1} March'.format(year, date))
    
if year < 1900:
    print('Invalid year. Program Ending')
    
elif year > 2099:
    print('Invalid year. Program Ending')
    
elif year == 1954:
    date = date - 7
    Easter(date)
        
elif year == 1981:
    date = date - 7
    Easter(date)

elif year == 2049:
    date = date - 7
    Easter(date)
        
elif year == 2076:
    date = date - 7
    Easter(date)
        
else:
    Easter(date)
```

---

# **Question 11**
**Code**:
```python
year = int(input('Year: '))
if (year % 400) == 0:
    print(year, 'is a leap year')
elif year % 100 == 0:
    print(year, 'is not a leap year')
elif year % 4 == 0:
    print(year, 'is a leap year')
else:
    print(year, 'is not a leap year')
```

---

# **Question 12**
**Code**:
```python
user_input = input('Date (in month/day/year): ')
date = user_input.split('/')

if len(date) != 3:
    print('{0} is invalid: must have exactly 3 parts (month/day/year).'.format(user_input))
else:
    try:
        month = int(date[0])
        day = int(date[1])
        year = int(date[2])
        if year <= 0:
            print('{0} is invalid: year must be a positive integer.'.format(user_input))
        else:
            if month == 2:
                if (year % 400) == 0 and 1 <= day <= 29:
                    print(user_input, 'is a valid date')
                elif year % 100 == 0 and 1 <= day <= 28:
                    print(user_input, 'is a valid date')
                elif year % 4 == 0 and 1 <= day <= 29:
                    print(user_input, 'is a valid date')
                else:
                    if 1 <= day <= 28:
                        print(user_input, 'is a valid date')
                    else:
                        print('{0} is an invalid day. It must be between 1 and 28'.format(user_input))
            elif month in [4, 6, 9, 11]:
                if 1 <= day <= 30:
                    print(user_input, 'is a valid date')
                else:
                    print('{0} is an invalid day. It must be between 1 and 30'.format(user_input))
            elif month in [1, 3, 5, 7, 8, 10, 12]:
                if 1 <= day <= 31:
                    print(user_input, 'is a valid date')
                else:
                    print('{0} is an invalid day. It must be between 1 and 31'.format(user_input))
            else:
                print('{0} is invalid: month must be 1-12.'.format(user_input))
                
    except ValueError:
        print('{0} is invalid: month, day, and year must be integers.'.format(user_input))
```

---

# **Question 13**
**Modified Code**:
```python
user_input = input('Date (in month/day/year): ')
date = user_input.split('/')

if len(date) != 3:
    print('{0} is invalid: must have exactly 3 parts (month/day/year).'.format(user_input))
else:
    try:
        month = int(date[0])
        day = int(date[1])
        year = int(date[2])
        if year <= 0:
            print('{0} is invalid: year must be a positive integer.'.format(user_input))
        else:
            if (year % 400) == 0:
                leap_year = True
            elif year % 100 == 0:
                leap_year = False
            elif year % 4 == 0:
                leap_year = True
            else:
                leap_year = False
            
            if month in [4, 6, 9, 11]:
                if 1 <= day <= 30:
                    if leap_year:
                        dayNum = (31 * (month - 1) + day) - ((4 * month + 23) //10) + 1
                    else:
                        dayNum = (31 * (month - 1) + day) - ((4 * month + 23) //10)
                    print('The corresponding day number for {0} is {1}'.format(user_input,dayNum))
                else:
                    print('{0} is an invalid day. It must be between 1 and 30'.format(user_input))
                    
            elif month in [1, 3, 5, 7, 8, 10, 12]:
                if month == 1 and 1 <= day <= 31:
                    print('The corresponding day number for {0} is {1}'.format(user_input,day))
                elif 1 <= day <= 31:
                    if leap_year:
                        dayNum = (31 * (month - 1) + day) - ((4 * month + 23) //10) + 1
                    else:
                        dayNum = (31 * (month - 1) + day) - ((4 * month + 23) //10)
                    print('The corresponding day number for {0} is {1}'.format(user_input,dayNum))
                else:
                    print('{0} is an invalid day. It must be between 1 and 31'.format(user_input))
                    
            elif month == 2:
                if leap_year and 1 <= day <= 29:
                    print('The corresponding day number for {0} is {1}'.format(user_input, 31 + day))
                else:
                    if 1 <= day <= 28:
                        print('The corresponding day number for {0} is {1}'.format(user_input, 31 + day))
                    else:
                        print('{0} is an invalid day. It must be between 1 and 28'.format(user_input))
                    
            else:
                print('{0} is invalid: month must be 1-12.'.format(user_input))
                
    except ValueError:
        print('{0} is invalid: month, day, and year must be integers.'.format(user_input))
```

---

# **Question 14**
**Modified Code**:
```python
from graphics import *
from math import *

# Input (floats for decimal values)
radius = float(input('What is the radius of the circle: '))
y_intercept = float(input('What is the y-intercept of the line: '))
if abs(y_intercept) > radius:
    print('The given y-intercept does not intersect the circle. Program Ending')
else:
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

# **Question 15**
**Modified Code**:
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
if dx == 0:
    print('This is a vertical line, thus the slope of the line is undefined')
else:
    slope = dy / dx
    print('The slope of the line is: ', round(slope,2))
length = sqrt(dx ** 2 + dy ** 2)
print('The length of the line is: ', round(length,2))

#Wait for click before close window
win.getMouse()
win.close()
```

---

# **Question 16**
**Modified Code**:
```python
from graphics import *
from math import *

def main():
    win = GraphWin("Archery Target", 500, 500)
    center = Point(250, 250)
    radius = 40  # Yellow circle radius
    n = 5
    score = 0
    
    # Define rings color from largest (outermost) to smallest (innermost)
    rings_color = ['white', 'black', 'blue', 'red', 'yellow']
    
    for color in rings_color:
        r = radius * n
        circle = Circle(center, r)
        circle.setFill(color)
        circle.draw(win)
        n = n - 1

    for i in range(5):
        shot = win.getMouse()
        euclidean = sqrt((shot.getX() - 250) ** 2 + (shot.getY() - 250) ** 2)
        if euclidean <= 40:
            point = 9
        elif euclidean <= 80:
            point = 7
        elif euclidean <= 120:
            point = 5
        elif euclidean <= 160:
            point = 3
        elif euclidean <= 200:
            point = 1
        else:
            point = 0
        score = score + point
        print(point, 'points scored!')
        print('Total score:', score)
        
    win.getMouse()
    win.close()
    
main()
```

---

# **Question 17**
**Code**:
```python
from graphics import *
win = GraphWin('Animation', 300, 300)
dx, dy = 1, 1
circle = Circle(Point(140,150), 20)
circle.draw(win)
for i in range(10000):
    if circle.getCenter().getY() - 20 == 0:
        dy = 1
    if circle.getCenter().getX() - 20 == 0:
        dx = 1
    if circle.getCenter().getY() + 20 == 300:
        dy = -1
    if circle.getCenter().getX() + 20 == 300:
        dx = -1
    circle.move(dx,dy)
    update(30) #pause so rate is not more than 30 times a second
    
win.close()
```

---

# **Question 18**
**Modified Code**:
```python
def grade(score):
    grades = ['F', 'F', 'F', 'F', 'F', 'F', 'D', 'C', 'B', 'A', 'A']
    return grades[score // 10]

try:
    score = int(input('What is your exam score: '))
    if 0 <= score <= 100:
        print("Grade:", grade(score))
    else:
        print('Please input score ranging from only 0 to 100. {0} was an invalid number'.format(score))

except ValueError:
    print('Please only input integer numbers ranging from 0 to 100')
```
