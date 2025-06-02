# **Question 1** 
a) `[2,1,4,3,'c','a','b']`  
b) `[2,1,4,3,2,1,4,3,2,1,4,3,'c','a','b','c','a','b']`  
c) `1`  
d) `[1,4]`  
e) `TypeError` → (cannot concatenate `list` + `str`)

---

# **Question 2** 
a)  
  `s1 = [1,4,3]` (removed `2`)  
  `s2 = ['c','a','b']` (unchanged)  
  
b)  
  `s1 = [1,2,3,4]` (sorted)  
  `s2 = ['c','a','b']` (unchanged)  
  
c)  
  `s1 = [2,1,4,3,[2]]` (appended `[s2.index('b')] = [2]`)  
  `s2 = ['c','a','b']` (unchanged)  
  
d)  
  `s1 = [2,1,3]` (`s1.pop(2)` removed `4` at index 2)  
  `s2 = ['c','a','b']` (unchanged, `s2.pop(4)` → IndexError)  
  
e)  
  `s1 = [2,1,4,3]` (unchanged)  
  `s2 = ['c','a','d','b']` (inserted `'d'` at index `s1[0] = 2`)
