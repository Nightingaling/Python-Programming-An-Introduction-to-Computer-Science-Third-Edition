# **Question 1**  
**Object:** A Car  
- **Attributes (data):**  
  - `make` (string): e.g., "Toyota"  
  - `model` (string): e.g., "Camry"  
  - `year` (integer): e.g., 2020  
  - `current_speed` (float): e.g., 60.5 (mph)  
  - `fuel_level` (float): e.g., 12.3 (gallons)  
  - `is_headlight_on` (boolean): e.g., `False`  
- **Methods (behaviors):**  
  - `accelerate(speed_increase)`: Increases `current_speed` by the given value.  
  - `brake(speed_decrease)`: Decreases `current_speed` by the given value.  
  - `refuel(amount)`: Adds fuel to `fuel_level`.  
  - `toggle_headlights()`: Switches headlights on/off.  
  - `check_fuel()`: Returns the current `fuel_level`.  

---

# **Question 2**  
a) **`Point(130, 130)`**  
- A single point at coordinates (130, 130). Appears as a small dot (default color: black).  

b) **`c = Circle(Point(30,40), 25)`**  
- A blue-filled circle with a red border, centered at (30, 40) with a radius of 25.  

c) **`r = Rectangle(Point(20,20), Point(40,40))`**  
- A light-green square (RGB: 0,255,150) with corners at (20,20) and (40,40). Border width is 3 (default color: black).  

d) **`l = Line(Point(100,100), Point(100,200))`**  
- A vertical dark-red line from (100,100) to (100,200) with an arrowhead at the starting point.  

e) **`Oval(Point(50,50), Point(60,100))`**  
- A tall, narrow oval fitting inside a rectangle from (50,50) to (60,100). Default fill and outline.  

f) **`shape = Polygon(Point(5,5), Point(10,10), Point(5,10), Point(10,5))`**  
- An orange-filled polygon connecting four points, forming a diamond or overlapping squares.  

g) **`t = Text(Point(100,100), "Hello World!")`**  
- Italicized "Hello World!" in 16pt Courier font, centered at (100,100). Default color: black.  

---

# **Question 3**  
Here's a step-by-step explanation of what happens when the program runs:

### **1. Window Creation**  
- A graphics window is created with default size (200x200 pixels).  

### **2. Red Circle Drawn**  
- A red circle (filled and outlined) with center at (50, 50) and radius 20 is drawn in the window.  

### **3. Loop for 10 Mouse Clicks**  
The program waits for the user to click **10 times** in the window. For each click:  
- **Step 3.1:** The mouse click coordinates (`p`) are recorded.  
- **Step 3.2:** The current center of the circle (`c`) is retrieved.  
- **Step 3.3:** The difference between the clicked position and the circle’s center is calculated (`dx` and `dy`).  
- **Step 3.4:** The circle is **moved** to the clicked location using `shape.move(dx, dy)`.  

### **4. After 10 Clicks**  
- The window closes automatically (`win.close()`).  

### **Key Behavior**  
- The circle "jumps" to wherever the user clicks, 10 times in total.  
- The window remains open until all 10 clicks are completed.  
