from tkinter import *

root = Tk()
root.title("Радуга")
root.geometry('220x220')
root.resizable(False, False)


def get_color(text_color, hex_color):
    e_code_color.delete(0, END)
    e_code_color.insert(0, hex_color)
    l_name_color['text'] = text_color


l_name_color = Label(root, text="Color")
l_name_color.pack(fill=X)

e_code_color = Entry(root, justify=CENTER)
e_code_color.pack(fill=X)

b_red = Button(root, bg='#ff0000',
               command=lambda: get_color('Red', '#ff0000')).pack(fill=X)

b_orange = Button(root, bg='#ff7d00',
                  command=lambda: get_color('Orange', '#ff7d00')).pack(fill=X)

b_yellow = Button(root, bg='#ffff00',
                  command=lambda: get_color('Yellow', '#ffff00')).pack(fill=X)

b_green = Button(root, bg='#00ff00',
                 command=lambda: get_color('Green', '#00ff00')).pack(fill=X)

b_blue = Button(root, bg='#007dff',
                command=lambda: get_color('Blue', '#007dff')).pack(fill=X)

b_dblue = Button(root, bg='#0000ff',
                 command=lambda: get_color('Dark Blue', '#0000ff')).pack(fill=X)

b_violet = Button(root, bg='#7d00ff',
                  command=lambda: get_color('Violet', '#7d00ff')).pack(fill=X)



root.mainloop()
