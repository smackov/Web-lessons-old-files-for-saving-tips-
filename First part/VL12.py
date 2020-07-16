print(2 > 3)
print(2 <= 3)
print()

print(2 == 3)
print(2 != 3)
print()

#
x = 0
if x:
    print('Variable x has came back true')
else:
    print('V has came back false')


print()


#
light = 'green'
if light == 'red':
    print('stop')
elif light == 'yellow':
    print('wait')
elif light == 'green':
    print('go')
else:
    print('what?)')

#
age = int(input('How old are you? '))

if age >= 18:
    print('Welcome!')
else:
    print(f'You are {age}, you need {18 - age} years.')


#
print()
time = 11
day = 'sunday'

if time < 12 and day != 'sunday':
    print('Open')
else:
    print('Close')

