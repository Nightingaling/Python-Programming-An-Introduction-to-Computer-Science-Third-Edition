# **Question 1**
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
while n < 1:
    print('Invalid input, n must be equal or higher than 1. Please try again')
    n = int(input("Enter n (n >= 1): "))
    
print("The Fibonacci number is:", Fibonacci(n))
```

---

# **Question 2**
**Code**:
```python
# Print temperature headers with an empty first column for wind speed
print('{0:>2}'.format(''), end='')
for t in range(-20, 61, 10):
    print('{0:>6}'.format(t), end='')
print()

# Print wind speed and windchill values
for v in range(0, 51, 5):
    print('{0:>2}'.format(v), end='')
    for t in range(-20, 61, 10):
        if v <= 3:
            # Formula not applicable; display temperature as is (or N/A)
            print('{0:>6}'.format("N/A"), end='')
        else:
            wc = 35.74 + 0.6215*t - 35.75*(v**0.16) + 0.4275*t*(v**0.16)
            print('{0:>6.1f}'.format(wc), end='')
    print()
```

---

# **Question 3**
**Code**:
```python
interest = float(input("What is the annualized interest rate: "))
investment = 1.0
target = investment * 2
years = 0

while investment < target:
    investment = investment * (1 + interest)
    years = years + 1

print("It takes", years, "years to double the initial investment.")
```

---

# **Question 4**
**Code**:
```python
num = int(input('Starting value of Syracuse sequence: '))
if num < 1:
    print('Invalid Input')
else:
    sequence = [str(num)]
    current = num
    while current != 1:
        if current % 2 == 0:
            current = int(current / 2)
        else:
            current = 3 * current + 1
        sequence.append(str(current))
    print('The Syracuse sequence starting with {0} is: {1}'.format(num, ", ".join(sequence)))
```

---

# **Question 5**
**Code**:
```python
from math import sqrt

n = int(input("Prime Number: "))
if n < 2:
    print("The number is not a prime number")
else:
    is_prime = True
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            is_prime = False
            break
if is_prime:
    print('The number is a prime number')
else:
    print('The number is not a prime number')
```

---

# **Question 6**
**Modified Code**:
```python
from math import sqrt

n = int(input("Enter a number: "))
primes = []

