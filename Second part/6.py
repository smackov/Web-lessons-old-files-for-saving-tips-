from tkinter import *

root = Tk()
root.title("Радуга")
root.geometry('220x220')
root.resizable(False, False)


def red():
    e_code_color.delete(0, END)
    e_code_color.insert(0, 'ff0000')
    l_name_color['text'] = 'Red'


def orange():
    e_code_color.delete(0, END)
    e_code_color.insert(0, 'ff7d00')
    l_name_color['text'] = 'Orange'


def yellow():
    e_code_color.delete(0, END)
    e_code_color.insert(0, 'ffff00')
    l_name_color['text'] = 'Yellow'


def green():
    e_code_color.delete(0, END)
    e_code_color.insert(0, '00ff00')
    l_name_color['text'] = 'Green'


def blue():
    e_code_color.delete(0, END)
    e_code_color.insert(0, '007dff')
    l_name_color['text'] = 'Blue'


def dblue():
    e_code_color.delete(0, END)
    e_code_color.insert(0, '0000ff')
    l_name_color['text'] = 'Dark blue'


def violet():
    e_code_color.delete(0, END)
    e_code_color.insert(0, '7d00ff')
    l_name_color['text'] = 'Violet'


l_name_color = Label(root, text="Color")
l_name_color.pack(fill=X)

e_code_color = Entry(root, justify=CENTER)
e_code_color.pack(fill=X)

b_red = Button(root, bg='#ff0000', command=red)
b_red.pack(fill=X)

b_orange = Button(root, bg='#ff7d00', command=orange)
b_orange.pack(fill=X)

b_yellow = Button(root, bg='#ffff00', command=yellow)
b_yellow.pack(fill=X)

b_green = Button(root, bg='#00ff00', command=green)
b_green.pack(fill=X)

b_blue = Button(root, bg='#007dff', command=blue)
b_blue.pack(fill=X)

b_dblue = Button(root, bg='#0000ff', command=dblue)
b_dblue.pack(fill=X)

b_violet = Button(root, bg='#7d00ff', command=violet)
b_violet.pack(fill=X)




root.mainloop()


