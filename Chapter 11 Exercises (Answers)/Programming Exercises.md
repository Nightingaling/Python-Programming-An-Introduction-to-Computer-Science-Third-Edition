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
# gpasort.py

from gpa import Student, makeStudent

def readStudents(filename):
    infile = open(filename, 'r')
    students = []
    for line in infile:
        students.append(makeStudent(line))
    infile.close()
    return students

def writeStudents(students, filename):
    outfile = open(filename, 'w')
    for s in students:
        print("{0}\t{1}\t{2}".format(s.getName(), s.getHours(), s.getQPoints()),file=outfile)
    outfile.close()

def main():
    filename = input("Enter the name of the data file: ")
    data = readStudents(filename)
    field = input("Sort student file based on (GPA, name or credit): ").lower()
    if field == "gpa":
        data.sort(key=Student.gpa)
    elif field == "name":
        data.sort(key=Student.getName)
    elif field == "credit":
        data.sort(key=Student.getHours)
    filename = input("Enter a name for the output file: ")
    writeStudents(data, filename)
    print("The data has been written to", filename)

if __name__ == '__main__':
    main()
```

---

# **Question 3**
**Modified Code**:
```python
# gpasort.py

from gpa import Student, makeStudent

def readStudents(filename):
    infile = open(filename, 'r')
    students = []
    for line in infile:
        students.append(makeStudent(line))
    infile.close()
    return students

def writeStudents(students, filename):
    outfile = open(filename, 'w')
    for s in students:
        print("{0}\t{1}\t{2}".format(s.getName(), s.getHours(), s.getQPoints()),file=outfile)
    outfile.close()

def main():
    filename = input("Enter the name of the data file: ")
    data = readStudents(filename)
    field = input("Sort student file based on (GPA, name or credit): ").lower()
    order = input("Sort in ascending or descending order: ").lower()
    if field == "gpa":
        data.sort(key=Student.gpa)
    elif field == "name":
        data.sort(key=Student.getName)
    elif field == "credit":
        data.sort(key=Student.getHours)
    if order == "descending":
        data.reverse()
    filename = input("Enter a name for the output file: ")
    writeStudents(data, filename)
    print("The data has been written to", filename)

if __name__ == '__main__':
    main()
```

---

# **Question 4**
**Modified Code**:
```python
from gpa import Student, makeStudent
from graphics import *
from button import Button

def readStudents(filename):
    infile = open(filename, 'r')
    students = []
    for line in infile:
        students.append(makeStudent(line))
    infile.close()
    return students

def writeStudents(students, filename):
    outfile = open(filename, 'w')
    for s in students:
        print("{0}\t{1}\t{2}".format(s.getName(), s.getHours(), s.getQPoints()),file=outfile)
    outfile.close()

def main():
    win = GraphWin("GPA Interface", 300, 300)
    # Create entry for input/output file
    infilename = Entry(Point(150,50), 10).draw(win)
    outfilename = Entry(Point(150,80), 10).draw(win)
    # Create text beside entry object to tell user which entry is input/output
    Text(Point(50,50), "Input File:").draw(win)
    Text(Point(50,80), "Output File:").draw(win)
    Text(Point(80,120), "Field to sort by:").draw(win)
    Text(Point(50,190), "Sort in:").draw(win)
    # Create sorting and quit buttons
    GPAbutton = Button(win, Point(60,150), 50, 25, "GPA")
    Namebutton = Button(win, Point(120,150), 50, 25, "Name")
    Creditbutton = Button(win, Point(180,150), 50, 25, "Credit")
    ascendbutton = Button(win, Point(80,220), 100, 25, "Ascending")
    descendbutton = Button(win, Point(200,220), 100, 25, "Descending")
    quitbutton = Button(win, Point(150,270), 50, 25, "Quit")
    GPAbutton.activate()
    Namebutton.activate()
    Creditbutton.activate()
    quitbutton.activate()
    # User selection and subsequent operations
    p = win.getMouse()
    while quitbutton.clicked(p) != True:
        data = readStudents(infilename.getText())
        if GPAbutton.clicked(p):
            data.sort(key=Student.gpa)
        elif Namebutton.clicked(p):
            data.sort(key=Student.getName)
        elif Creditbutton.clicked(p):
            data.sort(key=Student.getHours)
        # enable ascending and descending button to be pressed
        ascendbutton.activate()
        descendbutton.activate()
        p = win.getMouse()
        if descendbutton.clicked(p):
            data.reverse()
        elif quitbutton.clicked(p):
            break
        writeStudents(data, outfilename.getText())
        # Create text to tell user output file has been successfully created and sorted
        outcome = Text(Point(150,10), "The data has been written to {0}".format(outfilename.getText())).draw(win)
        ascendbutton.deactivate()
        descendbutton.deactivate()
        p = win.getMouse()
        outcome.undraw()
    win.close()