if n >= 2:
    for i in range(2, n + 1):
        is_prime = True
        for j in range(2, int(sqrt(i)) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(str(i))
if primes:
    message = ", ".join(primes)
else:
    message = "None"
print('These are the prime numbers less than or equal to {0}: {1}'.format(n, message))
```

---

# **Question 7**
**Code**:
```python
from math import sqrt

n = int(input("Enter an even number: "))
primes = []
found = False

if n > 2 and (n % 2) == 0:
    for i in range(2, n + 1):
        is_prime = True
        for j in range(2, int(sqrt(i)) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    for i in primes:
        for j in primes:
            if i + j == n:
                print('The two prime numbers that add up to {0} are: {1} and {2}'.format(n,i,j))
                found = True
                break
        if found:
            break
    if not found:
        print('No primes found for', n)
elif n <= 2:
    print('Please enter an even number larger than 2')
else:
    print('Please enter an even number')
```

---

# **Question 8**
**Code**:
```python
def gcd(n, m):
    while m != 0:
        n, m = m, n % m
    return n

n, m = 15, 10
result = gcd(n, m)
print('The GCD of {0} and {1} is: {2}'.format(n, m, result))
```

---

# **Question 9**
**Code**:
```python
initial = float(input("What is the starting odometer value: "))
previous_odo = initial
total_miles = 0.0
total_gas = 0.0
leg = 1

while True:
    data = input("Enter current odometer and gas used (or blank to end): ").strip()
    if not data:
        break
    try:
        current_odo = float(data.split()[0])
        gas = float(data.split()[1])
        leg_miles = current_odo - previous_odo
        leg_mpg = leg_miles / gas
        print("Leg {0} MPG: {1:.1f}".format(leg, leg_mpg))
        total_miles = total_miles + leg_miles
        total_gas = total_gas + gas
        previous_odo = current_odo
        leg = leg + 1
    except:
        print("Invalid input. Try again.")

if total_gas > 0:
    print("Total trip MPG:", round(total_miles / total_gas, 1))
else:
    print("No legs recorded.")
```

---

# **Question 10**
**Modified Code**:
```python
mpg_file = open('leg.txt', 'r')

total_miles = 0.0
total_gas = 0.0
leg = 0

for data in mpg_file:
    if leg >= 1:
        current_odo = float(data.split()[0])
        gas = float(data.split()[1])
        leg_miles = current_odo - previous_odo
        leg_mpg = leg_miles / gas
        print("Leg {0} MPG: {1:.1f}".format(leg, leg_mpg))
        total_miles = total_miles + leg_miles
        total_gas = total_gas + gas
        previous_odo = current_odo
        leg = leg + 1
    else:
        previous_odo = float(data)
        leg = leg + 1

if total_gas > 0:
    print("Total trip MPG:", round(total_miles / total_gas, 1))
else:
    print("No legs recorded.")

mpg_file.close()
```

---

# **Question 11**
**Code**:
```python
heating_days = 0
cooling_days = 0

temp = input('What is the sequence of average temperature(separated by space): ').split()
for i in temp:
    if float(i) < 60:
        heating_days = heating_days + (60 - float(i))
    elif float(i) > 80:
        cooling_days = cooling_days + (float(i) - 80)
print('The running total of cooling degree days is:' , cooling_days)
print('The running total of heating degree days is:' , heating_days)
```

---

# **Question 12**
**Modified Code**:
```python
temp = open('temp.txt','r')
heating_days = 0
cooling_days = 0

for i in temp.readlines():
    if float(i) < 60:
        heating_days = heating_days + (60 - float(i))
    elif float(i) > 80:
        cooling_days = cooling_days + (float(i) - 80)
print('The running total of cooling degree days is:' , cooling_days)
print('The running total of heating degree days is:' , heating_days)

temp.close()
```

---

# **Question 13**
**Code**:
```python
from graphics import *

win = GraphWin('Regression Line', 300, 300)
win.setCoords(0, 0, 300, 300)  # Ensure coordinate system matches window edges

# Draw "Done" button (bottom-left corner)
done_rect = Rectangle(Point(0, 0), Point(50, 50))
done_rect.draw(win)
Text(Point(25, 25), 'Done').draw(win)

sum_x = 0.0
sum_y = 0.0
sum_x2 = 0.0
sum_xy = 0.0
n = 0

while True:
    click = win.getMouse()
    # Check if click is in "Done" area (X: 0-50, Y: 0-50)
    if 0 <= click.getX() <= 50 and 0 <= click.getY() <= 50:
        if n < 2:
            print("At least 2 points are required. Continue clicking.")
        else:
            break
    else:
        # Draw point and track sums
        x = click.getX()
        y = click.getY()
        sum_x = sum_x + x
        sum_y = sum_y + y
        sum_x2 = sum_x2 + x**2
        sum_xy = sum_xy + x * y
        Point(x, y).draw(win)
        n = n + 1

# Calculate regression line
x_mean = sum_x / n
y_mean = sum_y / n

# Compute slope (m)
denominator = sum_x2 - n * (x_mean ** 2)
if denominator == 0:
    print("All x-values are identical. Cannot compute slope.")
    
else:
    m = (sum_xy - n * x_mean * y_mean) / denominator

    # Compute y-values at window edges (x=0 and x=300)
    left_y = y_mean + m * (0 - x_mean)
    right_y = y_mean + m * (300 - x_mean)

    # Draw regression line spanning the entire window
    Line(Point(0, left_y), Point(300, right_y)).draw(win)

    win.getMouse()

win.close()
```

---

# **Question 14**
**Code**:
```python
from graphics import *

# Prompt user for input file
input_file = input("Enter the name of the image file (GIF/PPM): ")

win = GraphWin('Grayscale', 600, 600)
image = Image(Point(300, 300), input_file)  # Center image in window
image.draw(win)
win.getMouse()  # Wait for click to convert

# Process all pixels using actual image dimensions
width = image.getWidth()
height = image.getHeight()
for x in range(width):
    for y in range(height):
        r, g, b = image.getPixel(x, y)
        brightness = int(round(0.299 * r + 0.587 * g + 0.114 * b))
        image.setPixel(x, y, color_rgb(brightness, brightness, brightness))
    update(30)  # Refresh after each row

# Save the grayscale image
filename = input('File name to store grayscale image (.ppm): ')
image.save(filename)
win.close()
```

---

# **Question 15**
**Modified Code**:
```python
from graphics import *

# Prompt user for input file
input_file = input("Enter the name of the image file (GIF/PPM): ")

win = GraphWin('Color Negative', 600, 600)
image = Image(Point(300, 300), input_file)  # Center image in window
image.draw(win)
win.getMouse()  # Wait for click to convert

# Process all pixels using actual image dimensions
width = image.getWidth()
height = image.getHeight()
for x in range(width):
    for y in range(height):
        r, g, b = image.getPixel(x, y)
        image.setPixel(x, y, color_rgb(255-r, 255-g, 255-b))
    update(30)  # Refresh after each row

# Save the grayscale image
filename = input('File name to store color negative image (.ppm): ')
image.save(filename)
win.close()
```

---

# **Question 16**
**Code**:
```python
from graphics import *

def handleKey(k, win):
    if k == 'r':
        win.setBackground('pink')
    elif k == 'w':
        win.setBackground('white')
    elif k == 'g':
        win.setBackground('lightgray')
    elif k == 'b':
        win.setBackground('lightblue')

def handleClick(pt, win):
    # create an Entry for user to type in
    entry = Entry(pt, 10)
    entry.draw(win)

    # Go modal: loop until user types <Enter> key
    while True: 
        key = win.getKey() 
        if key == "Return":
            # undraw the entry and create and draw Text0
            entry.undraw()
            typed = entry.getText()
            Text(pt, typed).draw(win)
            break
        
        elif key == 'Escape':
            entry.undraw()
            break

    #clear (ignore) any mouse click that occured during text entry
    win.checkMouse()

def main():
    win = GraphWin('Click and Type', 500, 500)

    # Event Loop: handle key presses and mouse clicks until the user presses the 'q' key.

    while True:
        key = win.checkKey()
        if key == 'q':
            break

        if key:
            handleKey(key,win)

        pt = win.checkMouse()
        if pt:
            handleClick(pt, win)

    win.close()

main()
```
