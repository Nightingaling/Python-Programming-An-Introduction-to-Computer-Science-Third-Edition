# **Question 1**
- **Similarities**:  
  Instance variables and "regular" function variables are variables that store data/value
- **Differences**:  
  - *Scope*:  
    - Regular function variables are **local** (exist only within the function).  
    - Instance variables are **object-bound** (accessible via `self` throughout the class).  
  - *Lifetime*:  
    - Regular variables are destroyed after function execution.  
    - Instance variables persist as long as the object exists.  
  - *Access*:  
    - Regular variables are accessed by name directly.  
    - Instance variables require `self.` (e.g., `self.name`).    

---

# **Question 2**   
```python
class Person:
    # c) Constructor
    def __init__(self, name, age):
        # b) Instance variables
        self.name = name  # Instance variable 1
        self.age = age    # Instance variable 2

    # a) Method
    def greet(self):
        return f"Hello, I'm {self.name}!"
    
    # d) Accessor (getter)
    def get_age(self):
        return self.age
    
    # e) Mutator (setter)
    def set_age(self, new_age):
        self.age = new_age
```

---

# **Question 3**
Output:  
Clowning around now.  
Creating a Bozo from: 3  
Creating a Bozo from: 4  
Clowning: 3  
18  
9  
Clowning: 2  
12  
Clowning:8  
64  
16
