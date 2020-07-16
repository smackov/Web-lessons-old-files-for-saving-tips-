# 1
def get_square(num):
    return num ** 2


print(get_square(5))

# 2
get_square_2 = lambda num: num ** 2
print(get_square_2(10))

# 3
print((lambda num: num ** 2)(7))

# 4
l = [1, 2, 3]  # [2, 4, 5]

def get_double(l):
    return [i * 2 for i in l]
print(get_double(l))

# 5
l = [1, 2, 3]  # [2, 4, 5]
def get_double_2(l):
    return list(map(lambda num: num * 2, l))
print(get_double_2(l))


