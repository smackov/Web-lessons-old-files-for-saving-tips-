from tkinter import *

root = Tk()  # object
root.title('My first GUI application')  # title
root.iconbitmap('python.ico')  # ico image
root.geometry('600x400+500+300')  # window's size and place
root.resizable(False, False)  # ability to change width and height of window
# root.config(bg='#156')  # change background's color
root['bg'] = '#156'  # one of methods to change background's color

root.mainloop()  # mainloop (cycle)
