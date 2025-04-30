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
<code>
```
