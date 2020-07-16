https://pypi.org/project/PyInstaller/

# сборка приложения с настройками по умолчанию
pyinstaller notepad.py

# сборка приложения в виде одного файла
pyinstaller -F notepad.py

# noconsole
pyinstaller -w notepad.py

# icon
pyinstaller -w -i "C:\Python\compilation\notepad\nt.ico" notepad.py