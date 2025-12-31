# **Question 1**
**Modified Code**:
```python
def fib(n):
    print('Computing fib({0})'.format(n))
    if n < 3:
        fib_num = 1
        count = 0
    else:
        num1, count1 = fib(n-1)
        num2, count2 = fib(n-2)
        fib_num = num1 + num2
        count = count1 + count2
        if n == 3:
            count = count + 1
    print('Leaving fib({0}) returning {1}'.format(n, fib_num))
    return fib_num, count

def main():
    n = 10
    fib_num, fib3_count = fib(n)
    print('Final Result: {0}'.format(fib_num))
    print('Total fib(3) count: {0}'.format(fib3_count))

if __name__ == '__main__':
    main()
```

---

# **Question 2**
**Code**:
```python
class FibCounter:
    def __init__(self):
        self.count = 0

    def getCount(self):
        return self.count

    def fib(self,n):
        self.count = self.count + 1
        if n < 3:
            return 1
        else:
            return self.fib(n-1) + self.fib(n-2)

    def resetCount(self):
        self.count = 0

def main():
    n = int(input('Fibonacci Number: '))
    counter = FibCounter()
    fib_value = counter.fib(n)
    call_count = counter.getCount()
    print('Fib({0}) is {1}'.format(n, fib_value))
    print('The fib function was called {0} times'.format(call_count))

if __name__ == '__main__':
    main()
```

---

# **Question 3**
**Code**:
```python
def palindrome(sentence):
    # Base case: If empty or 1 character, it's a palindrome
    if len(sentence) <= 1:
        return True

    # Get lowercase of first and last character of the sentence
    first_ch = sentence[0].lower()
    last_ch = sentence[-1].lower()

    # Remember every ASCII character has a numeric value
    # Check if any character is not in range of 'a' to 'z'
    # If character is not a letter from 'a' to 'z'. Skip it.
    if not (97 <= ord(first_ch) <= 122):
        return palindrome(sentence[1:])
    elif not (97 <= ord(last_ch) <= 122):
        return palindrome(sentence[:-1])
    else:
        if first_ch == last_ch:
            return palindrome(sentence[1:-1])
        else:
            return False

def main():
    print('Palindrome Phrase Checker')
    sentence = input('Input your phrase: ')
    if palindrome(sentence):
        print('"{0}" is a palindrome phrase'.format(sentence))
    else:
        print('"{0}" is a not palindrome phrase'.format(sentence))

if __name__ == '__main__':
    main()     
```

---

# **Question 4**
**Code**:
```python
def max(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        num = max(lst[1:])
        if lst[0] > num:
            largest = lst[0]
        else:
            largest = num
        return largest
```

---

# **Question 5**
**Code**:
```python
def baseConversion(num, base):
    if num < base:
        print(num, end=' ')
        return num
    else:
        baseConversion(num//base, base)
        print(num%base, end=' ')

def main():
    num = int(input('Enter a Number: '))
    base = int(input('Enter a Base: '))
    baseConversion(num, base)
        
if __name__ == '__main__':
    main()
```

---

# **Question 6**
**Code**:
```python
def num2english(num):
    numberdict = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',
                  6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 0: 'Zero'}
    if num < 10:
        print(numberdict[num%10], end=' ')
        return num
    else:
        num2english(num//10)
    print(numberdict[num%10], end=' ')

def main():
    num = int(input('Enter a Number: '))
    num2english(num)

if __name__ == '__main__':
    main()
```

---

# **Question 7**
**Code**:
```python
def iter_combinatorics(n, k):
    if n < k:
        return 0  
    n_fact = k_fact = nk_fact = 1
    for i in range(1, n + 1):
        n_fact = n_fact * i
    for i in range(1, k + 1):
        k_fact = k_fact * i
    for i in range(1, n - k + 1):
        nk_fact = nk_fact * i
    return n_fact / (k_fact * nk_fact)

def recu_combinatorics(n, k):
    if n < k:
        return 0
    if k == 1: # n possible combination
        return n
    if k == 0 or k == n: # Only 1 possible combination
        return 1
    return recu_combinatorics(n-1, k-1) + recu_combinatorics(n-1, k)

def main():
    n, k = 10, 3
    print('Iterative C({0},{1}): {2}'.format(n, k, iter_combinatorics(n, k)))
    print('Recursive C({0},{1}): {2}'.format(n, k, recu_combinatorics(n, k)))

if __name__ == '__main__':
    main()
```

---

