# **Question 1**
**Modified Code**:
```python
# convert.py
# A program to convert Celsius temps to Fahrenheit
def main():
    print("This program converts Celsius temperatures to Fahrenheit.")
    celsius = eval(input("What is the Celsius temperature? "))
    fahrenheit = 9/5 * celsius + 32
    print("The temperature is", fahrenheit, "degrees Fahrenheit.")
main()
```

---

# **Question 2**
**Modified Code**:
```python
# convert.py
# A program to convert Celsius temps to Fahrenheit
def main():
    print("This program converts Celsius temperatures to Fahrenheit.")
    celsius = float(input("What is the Celsius temperature? "))
    fahrenheit = 9/5 * celsius + 32
    print("The temperature is", fahrenheit, "degrees Fahrenheit.")
    input("Press the <Enter> key to quit.")
main()
```

---

# **Question 3**
**Modified Code**:
```python
# avg2.py
# A simple program to average three exam scores
def main():
    print("This program computes the average of three exam scores.")
    score1, score2, score3 = eval(input("Enter three scores separated by a comma: "))
    average = (score1 + score2 + score3) / 3
    print("The average of the scores is:", average)
    input("Press the <Enter> key to quit.")
main()
```

---

# **Question 4**
**Modified Code**:
```python
# convert.py
# A program to convert Celsius temps to Fahrenheit
def main():
    for i in range(5):
        celsius = float(input("What is the Celsius temperature? "))
        fahrenheit = 9/5 * celsius + 32
        print("The temperature is", fahrenheit, "degrees Fahrenheit.")
    input("Press the <Enter> key to quit.")
main()
```

---

# **Question 5**
**Modified Code**:
```python
# convert.py
# A program to convert Celsius temps to Fahrenheit
def main():
    print("Celsius | Fahrenheit")
    print("---------------------")
    for celsius in range(0, 101, 10):
        fahrenheit = 9/5 * celsius + 32
        print(celsius, "°C |", fahrenheit, "°F")
    input("Press the <Enter> key to quit.")
main()
```

---

# **Question 6**
**Modified Code**:
```python
# futval.py
# A program to compute the value of an investment
def main():
    print("This program calculates the future value")
    principal = eval(input("Enter the initial principal: "))
    apr = float(input("Enter the annual interest rate (e.g., 0.05 for 5%): "))
    years = int(input("Enter the number of years: "))
    for i in range(years):
        principal = principal * (1 + apr)
    print("The value after", years, "years is: $", principal)
    input("Press the <Enter> key to quit.")
main()
```

---

# **Question 7**
**Modified Code**:
```python
# futval.py
# A program to compute the value of an investment
def main():
    print("This program calculates the total accumulation of yearly investments.")
    yearly = float(input("Enter the amount to invest each year: $"))
    rate = float(input("Enter the annual interest rate (e.g., 0.05 for 5%): "))
    years = int(input("Enter the number of years: "))
    total = 0
    for i in range(years):
        total = total + yearly
        total = total * (1 + rate)
    print("Total accumulation after", years, "years: $", total)
    input("Press <Enter> to quit.")
main()
```

---

# **Question 8**
**Modified Code**:
```python
# futval.py
# A program to compute the value of an investment
def main():
    print("This program calculates future value with compounded interest.")
    principal = float(input("Enter the initial principal: $"))
    rate = float(input("Enter the nominal yearly interest rate (e.g., 0.03 for 3%): "))
    periods = int(input("Enter the number of compounding periods per year: "))
    years = int(input("Enter the number of years: "))
    for i in range(years * periods):
        principal = principal * (1 + rate / periods)
    print("Total value after", years, "years: $", principal)
    input("Press <Enter> to quit.")
main()
```

---

# **Question 9**
**Modified Code**:
```python
def main():
    print("This program converts Fahrenheit to Celsius.")
    f = float(input("Enter temperature in Fahrenheit: "))
    c = 5/9 * (f - 32)
    print("Temperature in Celsius:", c)
    input("Press <Enter> to quit.")
main()
```

---

# **Question 10**
**Modified Code**:
```python
def main():
    print("This program converts kilometers to miles.")
    km = float(input("Enter distance in kilometers: "))
    miles = km * 0.62
    print("Distance in miles:", miles)
    input("Press <Enter> to quit.")
main()
```

---

# **Question 11**
**Modified Code**:
```python
def main():
    print("This program converts kilograms to pounds.")
    kg = float(input("Enter weight in kilograms: "))
    pounds = kg * 2.20462
    print("Weight in pounds:", pounds)
    input("Press <Enter> to quit.")
main()
```

---

# **Question 12**
**Modified Code**:
```python
def main():
    print("Interactive Python Calculator (Type expressions to evaluate)")
    for i in range(100):
        expr = (input(">>> ")
        print("Result:", eval(expr))
    input("Press <Enter> to exit.")
main()
```
