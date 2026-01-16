# Day 2: 30 Days of Python Programming

# 1. Declare variables
age = 26                      # integer
height = 1.75                 # float
complex_number = 2 + 3j       # complex

# 2. Area of a triangle
base = float(input("Enter base: "))
height_triangle = float(input("Enter height: "))
area_triangle = 0.5 * base * height_triangle
print("The area of the triangle is", area_triangle)

# 3. Perimeter of a triangle
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
perimeter_triangle = a + b + c
print("The perimeter of the triangle is", perimeter_triangle)

# 4. Rectangle area and perimeter
length = float(input("Enter length of rectangle: "))
width = float(input("Enter width of rectangle: "))
area_rectangle = length * width
perimeter_rectangle = 2 * (length + width)
print("Area of rectangle:", area_rectangle)
print("Perimeter of rectangle:", perimeter_rectangle)

# 5. Circle area and circumference
radius = float(input("Enter radius of the circle: "))
pi = 3.14
area_circle = pi * radius * radius
circumference = 2 * pi * radius
print("Area of the circle:", area_circle)
print("Circumference of the circle:", circumference)

# 6. Slope, x-intercept, y-intercept of y = 2x - 2
m = 2
y_intercept = -2
x_intercept = 1   # when y = 0 → 0 = 2x - 2 → x = 1
print("Slope:", m)
print("X-intercept:", x_intercept)
print("Y-intercept:", y_intercept)

# 7. Slope and Euclidean distance
x1, y1 = 2, 2
x2, y2 = 6, 10
slope = (y2 - y1) / (x2 - x1)
distance = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
print("Slope:", slope)
print("Euclidean distance:", distance)

# 8. Compare slopes
print("Slopes are equal:", m == slope)

# 9. Quadratic equation y = x^2 + 6x + 9
# y = (x + 3)^2 → y = 0 when x = -3
x = -3
y = x**2 + 6*x + 9
print("Value of y when x = -3:", y)

# 10. Length comparison
print(len("python") != len("dragon"))

# 11. Check 'on' in both words
print("on" in "python" and "on" in "dragon")

# 12. Check jargon
sentence = "I hope this course is not full of jargon"
print("jargon" in sentence)

# 13. Confirm no 'on'
print("on" not in "python" and "on" not in "dragon")

# 14. Convert length of python
length_python = len("python")
print(str(float(length_python)))

# 15. Check even number
number = int(input("Enter a number: "))
print("Even number:", number % 2 == 0)

# 16. Floor division check
print(7 // 3 == int(2.7))

# 17. Type comparison
print(type('10') == type(10))

# 18. int('9.8') == 10
# This will raise an error, so correct way:
print(int(float('9.8')) == 10)

# 19. Weekly earnings
hours = float(input("Enter hours: "))
rate = float(input("Enter rate per hour: "))
earning = hours * rate
print("Your weekly earning is", earning)

# 20. Lifetime in seconds
years = int(input("Enter number of years you have lived: "))
seconds_lived = years * 365 * 24 * 60 * 60
print("You have lived for", seconds_lived, "seconds.")

# 21. Display table
print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")
