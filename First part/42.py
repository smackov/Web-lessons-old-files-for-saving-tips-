def hello():
    return 'Hello, I am func "hello"'

def hello2():
    return 'Hello, I am func "hello22"'

def hello3():
    return 'Hello, I am func "hello33"'

def super_func(func):
    print('Hello, I am func "super_func"')
    print(func())

super_func(hello2)

test = hello
print('\nTest: ', test())
print('******END******\n')
#  *************************


def my_decorator(func):
    def func_wrapper():
        print('Code before')
        func()
        print('Code after')
    return func_wrapper

@my_decorator
def func_test():
    print('Hi, hi, I am func "func_test"')

#  test2 = my_decorator(func_test)
#  test2()
func_test()

print('******END******\n')
#  *************************


def make_title(fn):
    def wrapped():
        title = fn()
        title = title.capitalize()
        title = title.replace(',', '')
        return title
    return wrapped

@make_title
def hi():
    return 'hello, world, hi!'

print(hi())


