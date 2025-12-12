# **Question 1**  
$\log_2 n$  
$n$  
$n \log_2 n$  
$n^2$  
$2^n$

---

# **Question 2**  
*Base Case: A non-recursive exit condition.*  

*Recursive Step: The recursive call must change the state to move closer to the base case. (Calling the function again without reducing the problem size, will get an infinite recursion).*

---

# **Question 3**
`['foo', 'ofo', 'oof', 'foo', 'ofo', 'oof']`

**Explanation:**
Standard anagram algorithms that generate permutations by position will produce duplicates if the input letters aren't unique.

---

# **Question 4**
The total number of multiplications performed is **5**.

### 1. Execution Trace Table

| Call Depth | Function Call | `n` Value | Condition | Action / Recursive Call | Multiplications Added |
| :---: | :--- | :---: | :--- | :--- | :---: |
| **1** | `recPower(3, 6)` | 6 | Even | Calls `recPower(3, 3)` | **1** |
| **2** | `recPower(3, 3)` | 3 | Odd | Calls `recPower(3, 1)` | **2** |
| **3** | `recPower(3, 1)` | 1 | Odd | Calls `recPower(3, 0)` | **2** |
| **4** | `recPower(3, 0)` | 0 | Base Case | Returns `1` | **0** |
| | | | | **Total** | **5** |


### 2. Step-by-Step Return Sequence

The multiplications happen as the recursion **unwinds** (returns).

1.  **Call 4 Returns:** `recPower(3, 0)` returns **1**.
    * *Multiplications performed:* 0

2.  **Call 3 Returns:** Back in `recPower(3, 1)` (Odd case).
    * Code executed: `return factor * factor * a`
    * Calculation: $1 \times 1 \times 3 = 3$
    * *Multiplications performed:* **2**

3.  **Call 2 Returns:** Back in `recPower(3, 3)` (Odd case).
    * Code executed: `return factor * factor * a`
    * Calculation: $3 \times 3 \times 3 = 27$
    * *Multiplications performed:* **2**

4.  **Call 1 Returns:** Back in `recPower(3, 6)` (Even case).
    * Code executed: `return factor * factor`
    * Calculation: $27 \times 27 = 729$
    * *Multiplications performed:* **1**

**Total:** $0 + 2 + 2 + 1 = \mathbf{5}$ multiplications.

---

# **Question 5**
Divide-and-conquer algorithms are efficient because they repeatedly split the problem size in half, which keeps the recursion depth shallow (specifically, $\log_2 n$ levels deep).
Unlike simpler algorithms that often use nested loops $O$($n^2$), divide-and-conquer reduces the number of times we must process the data. 
For sorting, this improves performance from quadratic time $O$($n^2$) to log-linear time $O$($nlogn$), which is significantly faster for large inputs.
