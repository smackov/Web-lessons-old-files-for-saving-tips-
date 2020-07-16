import zipfile
import os

folder_path = 'c:\\code\\Python Webformyself\First part\\Folder'
zip_path = 'c:\\code\\Python Webformyself\\First part\\Folder\\test.zip'
zip_name = 'test.zip'

my_zip = zipfile.ZipFile(zip_path, 'w')

my_zip.write('c:\\code\\Python Webformyself\\First part\\Folder\\1.txt', compress_type=zipfile.ZIP_DEFLATED, arcname='1.txt')

for folder, subfolders, files in os.walk(folder_path):
    print(folder, files)
    for file in files:
        if file == zip_name:
            continue
        my_zip.write(os.path.join(folder, file),
            os.path.relpath(os.path.join(folder, file), folder_path),
            compress_type=zipfile.ZIP_DEFLATED,
            compresslevel=1)
        print('\n Join: ', os.path.join(folder, file))
        print('\n Relpath: ', os.path.relpath(os.path.join(folder, file)))


my_zip.close()



