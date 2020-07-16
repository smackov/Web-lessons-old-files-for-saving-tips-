
#сборка приложения по умолчанию
pyinstaller notepad.py

#сборка приложения в один файл
pyinstaller -F -w -i "C:\code\Python Webformyself\Second part\wt.ico" Weather.py

#nocosole
pyinstaller -w notepad.py

#ico
pyinstaller -i "C:\\code\\Python Webformyself\\Lessons by author\\part2\\ico.ico" notepad.py