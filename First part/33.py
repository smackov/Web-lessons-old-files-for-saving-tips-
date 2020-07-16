f = open('file.txt', 'r', encoding='utf-8')
text = f.read()
print(f.encoding)  # utf-8
f.close()
print(text)


f = open('file.txt', 'a', encoding='utf-8')  # a - append
f.write('New line!\n')
lines = ['New line 1', 'New line 2']
for i in lines:
    f.write(i + '\n')
f.writelines(f'{i}\n' for i in lines)
print()
f.close()


f = open('file.txt', 'r', encoding='utf-8')
for line in f:
    print(line)
f.close()

# f.writelines(f'{i}\n' for i in lines)
