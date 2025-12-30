# **Question 1**  
Functions help organize code into reusable blocks, reducing redundancy and improving readability. They also make programs easier to maintain and debug by isolating specific tasks.  

---

# **Question 2**  
Yes. While functions introduce modularity, the program still executes sequentially. When a function is called, the main program suspends, the function body runs step-by-step, and control returns to the main program after completion.  

---

# **Question 3**  
**(a) Purpose of parameters:**  
Parameters act as inputs to a function, allowing data to be passed from the caller for processing.  

**(b) Formal vs. actual parameters:**  
- **Formal parameters:** Variables defined in the function header.  
- **Actual parameters:** Values or variables passed during the function call.  

**(c) Similarities and differences between parameters and ordinary variables:**    
- **Similarities:**
  - Both store values and can use expressions.  
- **Differences:**  
  - Parameters are local to the function and exist only during its execution.  
  - Ordinary variables have broader scope

---

# **Question 4**  
**(a) Providing input to a function:**  
Input is provided through actual parameters passed to the function’s formal parameters.  

**(b) Providing output from a function:**  
A function provide output using the `return` statement, which the caller can capture in a variable or use directly.  

---

# **Question 5**  
**(a) What does this function do?**  
It computes and returns the cube of `x`

**(b) How to use it to print \(y^3\):**  
**Code**:  
```python  
y = 5  
result = cube(y)  
print(result)  
```  

**(c) Why the output is `4 27`, not `27 27`:**  
Modifying the local variable `answer` inside the `cube` function does not affect the variable `answer` in the main program. When the function is called, Python passes the value of `x` into the function by object reference. However, since integers are immutable, the assignment `answer = x * x * x` inside the function simply creates or updates a new local variable named answer that exists only within the function’s scope. Therefore, the global `answer` in the main program remains `4`, and the function computes `27` and returns it, thus the output is `4 27`.
