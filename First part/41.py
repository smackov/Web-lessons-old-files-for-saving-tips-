from classes import Person, Employee
# import classes


person2 = Person('Dinis', 22)
person2._age = 30
person2.print_info()

employee = Employee('Nick', 30, 'Facebook')
employee.print_info()
print(employee)