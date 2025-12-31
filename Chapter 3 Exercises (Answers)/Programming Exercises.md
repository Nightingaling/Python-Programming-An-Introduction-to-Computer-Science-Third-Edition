# **Question 1**
**Code**:
```python
import math

radius = float(input("Enter the radius of the sphere: "))
volume = (4/3) * math.pi * radius**3
surface_area = 4 * math.pi * radius**2

print("Volume:", volume)
print("Surface Area:", surface_area)
```

---

# **Question 2**
**Code**:
```python
import math

diameter = float(input("Enter the diameter of the pizza (inches): "))
price = float(input("Enter the price of the pizza ($): "))
radius = diameter / 2
area = math.pi * radius**2
cost_per_sqin = price / area

print("Cost per square inch:", cost_per_sqin)
```

---

# **Question 3**
**Code**:
```python
h = int(input("Enter number of hydrogen atoms: "))
c = int(input("Enter number of carbon atoms: "))
o = int(input("Enter number of oxygen atoms: "))

weight = h * 1.00794 + c * 12.0107 + o * 15.9994
print("Molecular weight:", weight, "grams/mole")
```

---

# **Question 4**
**Code**:
```python
time = float(input("Enter time elapsed (seconds): "))
distance_miles = (time * 1100) / 5280

print("Distance to lightning strike:", distance_miles, "miles")
```

---

# **Question 5**
**Code**:
```python
pounds = float(input("Enter coffee weight (pounds): "))
total = (10.50 * pounds) + (0.86 * pounds + 1.50)

print("Total cost: $", total)
```

---

# **Question 6**
**Code**:
```python
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

slope = (y2 - y1) / (x2 - x1)
print("Slope:", slope)
```

---

# **Question 7**
**Code**:
```python
import math

x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("Distance:", distance)
```

---

# **Question 8**
**Code**:
```python
year = int(input("Enter a 4-digit year: "))
C = year // 100
epact = (8 + (C // 4) - C + ((8 * C + 13) // 25) + 11 * (year % 19)) % 30
print("Epact value:", epact)
```

---

# **Question 9**
**Code**:
```python
import math

a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

s = (a + b + c) / 2
area = math.sqrt(s * (s - a) * (s - b) * (s - c))
print("Area:", area)
```

---

# **Question 10**
**Code**:
```python
import math

height = float(input("Enter height: "))
degrees = float(input("Enter angle in degrees: "))

radians = math.pi / 180 * degrees
length = height / math.sin(radians)
print("Ladder length:", length, 'meters')
```

---

# **Question 11**
**Code**:
```python
n = int(input("Enter n: "))
total = 0
for i in range(1, n+1):
  total = total + i
print("Sum:", total)
```

---

# **Question 12**
**Code**:
```python
n = int(input("Enter n: "))
total = 0
for i in range(1, n+1):
  total = total + (i ** 3)
print("Sum of cubes:", total)
```

---

# **Question 13**
**Code**:
```python
count = int(input("How many numbers to sum? "))
total = 0
for i in range(count):
    num = float(input("Enter a number: "))
    total = total + num
print("Total sum:", total)
```

---

# **Question 14**
**Code**:
```python
count = int(input("How many numbers? "))
total = 0
for i in range(count):
    num = float(input("Enter a number: "))
    total = total + num
average = total / count
print("Average:", average)
```

---

# **Question 15**
**Code**:
```python
import math

n = int(input("Enter the number of terms to sum (n): "))
total = 0

# First loop: Positive terms
for i in range(1, n + 1, 2):
    total = total + (4 / (2 * i - 1))

# Second Loop: Negative terms
for j in range(2, n + 1, 2):
    total = total - (4 / (2 * j - 1))

print("Approximation of pi:", total)
print("Difference from actual π:", abs(math.pi - total))
```

---

# **Question 16**
**Code**:
```python
n = int(input("Enter n (n >= 1): "))
prev_prev, prev, current = 0, 1, 1
for i in range(1, n):
    current = prev_prev + prev
    prev_prev = prev
    prev = current
print("The Fibonacci number is:", current)
```

---

# **Question 17**
**Code**:
```python
import math

x = float(input("Enter the value to find the square root of: "))
iterations = int(input("Enter the number of iterations: "))

guess = x / 2  # Initial guess

for i in range(iterations):
    guess = (guess + x / guess) / 2

difference = math.sqrt(x) - guess

print("Estimated square root:", guess)
print("Difference from math.sqrt(x):", difference)
```
