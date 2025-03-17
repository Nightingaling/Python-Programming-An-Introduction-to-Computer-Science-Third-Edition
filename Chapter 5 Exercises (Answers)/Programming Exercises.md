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
ch = input('Single Text: ')
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
