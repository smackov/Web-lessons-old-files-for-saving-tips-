class A:
    property1 = 'Property 1'
    property2 = 'Property 2'
    name = 'guest'

    def say_hi(self, name='guest'):
        return 'Hi, '+ name

    def say_hi_2(self, name=''):
        if name:
            return 'Hi, ' + name
        else:
            return 'Hello, ' + self.name


a = A()
# print(a)
# a.property1 = 'Property 1'
# a.property2 = 'Property 2'


print(a.property1)
print(a.say_hi('Mike'))
print(a.say_hi())
print()

print(a.say_hi_2())

