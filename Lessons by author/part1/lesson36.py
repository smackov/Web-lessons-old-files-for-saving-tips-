class A:
    property1 = 'Property 1'
    property2 = 'Property 2'
    name = 'guest'

    def say_hi(self, name=''):
        if name:
            return 'Hi, ' + self.name
        else:
            return 'Hello, ' + self.name


a = A()
b = A()

print(a.property1)
print(a.property2, end='\n\n')

a.property1 = 'Property 1'
a.property2 = 'Property 2'

print(a)
print(b, end='\n\n')

print(a.property1)
print(a.say_hi('John'), end='\n\n')

name = 'John'
print(a.say_hi())
