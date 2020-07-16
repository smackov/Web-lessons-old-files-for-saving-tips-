name = 'Jone'
age = 30

print('My name is ' + name + '. I\'m ' + str(age))
print('My name is %(name)s. I\'m %(age)d' % {'name': name, 'age': age})
print('My name is %s. I\'m %d' % ('David', age))
print('Title: %s, Price %.2f' % ('Sony', 40))

# format
print()
print('My name is {}. I\'m {}'.format(name, age))
print('My {1} name is {0}. I\'m {1}'.format(name, age))

print()
print('My name is {name}. I\'m {age}'.format(name=name, age=age))

# f-string
print()
print(f'My name is {name}. I\'m {age+4}')

print()
print('5+7 = {}'.format(5+7))
print(f'5+7 = {5+7}')
