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
**Modified Code**:
```python
<code>
```
