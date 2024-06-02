# Chapter 1: Computers and Programs

</br>

## Review Questions
True/False

    1. Computer science is the study of computers.
    2. The CPU is the "brain" of the computer.
    3. Secondary memory is also called RAM.
    4. All information that a computer is currently working on is stored in main memory.
    5. The syntax of a language is its meaning, and semantics is its form.
    6. A function definition is a sequence of statements that defines a new command.
    7. A programming environment refers to a place where programmers work.
    8. A variable is used to give a name to a value so it can be referred to in other places.
    9. A loop is used to skip over a section of a program.
    10. A chaotic function can't be computed by a computer

</br>

## Multiple Choice
### 1. What is the fundamental question of computer science?
    a) How fast can a computer compute?
    b) What can be computed?
    c) What is the most effective programming language?
    d) How much money can a programmer make?
    
### 2. An algorithm is like a
    a) newspaper b) venus flytrap c) drum d) recipe

### 3. A problem is intractable when
    a) you cannot reverse its solution
    b) it involves tractors
    c) it has many solutions
    d) it is not practical to solve

### 4. Which of the following is not an example of secondary memory?
    a) RAM b) hard drive c) USB flash drive d) DVD

### 5. Computer languages designed to be used and understood by humans are
    a) natural languages
    b) high-level computer languages
    c) machine languages
    d) fetch-execute languages

### 6. A statement is
    a) a translation of machine language
    b) a complete computer command
    c) a precise description of a problem
    d) a section of an algorithm

### 7. One difference between a compiler and an interpreter is
    a) a compiler is a program
    b) a compiler is used to translate high-level language into machine language
    c) a compiler is no longer needed after a program is translated
    d) a compiler processes source code

### 8. By convention, the statements of a program are often placed in a function called
    a) import b) main c) program d) IDLE

### 9. Which of the following is not true of comments?
    a) They make a program more efficient.
    b) They are intended for human readers.
    c) They are ignored by Python.
    d) In Python, they begin with a pound sign (#).

### 10. The items listed in the parentheses of a function definition are called
    a) parentheticals
    b) parameters
    c) arguments
    d) both b) and c) are correct

</br>

## Discussion
### 1. Compare and contrast the following pairs of concepts from the chapter:
    a) Hardware vs. Software
    b) Algorithm vs. Program
    c) Programming Language vs. Natural Language
    d) High-Level Language vs. Machine Language
    e) Interpreter vs. Compiler
    f) Syntax vs. Semantics

</br>

### 2. List and explain in your own words the role of each of the five basic functional units of a computer depicted in Figure 1.1.
![image](https://github.com/Nightingaling/-Python-Programming-An-Introduction-to-Computer-Science-Third-Edition/assets/130979519/5714ccbd-ebcf-4808-9862-967f3d5b0ebb)

</br>

### 3. Write a detailed algorithm for making a peanut butter and jelly sandwich (or some other everyday activity). You should assume that you are talking to someone who is conceptually able to do the task, but has never actually done it before. For example, you might be telling a young child.

</br>

### 4. As you will learn in a later chapter, many of the numbers stored in a computer are not exact values, but rather close approximations. For example, the value 0.1 might be stored as 0.10000000000000000555. Usually, such small differences are not a problem; however, given what you have learned about chaotic behavior in Chapter 1, you should realize the need for caution in certain situations. Can you think of examples where this might be a problem? Explain.

</br>

### 5. Trace through the chaos program from Section 1.6 by hand using 0.15 as the input value. Show the sequence of output that results. 
    # File: chaos. py
    # A simple program illustrating chaotic behavior.
    def main() :
      print("This program illustrates a chaotic function")
      x = eval(input("Enter a number between 0 and 1: ") )
      for i in range(10) :
        X = 3.9 * x * (1 - x)
        print(x)
    main()

</br>

## Programming Exercises
### 1. Start up an interactive Python session and try typing in each of the following commands. Write down the results you see.
    a) print("Hello, world! ")
    b) print("Hello", "world!")
    c) print(3)
    d) print(3.0)
    e) print(2 + 3)
    f) print(2. 0 + 3. 0)
    g) print("2" + "3")
    h) print("2 + 3 =", 2 + 3)
    i) print(2 * 3)
    j) print(2 ** 3)
    k) print(7 / 3)
    l) print(7 // 3)
    
</br>

### 2. Enter and run the chaos program from Section 1.6. Try it out with various values of input to see that it functions as described in the chapter.
    # File: chaos. py
    # A simple program illustrating chaotic behavior.
    def main() :
      print("This program illustrates a chaotic function")
      x = eval(input("Enter a number between 0 and 1: ") )
      for i in range(10) :
        X = 3.9 * x * (1 - x)
        print(x)
    main()
    
</br>

### 3. Modify the chaos program using 2.0 in place of 3.9 as the multiplier in the logistic function. Your modified line of code should look like this:
    X = 2.0 * x * (1 - x) 
### Run the program for various input values and compare the results to those obtained from the original program. Write a short paragraph describing any differences that you notice in the behavior of the two versions.

<br/>

### 4. Modify the chaos program so that it prints out 20 values instead of 10.

</br>

### 5. Modify the chaos program so that the number of values to print is determined by the user. You will have to add a line near the top of the program to get another value from the user:
    n = eval(input("How many numbers should I print? ") )
### Then you will need to change the loop to use n instead of a specific number.

<br/>

### 6. The calculation performed in the chaos program can be written in a number of ways that are algebraically equivalent. Write a version of the program for each of the following ways of doing the computation. Have your modified programs print out 100 iterations of the calculation and compare the results when run on the same input.
    a) 3 . 9 * x * ( 1 - x)
    b) 3.9 * (x - x * x)
    C) 3.9 * X - 3.9 * X * X
### Explain the results of this experiment. Hint: See discussion question number 4, above.

<br/>

### 7. (Advanced) Modify the chaos program so that it accepts two inputs and then prints a table with two columns similar to the one shown in Section 1.8. (Note: You will probably not be able to get the columns to line up as nicely as those in the example. Chapter 5 discusses how to print numbers with a fixed number of decimal places.)
