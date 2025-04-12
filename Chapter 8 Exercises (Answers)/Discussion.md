# **Question 1**  
**a) Definite Loop vs. Indefinite Loop**   
- **Definite loop:** Executes a predetermined number of times (e.g., `for` loop with `range`).  
- **Indefinite loop:** Runs until a condition is met, potentially infinitely (e.g., `while` loop).  

**1b) For Loop vs. While Loop**  
- **For loop:** Typically definite, iterating over a sequence (e.g., `for i in range(10)`).  
- **While loop:** Indefinite, runs while a condition is true (e.g., `while x < 10`).  

**1c) Interactive Loop vs. Sentinel Loop**  
- **Interactive loop:** Prompts the user each iteration (e.g., "Continue? (y/n)").  
- **Sentinel loop:** Stops when a specific value is entered (e.g., "Enter 999 to quit").  

**1d) Sentinel Loop vs. End-of-File Loop**  
- **Sentinel loop:** Terminates when a predefined value is met.  
- **End-of-file (EOF) loop:** Terminates when the end of a *file* is reached.  

---

# **Question 2**  
a)
| P     | Q     | Result |
|-------|-------|--------|
| False | False | True   |
| False | True  | True   |
| True  | False | True   |
| True  | True  | False  |

b)
| P     | Q     | Result |
|-------|-------|--------|
| False | False | False  |
| False | True  | True   |
| True  | False | False  |
| True  | True  | False  |

c)
| P     | Q     | Result |
|-------|-------|--------|
| False | False | True   |
| False | True  | True   |
| True  | False | True   |
| True  | True  | False  |

d)
| P     | Q     | R     | Result |
|-------|-------|-------|--------|
| False | False | False | False  |
| False | False | True  | True   |
| False | True  | False | False  |
| False | True  | True  | True   |
| True  | False | False | False  |
| True  | False | True  | True   |
| True  | True  | False | True   |
| True  | True  | True  | True   | 

e)
| P     | Q     | R     | Result |
|-------|-------|-------|--------|
| False | False | False | False  |
| False | False | True  | True   |
| False | True  | False | False  |
| False | True  | True  | True   |
| True  | False | False | False  |
| True  | False | True  | True   |
| True  | True  | False | True   |
| True  | True  | True  | True   | 

---

# **Question 3**  
a)  
**Code**:
```python  
n = int(input("Enter n: "))  
total = 0  
i = 1  
while i <= n:  
    total = total + i  
    i = i + 1  
print(total)  
```  

b)  
**Code**:
```python  
n = int(input("Enter n: "))  
total = 0  
current_odd = 1  
count = 0  
while count < n:  
    total = total + current_odd  
    current_odd = current_odd + 2  
    count = count + 1  
print(total)  
```  

c)  
**Code**:
```python  
total = 0  
user_input = input("Enter a number (999 to quit): ")  
while user_input != "999":  
    total = total + int(user_input)  
    user_input = input("Enter a number (999 to quit): ")  
print(total)  
```  

d)  
**Code**:
```python  
n = int(input("Enter n: "))  
count = 0  
while n > 1:  
    n = n // 2  
    count = count + 1  
print(count)  
```  
