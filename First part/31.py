from datetime import date, datetime, timedelta
import locale


# date
today = date.today()
print(today)
print(today.day)
print(today.month)
print(today.year)
print(today.weekday())

# datetime

now = datetime.now()
now2 = datetime.today()
print(now, now2, sep='\n')
print()
print(now.day)
print(now.month)
print(now.year)
print(now.weekday())
print(now.hour)
print(now.minute)
print(now.second)

days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
print('\nToday is ', days[now.weekday()])
print()


locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')

now = datetime.now()
print(now)
print(now.strftime('%a'))
print(now.strftime('%A'))

print(f'Дата: {now.strftime("%A, %d, %b, %Y")}')
print(f'Время: {now.strftime("%H:%M:%S")}')

print(now.strftime('%c'))
print(now.strftime('%X'))
print(now.strftime('%x'))

print()
print(now.strftime('%c'))
d1 = now + timedelta(days=1, hours=2, minutes=10)
print(d1.strftime('%c'))

