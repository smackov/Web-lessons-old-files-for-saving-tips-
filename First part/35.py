# print(100 / 0)
# print(1 + '2')
# print(int('test'))

try:
    num = 100 / '2'
except Exception:
    num = 0
else:
    print('Else')
finally:
    print('Finally')

while True:
    try:
        num = int(input('Enter your number: '))
        print(f'100 / {num} = {100 / num}')
    except ZeroDivisionError:
        print('The number must be greater than zero')
    except ValueError:
        print('Must be a number')

