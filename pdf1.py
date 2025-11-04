# <<mohammad mahdi kheiri>>

# Hello World
print("Hello, World!")

# Indentation
if 5 > 2:
    print("Five is greater than two!")

# Variables
x = 5
y = "Hello, World!"
print(x, y)

# Casting
x_cast = str(3)
y_cast = int(3)
z_cast = float(3)
print(x_cast, y_cast, z_cast)

# Type
print(type(5), type("John"))

# Quotes
name1 = "John"
name2 = 'John'
print(name1 == name2)

# Case Sensitivity
a = 4
A = "Sally"
print(a, A)

# Naming
myvar = "John"
myVariableName = "John"
MyVariableName = "John"
my_variable_name = "John"

# Multiple Assignment
x, y, z = "Orange", "Banana", "Cherry"
print(x, y, z)

# Same Value
x = y = z = "Orange"
print(x, y, z)

# Unpack
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x, y, z)

# Print and Concatenate
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
print(x + " " + y + " " + z)
print(5 + 10)
print(5, "John")

# Global
x = "awesome"
def myfunc1():
    print("Python is " + x)
myfunc1()

x = "awesome"
def myfunc2():
    x = "fantastic"
    print("Python is " + x)
myfunc2()
print("Python is " + x)

x = "awesome"
def myfunc3():
    global x
    x = "fantastic"
myfunc3()
print("Python is " + x)

# Exercises
print('Hello', 'World')
x = 'awesome'
def myfunc():
    x = 'fantastic'
myfunc()
print('Python is ' + x)
