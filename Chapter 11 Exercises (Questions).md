# Chapter 11: Data Collections

</br>

## Review Questions
True/False

    1. The median is the average of a set of data.
    2. Standard deviation measures how spread out a data set is.
    3. Arrays are usually heterogeneous, but lists are homogeneous.
    4. A Python list cannot grow and shrink in size.
    5. Unlike strings, Python lists are not mutable.
    6. A list must contain at least one item.
    7. Items can be removed from a list with the del operator.
    8. A tuple is similar to an immutable list.
    9. A Python dictionary is a kind of sequence.

</br>

## Multiple Choice
### 1. Where mathematicians use subscripting, computer programmers use
    a) slicing b) indexing c) Python d) caffeine
    
### 2. Which of the following is not a built-in sequence operation in Python?
    a) sorting b) concatenation c) slicing d) repetition
    
### 3. The method that adds a single item to the end of a list is
    a) extend b) add c) plus d) append
    
### 4. Which of the following is not a Python list method?
    a) index b) insert c) get d) pop
    
### 5. Which of the following is not a characteristic of a Python list?
    a) It is an object. b) It is a sequence.
    c) It can hold objects. d) It is immutable.
    
### 6. Which of the following expressions correctly tests if x is even?
    a) x % 2 == 0 b) even(x) c) not odd(x) d) x % 2 == x
    
### 7. The parameter xbar in stdDev is what?
    a) median b) mode c) spread d) mean
    
### 8. What keyword parameter is used to send a key-function to the sort method?
    a) reverse b) reversed c) cmp d) key
    
### 9. Which of the following is not a dictionary method?
    a) get b) keys c) sort d) clear
    
### 10. The items dictionary method returns
    a) int b) sequence of tuples c) bool d) dictionary

</br>

## Discussion
### 1. Given the initial statements
    s1 = [2,1,4,3]
    s2 = ['c','a','b']
### Show the result of evaluating each of the following sequence expressions:
    a) s1 + s2
    b) 3 * s1 + 2 * s2
    c) s1[1]
    d) s1[1:3]
    e) s1 + s2[-1]

</br>

### 2. Given the same initial statements as in the previous problem, show the values of s1 and s2 after executing each of the following statements. Treat each part independently (i.e., assume that s1 and s2 start with their original values each time).
    a) s1.remove(2)
    b) s1.sort()
    c) s1.append([s2.index('b')])
    d) s2.pop(s1.pop(2))
    e) s2.insert(s1[0], 'd')

</br>

## Programming Exercises
PAGE 429
