import re

# s = 'It is just line of code. And it is also line of code.'
# pattern = 'line'
#
# print(s.find(pattern))
# print(pattern in s)
#
# if re.search(pattern, s):
# # if pattern in s:
#     print('Matched')
# else:
#     print('No match')
#
# match = re.search(pattern, s)
# print(match)
# print(match.start())
# print(match.end())
#
# print(re.findall(pattern, s))
# print(re.split(r'\.', s))

s = '''It is just line of code.
And it is also line of code.
That is line of numbers: 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 10
That line of different signs: "!", "@", "-", "&", "?", "__"
a\\b\tc
test string'''

# pattern = r'\w+'  # get numbers and bukvi
pattern = r'[a-zA-Z]+'  # get bukvi in range a-z and A-Z
pattern_2 = r'[a-z]+'
pattern_3 = r'\d+'  # get numbers
print(re.findall(pattern, s))
print(re.findall(pattern_2, s, flags=re.IGNORECASE))
print(re.findall(pattern_3, s))


s = 'sdfvdfsv iframe@gmail.com dfv df com gmail load@mail.ru'
result = re.findall(r'\w+@\w+\.\w+', s)
print(result)

