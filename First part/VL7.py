# test = None
# test = 342
# print(test)
y = 1
x = 5
print(x, y)
print()

x, y = (1, 5)
print(x, y)
print()

my_true = True
my_false = False
print(my_true, my_false)
print(type(my_true))
print(type(my_false))
print()

# str() int () float () bool()
x = 5.2
print('x = ', x, 'type = ', type(x))
x = int(x)
print('x = ', x, 'type = ', type(x))
print()

x = 5.2
print('x = ', x, 'type = ', type(x))
x = str(x)
print('x = ', x, 'type = ', type(x))
print()

x = 5.2
print('x = ', x, 'type = ', type(x))
x = bool(x)
print('x = ', x, 'type = ', type(x))
print()

x = 0
print('x = ', x, 'type = ', type(x))
x = bool(x)
print('x = ', x, 'type = ', type(x))
print()

x = None
print('x = ', x, 'type = ', type(x))
x = bool(x)
print('x = ', x, 'type = ', type(x))
print()
