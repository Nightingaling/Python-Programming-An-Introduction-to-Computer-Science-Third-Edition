# **Question 1**
Given `s1 = "spam"` and `s2 = "ni!"`:  
**a)** `"The Knights who say, " + s2` → `"The Knights who say, ni!"`  
**b)** `3 * s1 + 2 * s2` → `"spamspamspamni!ni!"`  
**c)** `s1[1]` → `'p'`  
**d)** `s1[1:3]` → `"pa"`  
**e)** `s1[2] + s2[:2]` → `"ani"`  
**f)** `s1 + s2[-1]` → `"spam!"`  
**g)** `s1.upper()` → `"SPAM"`  
**h)** `s2.upper().ljust(4) * 3` → `"NI! NI! NI! "`  

---

# **Question 2**
**a)** `s2[:2].upper()` → `"NI"`  
**b)** `s2 + s1 + s2` → `"ni!spamni!"`  
**c)** `' '.join([s1.capitalize() + ' ' + s2.capitalize()] * 3)  ` → `"Spam Ni! Spam Ni! Spam Ni!"`  
**d)** `s1` → `"spam"`  
**e)** `s1.split("a")` → `["sp", "m"]`  
**f)** `s1.replace("a", "")` → `"spm"`

---

# **Question 3**
**a)**  
   ```plaintext
   a
   a
   r
   d
   v
   a
   r
   k
   ```  
**b)**
   ```plaintext
   Now
   is
   the
   winter
   of
   our
   discontent...
   ```  
**c)** `"M ss ss pp"`  
**d)** `"scrt"`  
**e)** `"tfdsfu"`  

---

# **Question 4**
#### **a)**  
```python  
"Looks like {1} and {0} for breakfast".format("eggs", "spam")  
```  
**Result:**  
`"Looks like spam and eggs for breakfast"`    

#### **b)**  
```python  
"There is {0} {1} {2} {3}".format(1, "spam", 4, "you")  
```  
**Result:**  
`"There is 1 spam 4 you"`  

#### **c)**  
```python  
"Hello {0}".format("Susan", "Computewell")  
```  
**Result:**  
`"Hello Susan"`   

#### **d)**  
```python  
"{0:0.2f} {0:0.2f}".format(2.3, 2.3468)  
```  
**Result:**  
`"2.30 2.30"`   

#### **e)**  
```python  
"{7.5f} {7.5f}".format(2.3, 2.3468)  
```  
**Result:**  
(IndexError: Replacement index 7 out of range for positional args tuple)  
**Explanation:**  
Due to invalid placeholder syntax in format string, the 7.5f is interpreted as an invalid index (not a valid integer), and there was no colon(:) to separate the index from the format specification

#### **f)**  
```python  
"Time left {0:02}:{1:05.2f}".format(1, 37.374)  
```  
**Result:**  
`"Time left 01:37.37"`  

#### **g)**  
```python  
"{1:3}".format("14")  
```  
**Result:**  
(IndexError: Replacement index 1 out of range for positional args tuple)  
**Explanation:**  
The operation is illegal because the placeholder {1:3} tries to access a non-existent second argument.

---

# **Question 5**
Public key encryption is more effective for securing Internet communications than private key encryption because it uses a pair of keys (public and private), eliminating the need to securely distribute a shared key, which is a challenge in private key systems. It scales better, allowing secure communication among many users without requiring unique keys for each pair, unlike private key encryption, which needs a separate key for every pair. Private key encryption depends on the secrecy of a shared key, which can be compromised during distribution.
