#mohammad mahdi kheiri

cas = ["Ford", "Volvo", "BMW"]

x = cars[0]
print(x)

import array
arr = array.array('i', [1, 2, 3, 4])
arr.append(5)
arr[1] = 10
print(arr)

lst = [1, 2, 3]
lst.append(4)
print("LIST=", lst)

import array
arr = array.array('i', [1, 2, 3])
arr.append(4)
print(arr)

import array
arr = array.array('i', [1, 2, 3, 4])
arr.append(5)
arr[1] = 10
print(arr)

print("Enter your name:")
name = input()
print(f"Hello {name}")

name = input("Enter your name:")
print(f"Hello {name}")
fav1 = input("What is your favorite animal:")
fav2 = input("What is your favorite color:")
fav3 = input("What is your favorite number:")
print(f"Do you want a {fav2} {fav1} with {fav3} legs?")

import math
x = input("Enter a number:")
y = math.sqrt(float(x))
print(f"The square root of {x} is {y}")

y = True
while y == True:
    x = input("Enter a number:")
    try:
        x = float(x)
        y = False
    except:
        print("Wrong input, please try again.")
print("Thank you!")

try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")

try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")

try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")

x = min(5, 10, 25)
y = max(5, 10, 25)
print(x)
print(y)

x = abs(-7.25)
print(x)

x = pow(4, 3)
print(x)

import math
x = math.sqrt(64)
print(x)

import math
x = math.ceil(1.4)
y = math.floor(1.4)
print(x)
print(y)
