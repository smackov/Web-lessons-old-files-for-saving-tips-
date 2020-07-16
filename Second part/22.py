from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry('400x300')

s = ttk.Style()
print(s.theme_names(), s.theme_use())
s.theme_use('clam')
# s.configure('.', foreground='red')
s.configure('TButton', foreground='red', padding=6)
s.configure('Blue.TButton', foreground='blue', padding=6)

# Button(root, text='Button 1', padx=40, pady=5).pack(pady=10)
# ttk.Button(root, text='Button 2', width=21).pack()
# ttk.Button(root, text='Button 3', style='Blue.TButton', width=21).pack(pady=10)
#
# Entry(root).pack(pady=10)
# ttk.Entry(root).pack()


def choose(event):
    print(select.current(), select.get())


select = ttk.Combobox(root, values=['January', 'February', 'March', 'April', 'May'])
select.place(relx=0.5, rely=0.5, anchor='s')
select.current(2)
select.bind('<<ComboboxSelected>>', choose)

root.mainloop()