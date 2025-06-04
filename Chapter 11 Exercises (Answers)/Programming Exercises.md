# **Question 1**
**Modified Code**:
```python
from math import sqrt

def getNumbers():
    nums = []   # start with an empty list
    # sentinel loop to get numbers
    xStr = input("Enter a number (<Enter> to quit) >> ")
    while xStr != "":
        x = float(xStr)
        nums.append(x)  # add this value to the list
        xStr = input("Enter a number (<Enter> to quit) >> ")
    return nums

def mean(nums):
    total = 0.0
    for num in nums:
        total = total + num
    return total / len(nums)

def stdDev(nums):
    n = len(nums)
    if n <= 1:
        return 0.0
    else:
        sumDevSq = 0.0
        xbar = mean(nums)
        for num in nums:
            dev = num - xbar
            sumDevSq = sumDevSq + dev * dev
        return sqrt(sumDevSq / (n-1))

def meanStdDev(nums):
    return (mean(nums), stdDev(nums))

def main():
    print("This program computes mean and/or standard deviation.")
    data = getNumbers()
    if len(data) == 0:
        print('No numbers entered. Exiting')
        return #exit from main()
    stats = input('Stats to compute (mean, stdDev, or both): '.lower())
    if stats == 'mean':
        print('The mean is {0:0.2f}'.format(mean(data)))
    elif stats == 'stddev':
        print('The standard deviation is {0:0.2f}'.format(stdDev(data)))
    elif stats == 'both':
        m, sd = meanStdDev(data)
        print('The mean is {0:0.2f}, and the standard deviation is {1:0.2f}'.format(m, sd))
    else:
        print('Invalid input, Exiting')

if __name__ == '__main__': main()
```

---

# **Question 2**
**Modified Code**:
```python
<code>
```
