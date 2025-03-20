# **Question 1**
**Modified Code**:
```python
# dataconvert.py
# Converts a date in form "mm/dd/yyyy" to "month day, year"

def main():
    # get the date
    dateStr = input('Enter a date (mm/dd/yyyy): ')

    # split into components
    monthStr, dayStr, yearStr = dateStr.split("/")

    # convert monthStr to the month name
    months = ["January", "February", "March", "April",
              "May", "June", "July", "August",
              "September", "October", "November", "December"]
    monthStr = months[int(monthStr)-1]

    # output result in month day, year format
    print("The converted date is: {0} {1}, {2}".format(monthStr, dayStr, yearStr))
main()
```

---

# **Question 2**
**Code**:
```python
score = int(input('What is your quiz score: '))
grades = ['F', 'F', 'D', 'C', 'B', 'A']
print('Your grades is: ', grades[score])
```

---

# **Question 3**
**Code**:
```python
score = int(input('What is your exam score: '))
grades = ['F', 'F', 'F', 'F', 'F', 'F', 'D', 'C', 'B', 'A', 'A']
print("Grade:", grades[score // 10])
```

# **Question 4**
**Code**:
```python
phrase = input('Phrase: ')
words = phrase.split()
acronym = ''
for word in words:
    acronym = acronym + word[0].upper()
print(acronym)
```

---

# **Question 5**
**Code**:
```python
name = input('Give a Single Name: ')
total = 0
for i in name.lower():
    n = ord(i) - 96
    total = total + n
print(total)
```

---

# **Question 6**
**Code**:
```python
name = input('Give a Full Name: ').lower()
total = 0
name = name.replace(" ", '')
for i in name:
    n = ord(i) - 96
    total = total + n
print(total)
```

---

# **Question 7**
**Code**:
```python
ch = input('Text: ')
key = int(input('Key: '))

# Encode
encode = ''
for i in ch:
    encode = encode + chr(ord(i) + key)
print(encode)

#Decode
decode = ''
for j in encode:
    decode = decode + chr(ord(j) - key)
print(decode)
```

---

# **Question 8**
**Code**:
```python
# Get the input text from the user
ch = input('Text: ')

# Get the key value from the user
key = int(input('Key: '))

# Initialize an empty string to store the encoded result
encoded = ''

# Loop through each character in the input text
for c in ch:
    # Calculate the position of the character in the alphabet (0-25)
    pos = ord(c) - ord('a')
    # Calculate new position with circular shift, (there are 26 alphabets thus % 26)
    new_pos = (pos + key) % 26
    # Convert new position back to a character and add to result
    encoded = encoded + chr(new_pos + ord('a'))

# Print the encoded text
print('Encoded:', encoded)

# Initialize an empty string to store the decoded result
decoded = ''

# Loop through each character in the encoded text
for c in encoded:
    # Calculate the position of the character in the alphabet (0-25)
    pos = ord(c) - ord('a')
    # Calculate original position by reversing the shift
    new_pos = (pos - key) % 26
    # Convert original position back to a character and add to result
    decoded = decoded + chr(new_pos + ord('a'))

# Print the decoded text
print('Decoded:', decoded)
```
> Note: The problem cannot be fully solved for inputs containing both uppercase and lowercase letters along with spaces using only the concepts covered in chapters 1 to 5. The code I have developed is designed to work specifically with lowercase letters and does not handle uppercase letters or spaces in the input text.

---

# **Question 9**
**Code**:
```python
sentence = input('Sentence: ').split()
print('Word Count: ', len(sentence))
```

---

# **Question 10**
**Code**:
```python
sentence = input('Sentence: ').split()
letter_count = 0
for word in sentence:
    letter_count = letter_count + len(word)
average = letter_count / len(sentence)
print('Average Word Length: ', average)
```

---

# **Question 11**
**Code**:
```python
# File: chaos.py 
# A simple program illustrating chaotic behavior.

def main():
    x1 = eval(input("Enter the first initial value (0-1): "))
    x2 = eval(input("Enter the second initial value (0-1): "))
    iterations = int(input("Enter the number of iterations: "))
    print("{0:>5} {1:>7} {2:>10}".format("Index", x1, x2))
    print("------------------------------")
    for i in range(iterations):
        x1 = 3.9 * x1 * (1 - x1)
        x2 = 3.9 * x2 * (1 - x2)
        print("{0:^5} {1:^10f} {2:^10f}".format((i+1), round(x1, 6), round(x2, 6)))
main()
```

