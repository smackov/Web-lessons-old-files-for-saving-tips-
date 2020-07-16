from tkinter import *

root = Tk()
root.geometry('800x600')


def about():
    print('About')


f_text = Frame(root)
f_text.pack(fill=BOTH, expand=1)

main_menu = Menu(root)
root.config(menu=main_menu)

# main_menu.add_command(label='File')
# main_menu.add_command(label='About')

#File
file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label='Open')
file_menu.add_command(label='Save')
file_menu.add_separator()
file_menu.add_command(label='Exit')
main_menu.add_cascade(label='File', menu=file_menu)

# About
help_menu = Menu(main_menu, tearoff=0)
help_menu_sub = Menu(help_menu, tearoff=0)
help_menu_sub.add_command(label='Online')
help_menu_sub.add_command(label='Offline', command=about)
help_menu.add_cascade(label='Help', menu=help_menu_sub)
help_menu.add_command(label='About program')
main_menu.add_cascade(label='Notes', menu=help_menu)


t = Text(f_text, bg='#343D46', fg='#C6DEC1', padx=10, pady=10,
         wrap=WORD, insertbackground='#EDA756', selectbackground='#4E5A65',
         spacing3=10)
t.pack(expand=1, fill=BOTH, side=LEFT)

scroll = Scrollbar(f_text, command=t.yview)
scroll.pack(fill=Y, side=LEFT)
t.config(yscrollcommand=scroll.set)


root.mainloop()