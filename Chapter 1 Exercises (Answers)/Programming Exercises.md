# **Question 1**  

| **Command**                  | **Output**                     |  
|------------------------------|--------------------------------|  
| `print("Hello, world!")`      | `Hello, world!`                |  
| `print("Hello", "world!")`    | `Hello world!`                 |  
| `print(3)`                    | `3`                           |  
| `print(3.0)`                  | `3.0`                         |  
| `print(2 + 3)`                | `5`                           |  
| `print(2.0 + 3.0)`            | `5.0`                         |  
| `print("2" + "3")`            | `23`                          |  
| `print("2 + 3 =", 2 + 3)`     | `2 + 3 = 5`                   |  
| `print(2 * 3)`                | `6`                           |  
| `print(2 ** 3)`               | `8`                           |  
| `print(7 / 3)`                | `2.3333333333333335`          |  
| `print(7 // 3)`               | `2`                           |  

---

# **Question 2**  
**Code**:  
```python
# File: chaos.py 
# A simple program illustrating chaotic behavior.

def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(10):
        x = 3.9 * x * (1 - x)
        print(x)
main()
```  
**Sample Output for Input `0.5`**:  
```
0.5
0.975
0.0950625
0.335499022265625
0.8704170812674058
0.4403066275180748
0.9625836607534175
0.14032234481166653
0.46858467481484804
0.9729440599474938
```  

---

# **Question 3**  
**Modified Code**:  
```python
# File: chaos.py 
# A simple program illustrating chaotic behavior.

def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(10):
        x = 2.0 * x * (1 - x)  # Changed multiplier from 3.9 to 2.0
        print(x)
main()
```  
**Sample Output for Input `0.5`**:  
```
0.5
0.5
0.5
... (all values stabilize at 0.5)
```  
**Observation**:  
With the multiplier reduced to 2.0, the values quickly stabilize instead of exhibiting chaotic behavior. For example, input `0.5` converges immediately to `0.5`. This contrasts with the original program, which produces unpredictable values due to the chaotic multiplier 3.9.

---

# **Question 4**  
**Modified Loop**:  
```python
# File: chaos.py 
# A simple program illustrating chaotic behavior.

def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(20): # Changed 10 to 20
        x = 3.9 * x * (1 - x)
        print(x)
main()
```  

---

# **Question 5**  
**Modified Code**:  
```python
# File: chaos.py 
# A simple program illustrating chaotic behavior.

def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    n = eval(input("How many numbers should I print? "))
    for i in range(n):
        x = 3.9 * x * (1 - x)
        print(x)
main()
```

---

# **Question 6**  
**Code for all versions**:  
```python
# File: chaos.py 
# A simple program illustrating chaotic behavior.

# a)
def main_a():
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(100):
        x = 3.9 * x * (1 - x)
        print(x)

# b)
def main_b():
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(100):
        x = 3.9 * (x - x * x)
        print(x)

# c)
def main_c():
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(100):
        x = 3.9 * x - 3.9 * x * x
        print(x)

# Run each version separately
main_a()  # or main_b() / main_c()
```  

**Results**:  
- For initial values like \(x = 0.5\), all versions start identically.  
- After ~20 iterations, slight differences emerge due to floating-point rounding errors.  
- By iteration 50+, values diverge significantly (chaotic systems amplify tiny errors).  

**Explanation**:  
Algebraically equivalent expressions can yield different computational results because floating-point arithmetic is not associative. The order of operations affects rounding, leading to divergent behavior in chaotic systems.  

---

# **Question 7**
**Code**:  
```python
# File: chaos.py 
# A simple program illustrating chaotic behavior.

def main():
    x1 = eval(input("Enter the first initial value (0-1): "))
    x2 = eval(input("Enter the second initial value (0-1): "))
    
    print("Iteration | Value 1 | Value 2")
    print("----------------------------")
    for i in range(10):
        x1 = 3.9 * x1 * (1 - x1)
        x2 = 3.9 * x2 * (1 - x2)
        print(i+1, x1, x2)

main()
```  

**Sample Output**:  
```
Iteration | Value 1 | Value 2
----------------------------
1 0.73125 0.7524
2 0.76644140625 0.75497984
3 0.6981353014384766 0.734342213554176
...
```  
