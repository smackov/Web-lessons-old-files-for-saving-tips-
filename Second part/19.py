from tkinter import *

root = Tk()
root.geometry('800x600')


def f_event(event,key):
    print(event, key)


e = Entry(root, justify=CENTER, bg='Blue')
e.pack(fill=X, expand=1, padx=10, pady=20)
e.bind('<Button-1>', lambda event, key='Left click': f_event(event, key))
e.bind('<Button-2>', lambda event, key='Middle click': f_event(event, key))
e.bind('<Button-3>', lambda event, key='Right click': f_event(event, key))
e.bind('<FocusIn>', lambda event, key='Focus': f_event(event, key))

root.mainloop()