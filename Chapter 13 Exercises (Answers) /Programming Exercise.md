# **Question 1**
**Modified Code**:
```python
fib3_calls = 0
def fib_traced(n):
    global fib3_calls
    print(f'Computing fib({n})')
    if n < 3:
        # BASE CASE
        result = 1
    else:
        # COUNTING: Check if this call is fib(3)
        if n == 3:
            fib3_calls = fib3_calls + 1  
        # RECURSIVE STEP
        result = fib_traced(n-1) + fib_traced(n-2)
    print(f'Leaving fib({n}) returning {result}')
    return result

# 2. Call the function
fib_traced(7)

# 3. Check the count
print(f"fib(3) was computed {fib3_calls} times.")
```

---

# **Question 2**
