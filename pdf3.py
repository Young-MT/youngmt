#mohammad mahdi kheiri


# ----- لیست‌ها (List) -----
fruits = ['apple', 'banana', 'cherry']
fruits.append('orange')
print(fruits)

a = ['apple', 'banana', 'cherry']
b = ['Ford', 'BMW', 'Volvo']
a.append(b)
print(a)

fruits = ['apple', 'banana', 'cherry', 'orange']
fruits.clear()
print(fruits)

fruits = ['apple', 'banana', 'cherry', 'orange']
x = fruits.copy()
print(x)

fruits = ['apple', 'banana', 'cherry']
x = fruits.count('cherry')
print(x)

points = [1, 4, 2, 9, 7, 8, 9, 3, 1]
x = points.count(9)
print(x)

fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)
print(fruits)

fruits = ['apple', 'banana', 'cherry']
x = fruits.index('cherry')
print(x)

fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango', 'orange', 'cherry']
x = fruits.index('cherry', 4)   
print(x)

fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, 'orange')
print(fruits)

fruits = ['apple', 'banana', 'cherry']
fruits.pop(1)
print(fruits)

my_list = [10, 20, 30]
x = my_list.pop()  
print(my_list)
print(x)

fruits = ['apple', 'banana', 'cherry', 'banana']
fruits.remove('banana')
print(fruits)

my_list = [1, 2, 3]
del my_list[1]
print(my_list)

fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
print(fruits)

cars = ['Ford', 'BMW', 'Volvo']
cars.sort()
print(cars)

# ----- تاپل‌ها (Tuple) -----
thistuple = ('apple', 'banana', 'cherry')
print(thistuple)

thistuple = ('apple', 'banana', 'cherry', 'apple', 'cherry')
print(thistuple)

thistuple = tuple(('apple', 'banana', 'cherry'))
print(thistuple)

my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print(my_tuple)

thistuple = ('apple', 'banana', 'cherry')
print(thistuple[1])

thistuple = ('apple', 'banana', 'cherry')
print(thistuple[-1])

thistuple = ('apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango')
print(thistuple[2:5])  
print(thistuple[:4])   

thistuple = ('apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango')
print(thistuple[-4:-1])  

thistuple = ('apple', 'banana', 'cherry')
if 'apple' in thistuple:
    print("Yes, 'apple' is in the fruits tuple")

x = ('apple', 'banana', 'cherry')
y = list(x)
y[1] = 'kiwi'
x = tuple(y)
print(x)

thistuple = ('apple', 'banana', 'cherry')
y = list(thistuple)
y.append('orange')
thistuple = tuple(y)
print(thistuple)

thistuple = ('apple', 'banana', 'cherry')
y = ('orange',)  
thistuple += y
print(thistuple)

thistuple = ('apple', 'banana', 'cherry')
y = list(thistuple)
y.remove('apple')
thistuple = tuple(y)
print(thistuple)

fruits = ('apple', 'banana', 'cherry')
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

fruits = ('apple', 'banana', 'cherry', 'strawberry', 'raspberry')
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

fruits = ('apple', 'mango', 'papaya', 'pineapple', 'cherry')
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)

thistuple = ('apple', 'banana', 'cherry')
for x in thistuple:
    print(x)

i = 0
while i < len(thistuple):
    print(thistuple[i])
    i = i + 1

tuple1 = ('a', 'b', 'c')
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

fruits = ('apple', 'banana', 'cherry')
mytuple = fruits * 2
print(mytuple)

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(5)
print(x)

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.index(8)
print(x)

# ----- مجموعه‌ها (Set) -----
thisset = {'apple', 'banana', 'cherry'}
print(thisset)

thisset = set(('apple', 'banana', 'cherry'))
print(thisset)

myset = {'apple', 'banana', 'cherry'}
print(type(myset))

thisset = {'apple', 'banana', 'cherry'}
for x in thisset:
    print(x)
thisset.add('orange')
print(thisset)

thisset = {'apple', 'banana', 'cherry'}
tropical = {'pineapple', 'mango', 'papaya'}
thisset.update(tropical)
print(thisset)

thisset = {'apple', 'banana', 'cherry'}
mylist = ['kiwi', 'orange']
thisset.update(mylist)
print(thisset)

thisset = {'apple', 'banana', 'cherry'}
thisset.remove('banana')
print(thisset)

thisset = {'apple', 'banana', 'cherry'}
thisset.discard('banana')
print(thisset)

thisset = {'apple', 'banana', 'cherry'}
x = thisset.pop()
print(x)
print(thisset)

thisset = {'apple', 'banana', 'cherry'}
thisset.clear()
print(thisset)

thisset = {'apple', 'banana', 'cherry'}
for x in thisset:
    print(x)

set1 = {'a', 'b', 'c'}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

set1 = {'a', 'b', 'c'}
set2 = {1, 2, 3}
set3 = set1 | set2
print(set3)

x = {'a', 'b', 'c'}
y = (1, 2, 3)
z = x.union(y)
print(z)

set1 = {'a', 'b', 'c'}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

set1 = {'apple', 'banana', 'cherry'}
set2 = {'google', 'microsoft', 'apple'}
set3 = set1.intersection(set2)
print(set3)

mylist = ['apple', 'banana', 'cherry']
x = frozenset(mylist)
print(x)

# ----- دیکشنری‌ها (Dictionary) -----
thisdict = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}
print(thisdict)
print(thisdict['brand'])

thisdict = dict(name='John', age=36, country='Norway')
print(thisdict)

thisdict = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}
x = thisdict['model']
print(x)

x = thisdict.get('model')
print(x)

thisdict = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}
x = thisdict.keys()
print(x)

car = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}
x = car.keys()
print(x)  
car['color'] = 'white'
print(x)  
print(car)

thisdict = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}
print(thisdict.values())

thisdict = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}
print(thisdict.items())

thisdict = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}
if 'model' in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")

thisdict = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}
thisdict.update({'year': 2020})
print(thisdict)

thisdict['color'] = 'red'
print(thisdict)

thisdict = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}
thisdict.pop('model')
print(thisdict)

thisdict = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}
thisdict.popitem()
print(thisdict)

thisdict = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}
del thisdict['model']
print(thisdict)

thisdict = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}
thisdict.clear()
print(thisdict)

thisdict = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}
for x in thisdict:
    print(x)

for x in thisdict:
    print(thisdict[x])

thisdict = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}
for x in thisdict.values():
    print(x)

for x in thisdict.keys():
    print(x)

for x, y in thisdict.items():
    print(x, y)

thisdict = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}
mydict = thisdict.copy()
print(mydict)

thisdict = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year': 1964
}
mydict = dict(thisdict)
print(mydict)

myfamily = {
    'child1': {'name': 'Emil', 'year': 2004},
    'child2': {'name': 'Tobias', 'year': 2007},
    'child3': {'name': 'Linus', 'year': 2011}
}
print(myfamily)

child1 = {'name': 'Emil', 'year': 2004}
child2 = {'name': 'Tobias', 'year': 2007}
child3 = {'name': 'Linus', 'year': 2011}
myfamily = {
    'child1': child1,
    'child2': child2,
    'child3': child3
}
print(myfamily)

print(myfamily['child2']['name'])

myfamily = {
    'child1': {'name': 'Emil', 'year': 2004},
    'child2': {'name': 'Tobias', 'year': 2007},
    'child3': {'name': 'Linus', 'year': 2011}
}
for x, obj in myfamily.items():
    print(x)
    for y in obj:
        print(y + ':', obj[y])