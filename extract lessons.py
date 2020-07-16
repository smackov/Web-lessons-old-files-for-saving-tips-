import os
import zipfile
import re


path_general = 'D:\\Torrent - Download\\[WebForMySelf] [Андрей Кудлай] Python. Полное руководство\\videokurs'
destination_path = 'C:\\code\\Python Webformyself\\Lessons by author'


for path_folder in ['part1', 'part2']:
    destination = os.path.join(destination_path, path_folder)
    print(destination)
    for folder, subfolders, files in os.walk(os.path.join(path_general, path_folder)):
        # print('Folder: ', folder, '\nSubfolders: ', subfolders, '\nFiles: ', files)
        for file in files:
            if file.endswith('.zip'):
                file_path = os.path.join(folder, file)
                # print(file_path)
                try:
                    my_zip = zipfile.ZipFile(file_path)
                    my_zip.extractall(destination)
                except:
                    print(f'Error, file {file} was not extract!')

