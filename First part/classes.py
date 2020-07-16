class Person:
    name = 'Jone'

    def __init__(self, name, _age):
        self.name = name
        self._age = _age


    def print_info(self):
        print(f'Name: {self.name}. Age: {self._age}')


    def age_2(self, value):
        if value in range(1, 101):
            self._age = value
        else:
            print('Wrong age!!')


class Employee(Person):

    def __init__(self, name, _age, company):
        super().__init__(name, _age)
        self.company = company


    def more_info(self):
        print(f'Name: {self.name} works in {self.company}. Age: {self._age}')


    def print_info(self):
        super().print_info()
        print(f'Works in {self.company}.')

    def __str__(self):
#        return f'Name: {self.name}'
        return f'Class ' + self.__class__.__name__