---

# **Question 12**
**Code**:
```python
# futval.py
# A program to compute the value of an investment
def main():
    print("This program calculates the future value")
    principal = eval(input("Enter the initial principal: "))
    apr = float(input("Enter the annual interest rate (e.g., 0.05 for 5%): "))
    years = int(input("Enter the number of years: "))
    print("{0} ${1:>7}".format('Year', 'Value'))
    print('--------------')
    print("{0:^5} ${1:0.2f}".format('0', principal))
    for i in range(years):
        principal = principal * (1 + apr)
        print("{0:^5} ${1:0.2f}".format((i + 1), principal))
main()
```

---

# **Question 13**
**Code**:
```python
# Batch-oriented for Question 9

def main():
    # get the file names
    sentence_file = input('What file is the sentence in? ')
    word_count_file = input('What file should the word count go in? ')

    #open and read the input file
    infile = open(sentence_file, 'r')
    sentence = infile.read()
    infile.close()

    # process the sentence
    word_list = sentence.split()
    word_count = len(word_list)

    # open and write to output file
    outfile = open(word_count_file, 'w')
    print(word_count, file=outfile)
    outfile.close()
    
main()
```

---

# **Question 14**
**Code**:
```python
def main():
    wc_file = input('File: ')
    infile = open(wc_file, 'r')
    line_count = 0
    word_count = 0
    character_count = 0
    for line in infile:
        word_count = word_count + len(line.split())
        character_count = character_count + len(line)
        line_count = line_count + 1
    print('Lines: {0}\nWords: {1}\nCharacters: {2}'.format(line_count, word_count, character_count))
    
main()
```

---

# **Question 15**
**Code**:
```python
from graphics import *

def main():
    # Open and read the exam scores file
    score_file = open('exam_scores.txt', 'r')
    file_lines = score_file.readlines()
    num_students = int(file_lines[0])
    score_file.close()

    # Set up the graphics window
    window_height = num_students * 20  # Adjust height based on number of students
    win = GraphWin('Exam Scores', 300, window_height)
    win.setCoords(0, 0, 3, num_students)  # Set coordinate system for proper alignment

    # Initialize positions for drawing elements
    text_y_position = num_students - 0.5  # Starting Y position for student names
    bar_y_position = num_students - 1     # Starting Y position for score bars

    # Draw each student's name and corresponding score bar
    for i in range(1, num_students + 1):
        # Extract student name and score from the current line
        student_name = file_lines[i].split()[0]
        student_score = int(file_lines[i].split()[1])
        
        # Draw student name
        name_point = Point(0.5, text_y_position)
        Text(name_point, student_name).draw(win)
        
        # Calculate bar length (scaled to fit within window)
        bar_length = 1 + student_score / 50
        
        # Draw score bar
        bar_start = Point(1, text_y_position + 0.25)
        bar_end = Point(bar_length, bar_y_position + 0.25)
        Rectangle(bar_start, bar_end).draw(win)
        
        # Move down to the next position for the next student
        text_y_position = text_y_position - 1
        bar_y_position = bar_y_position - 1

    # Wait for user interaction before closing
    win.getMouse()
    win.close()

main()
```

---

# **Question 16**
**Code**:
```python
from graphics import *

def main():
    # Create graphics window
    window = GraphWin('Quiz Score', 250, 250)
    
    # Open and read the score file
    score_file = open('quiz_score.txt', 'r')
    file_contents = score_file.read()
    score_file.close()

    # Initialize coordinates for drawing
    bar_x, bar_y = 25, 230
    label_x, label_y = 30, 240
    
    # Draw bars and labels for each score
    for score_value in range(11):
        # Calculate the height based on the count of the current score
        count = file_contents.count(str(score_value))
        bar_height = count * 10
        
        # Draw the rectangle bar
        Rectangle(Point(bar_x, bar_y), Point(bar_x + 10, bar_y - bar_height)).draw(window)
        
        # Draw the score label
        Text(Point(label_x, label_y), score_value).draw(window)
        
        # Move to the next position for the next score
        bar_x = bar_x + 20
        label_x = label_x + 20
    
    # Wait for user click before closing
    window.getMouse()
    window.close()

main()
```        
