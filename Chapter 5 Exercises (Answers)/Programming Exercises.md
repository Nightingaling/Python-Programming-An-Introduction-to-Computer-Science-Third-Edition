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
