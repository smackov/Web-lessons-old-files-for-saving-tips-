import os

tree = os.walk('folder')
print(tree)
for files in tree:
    print(files)

print()

def read_dir(folder):
    for root, dirs, files in os.walk(folder):
        level = root.count(os.sep)
        indent = ' ' * 4 * level
        print(f'{indent} [{os.path.basename(root)}]')
        sub_indent = ' ' * 4 * (level + 1)
        for file in files:
            print(f'{sub_indent} {file}')
        # print(root, files, indent, sub_indent)
        # print(root, dirs, indent)




read_dir('folder')

