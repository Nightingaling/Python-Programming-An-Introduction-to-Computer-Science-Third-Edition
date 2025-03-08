# **Question 1**  
   - **1. Problem Analysis:** Understand the problem and requirements.  
   - **2. Specification:** Define what the program will do (inputs, outputs, behavior).  
   - **3. Design:** Plan the structure and algorithms (flowcharts, pseudocode).  
   - **4. Implementation:** Write the actual code in a programming language.  
   - **5. Testing/Debugging:** Verify correctness and fix errors.  
   - **6. Maintenance:** Update and improve the program post-deployment.  

---

# **Question 2**  
**Code**:  
```python
# File: chaos.py 
# A simple program illustrating chaotic behavior.

def main():  # function definition
    print("This program illustrates a chaotic function")  # output statement
    x = eval(input("Enter a number between 0 and 1: "))  # assignment
    for i in range(10):  # loop statement
        x = 3.9 * x * (1 - x)  # assignment
        print(x)  # output statement
main()  # function call
```  

1. **Identifiers:**  
   - `main`, `print`, `x`, `eval`, `input`, `i`, `range`.  

2. **Expressions:**  
   - `"This program illustrates a chaotic function"`  
   - `eval(input("Enter a number between 0 and 1: "))` 
   - `range(10)`  
   - `3.9 * x * (1 - x)` 
   - `x`  

---

# **Question 3**  
   - **Definite Loop:** Executes a predetermined number of times.  
   - **For Loop:** A Python construct to implement loops, often definite.  
   - **Counted Loop:** A subset of definite loops that use a counter (e.g., `for i in range(5)`).  
   
   **Summary:** A counted loop is a type of definite loop implemented using a `for` loop.  

---

# **Question 4**  
a)  
**Code**:
```python
for i in range(5):
    print(i * i)
```

**Output:**  
```
0
1
4
9
16
```  

b)  
**Code**:
```python
for d in [3,1,4,1,5]:
    print(d, end=" ")
```

**Output:**  
```
3 1 4 1 5 
```   

c)  
**Code**:
```python
for i in range(4):
    print("Hello")
```

**Output:**  
```
Hello
Hello
Hello
Hello
```   

d)  
**Code**:
```python
for i in range(5):
    print(i, 2**i)
```

**Output:**  
```
0 1
1 2
2 4
3 8
4 16
```   

---

# **Question 5**  
   Pseudocode allows focusing on logic without syntax constraints, making it easier to spot flaws early.  

---

# **Question 6**  
   The `sep` parameter specifies the separator between multiple items in a `print` statement (e.g., `print(1, 2, sep='-')` which outputs `1-2`).  

---

# **Question 7**  
**Code**:
```python
print("start")
for i in range(0):  # Loop runs 0 times (range(0) is empty)
    print("Hello")   # This line is never executed
print("end")
```

**Output:**  
```
start
end
```
