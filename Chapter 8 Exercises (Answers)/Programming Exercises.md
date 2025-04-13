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
