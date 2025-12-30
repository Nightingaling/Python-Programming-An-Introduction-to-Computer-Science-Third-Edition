# **Question 1**  
a) **7.4** (float)  

b) **5.0** (float)   

c) **8** (int)  

d) **Illegal**  
sqrt(4.5 - 5.0) = sqrt(-0.5) -> Math domain error (cannot compute square root of a negative number).  

e) **11** (int)  

f) **27** (int)  

---

# **Question 2**  
a) `(3 + 4) * 5`  
b) `n * (n - 1) / 2`  
c) `4 * math.pi * r**2`  
d) `math.sqrt(r * (math.cos(a)**2) + r * (math.sin(b)**2))`  
e) `(y2 - y1) / (x2 - x1)`  

---

# **Question 3**  
a) `[0, 1, 2, 3, 4]`  
b) `[3, 4, 5, 6, 7, 8, 9]`  
c) `[4, 7, 10]`  
d) `[15, 13, 11, 9, 7]`  
e) `[]` (empty sequence; start > end with default step=1).  

--- 

# **Question 4**
**a)**
**Code**:
```python
for i in range(1, 11):
    print(i * i)
```

**Output:**  
```
1  
4  
9  
16  
25  
36  
49  
64  
81  
100  
```  

---

**b)**  
**Code**:
```python
for i in [1, 3, 5, 7, 9]:
    print(i, ":", i ** 3)
print(i)
```

**Output:**  
```
1 : 1
3 : 27
5 : 125
7 : 343
9 : 729
9
```   

---

**c)**  
**Code**:
```python
x = 2
y = 10
for j in range(0, y, x):
    print(j, end="")  # No space/newline between outputs
print(x + y)
print("done")
```

**Output:**  
```
0246812
done
```  

---

**d)**  
**Code**:
```python
ans = 0
for i in range(1, 11):
    ans = ans + i * i
    print(i)
print(ans)
```

**Output:**  
```
1  
2  
3  
4  
5  
6  
7  
8  
9  
10  
385  
```  

---

# **Question 5**  
**Example:** `round(314.159265, -1)`  
- The second parameter `-1` rounds to the **tens place**.  
- `round(314.159265, -1)` → `310.0` (rounds to tens place).
- `round(314.159265, -2)` → `300.0` (rounds to hundreds place).  

---

# **Question 6**  
**Python’s Rules:**  
- Integer division (`//`) uses **floor division** (rounds down).  
- Remainder (`%`) satisfies: ( a = (a // b) * b + (a % b) ).  

| Expression | Python Result | Explanation |  
|------------|---------------|-------------|  
| **a)** `-10 // 3` | `-4` | (-10 ÷ 3 = -3.333 → floor is -4) |  
| **b)** `-10 % 3` | `2` | -10 = (-4) * 3 + 2 |  
| **c)** `10 // -3` | `-4` | (10 ÷ -3 = -3.333 → floor is -4) |  
| **d)** `10 % -3` | `-2` | 10 = (-4) * (-3) + (-2) |  
| **e)** `-10 // -3` | `3` | (-10 ÷ -3 = 3.333 → floor is 3) |  
