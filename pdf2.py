#<<mohammad mahdi kheiri>>
# Type
x = 5
print(type(x))
x = "Hello World"
print(x, type(x))
x = ["apple", "banana", "cherry"]
print(x, type(x))

# Casting
print(int(1), int(2.8), int("3"))
print(float(1), float(2.8), float("3"))
print(str("s1"), str(2), str(3.0))

# Numbers
x_int = 1
y_float = 2.8
z_complex = 1j
print(type(x_int), type(y_float), type(z_complex))

# Strings
print("Hello")
print('Hello')
print("It's alright")
print("He is called 'Johnny' ")
print('He is called "Johnny" ')

# Multiline
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit."""
print(a)

# String as Array
a = "Hello, World!"
print(a[1])
for ch in "banana":
    pass
print(len(a))
print("free" in "The best things in life are free!")

# Slicing
b = "Hello, World!"
print(b[2:5], b[:5], b[2:], b[-5:-2])

# String Methods
a = " Hello, World! "
print(a.upper())
print(a.lower())
print(a.strip())
print("Hello, World!".replace("H", "J"))
print("Hello,World!".split(","))

# Concatenation
a, b = "Hello", "World"
print(a + b)
print(a + " " + b)

# f-string
age = 36
txt = f"My name is John, I am {age}"
print(txt)
price = 59
print(f"The price is {price} dollars")
print(f"The price is {price:.2f} dollars")
print(f"The price is {20 * 59} dollars")

# Escape
print('It\'s alright.')
print("This will insert one \\ (backslash).")
print("Hello\nWorld!")
print("Hello\rWorld!")
print("Hello\tWorld!")
print("Hello \bWorld!")

# Boolean
print(10 > 9, 10 == 9, 10 < 9)
a = 200
b = 33
print("b is greater than a" if b > a else "b is not greater than a")
x = 200
print(isinstance(x, int))

# Arithmetic Operators
x, y = 5, 3
print(x + y, x - y, x * y)
x, y = 12, 3
print(x / y)
x, y = 15, 2
print(x // y)
x, y = 2, 5
print(x ** y)

# Assignment
x = 5
x += 3
print(x)

# Comparison
x, y = 5, 3
print(x == y, x != y, x >= y)

# Logical
x = 5
print(x > 3 and x < 10)
print(x > 3 or x < 4)
print(not (x > 3 and x < 10))

# Identity
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)
print(x is y)
print(x == y)

# Membership
x = ["apple", "banana"]
print("banana" in x)
print("pineapple" not in x)

# Bitwise
print(6 & 3)
print(6 | 3)

# Operator Precedence
print((6 + 3) - (6 + 3))
