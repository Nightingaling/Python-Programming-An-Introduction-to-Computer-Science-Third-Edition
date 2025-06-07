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
    print(line)
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
<code>
``` 
