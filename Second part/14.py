from tkinter import *

root = Tk()
root.geometry('800x600')


def about():
    print('About')


def change_theme(theme):
    t['bg'] = theme_colors[theme]['text_bg']
    t['fg'] = theme_colors[theme]['text_fg']
    t['insertbackground'] = theme_colors[theme]['cursor']
    t['selectbackground'] = theme_colors[theme]['select_bg']

f_text = Frame(root)
f_text.pack(fill=BOTH, expand=1)

main_menu = Menu(root)
root.config(menu=main_menu)

#File
file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label='Open')
file_menu.add_command(label='Save')
file_menu.add_separator()
file_menu.add_command(label='Exit')
main_menu.add_cascade(label='File', menu=file_menu)

# Theme
theme_menu = Menu(main_menu, tearoff=0)
theme_menu_sub = Menu(theme_menu, tearoff=0)
theme_menu_sub.add_command(label='Dark', command=lambda: change_theme('dark'))
theme_menu_sub.add_command(label='Light', command=lambda: change_theme('light'))
theme_menu.add_cascade(label='Theme', menu=theme_menu_sub)
theme_menu.add_command(label='About program')
main_menu.add_cascade(label='Notes', menu=theme_menu)

theme_colors = {
    'dark': {
        'text_bg': '#343D46', 'text_fg': '#C6DEC1',
        'cursor': '#EDA756', 'select_bg': '#4E5A65'
    },
    'light': {
        'text_bg': '#fff', 'text_fg': '#000',
        'cursor': '#8000FF', 'select_bg': '#777'
    }
}

t = Text(f_text, bg=theme_colors['dark']['text_bg'],
         fg=theme_colors['dark']['text_fg'],
         padx=10, pady=10, wrap=WORD,
         insertbackground=theme_colors['dark']['cursor'],
         selectbackground=theme_colors['dark']['select_bg'],
         spacing3=10, font=('Courier New', 11))
t.pack(expand=1, fill=BOTH, side=LEFT)


scroll = Scrollbar(f_text, command=t.yview)
scroll.pack(fill=Y, side=LEFT)
t.config(yscrollcommand=scroll.set)

root.mainloop()