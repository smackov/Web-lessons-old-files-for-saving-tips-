from classes import Person, Employee
# import classes


person2 = Person('Dinis', 22)
person2._age = 30
person2.print_info()

employee = Employee('Nick', 30)
employee.name = 'Daniel'
employee.company = 'PaidyPiy'
employee.age_2(40)
employee.more_info()