# **Question 8**
**Code**:
```python
from math import *
from graphics import *

class Turtle:

    def __init__(self, win):
        self.win = win
        self.location = Point(250,250)
        self.direction = 0.0

    def moveTo(self, somePoint):
        self.location = somePoint
   
    def draw(self, length):
        x1 = self.location.getX()
        y1 = self.location.getY()
        dx = length * cos(self.direction)
        dy = length * sin(self.direction)
        x2 = x1 + dx
        y2 = y1 + dy
        Line(Point(x1,y1), Point(x2,y2)).draw(self.win)
        self.moveTo(Point(x2,y2))

    def turn(self, degrees):
        # self.direction = radians(degrees) resets the direction it is facing
        # The turtle moves relative to its current heading
        self.direction = self.direction + radians(degrees)


def Koch(Turtle, length, degree):
  if degree == 0:
    Turtle.draw(length)

  else:
    length1 = length / 3
    degree1 = degree - 1
    Koch(Turtle, length1, degree1)
    Turtle.turn(60) # Tell turtle to turn left 60 degree
    Koch(Turtle, length1, degree1)
    Turtle.turn(-120) # Tell turtle to turn right 120 degree
    Koch(Turtle, length1, degree1)
    Turtle.turn(60) # Tell turtle to turn left 60 degree
    Koch(Turtle, length1, degree1)


def main():
    win = GraphWin('Koch', 500, 500)
    win.setCoords(0, 0, 500, 500)
    t = Turtle(win)
    Koch(t, 200, 4)
    t.turn(-120) # Tell turtle to turn right 120 degree
    Koch(t, 200, 4)
    t.turn(-120) # Tell turtle to turn right 120 degree
    Koch(t, 200, 4)
    win.getMouse()
    win.close()


if __name__ == '__main__':
  main()
```

---

# **Question 9**
**Code**:
```python
from math import *
from graphics import *

class Turtle:

    def __init__(self, win):
        self.win = win
        self.location = Point(250,250)
        self.direction = 0.0

    def moveTo(self, somePoint):
        self.location = somePoint
        
    def draw(self, length):
        x1 = self.location.getX()
        y1 = self.location.getY()
        dx = length * cos(self.direction)
        dy = length * sin(self.direction)
        x2 = x1 + dx
        y2 = y1 + dy
        Line(Point(x1,y1), Point(x2,y2)).draw(self.win)
        self.moveTo(Point(x2,y2))

    def turn(self, degrees):
        # self.direction = radians(degrees) resets the direction it is facing
        # The turtle moves relative to its current heading
        self.direction = self.direction + radians(degrees)


def Koch(Turtle, length, degree):
  if degree == 0:
    Turtle.draw(length)

  else:
    length1 = length / sqrt(2)
    degree1 = degree - 1
    Turtle.turn(45) # Tell Turtle to turn left 45 degree
    Koch(Turtle, length1, degree1)
    Turtle.turn(-90) # Tell turtle to turn right 90 degree
    Koch(Turtle, length1, degree1)
    Turtle.turn(45) # Tell turtle to turn left 45 degree


def main():
    win = GraphWin('Koch', 500, 500)
    t = Turtle(win)
    Koch(t, 60, 12)
    win.getMouse()
    win.close()


if __name__ == '__main__':
  main()
```

---

# **Question 10**
**Modified Code**:
```python
def recBinSearch(word, dictionary, low, high):
    if low > high:
        return None

    mid = (low + high) // 2
    item = dictionary[mid]

    if word == item:
        return mid
    elif word < item:
        return recBinSearch(word, dictionary, low, mid-1)
    else:
        return recBinSearch(word, dictionary, mid+1, high)


def search(word, dictionary):
    return recBinSearch(word, dictionary, 0, len(dictionary)-1)


def main():
    try:
        # Ask user for filename and read file
        filename = input('Enter the file name to analyze:')
        document = open(filename, 'r')
        dictionary = open('words.txt', 'r')

        # Store all the words in the dictionary into list called 'wordlist'
        wordlist = [word.rstrip().lower() for word in dictionary]

        # Store content of document as a single multiline string
        documentcontent = document.read()

        # Build a list of valid characters and replace any invalid character
        clean_chars = []
        for char in documentcontent:
            # Check if char is a letter (A-Z or a-z)
            if ('a' <= char <= 'z') or ('A' <= char <= 'Z'):
                clean_chars.append(char)
            else:
                # If not a letter (punctuation/number), replace with space
                clean_chars.append(' ')

        # Join the characters back into a string, and split into words
        clean_text = ''.join(clean_chars)
        documentlist = clean_text.split()

        # Binary search for every word in the document
        print('Checking document...')
        for word in documentlist:
            result = search(word.lower(), wordlist) #.lower() to match dictionary format
            if result == None:
                print("'{0}' is flagged as potentially incorrect".format(word))
        print('Document scan completed')
        dictionary.close()
        document.close()

    except FileNotFoundError:
        print('Error: File not found. Please check the spelling.')


if __name__ == '__main__':
    main()
```

---

# **Question 11**
**Code**:
```python
def recBinSearch(word, dictionary, low, high):
    if low > high:
        return None

    mid = (low + high) // 2
    item = dictionary[mid]

    if word == item:
        print("{0} is in the dictionary".format(word))
        return mid
    elif word < item:
        return recBinSearch(word, dictionary, low, mid-1)
    else:
        return recBinSearch(word, dictionary, mid+1, high)


def search(word, dictionary):
    return recBinSearch(word, dictionary, 0, len(dictionary)-1)


def anagrams(s):
    if s == "":
        return [s]
    else:
        ans = []
        for w in anagrams(s[1:]):
            for pos in range(len(w)+1):
                ans.append(w[:pos]+s[0]+w[pos:])
        return ans


def main():
    dictionary = open('words.txt', 'r')
    wordlist = [word.rstrip().lower() for word in dictionary]
    wordlist.sort()
    dictionary.close()
    word = input('Type in any scrambled word: ').lower()

    anagramset = set(anagrams(word)) #removes any duplicate anagrams
    for anagram in anagramset:
        search(anagram, wordlist)


if __name__ == '__main__':
    main()
```