if __name__ == '__main__':
    main()
```

---

# **Question 5**
**Code**:
```python
# a)
def count(myList, x):
    count = 0
    for i in myList:
        if i == x: count = count + 1
    return count

# b)
def isin(myList, x):
    for i in myList:
        if i == x: return True
    return False

# c)
def index(myList, x):
    for i in range(len(myList)):
        if myList[i] == x: return i
    return "ValueError: {0} is not in the list".format(x)

# d)
def reverse(myList):
    for i in range(len(myList) // 2):
        start = myList[i]
        myList[i] = myList[-i-1]
        myList[-i-1] = start

# e)
def sort(myList):
    for j in range(len(myList) - 1):
        for i in range(len(myList) - j - 1):
            if myList[i+1] < myList[i]:
                current = myList[i]
                myList[i] = myList[i+1]
                myList[i+1] = current
```

---

# **Question 6**
**Code**:
```python
from random import randrange

def shuffle(myList):
    # Create a copy to avoid modifying the original list
    shuffled = myList[:]  
    n = len(shuffled)
    for i in range(n - 1, 0, -1):  # Start from the last element
        j = randrange(0, i + 1)   # Random index between 0 and i
        shuffled[i], shuffled[j] = shuffled[j], shuffled[i]  # Swap
    return shuffled
```

---

# **Question 7**
**Code**:
```python
def innerProd(x,y):
    total = 0
    for i in range(len(x)):
        total = total + (x[i] * y[i])
    return total
```

---

# **Question 8**
**Code**:
```python
def removeDuplicates(somelist):
    noduplicate = []
    for i in somelist:
        if i not in noduplicate:
            noduplicate.append(i)
    return noduplicate
```

---

# **Question 9**
**Modified Code**:    
gpasort.py
```python
from gpa import Student, makeStudent

def readStudents(filename):
    infile = open(filename, 'r')
    students = []
    for line in infile:
        students.append(makeStudent(line))
    infile.close()
    return students

def writeStudents(students, filename):
    outfile = open(filename, 'w')
    for n in students:
        s = n[1]
        print("{0}\t{1}\t{2}".format(s.getName(), s.getHours(), s.getQPoints()),file=outfile)
    outfile.close()

def main():
    print("This program sorts student grade information by GPA")
    filename = input("Enter the name of the data file: ")
    data = readStudents(filename)
    # Bubble sort
    for j in range(len(data) - 1):
        for i in range(len(data) - 1 - j):
            if data[i][0] > data[i+1][0]:
                data[i], data[i+1] = data[i+1], data[i]
    filename = input("Enter a name for the output file: ")
    writeStudents(data, filename)
    print("The data has been written to", filename)

if __name__ == '__main__':
    main()
```

gpa.py
```python

#   Program to find student with highest GPA

class Student:
    def __init__(self, name, hours, qpoints):
        self.name = name
        self.hours = float(hours)
        self.qpoints = float(qpoints)
    
    def getName(self): 
        return self.name
    
    def getHours(self): 
        return self.hours
    
    def getQPoints(self): 
        return self.qpoints
    
    def gpa(self):
        return self.qpoints / self.hours

def makeStudent(infoStr):
    # infoStr is a tab-separated line: name hours qpoints
    # returns a corresponding Student object
    name, hours, qpoints = infoStr.split("\t")
    return (int(qpoints)/int(hours), Student(name, hours, qpoints))

def main():
    # open the input file for reading
    filename = input("Enter the name of the grade file: ")
    infile = open(filename, 'r')

    # set best to the record for the first student in the file
    best = makeStudent(infile.readline())

    # process subsequent lines of the file
    for line in infile:
        # turn the line into a student record
        s = makeStudent(line)
        # if this student is best so far, remember it.
        if s.gpa() > best.gpa():
            best = s
    infile.close()

    # print information about the best student
    print("The best student is:", best.getName())
    print("hours:", best.getHours())
    print("GPA:", best.gpa())

if __name__ == '__main__':
    main()
```        

---

# **Question 10**
**Code**:
```python
n = int(input('Primes up to: '))
list = []
prime_numbers = []
for i in range(2, n+1):
    list.append(i)
while list != []:
    prime = list.pop(0)
    prime_numbers.append(prime)
    for i in list:
        if i % prime == 0:
            list.remove(i)
print('The prime numbers up to {0} are: {1}'.format(n, prime_numbers))
```        

---

# **Question 11**
**Code**:
```python
filename = input('Enter the name of the data file: ')
outfilename = input('Enter the name for the output file: ')
outfile = open(outfilename, 'w')
infile = open(filename, 'r')
for line in infile:
    words = line.split()
    processed_words = []
    for word in words:
        if len(word) == 4:
            processed_words.append("****")
        else:
            processed_words.append(word)
    line = " ".join(processed_words)
    print(line, file=outfile)
infile.close()
outfile.close()
```        
> The question specifically mentioned 'You can ignore punctuation'. Thus, in the input file, there must not have any punctuation. If the input file has punctuations, any word with 4 letters with the punctuation will count as a 5 letter word, causing contradiction with the question.

---

# **Question 12**
**Modified Code**:
```python
filename = input('Enter the name of the data file: ')
censoredfilename = input('Enter the name of the file for the censored words: ')
outfilename = input('Enter the name for the output file: ')
infile = open(filename, 'r')
censored = open(censoredfilename, 'r')
outfile = open(outfilename, 'w')
cwords_list = []
for cword in censored.readlines():
    cwords_list.append(cword.rstrip())
censored.close()
for line in infile:
    words = line.split()
    processed_words = []
    for word in words:
        if(word.lower() in cwords_list):
            processed_words.append("*" * len(word))
        else:
            processed_words.append(word)
    line = " ".join(processed_words)
    print(line, file=outfile)
infile.close()
outfile.close()
``` 

---

# **Question 13**
**Code**:
```python
class Card:

    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank

    def getRank(self):
        return self.rank

    def getSuit(self):
        return self.suit

    def __str__(self):
        if self.rank == 1:
            self.display_rank = 'Ace'
        elif self.rank == 11:
            self.display_rank = 'Jack'
        elif self.rank == 12:
            self.display_rank = 'Queen'
        elif self.rank == 13:
            self.display_rank = 'King'
        else:
            self.display_rank = self.rank
        return ('{0} of {1}'.format(self.display_rank, self.suit))


def main():
    # read list of cards from a file
    infile = open('cards.txt', 'r')
    deck = []
    for card in infile.readlines():
        rank, suit = card.split()
        deck.append(Card(int(rank),suit))
    deck.sort(key=Card.getRank)
    deck.sort(key=Card.getSuit)
    for card in deck:
        print(card)
    infile.close()


if __name__ == "__main__":
    main()
``` 

---

# **Question 14**
**Modified Code**:
```python
class Card:

    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank

    def getRank(self):
        return self.rank

    def getSuit(self):
        return self.suit

    def __str__(self):
        if self.rank == 1:
            self.display_rank = 'Ace'
        elif self.rank == 11:
            self.display_rank = 'Jack'
        elif self.rank == 12:
            self.display_rank = 'Queen'
        elif self.rank == 13:
            self.display_rank = 'King'
        else:
            self.display_rank = self.rank
        return('{0} of {1}'.format(self.display_rank, self.suit))

    def XHigh(self, num, ace):
        if num == 11:
            self.rank = 'Jack'
        elif num == 12:
            self.rank = 'Queen'
        elif num == 13:
            self.rank = 'King'
        else:
            self.rank = num
        if ace:
            print('The hand is Ace high')
        else:
            print('The hand is {0} high'.format(self.rank))


def main():
    # read list of cards from a file
    infile = open('cards.txt', 'r')
    hand = []
    handranks = []
    handsuits = []
    ace = False
    for card in infile.readlines():
        rank, suit = card.split()
        if int(rank) == 1:
            ace = True
        handranks.append(int(rank))
        handsuits.append(suit)
        hand.append(Card(int(rank),suit))
        if len(hand) == 5:
            break
    hand.sort(key=Card.getRank)
    hand.sort(key=Card.getSuit)
    handranks.sort()
    for card in hand:
        print(card)
    infile.close()
    suitscount = handsuits.count(handsuits[0])
    rankscount = handranks.count(handranks[1])
    rankscount_1 = handranks.count(handranks[3])
    # using middle to count for Three of a kind
    rankscount_2 = handranks.count(handranks[2])
    ranks_in_a_row = 0
    for i in range(len(handranks) - 1):
        if (handranks[i] + 1) != handranks[i+1]:
            break
        else:
            ranks_in_a_row = ranks_in_a_row + 1
    if handranks == [1,10,11,12,13] and suitscount == 5:
        print('Your hand is a Royal Flush')
    elif suitscount == 5:
        if ranks_in_a_row == 4:
            print('Your hand is a Straight Flush')
        else:
            print('Your hand is a Flush')
    elif rankscount == 4:
        print('Your hand is a Four of a Kind')
    elif (rankscount == 3 and rankscount_1 == 2) or (rankscount == 2 and rankscount_1 == 3):
        print('Your hand is a Full House')
    elif (ranks_in_a_row == 4) or (handranks == [1,10,11,12,13]):
        print('Your hand is a Straight')
    #[1,1,1,2,3] or [1,2,2,2,3] or [1,2,3,3,3]
    elif rankscount_2 == 3:
        print('Your hand is a Three of a kind')
    #[1,1,2,2,3] or [1,2,2,3,3] or [1,1,2,3,3]
    elif (rankscount == 2) and (rankscount_1 == 2):
        print('Your hand is a Two pair')
    #[1,1,2,3,4] or [1,2,2,3,4] or [1,2,3,3,4] or [1,2,3,4,4]
    elif (rankscount == 2) or (rankscount_1 == 2):
        print('Your hand is a Pair')
    else:
        card.XHigh(handranks[-1], ace)


if __name__ == "__main__":
    main()
``` 

---

# **Question 15**
**Code**:
```python
from random import randrange

class Deck:

    def __init__(self):
        self.deck = []
        for i in ['Diamonds', 'Clubs', 'Hearts', 'Spades']:
            self.deck.append(['Ace', i])
            for j in range(2, 11):
                self.deck.append([j, i])
            self.deck.append(['Jack', i])
            self.deck.append(['Queen', i])
            self.deck.append(['King', i])

    def shuffle(self):
        for i in range(len(self.deck) - 1, -1, -1):
            j = randrange(0, i + 1)
            self.deck[i], self.deck[j] = self.deck[j], self.deck[i]
            
    def dealCard(self):
        return self.deck.pop(0)
    
    def cardsLeft(self):
        return len(self.deck)


def main():
    k = int(input('Enter number of cards to deal: '))
    deck = Deck()
    deck.shuffle()
    n = 0
    lose = 0
    while deck.cardsLeft() >= k:
        hand = []
        n = n + 1
        for i in range(k):
            hand.append(deck.dealCard())
        print(hand)
        total = 0
        hasAce = False
        for i in hand:
            if i[0] == "Ace" and (not hasAce):
                total = total + 11
                hasAce = True
            elif str(i[0]) in 'Jack Queen King':
                total = total + 10
            elif i[0] == 'Ace' and hasAce:
                total = total + 1
            else:
                total = total + i[0]
        while True:
            if deck.cardsLeft() == 0:
                break
            if 17 <= total <= 21:
                break
            elif total > 21:
                lose = lose + 1
                break
            else:
                draw = deck.dealCard()
                if draw[0] == "Ace" and hasAce:
                    total = total + 1
                elif str(draw[0]) in 'Jack Queen King':
                    total = total + 10
                elif draw[0] == "Ace":
                    total = total + 11
                    hasAce = True
                    if total > 21:
                        total = total - 10
                else:
                    total = total + draw[0]
    print('The probability that the dealer will bust is: {0:0.2f}'.format(lose/n))


if __name__ == '__main__':
    main()
``` 

---

# **Question 16**
**Code**:
```python
from math import sqrt

class StatSet:

    def __init__(self):
        self.nums = []

    def addNumber(self,x):
        self.nums.append(x)

    def mean(self):
        total = 0.0
        for num in self.nums:
            total = total + num
        return total / len(self.nums)

    def median(self):
        copy = self.nums
        copy.sort()
        size = len(copy)
        midPos = size // 2
        if size % 2 == 0:
            med = (copy[midPos] + copy[midPos-1]) / 2.0
        else:
            med = copy[midPos]
        return med

    def stdDEV(self):
        sumDevSq = 0.0
        for num in self.nums:
            dev = num - self.mean()
            sumDevSq = sumDevSq + dev * dev
        return sqrt(sumDevSq / (len(self.nums) - 1))

    def count(self):
        return len(self.nums)

    def min(self):
        smallest = self.nums[0]
        for i in range(1, len(self.nums)):
            if self.nums[i] < smallest:
                smallest = self.nums[i]
        return smallest

    def max(self):
        largest = self.nums[0]
        for i in range(1, len(self.nums)):
            if self.nums[i] > largest:
                largest = self.nums[i]
        return largest
``` 

---

# **Question 17**
**Code**:
```python
from graphics import *

class GraphicsGroup:

    def __init__(self, anchor):
        self.group = []
        # By using .clone() ensures the cloned point is move, but the orignial point remains
        self.p = anchor.clone()

    def getAnchor(self):
        return self.p

    def addObject(self, gObject):
        self.group.append(gObject)

    def move(self, dx, dy):
        self.p.move(dx,dy)
        for obj in self.group:
            obj.move(dx,dy)

    def draw(self, win):
        for obj in self.group:
            obj.draw(win)

    def undraw(self):
        for obj in self.group:
            obj.undraw()
``` 

---

# **Question 18**
**Modified Code**:
```python
from random import randrange

n = int(input("Length of sidewalk: "))
position = (n // 2)
sidewalk = [0] * n
sidewalk[position] = sidewalk[position] + 1
while True:
    if randrange(0, 2) == 1:
        position = position + 1
        if position >= n:
            break
        sidewalk[position] = sidewalk[position] + 1
    else:
        position = position - 1
        if position < 0:
            break
        sidewalk[position] = sidewalk[position] + 1
for i in range(len(sidewalk)):
    print('Square {0}: {1} steps'.format(i, sidewalk[i]))
``` 

---

# **Question 19**
**Code**:
```python
<code>
```
