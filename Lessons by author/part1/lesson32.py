import os


def read_dir(folder):
    for root, dirs, files in os.walk(folder):
        # print('root ', root)
        # print('subfolders ', dirs)
        # print('files', files)
        # print('SEP ', os.sep)
        level = root.count(os.sep)
        # print(level)
        indent = ' ' * 4 * level
        print(f'{indent}[{os.path.basename(root)}]')
        sub_indent = ' ' * 4 * (level + 1)
        # print(root, files, level, indent, sub_indent)
        for file in files:
            print(f'{sub_indent}{file}')
        # print('END\n')


read_dir('folder')


tree = os.walk('folder')
for files in tree:
    print(files)

print('\nEdu')
for root, dirs, files in os.walk('folder'):
    print('root ', root)
    print('subfolders ', dirs)
    print('files', files)


"""
    Адрес очередного каталога в виде строки.
    В форме списка имена подкаталогов первого уровня вложенности для данного каталога.
    В виде списка имена файлов данного каталога.
"""