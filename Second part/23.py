from tkinter import ttk
from ttkthemes import ThemedTk

root = ThemedTk(theme='clearlooks')
root.geometry('400x300')

ttk.Button(root, text='Button').pack(pady=10)
ttk.Entry(root).pack()

def choose(event):
    print(select.current(), select.get())


select = ttk.Combobox(root, values=['January', 'February', 'March', 'April', 'May'])
select.place(relx=0.5, rely=0.5, anchor='s')
select.current(2)
select.bind('<<ComboboxSelected>>', choose)


root.mainloop()