# Chapter 10: Defining Classes

</br>

## Review Questions
True/False

    1. New objects are created by invoking a constructor.
    2. Functions that live in objects are called instance variables.
    3. The first parameter of a Python method definition is called this.
    4. An object may have only one instance variable.
    5. In data processing, a collection of information about a person or thing is called a file.
    6. In a Python class, the constructor is called __init__.
    7. A docstring is the same thing as a comment.
    8. Instance variables go away once a method terminates.
    9. Method names should always begin with one or two underscores.
    10. It is considered bad style to directly access an instance variable outside of a class definition.

</br>

## Multiple Choice
### 1. What Python reserved word starts a class definition?
    a) def b) class c) object d) __init__
    
### 2. A method definition with four formal parameters is generally called with how many actual parameters?
    a) three b) four c) five d) it depends
    
### 3. A method definition is similar to a(n)
    a) loop b) module c) import statement d) function definition
    
### 4. Within a method definition, the instance variable x could be accessed via which expression?
    a) x b) self.x c) self[x] d) self.getX()
      
### 5. A Python convention for defining methods that are "private" to a class is to begin the method name with
    a) "private" b) a pound sign (#)
    c) an underscore (_) d) a hyphen (-)
    
### 6. The term applied to hiding details inside class definitions is
    a) obscuring b) subclassing
    c) documentation d) encapsulation
    
### 7. A Python string literal can span multiple lines if enclosed with
    a) " b) ' c) """ d) \
    
### 8. In a Button widget, what is the data type of the instance variable active?
    a) bool b) int c) float d) str
    
### 9. Which of the following methods is not part of the Button class in this chapter?
    a) activate b) deactivate c) setLabel d) clicked
    
### 10. Which of the following methods is part of the DieView class in this chapter?
    a) activate b) setColor c) setValue d) clicked

</br>

## Discussion
### 1. Explain the similarities and differences between instance variables and "regular" function variables. 

</br>

### 2. Explain the following in terms of actual code that might be found in a class definition:
    a) method
    b) instance variable
    c) constructor
    d) accessor
    e) mutator

</br>

### 3. Show the output that would result from the following nonsense program:
    class Bozo:
    
        def __init__ (self, value):
            print("Creating a Bozo from:", value)
            self.value = 2 * value
            
        def clown(self, x):
            print("Clowning:", x)
            print(x * self.value)
            return x + self.value
            
    def main():
        print("Clowning around now.")
        c1 = Bozo(3)
        c2 = Bozo(4)
        print c1.clown(3)
        print c2.clown(c1.clown(2))
        
    main()

</br>

## Programming Exercises
PAGE 375
